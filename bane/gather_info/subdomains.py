from bane.gather_info.utils import *
from bane.gather_info.domains import resolve

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