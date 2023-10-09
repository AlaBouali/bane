<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.gather_info.subdomains API documentation</title>
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
<h1 class="title">Module <code>bane.gather_info.subdomains</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.gather_info.utils import *
from bane.gather_info.domains import resolve

def subdomains_crt(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True,subdomain_check_timeout=10, crt_timeout=120,cookie=None, user_agent=None, proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    if "://" in domain:
        domain = domain.split("://")[1].split("/")[0]
    if "www." in domain:
        domain = domain.replace("www.", "")
    if logs==True:
        print('[*] searching with crt.sh ...\n')
    try:
        r = requests.Session().get(
            "https://crt.sh/?output=json&amp;q=%25." + domain,
            headers=hed,
            proxies=proxy,
            timeout=crt_timeout,
            verify=False,
        ).json()
        #print(r)
        a = [x["name_value"].split("\\")[0] for x in r if ("*." not in x["name_value"])]
        l = []
        for x in a:
            if "\n" in x:
                l += x.split("\n")
            else:
                l.append(x)
        l= list(dict.fromkeys(l))
        result={}
        for x in l:
            if extract_root_domain(x)==domain:
                try:
                    r=requests.Session().get('http://'+x,headers=hed,proxies=proxy,timeout=subdomain_check_timeout,verify=False)
                    if extract_root_domain(r.url.split('://')[1].split('/')[0])==extract_root_domain(x):
                        result.update({x:r.url})
                        if logs==True:
                            print('\t[+] {}'.format(x))
                except:
                    try:
                        result.update({x:resolve(x,server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime)})
                    except:
                        pass
        if logs==True:
            print()
        if subdomains_only==True:
            return list(result.keys())
        return result

    except Exception as ex:
        #print(ex)
        if subdomains_only==True:
            return {}
        return []

"""
def subdomains_finder(
    u, process_check_interval=5, logs=True, requests_timeout=15, https=False,proxy=None
):
    https_flag = 0
    if (https == True) or ("https://" in u):
        https_flag = 1
    if "://" in u:
        host = u.split("://")[1].split("/")[0]
    else:
        host = u
    sd = []
    while True:
        try:
            s = requests.Session().session()
            r = s.post(
                "https://scan.penteston.com/scan_system.php",
                data={
                    "scan_method": "S201",
                    "test_protocol": https_flag,
                    "test_host": host,
                },
                timeout=requests_timeout,
                proxies=proxy
            ).text
            if '"isFinished":"no"' not in r:
                if logs == True:
                    print("\n[+]Scan results:")
                c = r.split("strong&gt;&lt;br\/&gt;")[1].replace('"}', "")
                for x in c.split("&lt;br\/&gt;"):
                    if logs == True:
                        print(x)
                    sd.append(x)
                break
            else:
                if logs == True:
                    sys.stdout.write("\r[*]Scan in progress...")
                    sys.stdout.flush()
                # print("[*]Scan in progress...")
        except KeyboardInterrupt:
            break
        except:
            pass
        try:
            time.sleep(process_check_interval)
        except KeyboardInterrupt:
            break
        except:
            pass
    return {u: sd}

"""

def get_subdomains_from_wayback(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True,user_agent=None,cookie=None,wayback_timeout=50,subdomain_check_timeout=10,max_urls=10,subdomains_only=False,proxy=None):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    subdomains = set()
    urls={}
    invalid_subd=[]
    if logs==True:
        print('[*] searching with wayback machine ...\n')
    url = "https://web.archive.org/cdx/search/cdx?url=*.{}/*&amp;output=json&amp;fl=original&amp;collapse=urlkey".format(domain)
    response = requests.Session().get(url,headers=hed,timeout=wayback_timeout,proxies=proxy)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            original_url = entry[0]
            match = re.match(r"https?://([^/]*)", original_url.split('?')[0])
            if match:
                subdomain = match.group(1)
                if subdomain not in invalid_subd and extract_root_domain(subdomain)==domain:
                    if subdomain not in urls:
                        try:
                            r=requests.Session().get(original_url,headers=hed,timeout=subdomain_check_timeout,proxies=proxy)
                            if extract_root_domain(r.url.split('://')[1].split('/')[0])==extract_root_domain(subdomain):
                                urls[subdomain]=set()
                                urls[subdomain].add(original_url)
                                if logs==True:
                                    print('\t[+] {}'.format(subdomain))
                        #if len(urls[subdomain])&lt;5:
                        except KeyboardInterrupt:
                            break
                        except:
                            try:
                                urls[subdomain].add(resolve(x.split(':')[0],server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime))
                                if logs==True:
                                    print('\t[+] {}'.format(subdomain))
                            except:
                                invalid_subd.append(subdomain)
                    else:
                        if len(urls[subdomain])&lt;max_urls:
                            urls[subdomain].add(original_url)
                        subdomains.add(subdomain)
    else:
        raise("Error fetching data from Wayback Machine")
    if logs==True:
        print()
    if subdomains_only==True:
        return list(urls.keys())
    for x in urls:
        urls[x]=list(urls[x])
    return urls




def get_subdomains(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True, crt_timeout=120,user_agent=None,cookie=None,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    subs=get_subdomains_from_wayback(domain,dns_server=dns_server,resolve_timeout=resolve_timeout,resolve_lifetime=resolve_lifetime,logs=logs,cookie=cookie,wayback_timeout=wayback_timeout,user_agent=user_agent,subdomain_check_timeout=subdomain_check_timeout,max_urls=max_wayback_urls,subdomains_only=subdomains_only,proxy=proxy)
    l=subdomains_crt(domain,dns_server=dns_server,resolve_timeout=resolve_timeout,resolve_lifetime=resolve_lifetime,logs=logs,subdomain_check_timeout=subdomain_check_timeout, crt_timeout=crt_timeout,cookie=cookie, user_agent=user_agent, proxy=proxy,subdomains_only=subdomains_only)
    if type(subs)==list:
        for x in l:
            if x not in subs:
                subs.append(x)
        return subs
    for x in l:
        if x not in subs:
            subs.update({x:l[x]})
        else:
            if l[x] not in subs[x]:
                subs[x].append(l[x])
    return subs</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.gather_info.subdomains.get_subdomains"><code class="name flex">
<span>def <span class="ident">get_subdomains</span></span>(<span>domain, dns_server='8.8.8.8', resolve_timeout=2, resolve_lifetime=1, logs=True, crt_timeout=120, user_agent=None, cookie=None, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, proxy=None, subdomains_only=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_subdomains(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True, crt_timeout=120,user_agent=None,cookie=None,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    subs=get_subdomains_from_wayback(domain,dns_server=dns_server,resolve_timeout=resolve_timeout,resolve_lifetime=resolve_lifetime,logs=logs,cookie=cookie,wayback_timeout=wayback_timeout,user_agent=user_agent,subdomain_check_timeout=subdomain_check_timeout,max_urls=max_wayback_urls,subdomains_only=subdomains_only,proxy=proxy)
    l=subdomains_crt(domain,dns_server=dns_server,resolve_timeout=resolve_timeout,resolve_lifetime=resolve_lifetime,logs=logs,subdomain_check_timeout=subdomain_check_timeout, crt_timeout=crt_timeout,cookie=cookie, user_agent=user_agent, proxy=proxy,subdomains_only=subdomains_only)
    if type(subs)==list:
        for x in l:
            if x not in subs:
                subs.append(x)
        return subs
    for x in l:
        if x not in subs:
            subs.update({x:l[x]})
        else:
            if l[x] not in subs[x]:
                subs[x].append(l[x])
    return subs</code></pre>
</details>
</dd>
<dt id="bane.gather_info.subdomains.get_subdomains_from_wayback"><code class="name flex">
<span>def <span class="ident">get_subdomains_from_wayback</span></span>(<span>domain, dns_server='8.8.8.8', resolve_timeout=2, resolve_lifetime=1, logs=True, user_agent=None, cookie=None, wayback_timeout=50, subdomain_check_timeout=10, max_urls=10, subdomains_only=False, proxy=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_subdomains_from_wayback(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True,user_agent=None,cookie=None,wayback_timeout=50,subdomain_check_timeout=10,max_urls=10,subdomains_only=False,proxy=None):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    subdomains = set()
    urls={}
    invalid_subd=[]
    if logs==True:
        print('[*] searching with wayback machine ...\n')
    url = "https://web.archive.org/cdx/search/cdx?url=*.{}/*&amp;output=json&amp;fl=original&amp;collapse=urlkey".format(domain)
    response = requests.Session().get(url,headers=hed,timeout=wayback_timeout,proxies=proxy)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            original_url = entry[0]
            match = re.match(r"https?://([^/]*)", original_url.split('?')[0])
            if match:
                subdomain = match.group(1)
                if subdomain not in invalid_subd and extract_root_domain(subdomain)==domain:
                    if subdomain not in urls:
                        try:
                            r=requests.Session().get(original_url,headers=hed,timeout=subdomain_check_timeout,proxies=proxy)
                            if extract_root_domain(r.url.split('://')[1].split('/')[0])==extract_root_domain(subdomain):
                                urls[subdomain]=set()
                                urls[subdomain].add(original_url)
                                if logs==True:
                                    print('\t[+] {}'.format(subdomain))
                        #if len(urls[subdomain])&lt;5:
                        except KeyboardInterrupt:
                            break
                        except:
                            try:
                                urls[subdomain].add(resolve(x.split(':')[0],server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime))
                                if logs==True:
                                    print('\t[+] {}'.format(subdomain))
                            except:
                                invalid_subd.append(subdomain)
                    else:
                        if len(urls[subdomain])&lt;max_urls:
                            urls[subdomain].add(original_url)
                        subdomains.add(subdomain)
    else:
        raise("Error fetching data from Wayback Machine")
    if logs==True:
        print()
    if subdomains_only==True:
        return list(urls.keys())
    for x in urls:
        urls[x]=list(urls[x])
    return urls</code></pre>
</details>
</dd>
<dt id="bane.gather_info.subdomains.subdomains_crt"><code class="name flex">
<span>def <span class="ident">subdomains_crt</span></span>(<span>domain, dns_server='8.8.8.8', resolve_timeout=2, resolve_lifetime=1, logs=True, subdomain_check_timeout=10, crt_timeout=120, cookie=None, user_agent=None, proxy=None, subdomains_only=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def subdomains_crt(domain,dns_server='8.8.8.8',resolve_timeout=2,resolve_lifetime=1,logs=True,subdomain_check_timeout=10, crt_timeout=120,cookie=None, user_agent=None, proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    if "://" in domain:
        domain = domain.split("://")[1].split("/")[0]
    if "www." in domain:
        domain = domain.replace("www.", "")
    if logs==True:
        print('[*] searching with crt.sh ...\n')
    try:
        r = requests.Session().get(
            "https://crt.sh/?output=json&amp;q=%25." + domain,
            headers=hed,
            proxies=proxy,
            timeout=crt_timeout,
            verify=False,
        ).json()
        #print(r)
        a = [x["name_value"].split("\\")[0] for x in r if ("*." not in x["name_value"])]
        l = []
        for x in a:
            if "\n" in x:
                l += x.split("\n")
            else:
                l.append(x)
        l= list(dict.fromkeys(l))
        result={}
        for x in l:
            if extract_root_domain(x)==domain:
                try:
                    r=requests.Session().get('http://'+x,headers=hed,proxies=proxy,timeout=subdomain_check_timeout,verify=False)
                    if extract_root_domain(r.url.split('://')[1].split('/')[0])==extract_root_domain(x):
                        result.update({x:r.url})
                        if logs==True:
                            print('\t[+] {}'.format(x))
                except:
                    try:
                        result.update({x:resolve(x,server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime)})
                    except:
                        pass
        if logs==True:
            print()
        if subdomains_only==True:
            return list(result.keys())
        return result

    except Exception as ex:
        #print(ex)
        if subdomains_only==True:
            return {}
        return []</code></pre>
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
<li><code><a href="index.md" title="bane.gather_info">bane.gather_info</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.gather_info.subdomains.get_subdomains" title="bane.gather_info.subdomains.get_subdomains">get_subdomains</a></code></li>
<li><code><a href="#bane.gather_info.subdomains.get_subdomains_from_wayback" title="bane.gather_info.subdomains.get_subdomains_from_wayback">get_subdomains_from_wayback</a></code></li>
<li><code><a href="#bane.gather_info.subdomains.subdomains_crt" title="bane.gather_info.subdomains.subdomains_crt">subdomains_crt</a></code></li>
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