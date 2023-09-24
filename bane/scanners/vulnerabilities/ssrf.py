from bane.scanners.vulnerabilities.utils import *


def ssrf_check(
    u,
    null_byte=False,
    link="http://www.google.com",
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    timeout=25,
    user_agent=None,
    cookie=None,
):
    """
    this function is for FI vulnerability test using a link"""
    l = link
    if proxies:
        proxy = random.choice(proxies)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    heads.update(
        {
            "Referer": u,
            "Origin": u.split("://")[0] + "://" + u.split("://")[1].split("/")[0],
        }
    )
    if "=" not in u:
        return (False, "")
    if null_byte == True:
        l += "%00"
    try:
        r = requests.get(
            u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
        )
        if (signature in r.text) or (r.status_code == 504):
            return (True, r.url)
    except Exception as e:
        if "Read timed out" in str(e):
            return (True, u.format(l))
    return (False, "")


def ssrf_urls(
    u,
    null_byte=False,
    link="http://www.google.com",
    timeout=120,
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
):
    res = []
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent)
    l = []
    d = a.values()
    for x in d:
        if len(x[3]) > 0:
            l.append(x)
    o = []
    for x in l:
        ur = x[1]
        if ur.split("?")[0] not in o:
            o.append(ur.split("?")[0])
            if (
                ur.split("?")[0][-1] != "/"
                and "." not in ur.split("?")[0].rsplit("/", 1)[-1]
            ):
                ur = ur.replace("?", "/?")
            for y in x[3]:
                if valid_parameter(y[1]) == True:
                    trgt = ur.replace(y[0] + "=" + y[1], y[0] + "={}")
                    q = ssrf_check(
                        trgt,
                        null_byte=null_byte,
                        proxy=proxy,
                        link=link,
                        signature=signature,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
    return res

def ssrf(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    link="http://www.google.com",
    timeout=120,
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=ssrf_urls(x,
                        null_byte=null_byte,
                        link=link,
                        timeout=timeout,
                        signature=signature,
                        proxy=proxy,
                        proxies=proxies,
                        user_agent=user_agent,
                        cookie=cookie)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]



def ssrf(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    link="http://www.google.com",
    timeout=120,
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=ssrf_urls(x,
                        null_byte=null_byte,
                        link=link,
                        timeout=timeout,
                        signature=signature,
                        proxy=proxy,
                        proxies=proxies,
                        user_agent=user_agent,
                        cookie=cookie)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]

