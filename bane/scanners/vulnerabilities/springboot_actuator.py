from bane.scanners.vulnerabilities.utils import *

class SpringBoot_Actuator_Exploit_Scanner:

    @staticmethod
    def scan(u,user_agent=None,cookie=None,timeout=None,path='/actuator',headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if u[len(u) - 1] == "/":
            u = u[0 : len(u) - 1]
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        try:
            return requests.Session().get(
                u + path,
                headers=hed,
                proxies=setup_proxy(proxies),
                timeout=timeout,
                verify=False,
            ).json()
        except:
            pass
