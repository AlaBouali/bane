from bane.bruteforce.utils import *

class Admin_Panel_Finder:
    __slots__ = ["stop", "finish", "result", "logs"]

    def done(self):
        return self.finish


    def __init__(
        self,
        target,  # (str) The target website URL
        logs=True,  # (bool) Enable or disable logging (default is True)
        threads_daemon=True,  # (bool) Set thread as daemon (default is True)
        user_agent=None,  # (str) Custom User-Agent header for requests
        cookie=None,  # (str) Custom cookies to include in requests
        ext="php",  # (str) Extension to use for URLs (default is 'php')
        timeout=10,  # (int) Request timeout in seconds (default is 10)
        headers={},  # (dict) Additional HTTP headers to include
        http_proxies=None,  # (list) List of HTTP proxies to use
        socks4_proxies=None,  # (list) List of SOCKS4 proxies to use
        socks5_proxies=None  # (list) List of SOCKS5 proxies to use
    ):
        """
        This function searches for potential admin panel URLs on a website using a predefined list of extensions.

        Parameters:
        - target (str): The target website URL.
        - logs (bool): Enable or disable logging (default is True).
        - threads_daemon (bool): Set thread as daemon (default is True).
        - user_agent (str): Custom User-Agent header for requests.
        - cookie (str): Custom cookies to include in requests.
        - ext (str): Extension to use for URLs (default is 'php').
        - timeout (int): Request timeout in seconds (default is 10).
        - headers (dict): Additional HTTP headers to include.
        - http_proxies (list): List of HTTP proxies to use.
        - socks4_proxies (list): List of SOCKS4 proxies to use.
        - socks5_proxies (list): List of SOCKS5 proxies to use.
        """
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                target,
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
        target,
        timeout,
        logs,
        ext,
        user_agent,
        cookie,
        proxies,
        headers
    ):
        u=target
        links = []
        ext = ext.strip()
        if ext.lower() == "php":
            links = Common_Variables.php_urls_list
        elif ext.lower() == "asp":
            links = Common_Variables.asp_urls_list
        elif ext.lower() == "aspx":
            links = Common_Variables.aspx_urls_list
        elif ext.lower() == "js":
            links = Common_Variables.js_urls_list
        elif ext == "/":
            links = Common_Variables.slash_urls_list
        elif ext.lower() == "cfm":
            links = Common_Variables.cfm_urls_list
        elif ext.lower() == "cgi":
            links = Common_Variables.cgi_urls_list
        elif ext.lower() == "brf":
            links = Common_Variables.brf_urls_list
        elif ext.lower() == "html":
            links = Common_Variables.html_urls_list
        k = []
        for i in links:
            if self.stop == True:
                break
            try:
                proxy = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(Common_Variables.user_agents_list)
                hed = {"User-Agent": us}
                if cookie:
                    hed.update({"Cookie": cookie})
                hed.update(headers)
                if u[len(u) - 1] == "/":
                    u = u[0 : len(u) - 1]
                g = u + i
                if logs == True:
                    print("[*]Trying:", g)
                r = requests.Session().get(
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

