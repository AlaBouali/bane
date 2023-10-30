from bane.gather_info.network import *


class Ports_Scanner:
        __slots__ = ["result"]

        def scan(self,target,port,check_open,timeout,retry):
            a = Network_Info.tcp_scan(
                target,
                port=int(port),
                check_open=check_open,
                timeout=timeout,
                retry=retry,
                proxy=None
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

