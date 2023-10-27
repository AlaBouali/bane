from bane.scanners.vulnerabilities.utils import *

def exposed_env(
    u,
    user_agent=None,
    cookie=None,
    path="",
    brute_force=False,
    timeout=15,
    headers={},
    http_proxies=None,
    socks4_proxies=None,
    socks5_proxies=None
    ):
    proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
    if brute_force == False:
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
            if urlparse(u).path == "/":
                u += path + ".env"
            elif len(urlparse(u).path) < 1:
                u += path + "/.env"
            else:
                u = u.replace(urlparse(u).path, path + "/.env")
            c = requests.Session().get(
                u, headers=hea, proxies=setup_proxy(proxies), timeout=timeout, verify=False
            ).text
            if ("APP_KEY=" in c) or ("DB_HOST=" in c):
                return (True, u)
        except:
            pass
        return (False, "")
    else:
        for x in Common_Variables.env_paths:
            proxy = random.choice(proxies)
            a = exposed_env(
                u,
                user_agent=user_agent,
                cookie=cookie,
                proxy=proxy,
                path=x,
                timeout=timeout,
                headers=headers
            )
            if a[0] == True:
                return a
        return (False, "")

