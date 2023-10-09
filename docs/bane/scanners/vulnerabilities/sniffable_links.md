<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.sniffable_links</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *

def sniffable_links(u, proxy=None, timeout=10, user_agent=None, cookie=None,content=None,logs=True,request_headers=None,headers={}):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update(headers)
    vul=[]
    try:
        if content==None:
            r=requests.Session().get(u,headers=heads,timeout=timeout,verify=False,proxies=proxy)
            for x in r.headers:
                    if x.lower().strip() == &#34;strict-transport-security&#34;:
                        if logs == True:
                            print(&#34;\n[-] Not vulnerable: Strict-Transport-Security is set&#34;)
                        return []
            soup = BeautifulSoup(r.content, &#39;html.parser&#39;)
        else:
            soup = BeautifulSoup(content, &#39;html.parser&#39;)
            if request_headers!=None:
                for x in request_headers:
                    if x.lower().strip() == &#34;strict-transport-security&#34;:
                        if logs == True:
                            print(&#34;\n[-] Not vulnerable: Strict-Transport-Security is set&#34;)
                        return []
        if u:
                parsed_url = urlparse(u)
                if parsed_url.netloc == urlparse(u).netloc:
                    if parsed_url.scheme != &#39;https&#39; and parsed_url.geturl().startswith(&#39;//&#39;)==False:
                        parsed_url=parsed_url.geturl()
                        if parsed_url not in vul:
                            vul.append(parsed_url)
                            if logs==True:
                                print(&#39;\t[+] Vulnerable : {}&#39;.format(parsed_url))
        media_elements=soup.find_all([&#39;img&#39;, &#39;audio&#39;, &#39;video&#39;, &#39;source&#39;,&#39;embed&#39;, &#39;script&#39;, &#39;link&#39;, &#39;a&#39;])
        for element in media_elements:
            src_or_href = element.get(&#39;src&#39;) or element.get(&#39;href&#39;)
            if src_or_href:
                parsed_url = urlparse(urljoin(u,src_or_href))
                if parsed_url.netloc == urlparse(u).netloc:
                    if parsed_url.scheme != &#39;https&#39; and parsed_url.geturl().startswith(&#39;//&#39;)==False:
                        parsed_url=parsed_url.geturl()
                        if parsed_url not in vul:
                            vul.append(parsed_url)
                            if logs==True:
                                print(&#39;\t[+] Vulnerable : {}&#39;.format(parsed_url))
    except Exception as ex:
        return vul
    return vul
    

def interceptable_links(
    u, 
    max_pages=5,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    content=None,
    logs=True,
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers={})
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=sniffable_links(x,
                        proxy=proxy,
                        timeout=timeout,
                        user_agent=user_agent, 
                        cookie=cookie,
                        content=content,
                        logs=logs,
                        headers=headers
                        )
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.sniffable_links.interceptable_links"><code class="name flex">
<span>def <span class="ident">interceptable_links</span></span>(<span>u, max_pages=5, proxy=None, timeout=10, user_agent=None, cookie=None, content=None, logs=True, pages=[], headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def interceptable_links(
    u, 
    max_pages=5,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    content=None,
    logs=True,
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers={})
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=sniffable_links(x,
                        proxy=proxy,
                        timeout=timeout,
                        user_agent=user_agent, 
                        cookie=cookie,
                        content=content,
                        logs=logs,
                        headers=headers
                        )
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.sniffable_links.sniffable_links"><code class="name flex">
<span>def <span class="ident">sniffable_links</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, content=None, logs=True, request_headers=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def sniffable_links(u, proxy=None, timeout=10, user_agent=None, cookie=None,content=None,logs=True,request_headers=None,headers={}):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update(headers)
    vul=[]
    try:
        if content==None:
            r=requests.Session().get(u,headers=heads,timeout=timeout,verify=False,proxies=proxy)
            for x in r.headers:
                    if x.lower().strip() == &#34;strict-transport-security&#34;:
                        if logs == True:
                            print(&#34;\n[-] Not vulnerable: Strict-Transport-Security is set&#34;)
                        return []
            soup = BeautifulSoup(r.content, &#39;html.parser&#39;)
        else:
            soup = BeautifulSoup(content, &#39;html.parser&#39;)
            if request_headers!=None:
                for x in request_headers:
                    if x.lower().strip() == &#34;strict-transport-security&#34;:
                        if logs == True:
                            print(&#34;\n[-] Not vulnerable: Strict-Transport-Security is set&#34;)
                        return []
        if u:
                parsed_url = urlparse(u)
                if parsed_url.netloc == urlparse(u).netloc:
                    if parsed_url.scheme != &#39;https&#39; and parsed_url.geturl().startswith(&#39;//&#39;)==False:
                        parsed_url=parsed_url.geturl()
                        if parsed_url not in vul:
                            vul.append(parsed_url)
                            if logs==True:
                                print(&#39;\t[+] Vulnerable : {}&#39;.format(parsed_url))
        media_elements=soup.find_all([&#39;img&#39;, &#39;audio&#39;, &#39;video&#39;, &#39;source&#39;,&#39;embed&#39;, &#39;script&#39;, &#39;link&#39;, &#39;a&#39;])
        for element in media_elements:
            src_or_href = element.get(&#39;src&#39;) or element.get(&#39;href&#39;)
            if src_or_href:
                parsed_url = urlparse(urljoin(u,src_or_href))
                if parsed_url.netloc == urlparse(u).netloc:
                    if parsed_url.scheme != &#39;https&#39; and parsed_url.geturl().startswith(&#39;//&#39;)==False:
                        parsed_url=parsed_url.geturl()
                        if parsed_url not in vul:
                            vul.append(parsed_url)
                            if logs==True:
                                print(&#39;\t[+] Vulnerable : {}&#39;.format(parsed_url))
    except Exception as ex:
        return vul
    return vul</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.sniffable_links.interceptable_links" href="#bane.scanners.vulnerabilities.sniffable_links.interceptable_links">interceptable_links</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.sniffable_links.sniffable_links" href="#bane.scanners.vulnerabilities.sniffable_links.sniffable_links">sniffable_links</a></code></li>
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