<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.admin_panel_finder</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *

class admin_panel_finder:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def done(self):
        return self.finish

    &#34;&#34;&#34;
   this function use a list of possible admin panel links with different extensions: php, asp, aspx, js, /, cfm, cgi, brf and html.
   
   ext: (set by default to: &#39;php&#39;) to define the link&#39;s extention.

   usage:

  &gt;&gt;&gt;import bane
  &gt;&gt;&gt;bane.admin_panel_finder(&#39;http://www.example.com&#39;,ext=&#39;php&#39;,timeout=7)

  &gt;&gt;&gt;bane.admin_panel_finder(&#39;http://www.example.com&#39;,ext=&#39;aspx&#39;,timeout=5)
 &#34;&#34;&#34;

    def __init__(
        self,
        u,
        logs=True, 
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        ext=&#34;php&#34;,
        timeout=10,
        proxy=None,
        proxies=None,
        headers={}
    ):
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
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
        timeout,
        logs,
        ext,
        user_agent,
        cookie,
        proxy,
        proxies,
        headers
    ):
        links = []
        ext = ext.strip()
        if ext.lower() == &#34;php&#34;:
            links = phpl
        elif ext.lower() == &#34;asp&#34;:
            links = aspl
        elif ext.lower() == &#34;aspx&#34;:
            links = aspxl
        elif ext.lower() == &#34;js&#34;:
            links = jsl
        elif ext == &#34;/&#34;:
            links = slashl
        elif ext.lower() == &#34;cfm&#34;:
            links = cfml
        elif ext.lower() == &#34;cgi&#34;:
            links = cgil
        elif ext.lower() == &#34;brf&#34;:
            links = brfl
        elif ext.lower() == &#34;html&#34;:
            links = htmll
        k = []
        for i in links:
            if self.stop == True:
                break
            try:
                if proxies:
                    proxy = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {&#34;User-Agent&#34;: us}
                if cookie:
                    hed.update({&#34;Cookie&#34;: cookie})
                hed.update(headers)
                if u[len(u) - 1] == &#34;/&#34;:
                    u = u[0 : len(u) - 1]
                g = u + i
                if logs == True:
                    print(&#34;[*]Trying:&#34;, g)
                r = requests.Session().get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.Session().codes.ok:
                    if logs == True:
                        print(&#34;[+]FOUND!!!&#34;)
                    k.append(g)
                else:
                    if logs == True:
                        print(&#34;[-]failed&#34;)
            except KeyboardInterrupt:
                break
            except Exception as e:
                if logs == True:
                    print(&#34;[-]Failed&#34;)
        self.result = {u: k}
        self.finish = True</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder"><code class="flex name class">
<span>class <span class="ident">admin_panel_finder</span></span>
<span>(</span><span>u, logs=True, threads_daemon=True, user_agent=None, cookie=None, ext='php', timeout=10, proxy=None, proxies=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class admin_panel_finder:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def done(self):
        return self.finish

    &#34;&#34;&#34;
   this function use a list of possible admin panel links with different extensions: php, asp, aspx, js, /, cfm, cgi, brf and html.
   
   ext: (set by default to: &#39;php&#39;) to define the link&#39;s extention.

   usage:

  &gt;&gt;&gt;import bane
  &gt;&gt;&gt;bane.admin_panel_finder(&#39;http://www.example.com&#39;,ext=&#39;php&#39;,timeout=7)

  &gt;&gt;&gt;bane.admin_panel_finder(&#39;http://www.example.com&#39;,ext=&#39;aspx&#39;,timeout=5)
 &#34;&#34;&#34;

    def __init__(
        self,
        u,
        logs=True, 
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        ext=&#34;php&#34;,
        timeout=10,
        proxy=None,
        proxies=None,
        headers={}
    ):
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
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
        timeout,
        logs,
        ext,
        user_agent,
        cookie,
        proxy,
        proxies,
        headers
    ):
        links = []
        ext = ext.strip()
        if ext.lower() == &#34;php&#34;:
            links = phpl
        elif ext.lower() == &#34;asp&#34;:
            links = aspl
        elif ext.lower() == &#34;aspx&#34;:
            links = aspxl
        elif ext.lower() == &#34;js&#34;:
            links = jsl
        elif ext == &#34;/&#34;:
            links = slashl
        elif ext.lower() == &#34;cfm&#34;:
            links = cfml
        elif ext.lower() == &#34;cgi&#34;:
            links = cgil
        elif ext.lower() == &#34;brf&#34;:
            links = brfl
        elif ext.lower() == &#34;html&#34;:
            links = htmll
        k = []
        for i in links:
            if self.stop == True:
                break
            try:
                if proxies:
                    proxy = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {&#34;User-Agent&#34;: us}
                if cookie:
                    hed.update({&#34;Cookie&#34;: cookie})
                hed.update(headers)
                if u[len(u) - 1] == &#34;/&#34;:
                    u = u[0 : len(u) - 1]
                g = u + i
                if logs == True:
                    print(&#34;[*]Trying:&#34;, g)
                r = requests.Session().get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.Session().codes.ok:
                    if logs == True:
                        print(&#34;[+]FOUND!!!&#34;)
                    k.append(g)
                else:
                    if logs == True:
                        print(&#34;[-]failed&#34;)
            except KeyboardInterrupt:
                break
            except Exception as e:
                if logs == True:
                    print(&#34;[-]Failed&#34;)
        self.result = {u: k}
        self.finish = True</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, timeout, logs, ext, user_agent, cookie, proxy, proxies, headers)</span>
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
    timeout,
    logs,
    ext,
    user_agent,
    cookie,
    proxy,
    proxies,
    headers
):
    links = []
    ext = ext.strip()
    if ext.lower() == &#34;php&#34;:
        links = phpl
    elif ext.lower() == &#34;asp&#34;:
        links = aspl
    elif ext.lower() == &#34;aspx&#34;:
        links = aspxl
    elif ext.lower() == &#34;js&#34;:
        links = jsl
    elif ext == &#34;/&#34;:
        links = slashl
    elif ext.lower() == &#34;cfm&#34;:
        links = cfml
    elif ext.lower() == &#34;cgi&#34;:
        links = cgil
    elif ext.lower() == &#34;brf&#34;:
        links = brfl
    elif ext.lower() == &#34;html&#34;:
        links = htmll
    k = []
    for i in links:
        if self.stop == True:
            break
        try:
            if proxies:
                proxy = random.choice(proxies)
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            hed = {&#34;User-Agent&#34;: us}
            if cookie:
                hed.update({&#34;Cookie&#34;: cookie})
            hed.update(headers)
            if u[len(u) - 1] == &#34;/&#34;:
                u = u[0 : len(u) - 1]
            g = u + i
            if logs == True:
                print(&#34;[*]Trying:&#34;, g)
            r = requests.Session().get(
                g,
                headers=hed,
                allow_redirects=False,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            )
            if r.status_code == requests.Session().codes.ok:
                if logs == True:
                    print(&#34;[+]FOUND!!!&#34;)
                k.append(g)
            else:
                if logs == True:
                    print(&#34;[-]failed&#34;)
        except KeyboardInterrupt:
            break
        except Exception as e:
            if logs == True:
                print(&#34;[-]Failed&#34;)
    self.result = {u: k}
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.admin_panel_finder.admin_panel_finder.done"><code class="name flex">
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
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder">admin_panel_finder</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder.crack" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder.done" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder.done">done</a></code></li>
<li><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder.finish" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder.logs" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder.result" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder.result">result</a></code></li>
<li><code><a title="bane.bruteforce.admin_panel_finder.admin_panel_finder.stop" href="#bane.bruteforce.admin_panel_finder.admin_panel_finder.stop">stop</a></code></li>
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