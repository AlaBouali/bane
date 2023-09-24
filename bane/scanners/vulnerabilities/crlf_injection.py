from bane.scanners.vulnerabilities.utils import *


def set_requests(
    u, method="GET", data={}, files={}, params={}, headers={}, proxy={}, timeout=15
):
    s = requests.Session()
    req = requests.Request(
        method=method, url=u, headers=headers, data=data, files=files, params=params
    )
    prep = req.prepare()
    prep.url = u
    return s.send(prep, verify=False, proxies=proxy, timeout=timeout)


def crlf_unicode_encode(
    random_level=0, line_feed_only=False, carriage_return_only=False
):
    if line_feed_only == False and carriage_return_only == False:
        if random_level == 1:
            return random.choice(["%E5%98%8D", "%0d"]) + random.choice(
                ["%E5%98%8A", "%0a"]
            )
        if random_level == 2:
            return "%E5%98%8D%E5%98%8A"
        else:
            return "%0d%0a"
    else:
        if line_feed_only == True and carriage_return_only == False:
            if random_level == 1:
                return random.choice(["%E5%98%8A", "%0a"])
            if random_level == 2:
                return "%E5%98%8A"
            else:
                return "%0a"
        if carriage_return_only == True and line_feed_only == False:
            if random_level == 1:
                return random.choice(["%E5%98%8D", "%0d"])
            if random_level == 2:
                return "%E5%98%8D"
            else:
                return "%0d"
    return "%0d%0a"


def crlf_header_injection(
    u,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + "banetest:%20test",
            method="GET",
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return "banetest" in r.headers
    except Exception as e:
        pass
    return False


def crlf_body_injection(
    u,
    proxy=None,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + "banetest:%20test",
            method="GET",
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return "banetest;$@*" in r.text
    except Exception as e:
        pass
    return False

