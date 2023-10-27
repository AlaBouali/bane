import requests, socks, socket, random, re,os,sys,threading,ssl
import bs4,bane,json
from bs4 import BeautifulSoup
from bane.common.payloads import *
from bane.utils.pager import crawl


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
                if proxy_check_socket(**proxy, timeout=self.timeout,verify_request=self.verify_request)==True:
                    self.result.append(proxy)
                    if self.logs==True:
                        print("Active proxy: {}".format(proxy))
            else:
                if proxy_check_requests(**proxy, timeout=self.timeout)==True:
                    self.result.append(proxy)
                    if self.logs==True:
                        print("Active proxy: {}".format(proxy))




def proxygeonode(is_socket=True,verify_request=False,protocols=['http','socks4','socks5'],anonymities=["elite" , "anonymous"],timeout=20,proxy=None,headers={'Referer': 'https://geonode.com/','User-Agent':random.choice(Common_Variables.user_agents_list)},check_proxies=True,check_timeout=10,logs=False,threads=250):
    a=[]
    for x in anonymities:
        a.append('&anonymityLevel='+x)
    url='https://proxylist.geonode.com/api/proxy-list?limit=500&page={}&sort_by=lastChecked&sort_type=desc&protocols='+'%2C'.join(protocols)+''.join(a)
    page=0
    proxies=[]
    while True:
        page+=1
        try:
            r=requests.Session().get(url.format(page),headers=headers,proxies=proxy,timeout=timeout).json()
            if r['data']!=[]:
                proxies+=r['data']
            else:
                break
        except Exception as ex:
            break
    l=[]
    pr=[]
    for x in proxies:
        try:
            pr.append({'proxy_host':x['ip'],'proxy_port':int(x['port']),'proxy_username':None,'proxy_password':None,'proxy_type':x['protocols'][0]})
        except:
            pass
    for x in pr:
        if x not in l:
            l.append(x)
    if check_proxies==False:
        return l
    return ProxyChecker(l,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result



def proxyscrape(is_socket=True,verify_request=False,protocols=['http','socks4','socks5'],anonymities=["elite" , "anonymous"],timeout=10, country="all",proxy=None,threads=250,check_timeout=10,logs=False,check_proxies=True):
    l=[]
    for protocol in protocols:
        for anonymity in anonymities:
            proxies= requests.Session().get(
                "https://api.proxyscrape.com/v2/?request=getproxies&protocol="
                + protocol
                + "&timeout="
                + str(timeout * 1000)
                + "&country="
                + country
                + "&anonymity="
                + anonymity,
                timeout=timeout,
                headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                proxies=proxy
            ).text.split("\r\n")
            for x in proxies:
                if x.strip()!='':
                    l.append(x.strip()+':'+protocol) 
    pr=[]
    for x in l:
        try:
            pr.append({'proxy_host':x.split(':')[0],'proxy_port':int(x.split(':')[1]),'proxy_username':None,'proxy_password':None,'proxy_type':x.split(':')[2]})
        except:
            pass
    l=[]
    for x in pr:
        if x not in l:
            l.append(x)
    if check_proxies==False:
        return l
    return ProxyChecker(l,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result


def proxylistdownload(protocols=['socks4','socks5'],check_proxies=True,timeout=15,check_timeout=10,logs=False,verify_request=False,is_socket=True,threads=250,proxy=None):
    l=[]
    for protocol in protocols:
        try:
            r=requests.Session().get('https://www.proxy-list.download/api/v1/get?type='+protocol,
                        timeout=timeout,
                    headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                    proxies=proxy).text.split('\n')
            l+=[x.strip()+':'+protocol for x in r if x.strip()!='']
        except Exception as ex:
            pass
    pr=[]
    for x in l:
        try:
            pr.append({'proxy_host':x.split(':')[0],'proxy_port':int(x.split(':')[1]),'proxy_username':None,'proxy_password':None,'proxy_type':x.split(':')[2]})
        except:
            pass
    l=[]
    for x in pr:
        if x not in l:
            l.append(x)
    if check_proxies==False:
        return l
    return ProxyChecker(l,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result




def proxyspace(protocols=['socks4','socks5'],check_proxies=True,timeout=15,check_timeout=10,logs=False,verify_request=False,is_socket=True,threads=250,proxy=None):
    l=[]
    for protocol in protocols:
        try:
            r=requests.Session().get('https://proxyspace.pro/{}.txt'.format(protocol),
                        timeout=timeout,
                    headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                    proxies=proxy).text.split('\n')
            l+=[x.strip()+':'+protocol for x in r if x.strip()!='']
        except Exception as ex:
            pass
    pr=[]
    for x in l:
        try:
            pr.append({'proxy_host':x.split(':')[0],'proxy_port':int(x.split(':')[1]),'proxy_username':None,'proxy_password':None,'proxy_type':x.split(':')[2]})
        except:
            pass
    l=[]
    for x in pr:
        if x not in l:
            l.append(x)
    if check_proxies==False:
        return l
    return ProxyChecker(l,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result



def proxybarcode(protocols=['socks4','socks5'],check_proxies=True,timeout=15,check_timeout=10,logs=False,verify_request=False,is_socket=True,threads=250,proxy=None):
    l=[]
    for protocol in protocols:
        try:
            r=requests.Session().get('https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/{}.txt'.format(protocol.upper()),
                        timeout=timeout,
                    headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                    proxies=proxy).text.split('\n')
            l+=[x.strip()+':'+protocol for x in r if x.strip()!='']
        except Exception as ex:
            pass
    pr=[]
    for x in l:
        try:
            pr.append({'proxy_host':x.split(':')[0],'proxy_port':int(x.split(':')[1]),'proxy_username':None,'proxy_password':None,'proxy_type':x.split(':')[2]})
        except:
            pass
    l=[]
    for x in pr:
        if x not in l:
            l.append(x)
    if check_proxies==False:
        return l
    return ProxyChecker(l,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result



def proxyopenlist(protocols=['socks4','socks5'],check_proxies=True,timeout=15,check_timeout=10,logs=False,verify_request=False,is_socket=True,threads=250,proxy=None):
    l=[]
    for protocol in protocols:
        try:
            r=requests.Session().get('https://api.openproxylist.xyz/{}.txt'.format(protocol),
                        timeout=timeout,
                    headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                    proxies=proxy).text.split('\n')
            l+=[x.strip()+':'+protocol for x in r if x.strip()!='']
        except Exception as ex:
            pass
    pr=[]
    for x in l:
        try:
            pr.append({'proxy_host':x.split(':')[0],'proxy_port':int(x.split(':')[1]),'proxy_username':None,'proxy_password':None,'proxy_type':x.split(':')[2]})
        except:
            pass
    l=[]
    for x in pr:
        if x not in l:
            l.append(x)
    if check_proxies==False:
        return l
    return ProxyChecker(l,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result



def get_valid_proxies(geonode=True,scrape=True,space=True,barcode=True,listdownload=True,openlist=True,update_default_list=True,protocols=['socks4','socks5','http'],check_proxies=True,timeout=15,check_timeout=5,logs=True,verify_request=False,is_socket=True,threads=300,proxy=None):
    l=[]
    if logs==True:
        print('[i] Fetching proxies...')
    if geonode==True:
        a=proxygeonode(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if scrape==True:
        a=proxyscrape(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if space==True:
        a=proxyspace(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if barcode==True:
        a=proxybarcode(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if listdownload==True:
        a=proxylistdownload(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if openlist==True:
        a=proxyopenlist(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    pr=[]
    for x in l:
        if x not in pr:
            pr.append(x)
    if logs==True:
            print('[+] Total unique proxies: {}'.format(len(pr)))
            print('[i] Checking if they are up...')
    l=ProxyChecker(pr,threads=threads,timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket).result
    if update_default_list==True:
        bane.default_proxies_list=l
    if logs==True:
            print('[*] Total working proxies: {}'.format(len(l)))
    return l




def parse_proxy_string(s,proxy_type):
    s=s.strip()
    s=s.split(':')
    try:
        socket.gethostbyname(s[0])
    except:
        return
    try:
        int(s[1])
    except:
        return
    if len(s)==2:
        return {'proxy_host':s[0],'proxy_port':int(s[1]),'proxy_username':None,'proxy_password':None,'proxy_type':proxy_type}
    if len(s)==3:
        return {'proxy_host':s[0],'proxy_port':int(s[1]),'proxy_username':s[2],'proxy_password':'','proxy_type':proxy_type}
    if len(s)==4:
        return {'proxy_host':s[0],'proxy_port':int(s[1]),'proxy_username':s[2],'proxy_password':s[3],'proxy_type':proxy_type}


def parse_proxies_list(l,proxy_type):
    if type(l)==str:
        if len(l.split('\n'))>1:
            l=l.split('\n')
    if type(l)==list or type(l)==tuple:
        l= [parse_proxy_string(x,proxy_type) for x in l]
        return [x for x in l if x!=None]
    else:
        return [parse_proxy_string(l,proxy_type)]



def get_tor_socks5_proxy_windows(host=Common_Variables.tor_proxy_host,port=Common_Variables.tor_proxy_socks5_port_windows,new_ip=True):
    if new_ip==True:
        usr=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
        pwd=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
        return get_requests_proxy(**parse_proxy_string('{}:{}:{}:{}'.format(host,port,usr,pwd),'socks5'))
    return get_requests_proxy(**parse_proxy_string('{}:{}'.format(host,port),'socks5'))


def get_tor_socks5_proxy_linux(host=Common_Variables.tor_proxy_host,port=Common_Variables.tor_proxy_socks5_port_linux,new_ip=True):
    if new_ip==True:
        usr=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
        pwd=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
        return get_requests_proxy(**parse_proxy_string('{}:{}:{}:{}'.format(host,port,usr,pwd),'socks5'))
    return get_requests_proxy(**parse_proxy_string('{}:{}'.format(host,port),'socks5'))


def get_tor_socks5_proxy(new_ip=True):
    if (sys.platform.lower() == "win32") or (sys.platform.lower() == "win64"):
        return get_tor_socks5_proxy_windows(new_ip=new_ip)
    return get_tor_socks5_proxy_linux(new_ip=new_ip)


def get_tor_http_proxy(host=Common_Variables.tor_proxy_host,port=Common_Variables.tor_proxy_http_port,new_ip=True):
    if new_ip==True:
        usr=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
        pwd=''.join([random.choice(Common_Variables.source_string) for x in range(10)])
        return get_requests_proxy(**parse_proxy_string('{}:{}:{}:{}'.format(host,port,usr,pwd),'http'))
    return get_requests_proxy(**parse_proxy_string('{}:{}'.format(host,port),'http'))


def get_burpsuit_proxy(host=Common_Variables.burpsuit_proxy_host,port=Common_Variables.burpsuit_proxy_port):
    proxy=Common_Variables.burpsuit_http_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy


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
        

def get_tor_socks5_socket(ip,port,timeout=5,no_delay=False,new_ip=True):
    return get_proxy_socket(ip,port,no_delay=no_delay,timeout=timeout,**get_tor_socks5_proxy(new_ip=new_ip))


def get_tor_http_socket(ip,port,timeout=5,new_ip=True):
    return get_proxy_socket(ip,port,timeout=timeout,**get_tor_http_proxy(new_ip=new_ip))


def wrap_socket_with_ssl(sock,target_host):
    if sock==None:
        return
    if hasattr(ssl, 'PROTOCOL_TLS_CLIENT'):
        # Since Python 3.6
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    elif hasattr(ssl, 'PROTOCOL_TLS'):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    else:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)#ssl.PROTOCOL_TLS)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context.wrap_socket(sock, server_hostname=target_host)



def get_requests_socks5_proxy(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,**kwargs):
    if proxy_username==None:
        return {'http': 'socks5h://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks5h://{}:{}'.format(proxy_host,proxy_port)}
    if proxy_password==None:
            proxy_password=''
    return {'http': 'socks5h://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port), 'https': 'socks5h://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port)}


def get_requests_socks4_proxy(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,**kwargs):
    if proxy_username==None:
        return {'http': 'socks4://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks4://{}:{}'.format(proxy_host,proxy_port)}
    if proxy_password==None:
            proxy_password=''
    return {'http': 'socks4://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port), 'https': 'socks4://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port)}


def get_requests_http_proxy(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,**kwargs):
    if proxy_username==None:
        return {'http': 'http://{}:{}'.format(proxy_host,proxy_port), 'https': 'http://{}:{}'.format(proxy_host,proxy_port)}
    if proxy_password==None:
            proxy_password=''
    return {'http': 'http://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port), 'https': 'http://{}:{}@{}:{}'.format(proxy_username,proxy_password,proxy_host,proxy_port)}



def get_requests_proxy(proxy_type=None,**kwargs):
    if list(kwargs.keys())==['http','https']:
        return kwargs
    if proxy_type in [3,'http','h']:
        return get_requests_http_proxy(**kwargs)
    if proxy_type in [4,'socks4','s4']:
        return get_requests_socks4_proxy(**kwargs)
    if proxy_type in [5,'socks5','s5']:
        return get_requests_socks5_proxy(**kwargs)
    kwargs.update({'proxy_type':proxy_type})
    raise Exception('invalid proxy settings: {}'.format(kwargs))


def proxy_check_socket(verify_request=False,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,proxy_type=None, timeout=5,**kwargs):
        #proxy=get_requests_proxy(proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password,proxy_type=proxy_type)
        try:
            s=wrap_socket_with_ssl(get_proxy_socket("www.google.com",443,timeout=timeout,proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password,proxy_type=proxy_type),"www.google.com")
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



def proxy_check_requests(proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,proxy_type=None, timeout=5,**kwargs):
        proxy=get_requests_proxy(proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password,proxy_type=proxy_type)
        try:
            response=requests.Session().get('https://www.google.com',headers={'User-Agent':random.choice(Common_Variables.user_agents_list)},proxies=proxy).text
            if 'google.com' not in str(response):
                return True
        except Exception as ex:
            return False


def load_and_parse_proxies(source,proxies_type):
    if source==None:
        return []
    elif type(source)==dict:
        if list(source.keys())==['proxy_host', 'proxy_port', 'proxy_username', 'proxy_password', 'proxy_type']:
            return [source]
        else:
            return []
    data=[]
    if type(source)==str:
        if ':' in source:
            return [parse_proxy_string(source,proxies_type)]
        if source.endswith('.json'):
            with open(source) as f:
                return load_and_parse_proxies(json.load(f),proxies_type)
        f=open(source,'r')
        data=f.readlines()
        f.close()
    elif type(source)==list or type(source)==tuple:
        if len(source)==0:
            return []
        if type(source[0])==dict:
            if list(source[0].keys())==['proxy_host', 'proxy_port', 'proxy_username', 'proxy_password', 'proxy_type']:
                return source
        for x in source:
            if type(x)==str:
                data.append(x)
    return parse_proxies_list(data,proxies_type)


def load_and_parse_proxies_all(http_proxies=None,socks4_proxies=None,socks5_proxies=None,json_file=None):
    l=load_and_parse_proxies(http_proxies,'http')
    l+=load_and_parse_proxies(socks4_proxies,'socks4')
    l+=load_and_parse_proxies(socks5_proxies,'socks5')
    l+=load_and_parse_proxies(json_file,None)
    d=[]
    for x in l:
        if x not in d:
            d.append(x)
    return d


def get_requests_proxies_from_parameter(parameter,proxies_type):
    if parameter==None:
        return [None]
    if type(parameter)==list or type(parameter)==tuple:
        l=[]
        for x in parameter:
            l+=get_requests_proxies_from_parameter(x,proxies_type)
        return [get_requests_proxy(**x) for x in l]
    if type(parameter)==dict:
        if list(parameter.keys())==['proxy_host', 'proxy_port', 'proxy_username', 'proxy_password', 'proxy_type']:
            return [get_requests_proxy(**parameter)]
        if list(parameter.keys())==['http','https']:
            return [parameter]
        raise Exception('Incorrect dict format')
    if type(parameter)==str:
        l=load_and_parse_proxies(parameter,proxies_type)
        d=[]
        for x in l:
            d.append(get_requests_proxy(**x))
        if len(d)>1:
            return [x for x in l if x!=None]
        return d



def get_requests_proxies_from_parameters(proxies=None,proxy=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None,json_file=None):
    l=get_requests_proxies_from_parameter(proxy,None)
    l+=get_requests_proxies_from_parameter(http_proxies,'http')
    l+=get_requests_proxies_from_parameter(socks4_proxies,'socks4')
    l+=get_requests_proxies_from_parameter(socks5_proxies,'socks5')
    a=load_and_parse_proxies(json_file,None)
    l+=[get_requests_proxy(**x) for x in a]
    l+=get_requests_proxies_from_parameter(proxies,None)
    d=[]
    for x in l:
        if x not in d:
            d.append(x)
    if len(d)>1:
        return [x for x in l if x!=None]
    return d


def requests_proxy_to_socket_proxy(proxy):
    p=proxy[list(proxy.keys())[0]]
    if p.startswith('http'):
        proxy_type='http'
    elif p.startswith('socks4'):
        proxy_type='socks4'
    else:
        proxy_type='socks5'
    pr=p.split('://')[1]
    if '@' in pr:
        user=pr.split('@')[0].split(':')[0]
        pwd=pr.split('@')[0].split(':')[1]
        ip=pr.split('@')[1].split(':')[0]
        port=int(pr.split('@')[1].split(':')[1])
    else:
        user=None
        pwd=None
        ip=pr.split(':')[0]
        port=int(pr.split(':')[1])
    return {'proxy_host':ip,'proxy_port':port,'proxy_username':user,'proxy_password':pwd,'proxy_type':proxy_type}






def get_socket_proxies_from_parameters(proxies=None,proxy=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None,json_file=None):
    l=get_requests_proxies_from_parameter(proxy,None)
    l+=get_requests_proxies_from_parameter(http_proxies,'http')
    l+=get_requests_proxies_from_parameter(socks4_proxies,'socks4')
    l+=get_requests_proxies_from_parameter(socks5_proxies,'socks5')
    a=load_and_parse_proxies(json_file,None)
    l+=[get_requests_proxy(**x) for x in a]
    l+=get_requests_proxies_from_parameter(proxies,None)
    d=[]
    for x in l:
        if x not in d:
            d.append(x)
    return [requests_proxy_to_socket_proxy(x) for x in d if x!=None]


