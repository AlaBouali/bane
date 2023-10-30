from bane.gather_info.utils import *

class Network_Info:

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
    def tcp_scan(ip, port=1, timeout=2, proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
        s = socks.socksocket()
        s.settimeout(timeout)
        if proxy_type==4 or proxy_type=='socks4' or proxy_type=='s4':
                s.setproxy( 
                            proxy_type=socks.SOCKS4,
                            addr=proxy_host,
                            port=proxy_port,
                            username=proxy_username,
                            password=proxy_password,
                    )
        elif proxy_type==5 or proxy_type=='socks5' or proxy_type=='s5':
                s.setproxy( 
                            proxy_type=socks.SOCKS5,
                            addr=proxy_host,
                            port=proxy_port,
                            username=proxy_username,
                            password=proxy_password,
                    )
        elif proxy_type==3 or proxy_type=='http' or proxy_type=='h':
                s.setproxy( 
                            proxy_type=socks.HTTP,
                            addr=proxy_host,
                            port=proxy_port,
                            username=proxy_username,
                            password=proxy_password,
                    )
        try:
            connection=s.connect_ex((ip,port))
            s.close()
            if connection==0:
                Network_Info.close_socket(s)
                return True
        except:
            pass
        Network_Info.close_socket(s)
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
    
    @staticmethod
    def get_banner(u, p=23, timeout=3, payload=None,**kwargs):
        try:
            return xtelnet.get_banner(u, p=p, timeout=timeout, payload=payload,**kwargs)
        except:
            return None


