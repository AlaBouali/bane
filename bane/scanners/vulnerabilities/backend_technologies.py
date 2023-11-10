from bane.scanners.vulnerabilities.utils import *
from bane.scanners.vulnerabilities.vulner_search import Vulners_Search_Scanner


class Backend_Technologies_Scanner:

    @staticmethod
    def scan(u, timeout=10, user_agent=None, cookie=None, logs=True,request_headers=None,headers={},api_key=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        started_at=time.time()
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        domain=u.split('://')[1].split('/')[0].split(':')[0]
        root_domain=Subdomain_Info.extract_root_domain(domain)
        ip=socket.gethostbyname(domain.split(':')[0])
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update(headers)
        try:
            if request_headers==None:
                r = requests.Session().get(
                    u, headers=heads, proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies), timeout=timeout, verify=False
                ).headers
            else:
                r=request_headers
            server=r.get('Server','')
            try:
                server_os=[x for x in server.split() if x.startswith('(')==True][0].replace('(','').replace(')','')
            except:
                server_os=''
            backend=r.get('X-Powered-By','')
            if logs==True:
                print("Site info:\n\n\tURL: {}\n\tDomain: {}\n\tRoot domain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n".format(u,domain,root_domain,ip,server,server_os,backend))
            backend_technology_exploits={}
            if backend!='':
                bk=[]
                for back in backend.split():
                    if logs==True:
                        print('[i] looking for exploits for : {}\n'.format(back))
                    if '/' not in back:
                        if logs==True:
                            print('\t[-] unknown version\n')
                    else:
                        bk=Vulners_Search_Scanner.scan(back.split('/')[0].lower(),version=back.split('/')[1],proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),api_key=api_key)
                    for x in bk:
                        for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                            try:
                                del x[i]
                            except:
                                pass
                    backend_technology_exploits.update({back:bk})
                    if logs==True:
                        if len(bk)==0:
                            print('\t[-] none was found')
                        else:
                            for x in bk:
                                print("\tTitle : {}\n\tDescription: {}\n\tLink: {}".format(x['title'],x['description'],x['href']))
                                print()
            server_exploits={}
            if server!='':
                for sv in server.split():
                    if sv.startswith('(')==False:
                        sv_e=[]
                        if logs==True:
                            print('[i] looking for exploits for : {}\n'.format(sv))
                        if '/' in sv:
                            sv_e=Vulners_Search_Scanner.scan(sv.split('/')[0].lower(),version=sv.split('/')[1],proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),api_key=api_key)
                        else:
                            if logs==True:
                                print('\t[-] unknown version\n')
                        for x in sv_e:
                            for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                                try:
                                    del x[i]
                                except:
                                    pass
                        server_exploits.update({sv:sv_e})
                        if logs==True:
                            if len(sv_e)==0:
                                print('\t[-] none was found')
                            else:
                                for x in sv_e:
                                    print("\tTitle : {}\n\tDescription: {}\n\tLink: {}".format(x['title'],x['description'],x['href']))
                                    print()        
        except Exception as e:
            return {}
        return {'shodan_report':IP_Info.check_ip_via_shodan(ip,logs=logs,timeout=timeout,proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)),'server_exploits':server_exploits,'backend_technology_exploits':backend_technology_exploits,'start_date':started_at,'end_date':time.time()}


