from bane.bruteforce.utils import *

class admin_panel_finder:
    __slots__ = ["stop", "finish", "result", "logs"]

    def done(self):
        return self.finish

    """
   this function use a list of possible admin panel links with different extensions: php, asp, aspx, js, /, cfm, cgi, brf and html.
   
   ext: (set by default to: 'php') to define the link's extention.

   usage:

  >>>import bane
  >>>bane.admin_panel_finder('http://www.example.com',ext='php',timeout=7)

  >>>bane.admin_panel_finder('http://www.example.com',ext='aspx',timeout=5)
 """

    def __init__(
        self,
        u,
        logs=True, 
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        ext="php",
        timeout=10,
        proxy=None,
        proxies=None,
        headers={}
    ):
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
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
        timeout,
        logs,
        ext,
        user_agent,
        cookie,
        proxy,
        proxies,
        headers
    ):
        links = []
        ext = ext.strip()
        if ext.lower() == "php":
            links = phpl
        elif ext.lower() == "asp":
            links = aspl
        elif ext.lower() == "aspx":
            links = aspxl
        elif ext.lower() == "js":
            links = jsl
        elif ext == "/":
            links = slashl
        elif ext.lower() == "cfm":
            links = cfml
        elif ext.lower() == "cgi":
            links = cgil
        elif ext.lower() == "brf":
            links = brfl
        elif ext.lower() == "html":
            links = htmll
        k = []
        for i in links:
            if self.stop == True:
                break
            try:
                if proxies:
                    proxy = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {"User-Agent": us}
                if cookie:
                    hed.update({"Cookie": cookie})
                hed.update(headers)
                if u[len(u) - 1] == "/":
                    u = u[0 : len(u) - 1]
                g = u + i
                if logs == True:
                    print("[*]Trying:", g)
                r = requests.get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.codes.ok:
                    if logs == True:
                        print("[+]FOUND!!!")
                    k.append(g)
                else:
                    if logs == True:
                        print("[-]failed")
            except KeyboardInterrupt:
                break
            except Exception as e:
                if logs == True:
                    print("[-]Failed")
        self.result = {u: k}
        self.finish = True

