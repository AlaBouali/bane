import requests, urllib, socket, random, time, re, threading, sys, json, os, xtelnet
import bs4
from bs4 import BeautifulSoup
from bane.payloads import *
import tldextract

def extract_root_domain(subdomain):
    extracted = tldextract.extract(subdomain)
    if extracted.suffix.count('.') > 1:
        root_domain = "{}.{}".format(extracted.domain,extracted.suffix)
    else:
        root_domain = extracted.registered_domain
    return root_domain


if sys.version_info < (3, 0):
    from scapy.config import conf

    conf.ipv6_enabled = False
    from scapy.all import *
else:
    from kamene.config import conf

    conf.ipv6_enabled = False
    from kamene.all import IP,TCP,sr
if os.path.isdir("/data/data/com.termux/") == False:
    import dns.resolver



def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)


def get_banner(u, p=23, timeout=3, payload=None):
    try:
        return xtelnet.get_banner(u, p=p, timeout=timeout, payload=payload)
    except:
        return None


def info(u, timeout=10, proxy=None, logs=False, returning=True):
    """
    this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
    with this format:
    'requested information: result'

    it takes 2 arguments:

    u: ip or domain
    timeout: (set by default to: 10) timeout flag for the request
    usage:
    >>>import bane
    >>>domain='www.google.com'
    >>>bane.info(domain)"""
    try:
        h = ""
        u = "https://check-host.net/ip-info?host=" + u
        c = requests.get(
            u, headers={"User-Agent": random.choice(ua)}, proxies=proxy, timeout=timeout
        ).text
        soup = BeautifulSoup(c, "html.parser")
        la = soup.find_all("a")
        l = []
        for i in la:
            if "#ip_info-dbip" in str(i):
                l.append(remove_html_tags(str(i)).strip().replace("\n", " "))
            if "#ip_info-ip2location" in str(i):
                l.append(remove_html_tags(str(i)).strip().replace("\n", " "))
            if "#ip_info-geolite2" in str(i):
                l.append(remove_html_tags(str(i)).strip().replace("\n", " "))
        p = soup.find_all("table")
        o = 0
        di = {}
        for x in p:
            try:
                do = {}
                y = x.find_all("tr")
                for w in y:
                    a = w.find_all("td")
                    try:
                        c = str(a[0]).split("<td>")[1].split("</td>")[0].strip()
                        d = str(a[1]).split("<td>")[1].split("</td>")[0].strip()
                        d = remove_html_tags(d).strip().replace("\n", " ")
                        do.update({c: d})
                    except:
                        pass
                di.update({l[o]: do})
                o += 1
            except:
                pass
        if logs == True:
            for x in di:
                print(x)
                print("")
                for y in di[x]:
                    print(y + ": " + di[x][y])
                print("")
        if returning == True:
            return di
    except:
        return None


def norton_rate(u, timeout=30, proxy=None):
    """
    this function takes any giving and gives a security report from: safeweb.norton.com, if it is a: spam domain, contains a malware...
    it takes 3 arguments:
    u: the link to check
    logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
    returning: (set by default to: False) returning the report as a string format if it is set to: True.
    usage:
    >>>import bane
    >>>url='http://www.example.com'
    >>>bane.norton_rate(domain)"""
    try:
        ur = urllib.quote(u, safe="")
        ul = "https://safeweb.norton.com/report/show?url=" + ur
        c = requests.get(
            ul,
            headers={"User-Agent": random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(c, "html.parser")
        s = soup.find_all("div", class_="communityRatings")
        s = remove_html_tags(str(s[0])).strip().split("\n")
        while "" in s:
            s.remove("")
        try:
            return {"Profile": s[0], "Rate": float(s[1]), "By": s[2]}
        except:
            return {"Profile": s[0], "Rate": float(s[1])}
    except:
        pass


def myip(proxy=None, timeout=15):
    """
    this function is for getting your ip using: ipinfo.io
    usage:
    >>>import bane
    >>>bane.myip()
    xxx.xx.xxx.xxx"""
    try:
        return requests.get(
            "http://ipinfo.io/ip",
            headers={"User-Agent": random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text.strip()
    except:
        pass
    return ""


def whois(u):
    try:
        r = requests.post("https://check-host.net/ip-info/whois", data={"host": u})
        a = r.text.split("\n\n")[0]
        b = a.split("\n")
        d = {}
        for x in b:
            d.update(
                {
                    x.split(":")[0]
                    .strip(): x.replace(x.split(":")[0].strip(), "")
                    .strip()[1:]
                    .strip()
                }
            )
        return d
    except:
        pass
    return {}


def geoip(u, timeout=15, proxy=None):
    """
    this function is for getting: geoip informations
    """
    try:
        r = requests.get(
            "https://geoip-db.com/jsonp/" + u,
            headers={"User-Agent": random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return json.loads(r.split("(")[1].split(")")[0])
    except:
        pass
    return {}


def http_options(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        s = requests.session()
        a = s.options(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return []
    b = []
    if "Access-Control-Allow-Methods" in a:
        b += [x.strip() for x in a["Access-Control-Allow-Methods"].split(",")]
    if "Allow" in a:
        b += [x.strip() for x in a["Allow"].split(",")]
    return b


def headers(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        #"safe": sec,
        s = requests.session()
        a = s.get(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return None
    if logs == True:
        for x in a:
            print("{} : {}".format(x, a[x]))
    if returning == True:
        return a


def reverse_ip_lookup(u, timeout=10, logs=True, returning=False, proxy=None):
    """
    this function is for: reverse ip look up
    if you've used it 100 times in 24 hours, your IP will be banned by "api.hackertarget.com" so i highly recommand you to use the "proxy" option by adding a http(s) proxy:

    bane.reverse_ip_lookup('XXX.XXX.XXX.XXX',proxy='IP:PORT')

    """
    try:
        r = requests.get(
            "https://api.hackertarget.com/reverseiplookup/?q=" + u,
            headers={"User-Agent": random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return r.split("\n")
    except Exception as ex:
        pass
    return []


"""
   end of the information gathering functions using: api.hackertarget.com
"""


def resolve(u, server="8.8.8.8", timeout=1, lifetime=1):
    o = []
    r = dns.resolver.Resolver()
    r.timeout = timeout
    r.lifetime = lifetime
    r.nameservers = [server]
    a = r.query(u)
    for x in a:
        o.append(str(x))
    return o


"""
this class is used to scan a target for open ports

usage:

a=bane.port_scan("8.8.8.8",ports=[21,22,23,80,443,3306],timeout=5)
print(a.result)

this should give you a dict like this:

{'443': 'Open', '22': 'Closed', '21': 'Closed', '23': 'Closed', '80': 'Closed', '3306': 'Closed'}

"""


def get_local_ip():
    try:
        return [
            l
            for l in (
                [
                    ip
                    for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")
                ][:1],
                [
                    [
                        (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                    ][0][1]
                ],
            )
            if l
        ][0][0]
    except:
        return "127.0.0.1"


def host_alive(target):
    if os.name == "nt":
        r = os.popen("ping -n 1 " + target).readlines()
    else:
        r = os.popen("ping -c 1 " + target).readlines()
    if "TTL" in str(r):
        r = None
        return True
    r = None
    return False

def close_socket(soc):
    try:
        soc.close()
    except:
        pass

def tcp_scan(ip, port=1, timeout=2, retry=1, check_open=False):
    s=socket.socket()
    s.settimeout(timeout)
    try:
        connection=s.connect_ex((ip,port))
        s.close()
        if connection==0:
            close_socket(s)
            return True
    except:
        pass
    close_socket(s)
    return False
    """syn = IP(dst=ip) / TCP(dport=port, flags="S")
    ans, unans = sr(syn, timeout=timeout, retry=retry, verbose=0)
    for sent, received in ans:
            print(port,received[TCP].flags)
        #if check_open == True:
            if received[TCP].flags == 18:
                return True
            else:
                return False
            '''if received[TCP].flags == "RA" or received[TCP].flags == "SA":
            return True'''
    return False"""


class port_scan:
    __slots__ = ["result"]

    def scan(self,target,port,check_open,timeout,retry):
        a = tcp_scan(
            target,
            port=int(port),
            check_open=check_open,
            timeout=timeout,
            retry=retry,
        )
        if a == True:
            self.result.update({str(port): "open"})
        else:
            self.result.update({str(port): "closed"})

    def __init__(
        self,
        u,
        ports=[21, 22, 23, 25, 43, 53, 80, 443, 2082, 3306],
        threads_daemon=True,
        timeout=3,
        retry=0,
        check_open=True,
    ):
            self.result={}
        #try:
            for x in ports:
                t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={"port": self.por[x]})
                t.daemon = threads_daemon
                t.start()
                #thr.append(t)
                time.sleep(0.001)
            while len(self.result) != len(ports):
                time.sleep(0.1)
        #except:
         #   pass
            """for x in self.__dict__:
            if x != "result":
                self.__dict__[x] = None"""


def subdomains_crt(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True,subdomain_check_timeout=10, crt_timeout=120,cookie=None, user_agent=None, proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    if "://" in domain:
        domain = domain.split("://")[1].split("/")[0]
    if "www." in domain:
        domain = domain.replace("www.", "")
    if logs==True:
        print('[*] searching with crt.sh ...\n')
    try:
        r = requests.get(
            "https://crt.sh/?output=json&q=%25." + domain,
            headers=hed,
            proxies=proxy,
            timeout=crt_timeout,
            verify=False,
        ).json()
        #print(r)
        a = [x["name_value"].split("\\")[0] for x in r if ("*." not in x["name_value"])]
        l = []
        for x in a:
            if "\n" in x:
                l += x.split("\n")
            else:
                l.append(x)
        l= list(dict.fromkeys(l))
        result={}
        for x in l:
            if extract_root_domain(x)==domain:
                try:
                    r=requests.get('http://'+x,headers=hed,proxies=proxy,timeout=subdomain_check_timeout,verify=False)
                    if extract_root_domain(r.url.split('://')[1].split('/')[0])==extract_root_domain(x):
                        result.update({x:r.url})
                        if logs==True:
                            print('\t[+] {}'.format(x))
                except:
                    try:
                        result.update({x:resolve(x,server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime)})
                    except:
                        pass
        if logs==True:
            print()
        if subdomains_only==True:
            return list(result.keys())
        return result

    except Exception as ex:
        #print(ex)
        if subdomains_only==True:
            return {}
        return []

"""
def subdomains_finder(
    u, process_check_interval=5, logs=True, requests_timeout=15, https=False,proxy=None
):
    https_flag = 0
    if (https == True) or ("https://" in u):
        https_flag = 1
    if "://" in u:
        host = u.split("://")[1].split("/")[0]
    else:
        host = u
    sd = []
    while True:
        try:
            s = requests.session()
            r = s.post(
                "https://scan.penteston.com/scan_system.php",
                data={
                    "scan_method": "S201",
                    "test_protocol": https_flag,
                    "test_host": host,
                },
                timeout=requests_timeout,
                proxies=proxy
            ).text
            if '"isFinished":"no"' not in r:
                if logs == True:
                    print("\n[+]Scan results:")
                c = r.split("strong><br\/>")[1].replace('"}', "")
                for x in c.split("<br\/>"):
                    if logs == True:
                        print(x)
                    sd.append(x)
                break
            else:
                if logs == True:
                    sys.stdout.write("\r[*]Scan in progress...")
                    sys.stdout.flush()
                # print("[*]Scan in progress...")
        except KeyboardInterrupt:
            break
        except:
            pass
        try:
            time.sleep(process_check_interval)
        except KeyboardInterrupt:
            break
        except:
            pass
    return {u: sd}

"""

def get_subdomains_from_wayback(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True,user_agent=None,cookie=None,wayback_timeout=50,subdomain_check_timeout=10,max_urls=10,subdomains_only=False,proxy=None):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    subdomains = set()
    urls={}
    invalid_subd=[]
    if logs==True:
        print('[*] searching with wayback machine ...\n')
    url = "https://web.archive.org/cdx/search/cdx?url=*.{}/*&output=json&fl=original&collapse=urlkey".format(domain)
    response = requests.get(url,headers=hed,timeout=wayback_timeout,proxies=proxy)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            original_url = entry[0]
            match = re.match(r"https?://([^/]*)", original_url.split('?')[0])
            if match:
                subdomain = match.group(1)
                if subdomain not in invalid_subd and extract_root_domain(subdomain)==domain:
                    if subdomain not in urls:
                        try:
                            r=requests.get(original_url,headers=hed,timeout=subdomain_check_timeout,proxies=proxy)
                            if extract_root_domain(r.url.split('://')[1].split('/')[0])==extract_root_domain(subdomain):
                                urls[subdomain]=set()
                                urls[subdomain].add(original_url)
                                if logs==True:
                                    print('\t[+] {}'.format(subdomain))
                        #if len(urls[subdomain])<5:
                        except KeyboardInterrupt:
                            break
                        except:
                            try:
                                urls[subdomain].add(resolve(x.split(':')[0],server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime))
                                if logs==True:
                                    print('\t[+] {}'.format(subdomain))
                            except:
                                invalid_subd.append(subdomain)
                    else:
                        if len(urls[subdomain])<max_urls:
                            urls[subdomain].add(original_url)
                        subdomains.add(subdomain)
    else:
        raise("Error fetching data from Wayback Machine")
    if logs==True:
        print()
    if subdomains_only==True:
        return list(urls.keys())
    for x in urls:
        urls[x]=list(urls[x])
    return urls




def get_subdomains(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True, crt_timeout=120,user_agent=None,cookie=None,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    subs=get_subdomains_from_wayback(domain,dns_server=dns_server,resolve_timeout=resolve_timeout,resolve_lifetime=resolve_lifetime,logs=logs,cookie=cookie,wayback_timeout=wayback_timeout,user_agent=user_agent,subdomain_check_timeout=subdomain_check_timeout,max_urls=max_wayback_urls,subdomains_only=subdomains_only,proxy=proxy)
    l=subdomains_crt(domain,dns_server=dns_server,resolve_timeout=resolve_timeout,resolve_lifetime=resolve_lifetime,logs=logs,subdomain_check_timeout=subdomain_check_timeout, crt_timeout=crt_timeout,cookie=cookie, user_agent=user_agent, proxy=proxy,subdomains_only=subdomains_only)
    if type(subs)==list:
        for x in l:
            if x not in subs:
                subs.append(x)
        return subs
    for x in l:
        if x not in subs:
            subs.update({x:l[x]})
        else:
            if l[x] not in subs[x]:
                subs[x].append(l[x])
    return subs