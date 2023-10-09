<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.gather_info.domains</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.gather_info.utils import *


def whois(u):
    try:
        r = requests.Session().post(&#34;https://check-host.net/ip-info/whois&#34;, data={&#34;host&#34;: u})
        a = r.text.split(&#34;\n\n&#34;)[0]
        b = a.split(&#34;\n&#34;)
        d = {}
        for x in b:
            d.update(
                {
                    x.split(&#34;:&#34;)[0]
                    .strip(): x.replace(x.split(&#34;:&#34;)[0].strip(), &#34;&#34;)
                    .strip()[1:]
                    .strip()
                }
            )
        return d
    except:
        pass
    return {}


def info(u, timeout=10, proxy=None, logs=False, returning=True):
    &#34;&#34;&#34;
    this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
    with this format:
    &#39;requested information: result&#39;

    it takes 2 arguments:

    u: ip or domain
    timeout: (set by default to: 10) timeout flag for the request
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;domain=&#39;www.google.com&#39;
    &gt;&gt;&gt;bane.info(domain)&#34;&#34;&#34;
    try:
        h = &#34;&#34;
        u = &#34;https://check-host.net/ip-info?host=&#34; + u
        c = requests.Session().get(
            u, headers={&#34;User-Agent&#34;: random.choice(ua)}, proxies=proxy, timeout=timeout
        ).text
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        la = soup.find_all(&#34;a&#34;)
        l = []
        for i in la:
            if &#34;#ip_info-dbip&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-ip2location&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-geolite2&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
        p = soup.find_all(&#34;table&#34;)
        o = 0
        di = {}
        for x in p:
            try:
                do = {}
                y = x.find_all(&#34;tr&#34;)
                for w in y:
                    a = w.find_all(&#34;td&#34;)
                    try:
                        c = str(a[0]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = str(a[1]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = remove_html_tags(d).strip().replace(&#34;\n&#34;, &#34; &#34;)
                        do.update({c: d})
                    except:
                        pass
                di.update({l[o]: do})
                o += 1
            except:
                pass
        if logs == True:
            for x in di:
                print(x)
                print(&#34;&#34;)
                for y in di[x]:
                    print(y + &#34;: &#34; + di[x][y])
                print(&#34;&#34;)
        if returning == True:
            return di
    except:
        return None


def resolve(u, server=&#34;8.8.8.8&#34;, timeout=1, lifetime=1):
    o = []
    r = dns.resolver.Resolver()
    r.timeout = timeout
    r.lifetime = lifetime
    r.nameservers = [server]
    a = r.query(u)
    for x in a:
        o.append(str(x))
    return o</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.gather_info.domains.info"><code class="name flex">
<span>def <span class="ident">info</span></span>(<span>u, timeout=10, proxy=None, logs=False, returning=True)</span>
</code></dt>
<dd>
<div class="desc"><p>this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
with this format:
'requested information: result'</p>
<p>it takes 2 arguments:</p>
<p>u: ip or domain
timeout: (set by default to: 10) timeout flag for the request
usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
domain='www.google.com'
bane.info(domain)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def info(u, timeout=10, proxy=None, logs=False, returning=True):
    &#34;&#34;&#34;
    this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as string
    with this format:
    &#39;requested information: result&#39;

    it takes 2 arguments:

    u: ip or domain
    timeout: (set by default to: 10) timeout flag for the request
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;domain=&#39;www.google.com&#39;
    &gt;&gt;&gt;bane.info(domain)&#34;&#34;&#34;
    try:
        h = &#34;&#34;
        u = &#34;https://check-host.net/ip-info?host=&#34; + u
        c = requests.Session().get(
            u, headers={&#34;User-Agent&#34;: random.choice(ua)}, proxies=proxy, timeout=timeout
        ).text
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        la = soup.find_all(&#34;a&#34;)
        l = []
        for i in la:
            if &#34;#ip_info-dbip&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-ip2location&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
            if &#34;#ip_info-geolite2&#34; in str(i):
                l.append(remove_html_tags(str(i)).strip().replace(&#34;\n&#34;, &#34; &#34;))
        p = soup.find_all(&#34;table&#34;)
        o = 0
        di = {}
        for x in p:
            try:
                do = {}
                y = x.find_all(&#34;tr&#34;)
                for w in y:
                    a = w.find_all(&#34;td&#34;)
                    try:
                        c = str(a[0]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = str(a[1]).split(&#34;&lt;td&gt;&#34;)[1].split(&#34;&lt;/td&gt;&#34;)[0].strip()
                        d = remove_html_tags(d).strip().replace(&#34;\n&#34;, &#34; &#34;)
                        do.update({c: d})
                    except:
                        pass
                di.update({l[o]: do})
                o += 1
            except:
                pass
        if logs == True:
            for x in di:
                print(x)
                print(&#34;&#34;)
                for y in di[x]:
                    print(y + &#34;: &#34; + di[x][y])
                print(&#34;&#34;)
        if returning == True:
            return di
    except:
        return None</code></pre>
</details>
</dd>
<dt id="bane.gather_info.domains.resolve"><code class="name flex">
<span>def <span class="ident">resolve</span></span>(<span>u, server='8.8.8.8', timeout=1, lifetime=1)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def resolve(u, server=&#34;8.8.8.8&#34;, timeout=1, lifetime=1):
    o = []
    r = dns.resolver.Resolver()
    r.timeout = timeout
    r.lifetime = lifetime
    r.nameservers = [server]
    a = r.query(u)
    for x in a:
        o.append(str(x))
    return o</code></pre>
</details>
</dd>
<dt id="bane.gather_info.domains.whois"><code class="name flex">
<span>def <span class="ident">whois</span></span>(<span>u)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def whois(u):
    try:
        r = requests.Session().post(&#34;https://check-host.net/ip-info/whois&#34;, data={&#34;host&#34;: u})
        a = r.text.split(&#34;\n\n&#34;)[0]
        b = a.split(&#34;\n&#34;)
        d = {}
        for x in b:
            d.update(
                {
                    x.split(&#34;:&#34;)[0]
                    .strip(): x.replace(x.split(&#34;:&#34;)[0].strip(), &#34;&#34;)
                    .strip()[1:]
                    .strip()
                }
            )
        return d
    except:
        pass
    return {}</code></pre>
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
<li><code><a title="bane.gather_info.domains.info" href="#bane.gather_info.domains.info">info</a></code></li>
<li><code><a title="bane.gather_info.domains.resolve" href="#bane.gather_info.domains.resolve">resolve</a></code></li>
<li><code><a title="bane.gather_info.domains.whois" href="#bane.gather_info.domains.whois">whois</a></code></li>
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