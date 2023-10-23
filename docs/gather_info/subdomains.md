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

def subdomains_crt(domain,dns_server=&#39;8.8.8.8&#39;,resolve_timeout=2,resolve_lifetime=1,logs=True,subdomain_check_timeout=10, crt_timeout=120,cookie=None, user_agent=None, proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    if &#34;://&#34; in domain:
        domain = domain.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
    if &#34;www.&#34; in domain:
        domain = domain.replace(&#34;www.&#34;, &#34;&#34;)
    if logs==True:
        print(&#39;[*] searching with crt.sh ...\n&#39;)
    try:
        r = requests.Session().get(
            &#34;https://crt.sh/?output=json&amp;q=%25.&#34; + domain,
            headers=hed,
            proxies=proxy,
            timeout=crt_timeout,
            verify=False,
        ).json()
        #print(r)
        a = [x[&#34;name_value&#34;].split(&#34;\\&#34;)[0] for x in r if (&#34;*.&#34; not in x[&#34;name_value&#34;])]
        l = []
        for x in a:
            if &#34;\n&#34; in x:
                l += x.split(&#34;\n&#34;)
            else:
                l.append(x)
        l= list(dict.fromkeys(l))
        result={}
        for x in l:
            if extract_root_domain(x)==domain:
                try:
                    r=requests.Session().get(&#39;http://&#39;+x,headers=hed,proxies=proxy,timeout=subdomain_check_timeout,verify=False)
                    if extract_root_domain(r.url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0])==extract_root_domain(x):
                        result.update({x:r.url})
                        if logs==True:
                            print(&#39;\t[+] {}&#39;.format(x))
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

&#34;&#34;&#34;
def subdomains_finder(
    u, process_check_interval=5, logs=True, requests_timeout=15, https=False,proxy=None
):
    https_flag = 0
    if (https == True) or (&#34;https://&#34; in u):
        https_flag = 1
    if &#34;://&#34; in u:
        host = u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
    else:
        host = u
    sd = []
    while True:
        try:
            s = requests.Session().session()
            r = s.post(
                &#34;https://scan.penteston.com/scan_system.php&#34;,
                data={
                    &#34;scan_method&#34;: &#34;S201&#34;,
                    &#34;test_protocol&#34;: https_flag,
                    &#34;test_host&#34;: host,
                },
                timeout=requests_timeout,
                proxies=proxy
            ).text
            if &#39;&#34;isFinished&#34;:&#34;no&#34;&#39; not in r:
                if logs == True:
                    print(&#34;\n[+]Scan results:&#34;)
                c = r.split(&#34;strong&gt;&lt;br\/&gt;&#34;)[1].replace(&#39;&#34;}&#39;, &#34;&#34;)
                for x in c.split(&#34;&lt;br\/&gt;&#34;):
                    if logs == True:
                        print(x)
                    sd.append(x)
                break
            else:
                if logs == True:
                    sys.stdout.write(&#34;\r[*]Scan in progress...&#34;)
                    sys.stdout.flush()
                # print(&#34;[*]Scan in progress...&#34;)
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

&#34;&#34;&#34;

def get_subdomains_from_wayback(domain,dns_server=&#39;8.8.8.8&#39;,resolve_timeout=2,resolve_lifetime=1,logs=True,user_agent=None,cookie=None,wayback_timeout=50,subdomain_check_timeout=10,max_urls=10,subdomains_only=False,proxy=None):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    subdomains = set()
    urls={}
    invalid_subd=[]
    if logs==True:
        print(&#39;[*] searching with wayback machine ...\n&#39;)
    url = &#34;https://web.archive.org/cdx/search/cdx?url=*.{}/*&amp;output=json&amp;fl=original&amp;collapse=urlkey&#34;.format(domain)
    response = requests.Session().get(url,headers=hed,timeout=wayback_timeout,proxies=proxy)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            original_url = entry[0]
            match = re.match(r&#34;https?://([^/]*)&#34;, original_url.split(&#39;?&#39;)[0])
            if match:
                subdomain = match.group(1)
                if subdomain not in invalid_subd and extract_root_domain(subdomain)==domain:
                    if subdomain not in urls:
                        try:
                            r=requests.Session().get(original_url,headers=hed,timeout=subdomain_check_timeout,proxies=proxy)
                            if extract_root_domain(r.url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0])==extract_root_domain(subdomain):
                                urls[subdomain]=set()
                                urls[subdomain].add(original_url)
                                if logs==True:
                                    print(&#39;\t[+] {}&#39;.format(subdomain))
                        #if len(urls[subdomain])&lt;5:
                        except KeyboardInterrupt:
                            break
                        except:
                            try:
                                urls[subdomain].add(resolve(x.split(&#39;:&#39;)[0],server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime))
                                if logs==True:
                                    print(&#39;\t[+] {}&#39;.format(subdomain))
                            except:
                                invalid_subd.append(subdomain)
                    else:
                        if len(urls[subdomain])&lt;max_urls:
                            urls[subdomain].add(original_url)
                        subdomains.add(subdomain)
    else:
        raise(&#34;Error fetching data from Wayback Machine&#34;)
    if logs==True:
        print()
    if subdomains_only==True:
        return list(urls.keys())
    for x in urls:
        urls[x]=list(urls[x])
    return urls




def get_subdomains(domain,dns_server=&#39;8.8.8.8&#39;,resolve_timeout=2,resolve_lifetime=1,logs=True, crt_timeout=120,user_agent=None,cookie=None,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,proxy=None,subdomains_only=False):
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
<pre><code class="python">def get_subdomains(domain,dns_server=&#39;8.8.8.8&#39;,resolve_timeout=2,resolve_lifetime=1,logs=True, crt_timeout=120,user_agent=None,cookie=None,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,proxy=None,subdomains_only=False):
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
<pre><code class="python">def get_subdomains_from_wayback(domain,dns_server=&#39;8.8.8.8&#39;,resolve_timeout=2,resolve_lifetime=1,logs=True,user_agent=None,cookie=None,wayback_timeout=50,subdomain_check_timeout=10,max_urls=10,subdomains_only=False,proxy=None):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    subdomains = set()
    urls={}
    invalid_subd=[]
    if logs==True:
        print(&#39;[*] searching with wayback machine ...\n&#39;)
    url = &#34;https://web.archive.org/cdx/search/cdx?url=*.{}/*&amp;output=json&amp;fl=original&amp;collapse=urlkey&#34;.format(domain)
    response = requests.Session().get(url,headers=hed,timeout=wayback_timeout,proxies=proxy)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            original_url = entry[0]
            match = re.match(r&#34;https?://([^/]*)&#34;, original_url.split(&#39;?&#39;)[0])
            if match:
                subdomain = match.group(1)
                if subdomain not in invalid_subd and extract_root_domain(subdomain)==domain:
                    if subdomain not in urls:
                        try:
                            r=requests.Session().get(original_url,headers=hed,timeout=subdomain_check_timeout,proxies=proxy)
                            if extract_root_domain(r.url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0])==extract_root_domain(subdomain):
                                urls[subdomain]=set()
                                urls[subdomain].add(original_url)
                                if logs==True:
                                    print(&#39;\t[+] {}&#39;.format(subdomain))
                        #if len(urls[subdomain])&lt;5:
                        except KeyboardInterrupt:
                            break
                        except:
                            try:
                                urls[subdomain].add(resolve(x.split(&#39;:&#39;)[0],server=dns_server,timeout=resolve_timeout,lifetime=resolve_lifetime))
                                if logs==True:
                                    print(&#39;\t[+] {}&#39;.format(subdomain))
                            except:
                                invalid_subd.append(subdomain)
                    else:
                        if len(urls[subdomain])&lt;max_urls:
                            urls[subdomain].add(original_url)
                        subdomains.add(subdomain)
    else:
        raise(&#34;Error fetching data from Wayback Machine&#34;)
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
<pre><code class="python">def subdomains_crt(domain,dns_server=&#39;8.8.8.8&#39;,resolve_timeout=2,resolve_lifetime=1,logs=True,subdomain_check_timeout=10, crt_timeout=120,cookie=None, user_agent=None, proxy=None,subdomains_only=False):
    domain=extract_root_domain(domain)
    if logs==True:
        print()
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    if &#34;://&#34; in domain:
        domain = domain.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
    if &#34;www.&#34; in domain:
        domain = domain.replace(&#34;www.&#34;, &#34;&#34;)
    if logs==True:
        print(&#39;[*] searching with crt.sh ...\n&#39;)
    try:
        r = requests.Session().get(
            &#34;https://crt.sh/?output=json&amp;q=%25.&#34; + domain,
            headers=hed,
            proxies=proxy,
            timeout=crt_timeout,
            verify=False,
        ).json()
        #print(r)
        a = [x[&#34;name_value&#34;].split(&#34;\\&#34;)[0] for x in r if (&#34;*.&#34; not in x[&#34;name_value&#34;])]
        l = []
        for x in a:
            if &#34;\n&#34; in x:
                l += x.split(&#34;\n&#34;)
            else:
                l.append(x)
        l= list(dict.fromkeys(l))
        result={}
        for x in l:
            if extract_root_domain(x)==domain:
                try:
                    r=requests.Session().get(&#39;http://&#39;+x,headers=hed,proxies=proxy,timeout=subdomain_check_timeout,verify=False)
                    if extract_root_domain(r.url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0])==extract_root_domain(x):
                        result.update({x:r.url})
                        if logs==True:
                            print(&#39;\t[+] {}&#39;.format(x))
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
<li><code><a title="bane.gather_info" href="index.md">bane.gather_info</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.gather_info.subdomains.get_subdomains" href="#bane.gather_info.subdomains.get_subdomains">get_subdomains</a></code></li>
<li><code><a title="bane.gather_info.subdomains.get_subdomains_from_wayback" href="#bane.gather_info.subdomains.get_subdomains_from_wayback">get_subdomains_from_wayback</a></code></li>
<li><code><a title="bane.gather_info.subdomains.subdomains_crt" href="#bane.gather_info.subdomains.subdomains_crt">subdomains_crt</a></code></li>
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