<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.backend_technologies</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *
from bane.scanners.vulnerabilities.vulner_search import vulners_search

def scan_backend_technology(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=True,request_headers=None,headers={},api_key=None):
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0].split(&#39;:&#39;)[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(&#39;:&#39;)[0])
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update(headers)
    try:
        if request_headers==None:
            r = requests.Session().get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
        else:
            r=request_headers
        server=r.get(&#39;Server&#39;,&#39;&#39;)
        try:
            server_os=[x for x in server.split() if x.startswith(&#39;(&#39;)==True][0].replace(&#39;(&#39;,&#39;&#39;).replace(&#39;)&#39;,&#39;&#39;)
        except:
            server_os=&#39;&#39;
        backend=r.get(&#39;X-Powered-By&#39;,&#39;&#39;)
        if logs==True:
            print(&#34;Site info:\n\n\tURL: {}\n\tDomain: {}\n\tRoot domain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n&#34;.format(u,domain,root_domain,ip,server,server_os,backend))
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
    except Exception as e:
        return {}
    return {&#39;server_exploits&#39;:server_exploits,&#39;backend_technology_exploits&#39;:backend_technology_exploits}</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.backend_technologies.scan_backend_technology"><code class="name flex">
<span>def <span class="ident">scan_backend_technology</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=True, request_headers=None, headers={}, api_key=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def scan_backend_technology(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=True,request_headers=None,headers={},api_key=None):
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0].split(&#39;:&#39;)[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(&#39;:&#39;)[0])
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update(headers)
    try:
        if request_headers==None:
            r = requests.Session().get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
        else:
            r=request_headers
        server=r.get(&#39;Server&#39;,&#39;&#39;)
        try:
            server_os=[x for x in server.split() if x.startswith(&#39;(&#39;)==True][0].replace(&#39;(&#39;,&#39;&#39;).replace(&#39;)&#39;,&#39;&#39;)
        except:
            server_os=&#39;&#39;
        backend=r.get(&#39;X-Powered-By&#39;,&#39;&#39;)
        if logs==True:
            print(&#34;Site info:\n\n\tURL: {}\n\tDomain: {}\n\tRoot domain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n&#34;.format(u,domain,root_domain,ip,server,server_os,backend))
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
    except Exception as e:
        return {}
    return {&#39;server_exploits&#39;:server_exploits,&#39;backend_technology_exploits&#39;:backend_technology_exploits}</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities" href="index.md">bane.scanners.vulnerabilities</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.vulnerabilities.backend_technologies.scan_backend_technology" href="#bane.scanners.vulnerabilities.backend_technologies.scan_backend_technology">scan_backend_technology</a></code></li>
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