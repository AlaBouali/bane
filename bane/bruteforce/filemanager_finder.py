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
        proxy=None,
        proxies=None,
        headers={}
    ):
        """
        u: the link: http://www.example.com
        logs: (set by default to True) the show the process and requests
        mapping: (set by default to: False) if it is set to True, it will stop the prcess when it finds the link, else: it continue for more
        possible links
        returning: (set by default to: False) if you want it to return a list of possibly accesseble links to be used in your scripts set it to: True
        timeout: (set by default to 10) timeout flag for the requests

        usage:

        >>>import bane
        >>>url='http://www.example.com/'
        >>>bane.filemanager_finder(url)
        """
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
                proxy,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(self, u, user_agent, cookie, timeout, proxy, proxies,headers):
        for i in manager:
            if self.stop == True:
                self.finish = True
                break
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            hed = {"User-Agent": us}
            if cookie:
                hed.update({"Cookie": cookie})
            hed.update(headers)
            try:
                if u[len(u) - 1] == "/":
                    u = u[0 : len(u) - 1]
                g = u + i
                r = requests.get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
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
                                    manager.index(g), len(manager), self.finish
                                )
                            )
                            sys.stdout.flush()
                        self.result.update({u: g})
                        break
                    else:
                        if self.logs == True:
                            sys.stdout.write(
                                "\rStats: {}/{} | Found: {}  ".format(
                                    manager.index(g), len(manager), self.finish
                                )
                            )
                            sys.stdout.flush()
                else:
                    if self.logs == True:
                        sys.stdout.write(
                            "\rStats: {}/{} | Found: {}  ".format(
                                manager.index(g), len(manager), self.finish
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
