<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.gather_info.ips</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.gather_info.utils import *


def myip(proxy=None, timeout=15):
    &#34;&#34;&#34;
    this function is for getting your ip using: ipinfo.io
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.myip()
    xxx.xx.xxx.xxx&#34;&#34;&#34;
    try:
        return requests.Session().get(
            &#34;http://ipinfo.io/ip&#34;,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text.strip()
    except:
        pass
    return &#34;&#34;



def geoip(u, timeout=15, proxy=None):
    &#34;&#34;&#34;
    this function is for getting: geoip informations
    &#34;&#34;&#34;
    try:
        r = requests.Session().get(
            &#34;https://geoip-db.com/jsonp/&#34; + u,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return json.loads(r.split(&#34;(&#34;)[1].split(&#34;)&#34;)[0])
    except:
        pass
    return {}


def reverse_ip_lookup(u, timeout=10, logs=True, returning=False, proxy=None):
    &#34;&#34;&#34;
    this function is for: reverse ip look up
    if you&#39;ve used it 100 times in 24 hours, your IP will be banned by &#34;api.hackertarget.com&#34; so i highly recommand you to use the &#34;proxy&#34; option by adding a http(s) proxy:

    bane.reverse_ip_lookup(&#39;XXX.XXX.XXX.XXX&#39;,proxy=&#39;IP:PORT&#39;)

    &#34;&#34;&#34;
    try:
        r = requests.Session().get(
            &#34;https://api.hackertarget.com/reverseiplookup/?q=&#34; + u,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return r.split(&#34;\n&#34;)
    except Exception as ex:
        pass
    return []</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.gather_info.ips.geoip"><code class="name flex">
<span>def <span class="ident">geoip</span></span>(<span>u, timeout=15, proxy=None)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for getting: geoip informations</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def geoip(u, timeout=15, proxy=None):
    &#34;&#34;&#34;
    this function is for getting: geoip informations
    &#34;&#34;&#34;
    try:
        r = requests.Session().get(
            &#34;https://geoip-db.com/jsonp/&#34; + u,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return json.loads(r.split(&#34;(&#34;)[1].split(&#34;)&#34;)[0])
    except:
        pass
    return {}</code></pre>
</details>
</dd>
<dt id="bane.gather_info.ips.myip"><code class="name flex">
<span>def <span class="ident">myip</span></span>(<span>proxy=None, timeout=15)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for getting your ip using: ipinfo.io
usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
bane.myip()
xxx.xx.xxx.xxx</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def myip(proxy=None, timeout=15):
    &#34;&#34;&#34;
    this function is for getting your ip using: ipinfo.io
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.myip()
    xxx.xx.xxx.xxx&#34;&#34;&#34;
    try:
        return requests.Session().get(
            &#34;http://ipinfo.io/ip&#34;,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text.strip()
    except:
        pass
    return &#34;&#34;</code></pre>
</details>
</dd>
<dt id="bane.gather_info.ips.reverse_ip_lookup"><code class="name flex">
<span>def <span class="ident">reverse_ip_lookup</span></span>(<span>u, timeout=10, logs=True, returning=False, proxy=None)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for: reverse ip look up
if you've used it 100 times in 24 hours, your IP will be banned by "api.hackertarget.com" so i highly recommand you to use the "proxy" option by adding a http(s) proxy:</p>
<p>bane.reverse_ip_lookup('XXX.XXX.XXX.XXX',proxy='IP:PORT')</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def reverse_ip_lookup(u, timeout=10, logs=True, returning=False, proxy=None):
    &#34;&#34;&#34;
    this function is for: reverse ip look up
    if you&#39;ve used it 100 times in 24 hours, your IP will be banned by &#34;api.hackertarget.com&#34; so i highly recommand you to use the &#34;proxy&#34; option by adding a http(s) proxy:

    bane.reverse_ip_lookup(&#39;XXX.XXX.XXX.XXX&#39;,proxy=&#39;IP:PORT&#39;)

    &#34;&#34;&#34;
    try:
        r = requests.Session().get(
            &#34;https://api.hackertarget.com/reverseiplookup/?q=&#34; + u,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        return r.split(&#34;\n&#34;)
    except Exception as ex:
        pass
    return []</code></pre>
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
<li><code><a title="bane.gather_info" href="index.md">bane.gather_info</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.gather_info.ips.geoip" href="#bane.gather_info.ips.geoip">geoip</a></code></li>
<li><code><a title="bane.gather_info.ips.myip" href="#bane.gather_info.ips.myip">myip</a></code></li>
<li><code><a title="bane.gather_info.ips.reverse_ip_lookup" href="#bane.gather_info.ips.reverse_ip_lookup">reverse_ip_lookup</a></code></li>
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