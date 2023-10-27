from bane.gather_info.utils import *



def norton_rate(u, timeout=30, proxy=None):
    """
    this function takes any giving and gives a security report from: safeweb.norton.com, if it is a: spam domain, contains a malware...
    it takes 3 arguments:
    u: the link to check
    logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
    returning: (set by default to: False) returning the report as a string format if it is set to: True.
    usage:
    >>>import bane
    >>>url='http://www.example.com'
    >>>bane.norton_rate(domain)"""
    try:
        ur = urllib.quote(u, safe="")
        ul = "https://safeweb.norton.com/report/show?url=" + ur
        c = requests.Session().et(
            ul,
            headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(c, "html.parser")
        s = soup.find_all("div", class_="communityRatings")
        s = remove_html_tags(str(s[0])).strip().split("\n")
        while "" in s:
            s.remove("")
        try:
            return {"Profile": s[0], "Rate": float(s[1]), "By": s[2]}
        except:
            return {"Profile": s[0], "Rate": float(s[1])}
    except:
        pass


def http_options(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(Common_Variables.user_agents_list)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        s = requests.session()
        a = s.options(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return []
    b = []
    if "Access-Control-Allow-Methods" in a:
        b += [x.strip() for x in a["Access-Control-Allow-Methods"].split(",")]
    if "Allow" in a:
        b += [x.strip() for x in a["Allow"].split(",")]
    return b


def headers(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(Common_Variables.user_agents_list)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        #"safe": sec,
        s = requests.session()
        a = s.get(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return None
    if logs == True:
        for x in a:
            print("{} : {}".format(x, a[x]))
    if returning == True:
        return a


def webhint_report(ur, proxy=None, timeout=10):
    """
    this function takes any webpage link and returns a report link from webhint.io."""
    u = "https://webhint.io/scanner/"
    r = ""
    if "://" not in ur:
        return r
    try:
        s = requests.session()
        s.get(u, proxies=proxy, timeout=timeout)
        data = {"url": ur}
        a = s.post(u, data, proxies=proxy, timeout=timeout).text
        soup = BeautifulSoup(a, "html.parser")
        s = soup.find_all("span", class_="permalink-content")
        for x in s:
            try:
                r = x.a["href"]
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return r

