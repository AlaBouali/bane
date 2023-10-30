from bane.bruteforce.utils import *

class filemanager_finder:
    __slots__ = ["logs", "stop", "finish", "result"]

    def __init__(
        self,
        u,
        logs=True,
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                user_agent,
                cookie,
                timeout,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(self, u, user_agent, cookie, timeout, proxies,headers):
        for i in Common_Variables.manager_urls_list:
            if self.stop == True:
                self.finish = True
                break
            if user_agent:
                us = user_agent
            else:
                us = random.choice(Common_Variables.user_agents_list)
            hed = {"User-Agent": us}
            if cookie:
                hed.update({"Cookie": cookie})
            hed.update(headers)
            try:
                if u[len(u) - 1] == "/":
                    u = u[0 : len(u) - 1]
                g = u + i
                r = requests.Session().get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies),
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.codes.ok:
                    if (
                        ("Uncaught exception" not in r.text)
                        and ("404 Not Found" not in r.text)
                        and ("could not be found" not in r.text)
                    ):
                        self.finish = True
                        if self.logs == True:
                            sys.stdout.write(
                                "\rStats: {}/{} | Found: {}  ".format(
                                    Common_Variables.manager_urls_list.index(g), len(Common_Variables.manager_urls_list), self.finish
                                )
                            )
                            sys.stdout.flush()
                        self.result.update({u: g})
                        break
                    else:
                        if self.logs == True:
                            sys.stdout.write(
                                "\rStats: {}/{} | Found: {}  ".format(
                                    Common_Variables.manager_urls_list.index(g), len(Common_Variables.manager_urls_list), self.finish
                                )
                            )
                            sys.stdout.flush()
                else:
                    if self.logs == True:
                        sys.stdout.write(
                            "\rStats: {}/{} | Found: {}  ".format(
                                Common_Variables.manager_urls_list.index(g), len(Common_Variables.manager_urls_list), self.finish
                            )
                        )
                        sys.stdout.flush()
            except KeyboardInterrupt:
                break
            except Exception as e:
                pass
        self.finish = True

    def done(self):
        return self.finish
