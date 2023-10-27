from bane.gather_info.utils import *

class NETWORk:

    @staticmethod
    def get_local_ip():
        try:
            return [
                l
                for l in (
                    [
                        ip
                        for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                        if not ip.startswith("127.")
                    ][:1],
                    [
                        [
                            (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                            for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                        ][0][1]
                    ],
                )
                if l
            ][0][0]
        except:
            return "127.0.0.1"


    @staticmethod
    def host_alive(target):
        if os.name == "nt":
            r = os.popen("ping -n 1 " + target).readlines()
        else:
            r = os.popen("ping -c 1 " + target).readlines()
        if "TTL" in str(r):
            r = None
            return True
        r = None
        return False

    @staticmethod
    def close_socket(soc):
        try:
            soc.close()
        except:
            pass

    @staticmethod
    def tcp_scan(ip, port=1, timeout=2, retry=1, check_open=False):
        s=socket.socket()
        s.settimeout(timeout)
        try:
            connection=s.connect_ex((ip,port))
            s.close()
            if connection==0:
                NETWORk.close_socket(s)
                return True
        except:
            pass
        NETWORk.close_socket(s)
        return False
        """syn = IP(dst=ip) / TCP(dport=port, flags="S")
        ans, unans = sr(syn, timeout=timeout, retry=retry, verbose=0)
        for sent, received in ans:
                print(port,received[TCP].flags)
            #if check_open == True:
                if received[TCP].flags == 18:
                    return True
                else:
                    return False
                '''if received[TCP].flags == "RA" or received[TCP].flags == "SA":
                return True'''
        return False"""




class port_scan:
        __slots__ = ["result"]

        def scan(self,target,port,check_open,timeout,retry):
            a = NETWORk.tcp_scan(
                target,
                port=int(port),
                check_open=check_open,
                timeout=timeout,
                retry=retry,
            )
            if a == True:
                self.result.update({str(port): "open"})
            else:
                self.result.update({str(port): "closed"})

        def __init__(
            self,
            u,
            ports=[21, 22, 23, 25, 43, 53, 80, 443, 2082, 3306],
            threads_daemon=True,
            timeout=3,
            retry=0,
            check_open=True,
        ):
                self.result={}
            #try:
                for x in ports:
                    t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={"port": self.por[x]})
                    t.daemon = threads_daemon
                    t.start()
                    #thr.append(t)
                    time.sleep(0.001)
                while len(self.result) != len(ports):
                    time.sleep(0.1)
            #except:
            #   pass
                """for x in self.__dict__:
                if x != "result":
                    self.__dict__[x] = None"""

