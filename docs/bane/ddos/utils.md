<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.ddos.utils API documentation</title>
<meta content="" name="description"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" rel="stylesheet preload"/>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script crossorigin="" defer="" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</meta></head>
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

if os.path.isdir("/data/data") == True:
    adr = True  # the device is an android
if os.path.isdir("/data/data/com.termux/") == True:
    termux = True  # the application which runs the module is Termux
if (termux == False) or (adr == False):
    from bane.utils.swtch import *

def reorder_headers_randomly(s):
    b = s.split("\r\n\r\n")[1]
    a = s.split("\r\n\r\n")[0]
    m = a.split("\r\n")[0]
    c = a.split("\r\n")[1:]
    random.shuffle(c)
    return m + "\r\n" + "\r\n".join(c) + "\r\n\r\n" + b


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
    q = ""
    for i in range(random.randint(2, 5)):
        q += random_param() + random_param()
    p = ""
    for i in range(random.randint(2, 5)):
        p += random_param() + random_param()
    if "?" in pa:
        jo = "&amp;"
    else:
        jo = "?"
    pa += jo + q + "=" + p
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
            ed += ", "
            ed += df
    l = random.choice(al)
    for n in range(random.randint(0, 5)):
        l += ";q={},".format(round(random.uniform(0.1, 1), 1)) + random.choice(al)
    kl = random.randint(1, 2)
    ck = ""
    if cookie:
        ck = "Cookie: " + cookie + "\r\n"
    if ty == 1:
        m = "GET {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nReferer: {}\r\nHost: {}\r\n\r\n".format(
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
        k = ""
        for _ in range(random.randint(post_field_min, post_field_max)):
            k += random.choice(lis)
        j = ""
        for x in range(random.randint(post_min, post_max)):
            j += random.choice(lis)
        par = k + "=" + j
        m = "POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n{}".format(
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
                "https://public-dns.info/nameservers.txt", timeout=timeout
            ).text
        ).split("\n")
    except:
        return []


class DDoS_Class:

    def done(self):
        if "stop" in dir(self):
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
        a = self.__dict__["counter"]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
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
                "https://public-dns.info/nameservers.txt", timeout=timeout
            ).text
        ).split("\n")
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
    b = s.split("\r\n\r\n")[1]
    a = s.split("\r\n\r\n")[0]
    m = a.split("\r\n")[0]
    c = a.split("\r\n")[1:]
    random.shuffle(c)
    return m + "\r\n" + "\r\n".join(c) + "\r\n\r\n" + b</code></pre>
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
    q = ""
    for i in range(random.randint(2, 5)):
        q += random_param() + random_param()
    p = ""
    for i in range(random.randint(2, 5)):
        p += random_param() + random_param()
    if "?" in pa:
        jo = "&amp;"
    else:
        jo = "?"
    pa += jo + q + "=" + p
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
            ed += ", "
            ed += df
    l = random.choice(al)
    for n in range(random.randint(0, 5)):
        l += ";q={},".format(round(random.uniform(0.1, 1), 1)) + random.choice(al)
    kl = random.randint(1, 2)
    ck = ""
    if cookie:
        ck = "Cookie: " + cookie + "\r\n"
    if ty == 1:
        m = "GET {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nReferer: {}\r\nHost: {}\r\n\r\n".format(
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
        k = ""
        for _ in range(random.randint(post_field_min, post_field_max)):
            k += random.choice(lis)
        j = ""
        for x in range(random.randint(post_min, post_max)):
            j += random.choice(lis)
        par = k + "=" + j
        m = "POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n{}".format(
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
        if "stop" in dir(self):
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
        a = self.__dict__["counter"]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
        return a</code></pre>
</details>
<h3>Subclasses</h3>
<ul class="hlist">
<li><a href="http_spam.md#bane.ddos.http_spam.http_spam" title="bane.ddos.http_spam.http_spam">http_spam</a></li>
<li><a href="proxies_hammer.md#bane.ddos.proxies_hammer.prox_hammer" title="bane.ddos.proxies_hammer.prox_hammer">prox_hammer</a></li>
<li><a href="proxies_http_spam.md#bane.ddos.proxies_http_spam.prox_http_spam" title="bane.ddos.proxies_http_spam.prox_http_spam">prox_http_spam</a></li>
<li><a href="proxies_xerxes.md#bane.ddos.proxies_xerxes.prox_xerxes" title="bane.ddos.proxies_xerxes.prox_xerxes">prox_xerxes</a></li>
<li><a href="slow_read.md#bane.ddos.slow_read.slow_read" title="bane.ddos.slow_read.slow_read">slow_read</a></li>
<li><a href="tcp.md#bane.ddos.tcp.tcp_flood" title="bane.ddos.tcp.tcp_flood">tcp_flood</a></li>
<li><a href="torshammer.md#bane.ddos.torshammer.torshammer" title="bane.ddos.torshammer.torshammer">torshammer</a></li>
<li><a href="udp.md#bane.ddos.udp.udp_flood" title="bane.ddos.udp.udp_flood">udp_flood</a></li>
<li><a href="vse.md#bane.ddos.vse.vse_flood" title="bane.ddos.vse.vse_flood">vse_flood</a></li>
<li><a href="xerxes.md#bane.ddos.xerxes.xerxes" title="bane.ddos.xerxes.xerxes">xerxes</a></li>
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
    if "stop" in dir(self):
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
    a = self.__dict__["counter"]
    self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
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
<li><code><a href="index.md" title="bane.ddos">bane.ddos</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.ddos.utils.get_public_dns" title="bane.ddos.utils.get_public_dns">get_public_dns</a></code></li>
<li><code><a href="#bane.ddos.utils.random_param" title="bane.ddos.utils.random_param">random_param</a></code></li>
<li><code><a href="#bane.ddos.utils.reorder_headers_randomly" title="bane.ddos.utils.reorder_headers_randomly">reorder_headers_randomly</a></code></li>
<li><code><a href="#bane.ddos.utils.setup_http_packet" title="bane.ddos.utils.setup_http_packet">setup_http_packet</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a href="#bane.ddos.utils.DDoS_Class" title="bane.ddos.utils.DDoS_Class">DDoS_Class</a></code></h4>
<ul class="">
<li><code><a href="#bane.ddos.utils.DDoS_Class.done" title="bane.ddos.utils.DDoS_Class.done">done</a></code></li>
<li><code><a href="#bane.ddos.utils.DDoS_Class.kill" title="bane.ddos.utils.DDoS_Class.kill">kill</a></code></li>
<li><code><a href="#bane.ddos.utils.DDoS_Class.reset" title="bane.ddos.utils.DDoS_Class.reset">reset</a></code></li>
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