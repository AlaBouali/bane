from ...scanners.cms.utils import *

class Jira_Scanner:

    @staticmethod
    def scan(u,user_agent=None,cookie=None,timeout=10,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        started_at=time.time()
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        domain=u.split('://')[1].split('/')[0].split(':')[0]
        root_domain=Subdomain_Info.extract_root_domain(domain)
        ip=socket.gethostbyname(domain.split(':')[0])
        if u[len(u) - 1] == "/":
            u = u[0 : len(u) - 1]
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        try:
            response = requests.Session().get(u, headers=hed, proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies), timeout=timeout, verify=False)
            version=response.text.lower().split('<meta name="ajs-version-number" content="')[1].split('"')[0]
        except Exception as ex:
            #raise(ex)
            version=''
        server=response.headers.get('Server','')
        try:
            server_os=[x for x in server.split() if x.startswith('(')==True][0].replace('(','').replace(')','')
        except:
            server_os=''
        backend=response.headers.get('X-Powered-By','')
        if logs==True:
            print("Jira site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tJira version: {}\n".format(u,domain,ip,server,server_os,backend,version))
        clickj=ClickJacking_Scanner.scan(u,request_headers=response.headers)
        if logs==True:
            print("[i] Looking for subdomains...")
        subs=Subdomain_Info.get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),subdomains_only=subdomains_only)
        if logs==True:
            print("[i] Cheking if we can sniff some cookies over some links...")
            print()
        media_non_ssl=Mixed_Content_Scanner.scan_url(u,content=response.text,logs=logs,request_headers=response.headers)
        if logs==True:
            print()
        wp_vulns=[]
        if version!='':
            if logs==True:
                print('[i] looking for exploits for version: {}\n'.format(version))
            wpvulns=Vulners_Search_Scanner.scan('jira server and data center',version=version,proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies),api_key=api_key)
            for x in wpvulns:
                if 'jira' in x['title'].lower() or 'jira' in x['description'].lower():
                    wp_vulns.append(x)
            for x in wp_vulns:
                for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                    try:
                        del x[i]
                    except:
                        pass
            if logs==True:
                if len(wp_vulns)==0:
                    print('\t[-] none was found')
                else:
                    for x in wp_vulns:
                        print("\tTitle : {}\n\tDescription: {}\n\tLink: {}".format(x['title'],x['description'],x['href']))
                        print()
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
        if type(subs)==dict:
            domains_list=list(subs.keys())
        else:
            domains_list=subs
        domains_list_report=IP_Info.check_ip_via_shodan(domains_list,logs=logs,timeout=timeout,proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies))
        return {'url':u,'domain':domain,'ip':ip,'shodan_report':IP_Info.check_ip_via_shodan(ip,logs=logs,timeout=timeout,proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)),'root_domain':root_domain,'sub_domains':subs,"subdomains_ips_report_shodan":domains_list_report,'server':server,'os':server_os,'backend_technology':backend,'jira_version':version,'sniffable_links':media_non_ssl,'clickjackable':clickj,"exploits":wp_vulns,'backend_technology_exploits':backend_technology_exploits,'server_exploits':server_exploits,'start_date':started_at,'end_date':time.time()}
