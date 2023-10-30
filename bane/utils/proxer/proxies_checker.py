from .utils import *
from ..socket_connection import *


class ProxyChecker:
    __slots__=['proxy_list','num_threads','timeout','logs','result','verify_request','is_socket']
    def __init__(self, proxy_list, threads=250, timeout=10,logs=True,verify_request=False,is_socket=True):
        self.proxy_list = proxy_list
        self.num_threads = threads
        if self.num_threads>len(self.proxy_list):
            self.num_threads=len(self.proxy_list)
        self.timeout = timeout
        self.logs=logs
        self.result=[]
        self.verify_request=verify_request
        self.is_socket=is_socket
        self.check_proxies()

    def check_proxies(self):
        chunk_size = len(self.proxy_list) // self.num_threads
        threads = []

        for i in range(0, len(self.proxy_list), chunk_size):
            chunk = self.proxy_list[i:i + chunk_size]
            thread = threading.Thread(target=self._check_chunk, args=(chunk,))
            threads.append(thread)
            thread.daemon = True
            thread.start()

        for thread in threads:
            thread.join()
        
        self.proxy_list = None
        self.num_threads = None
        self.timeout = None
        self.logs=None
        self.verify_request=None

    def _check_chunk(self, chunk):
        for proxy in chunk:
            if self.is_socket==True:
                if self.proxy_check_socket(**proxy, timeout=self.timeout,verify_request=self.verify_request)==True:
                    self.result.append(proxy)
                    if self.logs==True:
                        print("Active proxy: {}".format(proxy))
            else:
                if self.proxy_check_requests(**proxy, timeout=self.timeout)==True:
                    self.result.append(proxy)
                    if self.logs==True:
                        print("Active proxy: {}".format(proxy))
    
    
    def proxy_check_socket(self,verify_request=False,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,proxy_type=None, timeout=5,**kwargs):
            #proxy=get_requests_proxy(proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password,proxy_type=proxy_type)
            try:
                s=Socket_Connection.wrap_socket_with_ssl(Proxies_Getter.get_proxy_socket("www.google.com",443,timeout=timeout,proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password,proxy_type=proxy_type),"www.google.com")
                if s!=None:
                    #print(str(s))
                    if verify_request==False:
                        return True
                    else:
                        http_request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format("www.google.com")
                        s.send(http_request.encode())
                        response = s.recv(4094)
                        s.close()
                        if 'google.com' not in str(response):
                            return False
            except Exception as ex:
                """if "403: Forbidden" in str(ex):
                    return True"""
                pass
            return False



    def proxy_check_requests(self,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,proxy_type=None, timeout=5,**kwargs):
            proxy=Proxies_Getter.get_requests_proxy(proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password,proxy_type=proxy_type)
            try:
                response=requests.Session().get('https://www.google.com',headers={'User-Agent':random.choice(Common_Variables.user_agents_list)},proxies=proxy).text
                if 'google.com' not in str(response):
                    return True
            except Exception as ex:
                return False





