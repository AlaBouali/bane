from bane.scanners.vulnerabilities.utils import *

class Exposed_Git_Scanner:

        @staticmethod
        def scan(u,user_agent=None,cookie=None,timeout=15,headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
                proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
                if u.endswith('/')==True:
                        u+=+'.git'
                else:
                        u+=+'/.git'
                if user_agent:
                        us = user_agent
                else:
                        us = random.choice(Common_Variables.user_agents_list)
                if cookie:
                        hea = {"User-Agent": us, "Cookie": cookie}
                else:
                        hea = {"User-Agent": us}
                hea.update(headers)
                try:
                        r=requests.Session().get(u,timeout=timeout,verify=False,proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies),headers=hea)
                        if "index of" in r.text.lower() and "/.git" in r.text.lower():
                                return True
                except:
                        return False

