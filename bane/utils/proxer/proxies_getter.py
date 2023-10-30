from .utils import *
from .burpsuit import *
from .proxies_parser import *

class Proxies_Getter(BurpSuite_Getter):

    @staticmethod
    def get_socks5_proxy_socket(host,port,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,no_delay=False,timeout=5,**kwargs):
        try:
            s = socks.socksocket()
            if no_delay==True:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(timeout)
            s.setproxy( 
                        proxy_type=socks.SOCKS5,
                        addr=proxy_host,
                        port=proxy_port,
                        username=proxy_username,
                        password=proxy_password,
                )
            s.connect((host,port))
            return s
        except:
            return


    @staticmethod
    def get_socks4_proxy_socket(host,port,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,no_delay=False,timeout=5,**kwargs):
        try:
            s = socks.socksocket()
            if no_delay==True:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(timeout)
            s.setproxy( 
                        proxy_type=socks.SOCKS4,
                        addr=proxy_host,
                        port=proxy_port,
                        username=proxy_username,
                        password=proxy_password,
                )
            s.connect((host,port))
            return s
        except:
            return


    @staticmethod
    def get_socks_proxy_socket(host,port,proxy_host=None,proxy_port=None,proxy_type=None,proxy_username=None,proxy_password=None,no_delay=False,timeout=5,**kwargs):
        try:
            s = socks.socksocket()
            if no_delay==True:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
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
            s.connect((host,port))
            return s
        except:
            return


    @staticmethod
    def get_http_proxy_socket(host,port,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,no_delay=False,timeout=5,**kwargs):
        try:
            s = socks.socksocket()
            if no_delay==True:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.settimeout(timeout)
            s.setproxy( 
                        proxy_type=socks.HTTP,
                        addr=proxy_host,
                        port=proxy_port,
                        username=proxy_username,
                        password=proxy_password,
                )
            s.connect((host,port))
            return s
        except:
            return


    @staticmethod
    def get_proxy_socket(host,port,proxy_host=None,proxy_port=None,proxy_type=None,proxy_username=None,proxy_password=None,timeout=5,no_delay=False,**kwargs):
        try:
            s = socks.socksocket()
            if no_delay==True:
                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
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
            s.connect((host,port))
            return s
        except Exception as ex:
            raise(ex)
    
    @staticmethod
    def get_tor_socks5_socket(ip,port,timeout=5,no_delay=False,new_ip=True):
        return Proxies_Getter.get_proxy_socket(ip,port,no_delay=no_delay,timeout=timeout,**Proxies_Getter.get_tor_socks5_proxy(new_ip=new_ip))


    @staticmethod
    def get_tor_http_socket(ip,port,timeout=5,new_ip=True):
        return Proxies_Getter.get_proxy_socket(ip,port,timeout=timeout,**Proxies_Getter.get_tor_http_proxy(new_ip=new_ip))




    @staticmethod
    def get_requests_socks5_proxy(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,**kwargs):
        if proxy_username==None:
            return {'http': 'socks5h://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks5h://{}:{}'.format(proxy_host,proxy_port)}
        if proxy_password==None:
                proxy_password=''
        return {'http': 'socks5h://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port), 'https': 'socks5h://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port)}


    @staticmethod
    def get_requests_socks4_proxy(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,**kwargs):
        if proxy_username==None:
            return {'http': 'socks4://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks4://{}:{}'.format(proxy_host,proxy_port)}
        if proxy_password==None:
                proxy_password=''
        return {'http': 'socks4://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port), 'https': 'socks4://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port)}


    @staticmethod
    def get_requests_http_proxy(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,**kwargs):
        if proxy_username==None:
            return {'http': 'http://{}:{}'.format(proxy_host,proxy_port), 'https': 'http://{}:{}'.format(proxy_host,proxy_port)}
        if proxy_password==None:
                proxy_password=''
        return {'http': 'http://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port), 'https': 'http://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port)}


    @staticmethod
    def get_tor_socks5_proxy_windows(host=Common_Variables.tor_proxy_host,port=Common_Variables.tor_proxy_socks5_port_windows,new_ip=True):
        if new_ip==True:
            usr=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
            pwd=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
            return Proxies_Getter.get_requests_proxy(**Proxies_Parser.parse_proxy_string('{}:{}:{}:{}'.format(host,port,usr,pwd),'socks5'))
        return Proxies_Getter.get_requests_proxy(**Proxies_Parser.parse_proxy_string('{}:{}'.format(host,port),'socks5'))


    @staticmethod
    def get_tor_socks5_proxy_linux(host=Common_Variables.tor_proxy_host,port=Common_Variables.tor_proxy_socks5_port_linux,new_ip=True):
        if new_ip==True:
            usr=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
            pwd=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
            return Proxies_Getter.get_requests_proxy(**Proxies_Parser.parse_proxy_string('{}:{}:{}:{}'.format(host,port,usr,pwd),'socks5'))
        return Proxies_Getter.get_requests_proxy(**Proxies_Parser.parse_proxy_string('{}:{}'.format(host,port),'socks5'))


    @staticmethod
    def get_tor_socks5_proxy(new_ip=True):
        if (sys.platform.lower() == "win32") or (sys.platform.lower() == "win64"):
            return Proxies_Getter.get_tor_socks5_proxy_windows(new_ip=new_ip)
        return Proxies_Getter.get_tor_socks5_proxy_linux(new_ip=new_ip)


    @staticmethod
    def get_tor_http_proxy(host=Common_Variables.tor_proxy_host,port=Common_Variables.tor_proxy_http_port,new_ip=True):
        if new_ip==True:
            usr=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
            pwd=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
            return Proxies_Getter.get_requests_proxy(**Proxies_Parser.parse_proxy_string('{}:{}:{}:{}'.format(host,port,usr,pwd),'http'))
        return Proxies_Getter.get_requests_proxy(**Proxies_Parser.parse_proxy_string('{}:{}'.format(host,port),'http'))

    @staticmethod
    def get_requests_proxy(proxy_type=None,**kwargs):
        if list(kwargs.keys())==['http','https']:
            return kwargs
        if proxy_type in [3,'http','h']:
            return Proxies_Getter.get_requests_http_proxy(**kwargs)
        if proxy_type in [4,'socks4','s4']:
            return Proxies_Getter.get_requests_socks4_proxy(**kwargs)
        if proxy_type in [5,'socks5','s5']:
            return Proxies_Getter.get_requests_socks5_proxy(**kwargs)
        kwargs.update({'proxy_type':proxy_type})
        raise Exception('invalid proxy settings: {}'.format(kwargs))