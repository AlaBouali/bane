from bane.bruteforce.services_login import *


class Hydra:
    __slots__ = ["stop", "finish", "result", "logs"]

    def __init__(
        self,
        u,
        p=22,
        protocol="ssh",
        word_list=[],
        threads_daemon=True,
        logs=True,
        exchange_key=None,
        timeout=5,
        ehlo=False,
        helo=True,
        ttls=False,
        user_agent=None,
        cookie=None,
        headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        s_proxies=Proxies_Interface.get_socket_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        socket_proxies=[x for x in s_proxies if x['proxy_type'] in ['socks4','socks5','s4','s5']]
        if socket_proxies==[]:
            socket_proxies=[{'proxy_host':None,'proxy_port':None,'proxy_username':None,'proxy_password':None,'proxy_type':None}]
        word_list=Userful_Utilities.load_word_list(word_list)
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                p,
                protocol,
                word_list,
                logs,
                exchange_key,
                timeout,
                ehlo,
                helo,
                ttls,
                proxies,
                socket_proxies,
                user_agent,
                cookie,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        p,
        protocol,
        word_list,
        logs,
        exchange_key,
        timeout,
        ehlo,
        helo,
        ttls,
        proxies,
        socket_proxies,
        user_agent,
        cookie,
        headers
    ):
        o = ""
        if protocol == "telnet":
            s = Services_Login.telnet
        if protocol == "ssh":
            s = Services_Login.ssh
        if protocol == "ftp":
            s = Services_Login.ftp
        if protocol == "smtp":
            s = Services_Login.smtp
        if protocol == "mysql":
            s = Services_Login.mysql
        if protocol == "wp":
            s = WordPress_Scanner.admin_login
        for x in word_list:
            if self.stop == True:
                break
            user = x.split(":")[0].strip()
            pwd = x.split(":")[1].strip()
            if self.logs == True:
                print("[*]Trying ==> {}:{}".format(user, pwd))
            if protocol == "ssh":
                r = s(u, user, pwd, timeout=timeout, p=p, exchange_key=exchange_key,**Vulnerability_Scanner_Utilities.setup_proxy(socket_proxies))
            elif protocol == "telnet":
                r = s(u, user, pwd, timeout=timeout, p=p,**Vulnerability_Scanner_Utilities.setup_proxy(socket_proxies))
            elif protocol == "mysql":
                r = s(u, user, pwd, timeout=timeout, p=p,**Vulnerability_Scanner_Utilities.setup_proxy(socket_proxies))
            elif protocol == "ftp":
                r = s(u, user, pwd, timeout=timeout,**Vulnerability_Scanner_Utilities.setup_proxy(socket_proxies))
            elif protocol == "wp":
                r = s(
                    u,
                    user,
                    pwd,
                    http_proxies=proxies,
                    user_agent=user_agent,
                    cookie=cookie,
                    timeout=timeout,
                    headers=headers
                )
            elif protocol == "smtp":
                r = s(u, p, user, pwd, ehlo=ehlo, helo=helo, ttls=ttls,**Vulnerability_Scanner_Utilities.setup_proxy(socket_proxies))
            else:
                r = s(u, user, pwd, timeout=timeout,**Vulnerability_Scanner_Utilities.setup_proxy(socket_proxies))
            if r == True:
                if self.logs == True:
                    print("[+]Found!!!")
                o = "{}:{}".format(user, pwd)
                break
            else:
                if self.logs == True:
                    print("[-]Failed")
        self.result = {u: o}
        self.finish = True


