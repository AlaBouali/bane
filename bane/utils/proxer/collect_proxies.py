from .utils import *
from .proxies_checker import *


class Proxies_Collector:

    @staticmethod
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



    @staticmethod
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


    @staticmethod
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




    @staticmethod
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



    @staticmethod
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



    @staticmethod
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
        a=Proxies_Collector.proxygeonode(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if scrape==True:
        a=Proxies_Collector.proxyscrape(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if space==True:
        a=Proxies_Collector.proxyspace(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if barcode==True:
        a=Proxies_Collector.proxybarcode(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if listdownload==True:
        a=Proxies_Collector.proxylistdownload(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
        for x in a:
            if x not in l:
                l.append(x)
        if logs==True:
            print('[*] Count: {}'.format(len(l)))
    if openlist==True:
        a=Proxies_Collector.proxyopenlist(check_proxies=False,protocols=protocols,timeout=timeout,check_timeout=check_timeout,logs=logs,verify_request=verify_request,is_socket=is_socket,threads=threads,proxy=proxy)
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
