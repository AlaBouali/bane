<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.gather_info.network API documentation</title>
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
<h1 class="title">Module <code>bane.gather_info.network</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.gather_info.utils import *

def get_local_ip():
    try:
        return [
            l
            for l in (
                [
                    ip
                    for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")
                ][:1],
                [
                    [
                        (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                    ][0][1]
                ],
            )
            if l
        ][0][0]
    except:
        return "127.0.0.1"


def host_alive(target):
    if os.name == "nt":
        r = os.popen("ping -n 1 " + target).readlines()
    else:
        r = os.popen("ping -c 1 " + target).readlines()
    if "TTL" in str(r):
        r = None
        return True
    r = None
    return False

def close_socket(soc):
    try:
        soc.close()
    except:
        pass

def tcp_scan(ip, port=1, timeout=2, retry=1, check_open=False):
    s=socket.socket()
    s.settimeout(timeout)
    try:
        connection=s.connect_ex((ip,port))
        s.close()
        if connection==0:
            close_socket(s)
            return True
    except:
        pass
    close_socket(s)
    return False
    """syn = IP(dst=ip) / TCP(dport=port, flags="S")
    ans, unans = sr(syn, timeout=timeout, retry=retry, verbose=0)
    for sent, received in ans:
            print(port,received[TCP].flags)
        #if check_open == True:
            if received[TCP].flags == 18:
                return True
            else:
                return False
            '''if received[TCP].flags == "RA" or received[TCP].flags == "SA":
            return True'''
    return False"""


class port_scan:
    __slots__ = ["result"]

    def scan(self,target,port,check_open,timeout,retry):
        a = tcp_scan(
            target,
            port=int(port),
            check_open=check_open,
            timeout=timeout,
            retry=retry,
        )
        if a == True:
            self.result.update({str(port): "open"})
        else:
            self.result.update({str(port): "closed"})

    def __init__(
        self,
        u,
        ports=[21, 22, 23, 25, 43, 53, 80, 443, 2082, 3306],
        threads_daemon=True,
        timeout=3,
        retry=0,
        check_open=True,
    ):
            self.result={}
        #try:
            for x in ports:
                t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={"port": self.por[x]})
                t.daemon = threads_daemon
                t.start()
                #thr.append(t)
                time.sleep(0.001)
            while len(self.result) != len(ports):
                time.sleep(0.1)
        #except:
         #   pass
            """for x in self.__dict__:
            if x != "result":
                self.__dict__[x] = None"""</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.gather_info.network.close_socket"><code class="name flex">
<span>def <span class="ident">close_socket</span></span>(<span>soc)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def close_socket(soc):
    try:
        soc.close()
    except:
        pass</code></pre>
</details>
</dd>
<dt id="bane.gather_info.network.get_local_ip"><code class="name flex">
<span>def <span class="ident">get_local_ip</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_local_ip():
    try:
        return [
            l
            for l in (
                [
                    ip
                    for ip in socket.gethostbyname_ex(socket.gethostname())[2]
                    if not ip.startswith("127.")
                ][:1],
                [
                    [
                        (s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close())
                        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                    ][0][1]
                ],
            )
            if l
        ][0][0]
    except:
        return "127.0.0.1"</code></pre>
</details>
</dd>
<dt id="bane.gather_info.network.host_alive"><code class="name flex">
<span>def <span class="ident">host_alive</span></span>(<span>target)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def host_alive(target):
    if os.name == "nt":
        r = os.popen("ping -n 1 " + target).readlines()
    else:
        r = os.popen("ping -c 1 " + target).readlines()
    if "TTL" in str(r):
        r = None
        return True
    r = None
    return False</code></pre>
</details>
</dd>
<dt id="bane.gather_info.network.tcp_scan"><code class="name flex">
<span>def <span class="ident">tcp_scan</span></span>(<span>ip, port=1, timeout=2, retry=1, check_open=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def tcp_scan(ip, port=1, timeout=2, retry=1, check_open=False):
    s=socket.socket()
    s.settimeout(timeout)
    try:
        connection=s.connect_ex((ip,port))
        s.close()
        if connection==0:
            close_socket(s)
            return True
    except:
        pass
    close_socket(s)
    return False
    """syn = IP(dst=ip) / TCP(dport=port, flags="S")
    ans, unans = sr(syn, timeout=timeout, retry=retry, verbose=0)
    for sent, received in ans:
            print(port,received[TCP].flags)
        #if check_open == True:
            if received[TCP].flags == 18:
                return True
            else:
                return False
            '''if received[TCP].flags == "RA" or received[TCP].flags == "SA":
            return True'''
    return False"""</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.gather_info.network.port_scan"><code class="flex name class">
<span>class <span class="ident">port_scan</span></span>
<span>(</span><span>u, ports=[21, 22, 23, 25, 43, 53, 80, 443, 2082, 3306], threads_daemon=True, timeout=3, retry=0, check_open=True)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class port_scan:
    __slots__ = ["result"]

    def scan(self,target,port,check_open,timeout,retry):
        a = tcp_scan(
            target,
            port=int(port),
            check_open=check_open,
            timeout=timeout,
            retry=retry,
        )
        if a == True:
            self.result.update({str(port): "open"})
        else:
            self.result.update({str(port): "closed"})

    def __init__(
        self,
        u,
        ports=[21, 22, 23, 25, 43, 53, 80, 443, 2082, 3306],
        threads_daemon=True,
        timeout=3,
        retry=0,
        check_open=True,
    ):
            self.result={}
        #try:
            for x in ports:
                t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={"port": self.por[x]})
                t.daemon = threads_daemon
                t.start()
                #thr.append(t)
                time.sleep(0.001)
            while len(self.result) != len(ports):
                time.sleep(0.1)
        #except:
         #   pass
            """for x in self.__dict__:
            if x != "result":
                self.__dict__[x] = None"""</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.gather_info.network.port_scan.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.gather_info.network.port_scan.scan"><code class="name flex">
<span>def <span class="ident">scan</span></span>(<span>self, target, port, check_open, timeout, retry)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def scan(self,target,port,check_open,timeout,retry):
    a = tcp_scan(
        target,
        port=int(port),
        check_open=check_open,
        timeout=timeout,
        retry=retry,
    )
    if a == True:
        self.result.update({str(port): "open"})
    else:
        self.result.update({str(port): "closed"})</code></pre>
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
<li><code><a href="index.md" title="bane.gather_info">bane.gather_info</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.gather_info.network.close_socket" title="bane.gather_info.network.close_socket">close_socket</a></code></li>
<li><code><a href="#bane.gather_info.network.get_local_ip" title="bane.gather_info.network.get_local_ip">get_local_ip</a></code></li>
<li><code><a href="#bane.gather_info.network.host_alive" title="bane.gather_info.network.host_alive">host_alive</a></code></li>
<li><code><a href="#bane.gather_info.network.tcp_scan" title="bane.gather_info.network.tcp_scan">tcp_scan</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a href="#bane.gather_info.network.port_scan" title="bane.gather_info.network.port_scan">port_scan</a></code></h4>
<ul class="">
<li><code><a href="#bane.gather_info.network.port_scan.result" title="bane.gather_info.network.port_scan.result">result</a></code></li>
<li><code><a href="#bane.gather_info.network.port_scan.scan" title="bane.gather_info.network.port_scan.scan">scan</a></code></li>
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