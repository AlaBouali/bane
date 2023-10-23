<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.cors_misconfigurations</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def cors_reflection(
    u,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    origin=&#34;www.evil-domain.com&#34;,
    debug=False,
    fill=10,
    headers={}
):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: origin})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == origin and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )


def cors_wildcard(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;*&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;*&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )


def cors_null(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;null&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;null&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )




def proxies_select(proxy, proxies):
    if proxy:
        return proxy
    if proxies:
        return random.choice(proxies)
    return None


def cors_misconfigurations_urls(
    u,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    res = {}
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Origin Reflection...&#34;)
        tes1 = cors_reflection(
            u,
            origin=origin,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes1[0] == True:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if wildcard_origin == True:
        if logs == True:
            print(&#34;[*] Testing for: Wildcard Origin...&#34;)
        tes2 = cors_wildcard(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes2[0] == True:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Null Origin...&#34;)
        tes3 = cors_null(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes3[0] == True:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    return res



def cors_misconfigurations(
    urls,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    l=[]
    for x in urls:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=cors_misconfigurations_urls(x,
                                            origin=origin,
                                            origin_reflection=origin_reflection,
                                            wildcard_origin=wildcard_origin,
                                            null_origin=null_origin,
                                            proxy=proxy,
                                            proxies=proxies,
                                            timeout=timeout,
                                            user_agent=user_agent,
                                            cookie=cookie,
                                            logs=logs,
                                            debug=debug,
                                            headers=headers
                                            )
        result={&#39;vulnerable&#39;:result[0],&#39;status&#39;:result[1]}
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;][&#39;vulnerable&#39;]!=False]</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations"><code class="name flex">
<span>def <span class="ident">cors_misconfigurations</span></span>(<span>urls, origin='www.evil-domain.com', origin_reflection=True, wildcard_origin=True, null_origin=True, proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, logs=True, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_misconfigurations(
    urls,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    l=[]
    for x in urls:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=cors_misconfigurations_urls(x,
                                            origin=origin,
                                            origin_reflection=origin_reflection,
                                            wildcard_origin=wildcard_origin,
                                            null_origin=null_origin,
                                            proxy=proxy,
                                            proxies=proxies,
                                            timeout=timeout,
                                            user_agent=user_agent,
                                            cookie=cookie,
                                            logs=logs,
                                            debug=debug,
                                            headers=headers
                                            )
        result={&#39;vulnerable&#39;:result[0],&#39;status&#39;:result[1]}
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;][&#39;vulnerable&#39;]!=False]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations_urls"><code class="name flex">
<span>def <span class="ident">cors_misconfigurations_urls</span></span>(<span>u, origin='www.evil-domain.com', origin_reflection=True, wildcard_origin=True, null_origin=True, proxy=None, proxies=None, timeout=10, user_agent=None, cookie=None, logs=True, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_misconfigurations_urls(
    u,
    origin=&#34;www.evil-domain.com&#34;,
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
    headers={}
):
    res = {}
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Origin Reflection...&#34;)
        tes1 = cors_reflection(
            u,
            origin=origin,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes1[0] == True:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;cors_reflection&#34;: tes1[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if wildcard_origin == True:
        if logs == True:
            print(&#34;[*] Testing for: Wildcard Origin...&#34;)
        tes2 = cors_wildcard(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes2[0] == True:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;wildcard_origin&#34;: tes2[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    if origin_reflection == True:
        if logs == True:
            print(&#34;[*] Testing for: Null Origin...&#34;)
        tes3 = cors_null(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
            headers=headers
        )
        if tes3[0] == True:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:True})
            if logs == True:
                print(&#34;[+] Vulnerable !!&#34;)
        else:
            res.update({&#34;null_origin&#34;: tes3[1],&#39;vulnerable&#39;:False})
            if logs == True:
                print(&#34;[-] Not vulnerable&#34;)
    return res</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_null"><code class="name flex">
<span>def <span class="ident">cors_null</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_null(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;null&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;null&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_reflection"><code class="name flex">
<span>def <span class="ident">cors_reflection</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, origin='www.evil-domain.com', debug=False, fill=10, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_reflection(
    u,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    origin=&#34;www.evil-domain.com&#34;,
    debug=False,
    fill=10,
    headers={}
):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: origin})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == origin and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.cors_wildcard"><code class="name flex">
<span>def <span class="ident">cors_wildcard</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cors_wildcard(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False,headers={}):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    heads.update({&#34;Origin&#34;: &#34;*&#34;})
    heads.update(headers)
    try:
        r = requests.Session().get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get(&#34;Access-Control-Allow-Origin&#34;, None)
        b = r.get(&#34;Access-Control-Allow-Credentials&#34;, None)
        if debug == True:
            for x in r:
                print(x + &#34; : &#34; + r[x])
        if a and b:
            if a == &#34;*&#34; and b == &#34;true&#34;:
                return (
                    True,
                    {
                        &#34;Access-Control-Allow-Origin&#34;: a,
                        &#34;Access-Control-Allow-Credentials&#34;: b,
                        &#34;Vulnerable&#34;: True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            &#34;Access-Control-Allow-Origin&#34;: a,
            &#34;Access-Control-Allow-Credentials&#34;: b,
            &#34;Vulnerable&#34;: False,
        },
    )</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.cors_misconfigurations.proxies_select"><code class="name flex">
<span>def <span class="ident">proxies_select</span></span>(<span>proxy, proxies)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def proxies_select(proxy, proxies):
    if proxy:
        return proxy
    if proxies:
        return random.choice(proxies)
    return None</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations">cors_misconfigurations</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations_urls" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_misconfigurations_urls">cors_misconfigurations_urls</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_null" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_null">cors_null</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_reflection" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_reflection">cors_reflection</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.cors_wildcard" href="#bane.scanners.vulnerabilities.cors_misconfigurations.cors_wildcard">cors_wildcard</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.cors_misconfigurations.proxies_select" href="#bane.scanners.vulnerabilities.cors_misconfigurations.proxies_select">proxies_select</a></code></li>
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