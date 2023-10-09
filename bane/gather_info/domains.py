from bane.gather_info.utils import *


def whois(u):
    try:
        r = requests.Session().post("https://check-host.net/ip-info/whois", data={"host": u})
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
        c = requests.Session().get(
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

