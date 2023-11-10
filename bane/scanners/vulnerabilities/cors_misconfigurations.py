from bane.scanners.vulnerabilities.utils import *


class CORS_Misconfiguration_Scanner:

    @staticmethod
    def cors_reflection(
        u,
        proxy=None,
        timeout=10,
        user_agent=None,
        cookie=None,
        origin="www.evil-domain.com",
        debug=False,
        fill=10,
        headers={}
    ):
        a = None
        b = None
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update({"Origin": origin})
        heads.update(headers)
        try:
            r = requests.Session().get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
            a = r.get("Access-Control-Allow-Origin", None)
            b = r.get("Access-Control-Allow-Credentials", None)
            if debug == True:
                for x in r:
                    print(x + " : " + r[x])
            if a and b:
                if a == origin and b == "true":
                    return (
                        True,
                        {
                            "Access-Control-Allow-Origin": a,
                            "Access-Control-Allow-Credentials": b,
                            "Vulnerable": True,
                        },
                    )
        except:
            pass
        return (
            False,
            {
                "Access-Control-Allow-Origin": a,
                "Access-Control-Allow-Credentials": b,
                "Vulnerable": False,
            },
        )


    @staticmethod
    def cors_wildcard(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
        a = None
        b = None
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update({"Origin": "*"})
        heads.update(headers)
        try:
            r = requests.Session().get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
            a = r.get("Access-Control-Allow-Origin", None)
            b = r.get("Access-Control-Allow-Credentials", None)
            if debug == True:
                for x in r:
                    print(x + " : " + r[x])
            if a and b:
                if a == "*" and b == "true":
                    return (
                        True,
                        {
                            "Access-Control-Allow-Origin": a,
                            "Access-Control-Allow-Credentials": b,
                            "Vulnerable": True,
                        },
                    )
        except:
            pass
        return (
            False,
            {
                "Access-Control-Allow-Origin": a,
                "Access-Control-Allow-Credentials": b,
                "Vulnerable": False,
            },
        )


    @staticmethod
    def cors_null(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
        a = None
        b = None
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update({"Origin": "null"})
        heads.update(headers)
        try:
            r = requests.Session().get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
            a = r.get("Access-Control-Allow-Origin", None)
            b = r.get("Access-Control-Allow-Credentials", None)
            if debug == True:
                for x in r:
                    print(x + " : " + r[x])
            if a and b:
                if a == "null" and b == "true":
                    return (
                        True,
                        {
                            "Access-Control-Allow-Origin": a,
                            "Access-Control-Allow-Credentials": b,
                            "Vulnerable": True,
                        },
                    )
        except:
            pass
        return (
            False,
            {
                "Access-Control-Allow-Origin": a,
                "Access-Control-Allow-Credentials": b,
                "Vulnerable": False,
            },
        )




    @staticmethod
    def proxies_select(proxy, proxies):
        if proxy:
            return proxy
        if proxies:
            return random.choice(proxies)
        return None


    @staticmethod
    def cors_misconfigurations_urls(
        u,
        origin="www.evil-domain.com",
        origin_reflection=True,
        wildcard_origin=True,
        null_origin=True,
        timeout=10,
        user_agent=None,
        cookie=None,
        logs=True,
        debug=False,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None):

        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        res = {}
        if origin_reflection == True:
            if logs == True:
                print("[*] Testing for: Origin Reflection...")
            tes1 = CORS_Misconfiguration_Scanner.cors_reflection(
                u,
                origin=origin,
                cookie=cookie,
                user_agent=user_agent,
                timeout=timeout,
                proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),
                debug=debug,
                headers=headers
            )
            if tes1[0] == True:
                res.update({"cors_reflection": tes1[1],'vulnerable':True})
                if logs == True:
                    print("[+] Vulnerable !!")
            else:
                res.update({"cors_reflection": tes1[1],'vulnerable':False})
                if logs == True:
                    print("[-] Not vulnerable")
        if wildcard_origin == True:
            if logs == True:
                print("[*] Testing for: Wildcard Origin...")
            tes2 = CORS_Misconfiguration_Scanner.cors_wildcard(
                u,
                cookie=cookie,
                user_agent=user_agent,
                timeout=timeout,
                proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),
                debug=debug,
                headers=headers
            )
            if tes2[0] == True:
                res.update({"wildcard_origin": tes2[1],'vulnerable':True})
                if logs == True:
                    print("[+] Vulnerable !!")
            else:
                res.update({"wildcard_origin": tes2[1],'vulnerable':False})
                if logs == True:
                    print("[-] Not vulnerable")
        if origin_reflection == True:
            if logs == True:
                print("[*] Testing for: Null Origin...")
            tes3 = CORS_Misconfiguration_Scanner.cors_null(
                u,
                cookie=cookie,
                user_agent=user_agent,
                timeout=timeout,
                proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),
                debug=debug,
                headers=headers
            )
            if tes3[0] == True:
                res.update({"null_origin": tes3[1],'vulnerable':True})
                if logs == True:
                    print("[+] Vulnerable !!")
            else:
                res.update({"null_origin": tes3[1],'vulnerable':False})
                if logs == True:
                    print("[-] Not vulnerable")
        return res


    @staticmethod
    def scan(
        urls,
        origin="www.evil-domain.com",
        origin_reflection=True,
        wildcard_origin=True,
        null_origin=True,
        proxy=None,
        proxies=None,
        timeout=10,
        user_agent=None,
        cookie=None,
        logs=True,
        debug=False,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        l=[]
        started_at=time.time()
        for x in urls:
            if logs==True:
                print('\n\nPage: {}\n'.format(x))
            result=CORS_Misconfiguration_Scanner.cors_misconfigurations_urls(x,
                                                origin=origin,
                                                origin_reflection=origin_reflection,
                                                wildcard_origin=wildcard_origin,
                                                null_origin=null_origin,
                                                proxy=proxy,
                                                proxies=proxies,
                                                timeout=timeout,
                                                user_agent=user_agent,
                                                cookie=cookie,
                                                logs=logs,
                                                debug=debug,
                                                headers=headers,
                                                http_proxies=http_proxies,
                                                socks4_proxies=socks4_proxies,
                                                socks5_proxies=socks5_proxies
                                                )
            result={'vulnerable':result[0],'status':result[1]}
            if logs==True:
                for r in result:
                    print(r)
            l.append({'page':x,'result':result})
        return  {'result':[x for x in l if x['result']['vulnerable']!=False],'start_date':started_at,'end_date':time.time()}



