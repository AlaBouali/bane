<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.filemanager_finder</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *

class filemanager_finder:
    __slots__ = [&#34;logs&#34;, &#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;]

    def __init__(
        self,
        u,
        logs=True,
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        timeout=10,
        proxy=None,
        proxies=None,
        headers={}
    ):
        &#34;&#34;&#34;
        u: the link: http://www.example.com
        logs: (set by default to True) the show the process and requests
        mapping: (set by default to: False) if it is set to True, it will stop the prcess when it finds the link, else: it continue for more
        possible links
        returning: (set by default to: False) if you want it to return a list of possibly accesseble links to be used in your scripts set it to: True
        timeout: (set by default to 10) timeout flag for the requests

        usage:

        &gt;&gt;&gt;import bane
        &gt;&gt;&gt;url=&#39;http://www.example.com/&#39;
        &gt;&gt;&gt;bane.filemanager_finder(url)
        &#34;&#34;&#34;
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                user_agent,
                cookie,
                timeout,
                proxy,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(self, u, user_agent, cookie, timeout, proxy, proxies,headers):
        for i in manager:
            if self.stop == True:
                self.finish = True
                break
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            hed = {&#34;User-Agent&#34;: us}
            if cookie:
                hed.update({&#34;Cookie&#34;: cookie})
            hed.update(headers)
            try:
                if u[len(u) - 1] == &#34;/&#34;:
                    u = u[0 : len(u) - 1]
                g = u + i
                r = requests.Session().get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.codes.ok:
                    if (
                        (&#34;Uncaught exception&#34; not in r.text)
                        and (&#34;404 Not Found&#34; not in r.text)
                        and (&#34;could not be found&#34; not in r.text)
                    ):
                        self.finish = True
                        if self.logs == True:
                            sys.stdout.write(
                                &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                    manager.index(g), len(manager), self.finish
                                )
                            )
                            sys.stdout.flush()
                        self.result.update({u: g})
                        break
                    else:
                        if self.logs == True:
                            sys.stdout.write(
                                &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                    manager.index(g), len(manager), self.finish
                                )
                            )
                            sys.stdout.flush()
                else:
                    if self.logs == True:
                        sys.stdout.write(
                            &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                manager.index(g), len(manager), self.finish
                            )
                        )
                        sys.stdout.flush()
            except KeyboardInterrupt:
                break
            except Exception as e:
                pass
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
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder"><code class="flex name class">
<span>class <span class="ident">filemanager_finder</span></span>
<span>(</span><span>u, logs=True, threads_daemon=True, user_agent=None, cookie=None, timeout=10, proxy=None, proxies=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>u: the link: <a href="http://www.example.com">http://www.example.com</a>
logs: (set by default to True) the show the process and requests
mapping: (set by default to: False) if it is set to True, it will stop the prcess when it finds the link, else: it continue for more
possible links
returning: (set by default to: False) if you want it to return a list of possibly accesseble links to be used in your scripts set it to: True
timeout: (set by default to 10) timeout flag for the requests</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
url='http://www.example.com/'
bane.filemanager_finder(url)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class filemanager_finder:
    __slots__ = [&#34;logs&#34;, &#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;]

    def __init__(
        self,
        u,
        logs=True,
        threads_daemon=True,
        user_agent=None,
        cookie=None,
        timeout=10,
        proxy=None,
        proxies=None,
        headers={}
    ):
        &#34;&#34;&#34;
        u: the link: http://www.example.com
        logs: (set by default to True) the show the process and requests
        mapping: (set by default to: False) if it is set to True, it will stop the prcess when it finds the link, else: it continue for more
        possible links
        returning: (set by default to: False) if you want it to return a list of possibly accesseble links to be used in your scripts set it to: True
        timeout: (set by default to 10) timeout flag for the requests

        usage:

        &gt;&gt;&gt;import bane
        &gt;&gt;&gt;url=&#39;http://www.example.com/&#39;
        &gt;&gt;&gt;bane.filemanager_finder(url)
        &#34;&#34;&#34;
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                user_agent,
                cookie,
                timeout,
                proxy,
                proxies,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(self, u, user_agent, cookie, timeout, proxy, proxies,headers):
        for i in manager:
            if self.stop == True:
                self.finish = True
                break
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            hed = {&#34;User-Agent&#34;: us}
            if cookie:
                hed.update({&#34;Cookie&#34;: cookie})
            hed.update(headers)
            try:
                if u[len(u) - 1] == &#34;/&#34;:
                    u = u[0 : len(u) - 1]
                g = u + i
                r = requests.Session().get(
                    g,
                    headers=hed,
                    allow_redirects=False,
                    proxies=proxy,
                    timeout=timeout,
                    verify=False,
                )
                if r.status_code == requests.codes.ok:
                    if (
                        (&#34;Uncaught exception&#34; not in r.text)
                        and (&#34;404 Not Found&#34; not in r.text)
                        and (&#34;could not be found&#34; not in r.text)
                    ):
                        self.finish = True
                        if self.logs == True:
                            sys.stdout.write(
                                &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                    manager.index(g), len(manager), self.finish
                                )
                            )
                            sys.stdout.flush()
                        self.result.update({u: g})
                        break
                    else:
                        if self.logs == True:
                            sys.stdout.write(
                                &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                    manager.index(g), len(manager), self.finish
                                )
                            )
                            sys.stdout.flush()
                else:
                    if self.logs == True:
                        sys.stdout.write(
                            &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                manager.index(g), len(manager), self.finish
                            )
                        )
                        sys.stdout.flush()
            except KeyboardInterrupt:
                break
            except Exception as e:
                pass
        self.finish = True

    def done(self):
        return self.finish</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, user_agent, cookie, timeout, proxy, proxies, headers)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(self, u, user_agent, cookie, timeout, proxy, proxies,headers):
    for i in manager:
        if self.stop == True:
            self.finish = True
            break
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        hed = {&#34;User-Agent&#34;: us}
        if cookie:
            hed.update({&#34;Cookie&#34;: cookie})
        hed.update(headers)
        try:
            if u[len(u) - 1] == &#34;/&#34;:
                u = u[0 : len(u) - 1]
            g = u + i
            r = requests.Session().get(
                g,
                headers=hed,
                allow_redirects=False,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            )
            if r.status_code == requests.codes.ok:
                if (
                    (&#34;Uncaught exception&#34; not in r.text)
                    and (&#34;404 Not Found&#34; not in r.text)
                    and (&#34;could not be found&#34; not in r.text)
                ):
                    self.finish = True
                    if self.logs == True:
                        sys.stdout.write(
                            &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                manager.index(g), len(manager), self.finish
                            )
                        )
                        sys.stdout.flush()
                    self.result.update({u: g})
                    break
                else:
                    if self.logs == True:
                        sys.stdout.write(
                            &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                                manager.index(g), len(manager), self.finish
                            )
                        )
                        sys.stdout.flush()
            else:
                if self.logs == True:
                    sys.stdout.write(
                        &#34;\rStats: {}/{} | Found: {}  &#34;.format(
                            manager.index(g), len(manager), self.finish
                        )
                    )
                    sys.stdout.flush()
        except KeyboardInterrupt:
            break
        except Exception as e:
            pass
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.filemanager_finder.filemanager_finder.done"><code class="name flex">
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
<h4><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder" href="#bane.bruteforce.filemanager_finder.filemanager_finder">filemanager_finder</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder.crack" href="#bane.bruteforce.filemanager_finder.filemanager_finder.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder.done" href="#bane.bruteforce.filemanager_finder.filemanager_finder.done">done</a></code></li>
<li><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder.finish" href="#bane.bruteforce.filemanager_finder.filemanager_finder.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder.logs" href="#bane.bruteforce.filemanager_finder.filemanager_finder.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder.result" href="#bane.bruteforce.filemanager_finder.filemanager_finder.result">result</a></code></li>
<li><code><a title="bane.bruteforce.filemanager_finder.filemanager_finder.stop" href="#bane.bruteforce.filemanager_finder.filemanager_finder.stop">stop</a></code></li>
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