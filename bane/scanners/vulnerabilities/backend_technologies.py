from bane.scanners.vulnerabilities.utils import *
from bane.scanners.vulnerabilities.vulner_search import vulners_search

def scan_backend_technology(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=True,request_headers=None):
    domain=u.split('://')[1].split('/')[0].split(':')[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(':')[0])
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        if request_headers==None:
            r = requests.get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
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
                    bk=vulners_search(back.split('/')[0].lower(),version=back.split('/')[1])
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
                        sv_e=vulners_search(sv.split('/')[0].lower(),version=sv.split('/')[1])
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
    return {'server_exploits':server_exploits,'backend_technology_exploits':backend_technology_exploits}


