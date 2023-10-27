from bane.gather_info.utils import *


def myip(proxy=None, timeout=15):
    """
    this function is for getting your ip using: ipinfo.io
    usage:
    >>>import bane
    >>>bane.myip()
    xxx.xx.xxx.xxx"""
    try:
        return requests.Session().get(
            "https://api.ipify.org",
            headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
            proxies=proxy,
            timeout=timeout,
        ).text.strip()
    except:
        pass
    return ""



def geoip(u, timeout=15, proxy=None):
    """
    this function is for getting: geoip informations
    """
    try:
        r = requests.Session().get(
            "https://geoip-db.com/jsonp/" + u,
            headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return json.loads(r.split("(")[1].split(")")[0])
    except:
        pass
    return {}


def reverse_ip_lookup(u, timeout=10, logs=True, returning=False, proxy=None):
    """
    this function is for: reverse ip look up
    if you've used it 100 times in 24 hours, your IP will be banned by "api.hackertarget.com" so i highly recommand you to use the "proxy" option by adding a http(s) proxy:

    bane.reverse_ip_lookup('XXX.XXX.XXX.XXX',proxy='IP:PORT')

    """
    try:
        r = requests.Session().get(
            "https://api.hackertarget.com/reverseiplookup/?q=" + u,
            headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return r.split("\n")
    except Exception as ex:
        pass
    return []


def check_ip_via_shodan(ip,proxy=None,timeout=15,logs=False):
    ip=socket.gethostbyname(ip)
    if logs==True:
        print('[i] IP scan via Shodan  ( in some cases they are outdated, so please verify them manually before submitting them ) :')
    try:
        d= requests.Session().get('https://internetdb.shodan.io/{}'.format(ip),headers={'User-Agent':random.choice(Common_Variables.user_agents_list)},proxies=proxy,timeout=timeout).json()
        v={}
        for x in d['vulns']:
            v.update({x:['https://www.cve.org/CVERecord?id='+x,'https://nvd.nist.gov/vuln/detail/'+x,'https://cve.mitre.org/cgi-bin/cvename.cgi?name='+x]})
        del d['vulns']
        d['exploits']=v
        if logs==True:
            print()
            print('[+] CPEs:')
            print()
            for x in d['cpes']:
                print(x)
            print() 
            print('[+] Hostnames:')
            print()
            for x in d['hostnames']:
                print(x)
            print() 
            print('[+] Open ports:')
            print()
            for x in d['ports']:
                print(x)
            print() 
            print('[+] Shodan tags:')
            print()
            for x in d['tags']:
                print(x)
            print() 
            print('[+] Exploits URLs :')
            print()
            for x in d['exploits']:
                for i in d['exploits'][x]:
                    print(i)
            print() 
                    
        return d
    except:
        return {}