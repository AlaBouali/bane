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
                    if not ip.startswith(&#34;127.&#34;)
                ][:1],
                [
                    [
                        (s.connect((&#34;8.8.8.8&#34;, 53)), s.getsockname()[0], s.close())
                        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                    ][0][1]
                ],
            )
            if l
        ][0][0]
    except:
        return &#34;127.0.0.1&#34;


def host_alive(target):
    if os.name == &#34;nt&#34;:
        r = os.popen(&#34;ping -n 1 &#34; + target).readlines()
    else:
        r = os.popen(&#34;ping -c 1 &#34; + target).readlines()
    if &#34;TTL&#34; in str(r):
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
    &#34;&#34;&#34;syn = IP(dst=ip) / TCP(dport=port, flags=&#34;S&#34;)
    ans, unans = sr(syn, timeout=timeout, retry=retry, verbose=0)
    for sent, received in ans:
            print(port,received[TCP].flags)
        #if check_open == True:
            if received[TCP].flags == 18:
                return True
            else:
                return False
            &#39;&#39;&#39;if received[TCP].flags == &#34;RA&#34; or received[TCP].flags == &#34;SA&#34;:
            return True&#39;&#39;&#39;
    return False&#34;&#34;&#34;


class port_scan:
    __slots__ = [&#34;result&#34;]

    def scan(self,target,port,check_open,timeout,retry):
        a = tcp_scan(
            target,
            port=int(port),
            check_open=check_open,
            timeout=timeout,
            retry=retry,
        )
        if a == True:
            self.result.update({str(port): &#34;open&#34;})
        else:
            self.result.update({str(port): &#34;closed&#34;})

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
                t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={&#34;port&#34;: self.por[x]})
                t.daemon = threads_daemon
                t.start()
                #thr.append(t)
                time.sleep(0.001)
            while len(self.result) != len(ports):
                time.sleep(0.1)
        #except:
         #   pass
            &#34;&#34;&#34;for x in self.__dict__:
            if x != &#34;result&#34;:
                self.__dict__[x] = None&#34;&#34;&#34;</code></pre>
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
                    if not ip.startswith(&#34;127.&#34;)
                ][:1],
                [
                    [
                        (s.connect((&#34;8.8.8.8&#34;, 53)), s.getsockname()[0], s.close())
                        for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
                    ][0][1]
                ],
            )
            if l
        ][0][0]
    except:
        return &#34;127.0.0.1&#34;</code></pre>
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
    if os.name == &#34;nt&#34;:
        r = os.popen(&#34;ping -n 1 &#34; + target).readlines()
    else:
        r = os.popen(&#34;ping -c 1 &#34; + target).readlines()
    if &#34;TTL&#34; in str(r):
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
    &#34;&#34;&#34;syn = IP(dst=ip) / TCP(dport=port, flags=&#34;S&#34;)
    ans, unans = sr(syn, timeout=timeout, retry=retry, verbose=0)
    for sent, received in ans:
            print(port,received[TCP].flags)
        #if check_open == True:
            if received[TCP].flags == 18:
                return True
            else:
                return False
            &#39;&#39;&#39;if received[TCP].flags == &#34;RA&#34; or received[TCP].flags == &#34;SA&#34;:
            return True&#39;&#39;&#39;
    return False&#34;&#34;&#34;</code></pre>
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
    __slots__ = [&#34;result&#34;]

    def scan(self,target,port,check_open,timeout,retry):
        a = tcp_scan(
            target,
            port=int(port),
            check_open=check_open,
            timeout=timeout,
            retry=retry,
        )
        if a == True:
            self.result.update({str(port): &#34;open&#34;})
        else:
            self.result.update({str(port): &#34;closed&#34;})

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
                t = threading.Thread(target=self.scan,args=(u,x,check_open,timeout,retry))#,kwargs={&#34;port&#34;: self.por[x]})
                t.daemon = threads_daemon
                t.start()
                #thr.append(t)
                time.sleep(0.001)
            while len(self.result) != len(ports):
                time.sleep(0.1)
        #except:
         #   pass
            &#34;&#34;&#34;for x in self.__dict__:
            if x != &#34;result&#34;:
                self.__dict__[x] = None&#34;&#34;&#34;</code></pre>
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
        self.result.update({str(port): &#34;open&#34;})
    else:
        self.result.update({str(port): &#34;closed&#34;})</code></pre>
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
<li><code><a title="bane.gather_info" href="index.md">bane.gather_info</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.gather_info.network.close_socket" href="#bane.gather_info.network.close_socket">close_socket</a></code></li>
<li><code><a title="bane.gather_info.network.get_local_ip" href="#bane.gather_info.network.get_local_ip">get_local_ip</a></code></li>
<li><code><a title="bane.gather_info.network.host_alive" href="#bane.gather_info.network.host_alive">host_alive</a></code></li>
<li><code><a title="bane.gather_info.network.tcp_scan" href="#bane.gather_info.network.tcp_scan">tcp_scan</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.gather_info.network.port_scan" href="#bane.gather_info.network.port_scan">port_scan</a></code></h4>
<ul class="">
<li><code><a title="bane.gather_info.network.port_scan.result" href="#bane.gather_info.network.port_scan.result">result</a></code></li>
<li><code><a title="bane.gather_info.network.port_scan.scan" href="#bane.gather_info.network.port_scan.scan">scan</a></code></li>
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