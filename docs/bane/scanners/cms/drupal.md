<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.cms.drupal</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.cms.utils import *


def get_drupal_infos(u,user_agent=None,cookie=None,timeout=10,proxy=None,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None):
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0].split(&#39;:&#39;)[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(&#39;:&#39;)[0])
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    try:
        response = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        version=response.text.lower().split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;drupal&#39;)[1].split(&#39;(&#39;)[0].strip()
    except Exception as ex:
        #raise(ex)
        version=&#39;&#39;
    server=response.headers.get(&#39;Server&#39;,&#39;&#39;)
    try:
        server_os=[x for x in server.split() if x.startswith(&#39;(&#39;)==True][0].replace(&#39;(&#39;,&#39;&#39;).replace(&#39;)&#39;,&#39;&#39;)
    except:
        server_os=&#39;&#39;
    backend=response.headers.get(&#39;X-Powered-By&#39;,&#39;&#39;)
    if logs==True:
        print(&#34;Joomla site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tDrupal version: {}\n&#34;.format(u,domain,ip,server,server_os,backend,version))
    clickj=page_clickjacking(u,request_headers=response.headers)
    if logs==True:
        print(&#34;[i] Looking for subdomains...&#34;)
    subs=get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=proxy,subdomains_only=subdomains_only)
    if logs==True:
        print(&#34;[i] Cheking if we can sniff some cookies over some links...&#34;)
        print()
    media_non_ssl=sniffable_links(u,content=response.text,logs=logs,request_headers=response.headers)
    if logs==True:
        print()
    wp_vulns=[]
    if version!=&#39;&#39;:
        if logs==True:
            print(&#39;[i] looking for exploits for version: {}\n&#39;.format(version))
        wpvulns=vulners_search(&#39;drupal&#39;,version=version,proxy=proxy,api_key=api_key)
        for x in wpvulns:
            if &#39;drupal&#39; in x[&#39;title&#39;].lower() or &#39;drupal&#39; in x[&#39;description&#39;].lower():
                wp_vulns.append(x)
        for x in wp_vulns:
            for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                try:
                    del x[i]
                except:
                    pass
        if logs==True:
            if len(wp_vulns)==0:
                print(&#39;\t[-] none was found&#39;)
            else:
                for x in wp_vulns:
                    print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                    print()
    backend_technology_exploits={}
    if backend!=&#39;&#39;:
        bk=[]
        for back in backend.split():
            if logs==True:
                print(&#39;[i] looking for exploits for : {}\n&#39;.format(back))
            if &#39;/&#39; not in back:
                if logs==True:
                    print(&#39;\t[-] unknown version\n&#39;)
            else:
                bk=vulners_search(back.split(&#39;/&#39;)[0].lower(),version=back.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
            for x in bk:
                for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                    try:
                        del x[i]
                    except:
                        pass
            backend_technology_exploits.update({back:bk})
            if logs==True:
                if len(bk)==0:
                    print(&#39;\t[-] none was found&#39;)
                else:
                    for x in bk:
                        print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                        print()
    server_exploits={}
    if server!=&#39;&#39;:
        for sv in server.split():
            if sv.startswith(&#39;(&#39;)==False:
                sv_e=[]
                if logs==True:
                    print(&#39;[i] looking for exploits for : {}\n&#39;.format(sv))
                if &#39;/&#39; in sv:
                    sv_e=vulners_search(sv.split(&#39;/&#39;)[0].lower(),version=sv.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
                else:
                    if logs==True:
                        print(&#39;\t[-] unknown version\n&#39;)
                for x in sv_e:
                    for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                        try:
                            del x[i]
                        except:
                            pass
                server_exploits.update({sv:sv_e})
                if logs==True:
                    if len(sv_e)==0:
                        print(&#39;\t[-] none was found&#39;)
                    else:
                        for x in sv_e:
                            print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                            print()
    return {&#39;url&#39;:u,&#39;domain&#39;:domain,&#39;ip&#39;:ip,&#39;root_domain&#39;:root_domain,&#39;sub_domains&#39;:subs,&#39;server&#39;:server,&#39;os&#39;:server_os,&#39;backend_technology&#39;:backend,&#39;drupal_version&#39;:version,&#39;sniffable_links&#39;:media_non_ssl,&#39;clickjackable&#39;:clickj,&#34;exploits&#34;:wp_vulns,&#39;backend_technology_exploits&#39;:backend_technology_exploits,&#39;server_exploits&#39;:server_exploits}</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.cms.drupal.get_drupal_infos"><code class="name flex">
<span>def <span class="ident">get_drupal_infos</span></span>(<span>u, user_agent=None, cookie=None, timeout=10, proxy=None, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_drupal_infos(u,user_agent=None,cookie=None,timeout=10,proxy=None,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None):
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0].split(&#39;:&#39;)[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(&#39;:&#39;)[0])
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    try:
        response = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        version=response.text.lower().split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;drupal&#39;)[1].split(&#39;(&#39;)[0].strip()
    except Exception as ex:
        #raise(ex)
        version=&#39;&#39;
    server=response.headers.get(&#39;Server&#39;,&#39;&#39;)
    try:
        server_os=[x for x in server.split() if x.startswith(&#39;(&#39;)==True][0].replace(&#39;(&#39;,&#39;&#39;).replace(&#39;)&#39;,&#39;&#39;)
    except:
        server_os=&#39;&#39;
    backend=response.headers.get(&#39;X-Powered-By&#39;,&#39;&#39;)
    if logs==True:
        print(&#34;Joomla site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tDrupal version: {}\n&#34;.format(u,domain,ip,server,server_os,backend,version))
    clickj=page_clickjacking(u,request_headers=response.headers)
    if logs==True:
        print(&#34;[i] Looking for subdomains...&#34;)
    subs=get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=proxy,subdomains_only=subdomains_only)
    if logs==True:
        print(&#34;[i] Cheking if we can sniff some cookies over some links...&#34;)
        print()
    media_non_ssl=sniffable_links(u,content=response.text,logs=logs,request_headers=response.headers)
    if logs==True:
        print()
    wp_vulns=[]
    if version!=&#39;&#39;:
        if logs==True:
            print(&#39;[i] looking for exploits for version: {}\n&#39;.format(version))
        wpvulns=vulners_search(&#39;drupal&#39;,version=version,proxy=proxy,api_key=api_key)
        for x in wpvulns:
            if &#39;drupal&#39; in x[&#39;title&#39;].lower() or &#39;drupal&#39; in x[&#39;description&#39;].lower():
                wp_vulns.append(x)
        for x in wp_vulns:
            for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                try:
                    del x[i]
                except:
                    pass
        if logs==True:
            if len(wp_vulns)==0:
                print(&#39;\t[-] none was found&#39;)
            else:
                for x in wp_vulns:
                    print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                    print()
    backend_technology_exploits={}
    if backend!=&#39;&#39;:
        bk=[]
        for back in backend.split():
            if logs==True:
                print(&#39;[i] looking for exploits for : {}\n&#39;.format(back))
            if &#39;/&#39; not in back:
                if logs==True:
                    print(&#39;\t[-] unknown version\n&#39;)
            else:
                bk=vulners_search(back.split(&#39;/&#39;)[0].lower(),version=back.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
            for x in bk:
                for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                    try:
                        del x[i]
                    except:
                        pass
            backend_technology_exploits.update({back:bk})
            if logs==True:
                if len(bk)==0:
                    print(&#39;\t[-] none was found&#39;)
                else:
                    for x in bk:
                        print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                        print()
    server_exploits={}
    if server!=&#39;&#39;:
        for sv in server.split():
            if sv.startswith(&#39;(&#39;)==False:
                sv_e=[]
                if logs==True:
                    print(&#39;[i] looking for exploits for : {}\n&#39;.format(sv))
                if &#39;/&#39; in sv:
                    sv_e=vulners_search(sv.split(&#39;/&#39;)[0].lower(),version=sv.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
                else:
                    if logs==True:
                        print(&#39;\t[-] unknown version\n&#39;)
                for x in sv_e:
                    for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                        try:
                            del x[i]
                        except:
                            pass
                server_exploits.update({sv:sv_e})
                if logs==True:
                    if len(sv_e)==0:
                        print(&#39;\t[-] none was found&#39;)
                    else:
                        for x in sv_e:
                            print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                            print()
    return {&#39;url&#39;:u,&#39;domain&#39;:domain,&#39;ip&#39;:ip,&#39;root_domain&#39;:root_domain,&#39;sub_domains&#39;:subs,&#39;server&#39;:server,&#39;os&#39;:server_os,&#39;backend_technology&#39;:backend,&#39;drupal_version&#39;:version,&#39;sniffable_links&#39;:media_non_ssl,&#39;clickjackable&#39;:clickj,&#34;exploits&#34;:wp_vulns,&#39;backend_technology_exploits&#39;:backend_technology_exploits,&#39;server_exploits&#39;:server_exploits}</code></pre>
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
<li><code><a title="bane.scanners.cms" href="index.md">bane.scanners.cms</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.cms.drupal.get_drupal_infos" href="#bane.scanners.cms.drupal.get_drupal_infos">get_drupal_infos</a></code></li>
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