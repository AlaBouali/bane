<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.network_protocols.ntp</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.network_protocols.utils import *

def ntp_factor(u, timeout=3):
    &#34;&#34;&#34;
calculate the amplification factor for any given ntp server
 &#34;&#34;&#34;

    req = IP(dst=u) / UDP(sport=random.randint(1025, 65500), dport=123) \
        / Raw(load=&#39;\x17\x00\x02\x2a&#39; + &#39;\x00&#39; * 4)
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                      socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(bytes(req), (u, 123))
    s.settimeout(timeout)
    d = &#39;&#39;
    while True:
        try:
            o = &#39;&#39;
            o += str(s.recv(4096))
        except KeyboardInterrupt:
            s.close()
            break
        except:
            pass
        if len(o) == 0:
            break
        else:
            d += o
    a = len(req)
    b = len(d)
    c = round(len(d) * 1. / len(req), 3)
    return {
        &#39;protocol&#39;: &#39;ntp&#39;,
        &#39;ip&#39;: u,
        &#39;sent&#39;: a,
        &#39;received&#39;: b,
        &#39;amplification_factor&#39;: c,
        }</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.network_protocols.ntp.ntp_factor"><code class="name flex">
<span>def <span class="ident">ntp_factor</span></span>(<span>u, timeout=3)</span>
</code></dt>
<dd>
<div class="desc"><p>calculate the amplification factor for any given ntp server</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ntp_factor(u, timeout=3):
    &#34;&#34;&#34;
calculate the amplification factor for any given ntp server
 &#34;&#34;&#34;

    req = IP(dst=u) / UDP(sport=random.randint(1025, 65500), dport=123) \
        / Raw(load=&#39;\x17\x00\x02\x2a&#39; + &#39;\x00&#39; * 4)
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                      socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(bytes(req), (u, 123))
    s.settimeout(timeout)
    d = &#39;&#39;
    while True:
        try:
            o = &#39;&#39;
            o += str(s.recv(4096))
        except KeyboardInterrupt:
            s.close()
            break
        except:
            pass
        if len(o) == 0:
            break
        else:
            d += o
    a = len(req)
    b = len(d)
    c = round(len(d) * 1. / len(req), 3)
    return {
        &#39;protocol&#39;: &#39;ntp&#39;,
        &#39;ip&#39;: u,
        &#39;sent&#39;: a,
        &#39;received&#39;: b,
        &#39;amplification_factor&#39;: c,
        }</code></pre>
</details>
</dd>
</dl>
</section>
<section>
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
<li><code><a title="bane.scanners.network_protocols" href="index.md">bane.scanners.network_protocols</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.network_protocols.ntp.ntp_factor" href="#bane.scanners.network_protocols.ntp.ntp_factor">ntp_factor</a></code></li>
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