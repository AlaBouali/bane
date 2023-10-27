from .utils import *
from .burpsuit import *
from .collect_proxies import *
from .proxies_checker import *
from .proxies_getter import *
from .proxies_checker import *

def load_and_parse_proxies_all(http_proxies=None,socks4_proxies=None,socks5_proxies=None,json_file=None):
    l=Proxies_Parser.load_and_parse_proxies(http_proxies,'http')
    l+=Proxies_Parser.load_and_parse_proxies(socks4_proxies,'socks4')
    l+=Proxies_Parser.load_and_parse_proxies(socks5_proxies,'socks5')
    l+=Proxies_Parser.load_and_parse_proxies(json_file,None)
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
        return [Proxies_Getter.get_requests_proxy(**x) for x in l]
    if type(parameter)==dict:
        if list(parameter.keys())==['proxy_host', 'proxy_port', 'proxy_username', 'proxy_password', 'proxy_type']:
            return [Proxies_Getter.get_requests_proxy(**parameter)]
        if list(parameter.keys())==['http','https']:
            return [parameter]
        raise Exception('Incorrect dict format')
    if type(parameter)==str:
        l=Proxies_Parser.load_and_parse_proxies(parameter,proxies_type)
        d=[]
        for x in l:
            d.append(Proxies_Getter.get_requests_proxy(**x))
        if len(d)>1:
            return [x for x in l if x!=None]
        return d



def get_requests_proxies_from_parameters(proxies=None,proxy=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None,json_file=None):
    l=get_requests_proxies_from_parameter(proxy,None)
    l+=get_requests_proxies_from_parameter(http_proxies,'http')
    l+=get_requests_proxies_from_parameter(socks4_proxies,'socks4')
    l+=get_requests_proxies_from_parameter(socks5_proxies,'socks5')
    a=Proxies_Parser.load_and_parse_proxies(json_file,None)
    l+=[Proxies_Getter.get_requests_proxy(**x) for x in a]
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
    a=Proxies_Parser.load_and_parse_proxies(json_file,None)
    l+=[Proxies_Getter.get_requests_proxy(**x) for x in a]
    l+=get_requests_proxies_from_parameter(proxies,None)
    d=[]
    for x in l:
        if x not in d:
            d.append(x)
    return [requests_proxy_to_socket_proxy(x) for x in d if x!=None]


