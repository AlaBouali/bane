from bane.scanners.vulnerabilities.utils import *


def exposed_git(
    u,
    user_agent=None,
    cookie=None,
    proxy=None,
    timeout=15,
    headers={}
):
    if u.endswith('/')==True:
        u+=+'.git'
    else:
        u+=+'/.git'
    if user_agent:
            us = user_agent
    else:
            us = random.choice(ua)
    if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
    else:
            hea = {"User-Agent": us}
    hea.update(headers)
    try:
        r=requests.get(u,timeout=timeout,verify=False,proxies=proxy,headers=hea)
        if "index of" in r.text.lower() and "/.git" in r.text.lower():
            return True
    except:
        return False

