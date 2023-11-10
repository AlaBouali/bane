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
                        x.split(":")[0].replace('&gt;&gt;&gt;','').replace('&lt;&lt;&lt;','')
                        .strip(): x.replace(x.split(":")[0].strip().replace('&gt;&gt;&gt;','').replace('&lt;&lt;&lt;',''), "")
                        .strip()[1:].replace('&gt;&gt;&gt;','').replace('&lt;&lt;&lt;','').replace('gt;&gt;&gt;:','')
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
                if "#ip_info-" in i.get('href'):
                    l.append(Userful_Utilities.remove_html_tags(str(i)).strip().replace("\n", " ").split('(')[0].strip().replace(' ','_').replace('-','_').replace('.','_'))
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
                            if "<strong" in str(a[1]):
                                c = a[0].find('strong').get_text().lower().replace(' ','_').replace('-','_').replace('.','_')
                            else:
                                c = a[0].get_text().lower().replace(' ','_').replace('-','_').replace('.','_')
                            if "<strong" in str(a[1]):
                                d = a[1].find('strong').get_text()
                            else:
                                 d = a[1].get_text()
                            d = Userful_Utilities.remove_html_tags(d).strip().replace("\n", " ")
                            do.update({c: d})
                        except Exception as ex:
                            pass
                    di.update({l[o]: do})
                    o += 1
                except Exception as exx:
                            pass
            return di
        except Exception as exxx:
                            pass


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
        started_at=time.time()
        d={'resolved_host':Domain_Info.resolve(domain,server=resolve_server,timeout=resolve_timeout,lifetime=resolve_lifetime)}
        d.update({'info':Domain_Info.info(domain,headers=headers,proxy=proxy,timeout=timeout,user_agent=user_agent,cookie=cookie)})
        d.update({'whois':Domain_Info.whois(domain,headers=headers,proxy=proxy,timeout=timeout,user_agent=user_agent,cookie=cookie)})
        d.update({'start_date':started_at,'end_date':time.time()})
        return d