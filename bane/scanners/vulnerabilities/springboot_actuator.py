from bane.scanners.vulnerabilities.utils import *

def springboot_actuator(u,user_agent=None,cookie=None,proxy=None,timeout=None,path='/actuator',headers={}):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    try:
        return requests.Session().get(
            u + path,
            headers=hed,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        ).json()
    except:
        pass
