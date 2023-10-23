<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.ssrf</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def ssrf_check(
    u,
    null_byte=False,
    link=&#34;http://www.google.com&#34;,
    signature=&#34;&lt;title&gt;Google&lt;/title&gt;&#34;,
    proxy=None,
    proxies=None,
    timeout=25,
    user_agent=None,
    cookie=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is for FI vulnerability test using a link&#34;&#34;&#34;
    l = link
    if proxies:
        proxy = random.choice(proxies)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update(
        {
            &#34;Referer&#34;: u,
            &#34;Origin&#34;: u.split(&#34;://&#34;)[0] + &#34;://&#34; + u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    heads.update(headers)
    if &#34;=&#34; not in u:
        return (False, &#34;&#34;)
    if null_byte == True:
        l += &#34;%00&#34;
    try:
        r = requests.Session().get(
            u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
        )
        if (signature in r.text) or (r.status_code == 504):
            return (True, r.url)
    except Exception as e:
        if &#34;Read timed out&#34; in str(e):
            return (True, u.format(l))
    return (False, &#34;&#34;)


def ssrf_urls(
    u,
    null_byte=False,
    link=&#34;http://www.google.com&#34;,
    timeout=120,
    signature=&#34;&lt;title&gt;Google&lt;/title&gt;&#34;,
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    headers={}
):
    res = []
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,headers=headers)
    l = []
    d = a.values()
    for x in d:
        if len(x[3]) &gt; 0:
            l.append(x)
    o = []
    for x in l:
        ur = x[1]
        if ur.split(&#34;?&#34;)[0] not in o:
            o.append(ur.split(&#34;?&#34;)[0])
            if (
                ur.split(&#34;?&#34;)[0][-1] != &#34;/&#34;
                and &#34;.&#34; not in ur.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]
            ):
                ur = ur.replace(&#34;?&#34;, &#34;/?&#34;)
            for y in x[3]:
                if valid_parameter(y[1]) == True:
                    trgt = ur.replace(y[0] + &#34;=&#34; + y[1], y[0] + &#34;={}&#34;)
                    q = ssrf_check(
                        trgt,
                        null_byte=null_byte,
                        proxy=proxy,
                        link=link,
                        signature=signature,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                        headers=headers
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
    return res



def ssrf(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    link=&#34;http://www.google.com&#34;,
    timeout=120,
    signature=&#34;&lt;title&gt;Google&lt;/title&gt;&#34;,
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers=headers)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=ssrf_urls(x,
                        null_byte=null_byte,
                        link=link,
                        timeout=timeout,
                        signature=signature,
                        proxy=proxy,
                        proxies=proxies,
                        user_agent=user_agent,
                        cookie=cookie,
                        headers=headers)
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
<dt id="bane.scanners.vulnerabilities.ssrf.ssrf"><code class="name flex">
<span>def <span class="ident">ssrf</span></span>(<span>u, max_pages=5, logs=True, null_byte=False, link='http://www.google.com', timeout=120, signature=&#x27;&lt;title&gt;Google&lt;/title&gt;&#x27;, proxy=None, proxies=None, user_agent=None, cookie=None, pages=[], headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssrf(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    link=&#34;http://www.google.com&#34;,
    timeout=120,
    signature=&#34;&lt;title&gt;Google&lt;/title&gt;&#34;,
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers=headers)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=ssrf_urls(x,
                        null_byte=null_byte,
                        link=link,
                        timeout=timeout,
                        signature=signature,
                        proxy=proxy,
                        proxies=proxies,
                        user_agent=user_agent,
                        cookie=cookie,
                        headers=headers)
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.ssrf.ssrf_check"><code class="name flex">
<span>def <span class="ident">ssrf_check</span></span>(<span>u, null_byte=False, link='http://www.google.com', signature=&#x27;&lt;title&gt;Google&lt;/title&gt;&#x27;, proxy=None, proxies=None, timeout=25, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for FI vulnerability test using a link</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssrf_check(
    u,
    null_byte=False,
    link=&#34;http://www.google.com&#34;,
    signature=&#34;&lt;title&gt;Google&lt;/title&gt;&#34;,
    proxy=None,
    proxies=None,
    timeout=25,
    user_agent=None,
    cookie=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is for FI vulnerability test using a link&#34;&#34;&#34;
    l = link
    if proxies:
        proxy = random.choice(proxies)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update(
        {
            &#34;Referer&#34;: u,
            &#34;Origin&#34;: u.split(&#34;://&#34;)[0] + &#34;://&#34; + u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    heads.update(headers)
    if &#34;=&#34; not in u:
        return (False, &#34;&#34;)
    if null_byte == True:
        l += &#34;%00&#34;
    try:
        r = requests.Session().get(
            u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
        )
        if (signature in r.text) or (r.status_code == 504):
            return (True, r.url)
    except Exception as e:
        if &#34;Read timed out&#34; in str(e):
            return (True, u.format(l))
    return (False, &#34;&#34;)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.ssrf.ssrf_urls"><code class="name flex">
<span>def <span class="ident">ssrf_urls</span></span>(<span>u, null_byte=False, link='http://www.google.com', timeout=120, signature=&#x27;&lt;title&gt;Google&lt;/title&gt;&#x27;, proxy=None, proxies=None, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssrf_urls(
    u,
    null_byte=False,
    link=&#34;http://www.google.com&#34;,
    timeout=120,
    signature=&#34;&lt;title&gt;Google&lt;/title&gt;&#34;,
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    headers={}
):
    res = []
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,headers=headers)
    l = []
    d = a.values()
    for x in d:
        if len(x[3]) &gt; 0:
            l.append(x)
    o = []
    for x in l:
        ur = x[1]
        if ur.split(&#34;?&#34;)[0] not in o:
            o.append(ur.split(&#34;?&#34;)[0])
            if (
                ur.split(&#34;?&#34;)[0][-1] != &#34;/&#34;
                and &#34;.&#34; not in ur.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]
            ):
                ur = ur.replace(&#34;?&#34;, &#34;/?&#34;)
            for y in x[3]:
                if valid_parameter(y[1]) == True:
                    trgt = ur.replace(y[0] + &#34;=&#34; + y[1], y[0] + &#34;={}&#34;)
                    q = ssrf_check(
                        trgt,
                        null_byte=null_byte,
                        proxy=proxy,
                        link=link,
                        signature=signature,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                        headers=headers
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
    return res</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.ssrf.ssrf" href="#bane.scanners.vulnerabilities.ssrf.ssrf">ssrf</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssrf.ssrf_check" href="#bane.scanners.vulnerabilities.ssrf.ssrf_check">ssrf_check</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssrf.ssrf_urls" href="#bane.scanners.vulnerabilities.ssrf.ssrf_urls">ssrf_urls</a></code></li>
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