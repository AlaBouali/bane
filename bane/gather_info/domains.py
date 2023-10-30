from bane.gather_info.utils import *

class Domain_Info:

    @staticmethod
    def whois(u,proxy=None,cookie=None,user_agent=None,timeout=10,headers={}):
        h={}
        if user_agent:
            h.update({"User-Agent": user_agent})
        else:
            h.update({"User-Agent": random.choice(Common_Variables.user_agents_list)})
        if cookie:
            h.update({"Cookie": cookie})
        h.update(headers)
        try:
            r = requests.Session().post("https://check-host.net/ip-info/whois",timeout=timeout,proxies=proxy,headers=h, data={"host": u})
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


    @staticmethod
    def info(u, timeout=10, proxy=None,user_agent=None, cookie=None,headers={}):
        hd={}
        if user_agent:
            hd.update({"User-Agent": user_agent})
        else:
            hd.update({"User-Agent": random.choice(Common_Variables.user_agents_list)})
        if cookie:
            hd.update({"Cookie": cookie})
        hd.update(headers)
        
        try:
            h = ""
            u = "https://check-host.net/ip-info?host=" + u
            c = requests.Session().get(
                u, headers=hd, proxies=proxy, timeout=timeout
            ).text
            soup = BeautifulSoup(c, "html.parser")
            la = soup.find_all("a")
            l = []
            for i in la:
                if "#ip_info-dbip" in str(i):
                    l.append(Userful_Utilities.remove_html_tags(str(i)).strip().replace("\n", " "))
                if "#ip_info-ip2location" in str(i):
                    l.append(Userful_Utilities.remove_html_tags(str(i)).strip().replace("\n", " "))
                if "#ip_info-geolite2" in str(i):
                    l.append(Userful_Utilities.remove_html_tags(str(i)).strip().replace("\n", " "))
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
                            d = Userful_Utilities.remove_html_tags(d).strip().replace("\n", " ")
                            do.update({c: d})
                        except:
                            pass
                    di.update({l[o]: do})
                    o += 1
                except:
                    pass
            return di
        except:
            return None


    @staticmethod
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

    @staticmethod
    def get_domain_info(domain,headers={},timeout=10,proxy=None,user_agent=None,cookie=None,resolve_server='8.8.8.8',resolve_timeout=1,resolve_lifetime=1):
        d={'resolved_host':Domain_Info.resolve(domain,server=resolve_server,timeout=resolve_timeout,lifetime=resolve_lifetime)}
        d.update({'info':Domain_Info.info(domain,headers=headers,proxy=proxy,timeout=timeout,user_agent=user_agent,cookie=cookie)})
        d.update({'whois':Domain_Info.whois(domain,headers=headers,proxy=proxy,timeout=timeout,user_agent=user_agent,cookie=cookie)})
        return d