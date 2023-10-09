from bane.bruteforce.utils import *


def access(u, timeout=10, user_agent=None, cookie=None, bypass=False, proxy=None,headers={}):
    if bypass == True:
        u += "#"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u,
            headers={"User-Agent": random.choice(ua)},
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



class force_browsing:
    __slots__ = ["stop", "finish", "result", "logs"]

    def __init__(
        self,
        u,
        timeout=10,
        threads_daemon=True,
        logs=True,
        ext="php",
        user_agent=None,
        cookie=None,
        proxy=None,
        proxies=None,
        headers={}
    ):
        """
        this function is using "Forced Browsing" technique which is aim to access restricted areas without providing any credentials!!!
        it is used here to gain access to admin control panel by trying different possible combinations of links with the given URL.
        it's possible to do that and this a proof of concept that unserured cpanels with lack of right sessions configurations can be
        accessed just by guessing the right links :)

        the function takes those arguments:

        u: the targeted link which should be leading to the control panel, example:
        http://www.example.com/admin/login.php
        you have to delete 'login.php' and insert the rest of the link in the function like this:

        >>>import bane
        >>>bane.force_browsing('http://www.example.com/admin/')

        then the function will try to find possible accesseble links:

        http://www.example.com/admin/edit.php
        http://www.example.com/admin/news.php
        http://www.example.com/admin/home.php

        timeout: (set by default to 10) timeout flag for the request
        logs: (set by default to: True) showing the process of the attack, you can turn it off by setting it to: False
        returning: (set by default to: False) return a list of the accessible link(s), to make the function return the list, set to: True
        mapping: (set by default to: True) find all possible links, to make stop if it has found 1 link just set it to: False
        ext: (set by default to: "php") it helps you to find links with the given extention, cuurentky it supports only 3 extentions: "php", "asp" and "aspx"( any other extention won't be used)."""
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
                proxy,
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
        proxy=None,
        proxies=None,
    ):
        l = []
        if u[len(u) - 1] == "/":
            u = u[0 : len(u) - 1]
        for x in innerl:
            if self.stop == True:
                break
            g = u + x + "." + ext
            if self.logs == True:
                print("[*]Trying:", g)
            try:
                if proxy:
                    proxy = proxy
                if proxies:
                    proxy=random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                h = access(g, user_agent=us, cookie=cookie, proxy=proxy)
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

