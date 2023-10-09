<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.gather_info.urls</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.gather_info.utils import *



def norton_rate(u, timeout=30, proxy=None):
    &#34;&#34;&#34;
    this function takes any giving and gives a security report from: safeweb.norton.com, if it is a: spam domain, contains a malware...
    it takes 3 arguments:
    u: the link to check
    logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
    returning: (set by default to: False) returning the report as a string format if it is set to: True.
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.norton_rate(domain)&#34;&#34;&#34;
    try:
        ur = urllib.quote(u, safe=&#34;&#34;)
        ul = &#34;https://safeweb.norton.com/report/show?url=&#34; + ur
        c = requests.Session().et(
            ul,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        s = soup.find_all(&#34;div&#34;, class_=&#34;communityRatings&#34;)
        s = remove_html_tags(str(s[0])).strip().split(&#34;\n&#34;)
        while &#34;&#34; in s:
            s.remove(&#34;&#34;)
        try:
            return {&#34;Profile&#34;: s[0], &#34;Rate&#34;: float(s[1]), &#34;By&#34;: s[2]}
        except:
            return {&#34;Profile&#34;: s[0], &#34;Rate&#34;: float(s[1])}
    except:
        pass


def http_options(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        s = requests.session()
        a = s.options(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return []
    b = []
    if &#34;Access-Control-Allow-Methods&#34; in a:
        b += [x.strip() for x in a[&#34;Access-Control-Allow-Methods&#34;].split(&#34;,&#34;)]
    if &#34;Allow&#34; in a:
        b += [x.strip() for x in a[&#34;Allow&#34;].split(&#34;,&#34;)]
    return b


def headers(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        #&#34;safe&#34;: sec,
        s = requests.session()
        a = s.get(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return None
    if logs == True:
        for x in a:
            print(&#34;{} : {}&#34;.format(x, a[x]))
    if returning == True:
        return a


def webhint_report(ur, proxy=None, timeout=10):
    &#34;&#34;&#34;
    this function takes any webpage link and returns a report link from webhint.io.&#34;&#34;&#34;
    u = &#34;https://webhint.io/scanner/&#34;
    r = &#34;&#34;
    if &#34;://&#34; not in ur:
        return r
    try:
        s = requests.session()
        s.get(u, proxies=proxy, timeout=timeout)
        data = {&#34;url&#34;: ur}
        a = s.post(u, data, proxies=proxy, timeout=timeout).text
        soup = BeautifulSoup(a, &#34;html.parser&#34;)
        s = soup.find_all(&#34;span&#34;, class_=&#34;permalink-content&#34;)
        for x in s:
            try:
                r = x.a[&#34;href&#34;]
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return r</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.gather_info.urls.headers"><code class="name flex">
<span>def <span class="ident">headers</span></span>(<span>u, timeout=10, user_agent=None, cookie=None, extra_headers=None, logs=True, returning=False, proxy=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def headers(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        #&#34;safe&#34;: sec,
        s = requests.session()
        a = s.get(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return None
    if logs == True:
        for x in a:
            print(&#34;{} : {}&#34;.format(x, a[x]))
    if returning == True:
        return a</code></pre>
</details>
</dd>
<dt id="bane.gather_info.urls.http_options"><code class="name flex">
<span>def <span class="ident">http_options</span></span>(<span>u, timeout=10, user_agent=None, cookie=None, extra_headers=None, logs=True, returning=False, proxy=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def http_options(
    u,
    timeout=10,
    user_agent=None,
    cookie=None,
    extra_headers=None,
    logs=True,
    returning=False,
    proxy=None,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        heads = {&#34;User-Agent&#34;: us}
    if extra_headers:
        heads.update(extra_headers)
    try:
        s = requests.session()
        a = s.options(u, headers=heads, proxies=proxy, timeout=timeout).headers
    except Exception as ex:
        return []
    b = []
    if &#34;Access-Control-Allow-Methods&#34; in a:
        b += [x.strip() for x in a[&#34;Access-Control-Allow-Methods&#34;].split(&#34;,&#34;)]
    if &#34;Allow&#34; in a:
        b += [x.strip() for x in a[&#34;Allow&#34;].split(&#34;,&#34;)]
    return b</code></pre>
</details>
</dd>
<dt id="bane.gather_info.urls.norton_rate"><code class="name flex">
<span>def <span class="ident">norton_rate</span></span>(<span>u, timeout=30, proxy=None)</span>
</code></dt>
<dd>
<div class="desc"><p>this function takes any giving and gives a security report from: safeweb.norton.com, if it is a: spam domain, contains a malware&hellip;
it takes 3 arguments:
u: the link to check
logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
returning: (set by default to: False) returning the report as a string format if it is set to: True.
usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
url='http://www.example.com'
bane.norton_rate(domain)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def norton_rate(u, timeout=30, proxy=None):
    &#34;&#34;&#34;
    this function takes any giving and gives a security report from: safeweb.norton.com, if it is a: spam domain, contains a malware...
    it takes 3 arguments:
    u: the link to check
    logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
    returning: (set by default to: False) returning the report as a string format if it is set to: True.
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.norton_rate(domain)&#34;&#34;&#34;
    try:
        ur = urllib.quote(u, safe=&#34;&#34;)
        ul = &#34;https://safeweb.norton.com/report/show?url=&#34; + ur
        c = requests.Session().et(
            ul,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        s = soup.find_all(&#34;div&#34;, class_=&#34;communityRatings&#34;)
        s = remove_html_tags(str(s[0])).strip().split(&#34;\n&#34;)
        while &#34;&#34; in s:
            s.remove(&#34;&#34;)
        try:
            return {&#34;Profile&#34;: s[0], &#34;Rate&#34;: float(s[1]), &#34;By&#34;: s[2]}
        except:
            return {&#34;Profile&#34;: s[0], &#34;Rate&#34;: float(s[1])}
    except:
        pass</code></pre>
</details>
</dd>
<dt id="bane.gather_info.urls.webhint_report"><code class="name flex">
<span>def <span class="ident">webhint_report</span></span>(<span>ur, proxy=None, timeout=10)</span>
</code></dt>
<dd>
<div class="desc"><p>this function takes any webpage link and returns a report link from webhint.io.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def webhint_report(ur, proxy=None, timeout=10):
    &#34;&#34;&#34;
    this function takes any webpage link and returns a report link from webhint.io.&#34;&#34;&#34;
    u = &#34;https://webhint.io/scanner/&#34;
    r = &#34;&#34;
    if &#34;://&#34; not in ur:
        return r
    try:
        s = requests.session()
        s.get(u, proxies=proxy, timeout=timeout)
        data = {&#34;url&#34;: ur}
        a = s.post(u, data, proxies=proxy, timeout=timeout).text
        soup = BeautifulSoup(a, &#34;html.parser&#34;)
        s = soup.find_all(&#34;span&#34;, class_=&#34;permalink-content&#34;)
        for x in s:
            try:
                r = x.a[&#34;href&#34;]
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return r</code></pre>
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
<li><code><a title="bane.gather_info.urls.headers" href="#bane.gather_info.urls.headers">headers</a></code></li>
<li><code><a title="bane.gather_info.urls.http_options" href="#bane.gather_info.urls.http_options">http_options</a></code></li>
<li><code><a title="bane.gather_info.urls.norton_rate" href="#bane.gather_info.urls.norton_rate">norton_rate</a></code></li>
<li><code><a title="bane.gather_info.urls.webhint_report" href="#bane.gather_info.urls.webhint_report">webhint_report</a></code></li>
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