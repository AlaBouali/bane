<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.crlf_injection</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def set_requests(
    u, method=&#34;GET&#34;, data={}, files={}, params={}, headers={}, proxy={}, timeout=15
):
    s = requests.Session()
    req = requests.Request(
        method=method, url=u, headers=headers, data=data, files=files, params=params
    )
    prep = req.prepare()
    prep.url = u
    return s.send(prep, verify=False, proxies=proxy, timeout=timeout)


def crlf_unicode_encode(
    random_level=0, line_feed_only=False, carriage_return_only=False
):
    if line_feed_only == False and carriage_return_only == False:
        if random_level == 1:
            return random.choice([&#34;%E5%98%8D&#34;, &#34;%0d&#34;]) + random.choice(
                [&#34;%E5%98%8A&#34;, &#34;%0a&#34;]
            )
        if random_level == 2:
            return &#34;%E5%98%8D%E5%98%8A&#34;
        else:
            return &#34;%0d%0a&#34;
    else:
        if line_feed_only == True and carriage_return_only == False:
            if random_level == 1:
                return random.choice([&#34;%E5%98%8A&#34;, &#34;%0a&#34;])
            if random_level == 2:
                return &#34;%E5%98%8A&#34;
            else:
                return &#34;%0a&#34;
        if carriage_return_only == True and line_feed_only == False:
            if random_level == 1:
                return random.choice([&#34;%E5%98%8D&#34;, &#34;%0d&#34;])
            if random_level == 2:
                return &#34;%E5%98%8D&#34;
            else:
                return &#34;%0d&#34;
    return &#34;%0d%0a&#34;


def crlf_header_injection(
    u,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    headers={}
):
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
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + &#34;banetest:%20test&#34;,
            method=&#34;GET&#34;,
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return &#34;banetest&#34; in r.headers
    except Exception as e:
        pass
    return False


def crlf_body_injection(
    u,
    proxy=None,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    headers={}
):
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
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + &#34;banetest:%20test&#34;,
            method=&#34;GET&#34;,
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return &#34;banetest;$@*&#34; in r.text
    except Exception as e:
        pass
    return False</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.crlf_injection.crlf_body_injection"><code class="name flex">
<span>def <span class="ident">crlf_body_injection</span></span>(<span>u, proxy=None, unicode_random_level=0, carriage_return_only=False, line_feed_only=False, timeout=10, user_agent=None, cookie=None, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crlf_body_injection(
    u,
    proxy=None,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    headers={}
):
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
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + &#34;banetest:%20test&#34;,
            method=&#34;GET&#34;,
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return &#34;banetest;$@*&#34; in r.text
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.crlf_injection.crlf_header_injection"><code class="name flex">
<span>def <span class="ident">crlf_header_injection</span></span>(<span>u, unicode_random_level=0, carriage_return_only=False, line_feed_only=False, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crlf_header_injection(
    u,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    headers={}
):
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
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + &#34;banetest:%20test&#34;,
            method=&#34;GET&#34;,
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return &#34;banetest&#34; in r.headers
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.crlf_injection.crlf_unicode_encode"><code class="name flex">
<span>def <span class="ident">crlf_unicode_encode</span></span>(<span>random_level=0, line_feed_only=False, carriage_return_only=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crlf_unicode_encode(
    random_level=0, line_feed_only=False, carriage_return_only=False
):
    if line_feed_only == False and carriage_return_only == False:
        if random_level == 1:
            return random.choice([&#34;%E5%98%8D&#34;, &#34;%0d&#34;]) + random.choice(
                [&#34;%E5%98%8A&#34;, &#34;%0a&#34;]
            )
        if random_level == 2:
            return &#34;%E5%98%8D%E5%98%8A&#34;
        else:
            return &#34;%0d%0a&#34;
    else:
        if line_feed_only == True and carriage_return_only == False:
            if random_level == 1:
                return random.choice([&#34;%E5%98%8A&#34;, &#34;%0a&#34;])
            if random_level == 2:
                return &#34;%E5%98%8A&#34;
            else:
                return &#34;%0a&#34;
        if carriage_return_only == True and line_feed_only == False:
            if random_level == 1:
                return random.choice([&#34;%E5%98%8D&#34;, &#34;%0d&#34;])
            if random_level == 2:
                return &#34;%E5%98%8D&#34;
            else:
                return &#34;%0d&#34;
    return &#34;%0d%0a&#34;</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.crlf_injection.set_requests"><code class="name flex">
<span>def <span class="ident">set_requests</span></span>(<span>u, method='GET', data={}, files={}, params={}, headers={}, proxy={}, timeout=15)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def set_requests(
    u, method=&#34;GET&#34;, data={}, files={}, params={}, headers={}, proxy={}, timeout=15
):
    s = requests.Session()
    req = requests.Request(
        method=method, url=u, headers=headers, data=data, files=files, params=params
    )
    prep = req.prepare()
    prep.url = u
    return s.send(prep, verify=False, proxies=proxy, timeout=timeout)</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.crlf_injection.crlf_body_injection" href="#bane.scanners.vulnerabilities.crlf_injection.crlf_body_injection">crlf_body_injection</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.crlf_injection.crlf_header_injection" href="#bane.scanners.vulnerabilities.crlf_injection.crlf_header_injection">crlf_header_injection</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.crlf_injection.crlf_unicode_encode" href="#bane.scanners.vulnerabilities.crlf_injection.crlf_unicode_encode">crlf_unicode_encode</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.crlf_injection.set_requests" href="#bane.scanners.vulnerabilities.crlf_injection.set_requests">set_requests</a></code></li>
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