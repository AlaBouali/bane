from bane.gather_info.network import *
from bane.utils.proxer import *


class Ports_Scanner:
        __slots__ = ["result","proxies"]

        def scan(self,target,port,check_open,timeout,retry):
            a = Network_Info.tcp_scan(
                target,
                port=int(port),
                check_open=check_open,
                timeout=timeout,
                retry=retry,
                **random.choice(self.proxies)
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
            check_open=True,http_proxies=None,
            socks4_proxies=None,
            socks5_proxies=None,
            ):
                self.proxies=Proxies_Interface.get_socket_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
                self.proxies=[x for x in self.proxies if x['proxy_type'] in ['socks4','socks5','s4','s5']]
                if self.proxies==[]:
                    self.proxies=[{'proxy_host':None,'proxy_port':None,'proxy_username':None,'proxy_password':None,'proxy_type':None}]
                self.result={}
            #try:
                started_at=time.time()
                for x in ports:
                    t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={"port": self.por[x]})
                    t.daemon = threads_daemon
                    t.start()
                    #thr.append(t)
                    time.sleep(0.001)
                while len(self.result) != len(ports):
                    time.sleep(0.1)
                self.result={'result':self.result.copy(),'start_date':started_at,'end_date':time.time()}
            #except:
            #   pass
                """for x in self.__dict__:
                if x != "result":
                    self.__dict__[x] = None"""

