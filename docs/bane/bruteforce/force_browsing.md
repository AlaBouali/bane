<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.force_browsing</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *


def access(u, timeout=10, user_agent=None, cookie=None, bypass=False, proxy=None,headers={}):
    if bypass == True:
        u += &#34;#&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            allow_redirects=False,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        if r.status_code == requests.codes.ok:
            if (&#34;Uncaught exception&#34; not in r.text) or (&#34;404 Not Found&#34; not in r.text):
                return True
    except Exception as e:
        pass
    return False



class force_browsing:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def __init__(
        self,
        u,
        timeout=10,
        threads_daemon=True,
        logs=True,
        ext=&#34;php&#34;,
        user_agent=None,
        cookie=None,
        proxy=None,
        proxies=None,
        headers={}
    ):
        &#34;&#34;&#34;
        this function is using &#34;Forced Browsing&#34; technique which is aim to access restricted areas without providing any credentials!!!
        it is used here to gain access to admin control panel by trying different possible combinations of links with the given URL.
        it&#39;s possible to do that and this a proof of concept that unserured cpanels with lack of right sessions configurations can be
        accessed just by guessing the right links :)

        the function takes those arguments:

        u: the targeted link which should be leading to the control panel, example:
        http://www.example.com/admin/login.php
        you have to delete &#39;login.php&#39; and insert the rest of the link in the function like this:

        &gt;&gt;&gt;import bane
        &gt;&gt;&gt;bane.force_browsing(&#39;http://www.example.com/admin/&#39;)

        then the function will try to find possible accesseble links:

        http://www.example.com/admin/edit.php
        http://www.example.com/admin/news.php
        http://www.example.com/admin/home.php

        timeout: (set by default to 10) timeout flag for the request
        logs: (set by default to: True) showing the process of the attack, you can turn it off by setting it to: False
        returning: (set by default to: False) return a list of the accessible link(s), to make the function return the list, set to: True
        mapping: (set by default to: True) find all possible links, to make stop if it has found 1 link just set it to: False
        ext: (set by default to: &#34;php&#34;) it helps you to find links with the given extention, cuurentky it supports only 3 extentions: &#34;php&#34;, &#34;asp&#34; and &#34;aspx&#34;( any other extention won&#39;t be used).&#34;&#34;&#34;
        self.stop = False
        self.finish = False
        self.result = {}
        self.logs = logs
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                timeout,
                logs,
                ext,
                user_agent,
                cookie,
                proxy,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        timeout=10,
        logs=True,
        ext=&#34;php&#34;,
        user_agent=None,
        cookie=None,
        proxy=None,
        proxies=None,
    ):
        l = []
        if u[len(u) - 1] == &#34;/&#34;:
            u = u[0 : len(u) - 1]
        for x in innerl:
            if self.stop == True:
                break
            g = u + x + &#34;.&#34; + ext
            if self.logs == True:
                print(&#34;[*]Trying:&#34;, g)
            try:
                if proxy:
                    proxy = proxy
                if proxies:
                    proxy=random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                h = access(g, user_agent=us, cookie=cookie, proxy=proxy)
            except KeyboardInterrupt:
                break
            if h == True:
                l.append(g)
                if self.logs == True:
                    print(&#34;[+]FOUND!!!&#34;)
            else:
                if self.logs == True:
                    print(&#34;[-]Failed&#34;)
        self.result = {u: l}
        self.finish = True

    def done(self):
        return self.finish</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.bruteforce.force_browsing.access"><code class="name flex">
<span>def <span class="ident">access</span></span>(<span>u, timeout=10, user_agent=None, cookie=None, bypass=False, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def access(u, timeout=10, user_agent=None, cookie=None, bypass=False, proxy=None,headers={}):
    if bypass == True:
        u += &#34;#&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            allow_redirects=False,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        if r.status_code == requests.codes.ok:
            if (&#34;Uncaught exception&#34; not in r.text) or (&#34;404 Not Found&#34; not in r.text):
                return True
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.bruteforce.force_browsing.force_browsing"><code class="flex name class">
<span>class <span class="ident">force_browsing</span></span>
<span>(</span><span>u, timeout=10, threads_daemon=True, logs=True, ext='php', user_agent=None, cookie=None, proxy=None, proxies=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is using "Forced Browsing" technique which is aim to access restricted areas without providing any credentials!!!
it is used here to gain access to admin control panel by trying different possible combinations of links with the given URL.
it's possible to do that and this a proof of concept that unserured cpanels with lack of right sessions configurations can be
accessed just by guessing the right links :)</p>
<p>the function takes those arguments:</p>
<p>u: the targeted link which should be leading to the control panel, example:
<a href="http://www.example.com/admin/login.php">http://www.example.com/admin/login.php</a>
you have to delete 'login.php' and insert the rest of the link in the function like this:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
bane.force_browsing('http://www.example.com/admin/')</p>
</blockquote>
</blockquote>
</blockquote>
<p>then the function will try to find possible accesseble links:</p>
<p><a href="http://www.example.com/admin/edit.php">http://www.example.com/admin/edit.php</a>
<a href="http://www.example.com/admin/news.php">http://www.example.com/admin/news.php</a>
<a href="http://www.example.com/admin/home.php">http://www.example.com/admin/home.php</a></p>
<p>timeout: (set by default to 10) timeout flag for the request
logs: (set by default to: True) showing the process of the attack, you can turn it off by setting it to: False
returning: (set by default to: False) return a list of the accessible link(s), to make the function return the list, set to: True
mapping: (set by default to: True) find all possible links, to make stop if it has found 1 link just set it to: False
ext: (set by default to: "php") it helps you to find links with the given extention, cuurentky it supports only 3 extentions: "php", "asp" and "aspx"( any other extention won't be used).</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class force_browsing:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def __init__(
        self,
        u,
        timeout=10,
        threads_daemon=True,
        logs=True,
        ext=&#34;php&#34;,
        user_agent=None,
        cookie=None,
        proxy=None,
        proxies=None,
        headers={}
    ):
        &#34;&#34;&#34;
        this function is using &#34;Forced Browsing&#34; technique which is aim to access restricted areas without providing any credentials!!!
        it is used here to gain access to admin control panel by trying different possible combinations of links with the given URL.
        it&#39;s possible to do that and this a proof of concept that unserured cpanels with lack of right sessions configurations can be
        accessed just by guessing the right links :)

        the function takes those arguments:

        u: the targeted link which should be leading to the control panel, example:
        http://www.example.com/admin/login.php
        you have to delete &#39;login.php&#39; and insert the rest of the link in the function like this:

        &gt;&gt;&gt;import bane
        &gt;&gt;&gt;bane.force_browsing(&#39;http://www.example.com/admin/&#39;)

        then the function will try to find possible accesseble links:

        http://www.example.com/admin/edit.php
        http://www.example.com/admin/news.php
        http://www.example.com/admin/home.php

        timeout: (set by default to 10) timeout flag for the request
        logs: (set by default to: True) showing the process of the attack, you can turn it off by setting it to: False
        returning: (set by default to: False) return a list of the accessible link(s), to make the function return the list, set to: True
        mapping: (set by default to: True) find all possible links, to make stop if it has found 1 link just set it to: False
        ext: (set by default to: &#34;php&#34;) it helps you to find links with the given extention, cuurentky it supports only 3 extentions: &#34;php&#34;, &#34;asp&#34; and &#34;aspx&#34;( any other extention won&#39;t be used).&#34;&#34;&#34;
        self.stop = False
        self.finish = False
        self.result = {}
        self.logs = logs
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                timeout,
                logs,
                ext,
                user_agent,
                cookie,
                proxy,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        timeout=10,
        logs=True,
        ext=&#34;php&#34;,
        user_agent=None,
        cookie=None,
        proxy=None,
        proxies=None,
    ):
        l = []
        if u[len(u) - 1] == &#34;/&#34;:
            u = u[0 : len(u) - 1]
        for x in innerl:
            if self.stop == True:
                break
            g = u + x + &#34;.&#34; + ext
            if self.logs == True:
                print(&#34;[*]Trying:&#34;, g)
            try:
                if proxy:
                    proxy = proxy
                if proxies:
                    proxy=random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                h = access(g, user_agent=us, cookie=cookie, proxy=proxy)
            except KeyboardInterrupt:
                break
            if h == True:
                l.append(g)
                if self.logs == True:
                    print(&#34;[+]FOUND!!!&#34;)
            else:
                if self.logs == True:
                    print(&#34;[-]Failed&#34;)
        self.result = {u: l}
        self.finish = True

    def done(self):
        return self.finish</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.force_browsing.force_browsing.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.force_browsing.force_browsing.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.force_browsing.force_browsing.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.force_browsing.force_browsing.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.force_browsing.force_browsing.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, timeout=10, logs=True, ext='php', user_agent=None, cookie=None, proxy=None, proxies=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(
    self,
    u,
    timeout=10,
    logs=True,
    ext=&#34;php&#34;,
    user_agent=None,
    cookie=None,
    proxy=None,
    proxies=None,
):
    l = []
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    for x in innerl:
        if self.stop == True:
            break
        g = u + x + &#34;.&#34; + ext
        if self.logs == True:
            print(&#34;[*]Trying:&#34;, g)
        try:
            if proxy:
                proxy = proxy
            if proxies:
                proxy=random.choice(proxies)
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            h = access(g, user_agent=us, cookie=cookie, proxy=proxy)
        except KeyboardInterrupt:
            break
        if h == True:
            l.append(g)
            if self.logs == True:
                print(&#34;[+]FOUND!!!&#34;)
        else:
            if self.logs == True:
                print(&#34;[-]Failed&#34;)
    self.result = {u: l}
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.force_browsing.force_browsing.done"><code class="name flex">
<span>def <span class="ident">done</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def done(self):
    return self.finish</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
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
<li><code><a title="bane.bruteforce" href="index.md">bane.bruteforce</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.bruteforce.force_browsing.access" href="#bane.bruteforce.force_browsing.access">access</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.bruteforce.force_browsing.force_browsing" href="#bane.bruteforce.force_browsing.force_browsing">force_browsing</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.force_browsing.force_browsing.crack" href="#bane.bruteforce.force_browsing.force_browsing.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.force_browsing.force_browsing.done" href="#bane.bruteforce.force_browsing.force_browsing.done">done</a></code></li>
<li><code><a title="bane.bruteforce.force_browsing.force_browsing.finish" href="#bane.bruteforce.force_browsing.force_browsing.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.force_browsing.force_browsing.logs" href="#bane.bruteforce.force_browsing.force_browsing.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.force_browsing.force_browsing.result" href="#bane.bruteforce.force_browsing.force_browsing.result">result</a></code></li>
<li><code><a title="bane.bruteforce.force_browsing.force_browsing.stop" href="#bane.bruteforce.force_browsing.force_browsing.stop">stop</a></code></li>
</ul>
</li>
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