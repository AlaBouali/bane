from bane.bruteforce.utils import *




class Force_Browsing:
    __slots__ = ["stop", "finish", "result", "logs"]

    @staticmethod
    def access(u, timeout=10, user_agent=None, cookie=None, bypass=False, proxy=None,headers={}):
        if bypass == True:
            u += "#"
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        try:
            r = requests.Session().get(
                u,
                headers=hed,
                allow_redirects=False,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            )
            if r.status_code == requests.codes.ok:
                if ("Uncaught exception" not in r.text) or ("404 Not Found" not in r.text):
                    return True
        except Exception as e:
            pass
        return False



    def __init__(
        self,
        u,
        timeout=10,
        threads_daemon=True,
        logs=True,
        ext="php",
        user_agent=None,
        cookie=None,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.stop = False
        self.finish = False
        self.result = {}
        self.logs = logs
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                timeout,
                logs,
                ext,
                user_agent,
                cookie,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        timeout=10,
        logs=True,
        ext="php",
        user_agent=None,
        cookie=None,
        proxies=None,
    ):
        l = []
        if u[len(u) - 1] == "/":
            u = u[0 : len(u) - 1]
        for x in Common_Variables.inner_urls_list:
            if self.stop == True:
                break
            g = u + x + "." + ext
            if self.logs == True:
                print("[*]Trying:", g)
            try:
                proxy=random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(Common_Variables.user_agents_list)
                h = Force_Browsing.access(g, user_agent=us, cookie=cookie, proxy=proxy)
            except KeyboardInterrupt:
                break
            if h == True:
                l.append(g)
                if self.logs == True:
                    print("[+]FOUND!!!")
            else:
                if self.logs == True:
                    print("[-]Failed")
        self.result = {u: l}
        self.finish = True

    def done(self):
        return self.finish

