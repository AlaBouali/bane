from bane.scanners.vulnerabilities.utils import *

class ClickJacking_Scanner:

    @staticmethod
    def scan(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=False,request_headers=None,headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update(headers)
        try:
            if request_headers==None:
                r = requests.Session().get(
                    u, headers=heads, proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies), timeout=timeout, verify=False
                ).headers
            else:
                r=request_headers
            click = True
            for x in r:
                if x.lower().strip() == "x-frame-options":
                    click = False
                if logs == True:
                    print(x + " : " + r[x])
        except:
            return False
        return click


