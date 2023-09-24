from bane.scanners.vulnerabilities.utils import *

def exposed_env(
    u,
    user_agent=None,
    cookie=None,
    proxies=None,
    proxy=None,
    path="",
    brute_force=True,
    timeout=15,
):
    if brute_force == False:
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
        else:
            hea = {"User-Agent": us}
        try:
            if urlparse(u).path == "/":
                u += path + ".env"
            elif len(urlparse(u).path) < 1:
                u += path + "/.env"
            else:
                u = u.replace(urlparse(u).path, path + "/.env")
            c = requests.get(
                u, headers=hea, proxies=proxy, timeout=timeout, verify=False
            ).text
            if ("APP_KEY=" in c) or ("DB_HOST=" in c):
                return (True, u)
        except:
            pass
        return (False, "")
    else:
        for x in env_paths:
            if proxy:
                proxy = proxy
            if proxies:
                proxy = random.choice(proxies)
            a = exposed_env(
                u,
                user_agent=user_agent,
                cookie=cookie,
                proxy=proxy,
                path=x,
                timeout=timeout,
            )
            if a[0] == True:
                return a
        return (False, "")

