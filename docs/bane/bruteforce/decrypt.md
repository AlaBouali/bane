<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.decrypt</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *


class decrypt:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        md5_hash=False,
        sha1_hash=False,
        sha256_hash=False,
        sha224_hash=False,
        sha384_hash=False,
        sha512_hash=False,
        base64_string=False,
        caesar_hash=False,
        logs=False,
    ):
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                word_list,
                md5_hash,
                sha1_hash,
                sha256_hash,
                sha224_hash,
                sha384_hash,
                sha512_hash,
                base64_string,
                caesar_hash,
                logs,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        word_list,
        md5_hash,
        sha1_hash,
        sha256_hash,
        sha224_hash,
        sha384_hash,
        sha512_hash,
        base64_string,
        caesar_hash,
        logs,
    ):
        if self.logs == True:
            print(&#34;[!]hash: &#34; + u + &#34;\nbruteforcing has started!!!\n&#34;)
        for x in word_list:
            if self.stop == True:
                break
            if md5_hash == True:
                if dmd5(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: md5&#34;)
                    self.result = {u: [&#34;md5:&#34; + x]}
                    break
            if sha1_hash == True:
                if dsha1(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha1&#34;)
                    self.result = {u: [&#34;sha1:&#34; + x]}
                    break
            if sha256_hash == True:
                if dsha256(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha256&#34;)
                    self.result = {u: [&#34;sha256:&#34; + x]}
                    break
            if sha224_hash == True:
                if dsha224(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha224&#34;)
                    self.result = {u: [&#34;sha224:&#34; + x]}
                    break
            if sha384_hash == True:
                if dsha384(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha384&#34;)
                    self.result = {u: [&#34;sha384:&#34; + x]}
                    break
            if sha512_hash == True:
                if dsha512(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha512&#34;)
                    self.result = {u: [&#34;sha512:&#34; + x]}
                    break
            if base64_string == True:
                if base64_decode(x) == u:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: base64&#34;)
                    self.result = {u: [&#34;base64:&#34; + x]}
                    break
            if caesar_hash == True:
                for i in range(1, 27):
                    if dcaesar(x, i) == True:
                        if self.logs == True:
                            print(
                                &#34;[+]Hash match found: &#34;
                                + x
                                + &#34; | Type: caesar | Key: &#34;
                                + str(i)
                            )
                        self.result = {u: [&#34;caesar&#34; + str(i) + &#34;:&#34; + x]}
                        break
        if self.result == {}:
            if self.logs == True:
                print(&#34;[-]No match found&#34;)
        self.finish = True

    def done(self):
        return self.finish</code></pre>
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
<dt id="bane.bruteforce.decrypt.decrypt"><code class="flex name class">
<span>class <span class="ident">decrypt</span></span>
<span>(</span><span>u, word_list=[], threads_daemon=True, md5_hash=False, sha1_hash=False, sha256_hash=False, sha224_hash=False, sha384_hash=False, sha512_hash=False, base64_string=False, caesar_hash=False, logs=False)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class decrypt:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        md5_hash=False,
        sha1_hash=False,
        sha256_hash=False,
        sha224_hash=False,
        sha384_hash=False,
        sha512_hash=False,
        base64_string=False,
        caesar_hash=False,
        logs=False,
    ):
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                word_list,
                md5_hash,
                sha1_hash,
                sha256_hash,
                sha224_hash,
                sha384_hash,
                sha512_hash,
                base64_string,
                caesar_hash,
                logs,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        word_list,
        md5_hash,
        sha1_hash,
        sha256_hash,
        sha224_hash,
        sha384_hash,
        sha512_hash,
        base64_string,
        caesar_hash,
        logs,
    ):
        if self.logs == True:
            print(&#34;[!]hash: &#34; + u + &#34;\nbruteforcing has started!!!\n&#34;)
        for x in word_list:
            if self.stop == True:
                break
            if md5_hash == True:
                if dmd5(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: md5&#34;)
                    self.result = {u: [&#34;md5:&#34; + x]}
                    break
            if sha1_hash == True:
                if dsha1(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha1&#34;)
                    self.result = {u: [&#34;sha1:&#34; + x]}
                    break
            if sha256_hash == True:
                if dsha256(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha256&#34;)
                    self.result = {u: [&#34;sha256:&#34; + x]}
                    break
            if sha224_hash == True:
                if dsha224(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha224&#34;)
                    self.result = {u: [&#34;sha224:&#34; + x]}
                    break
            if sha384_hash == True:
                if dsha384(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha384&#34;)
                    self.result = {u: [&#34;sha384:&#34; + x]}
                    break
            if sha512_hash == True:
                if dsha512(x, u) == True:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha512&#34;)
                    self.result = {u: [&#34;sha512:&#34; + x]}
                    break
            if base64_string == True:
                if base64_decode(x) == u:
                    if self.logs == True:
                        print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: base64&#34;)
                    self.result = {u: [&#34;base64:&#34; + x]}
                    break
            if caesar_hash == True:
                for i in range(1, 27):
                    if dcaesar(x, i) == True:
                        if self.logs == True:
                            print(
                                &#34;[+]Hash match found: &#34;
                                + x
                                + &#34; | Type: caesar | Key: &#34;
                                + str(i)
                            )
                        self.result = {u: [&#34;caesar&#34; + str(i) + &#34;:&#34; + x]}
                        break
        if self.result == {}:
            if self.logs == True:
                print(&#34;[-]No match found&#34;)
        self.finish = True

    def done(self):
        return self.finish</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.decrypt.decrypt.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.decrypt.decrypt.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.decrypt.decrypt.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.decrypt.decrypt.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.decrypt.decrypt.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, word_list, md5_hash, sha1_hash, sha256_hash, sha224_hash, sha384_hash, sha512_hash, base64_string, caesar_hash, logs)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(
    self,
    u,
    word_list,
    md5_hash,
    sha1_hash,
    sha256_hash,
    sha224_hash,
    sha384_hash,
    sha512_hash,
    base64_string,
    caesar_hash,
    logs,
):
    if self.logs == True:
        print(&#34;[!]hash: &#34; + u + &#34;\nbruteforcing has started!!!\n&#34;)
    for x in word_list:
        if self.stop == True:
            break
        if md5_hash == True:
            if dmd5(x, u) == True:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: md5&#34;)
                self.result = {u: [&#34;md5:&#34; + x]}
                break
        if sha1_hash == True:
            if dsha1(x, u) == True:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha1&#34;)
                self.result = {u: [&#34;sha1:&#34; + x]}
                break
        if sha256_hash == True:
            if dsha256(x, u) == True:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha256&#34;)
                self.result = {u: [&#34;sha256:&#34; + x]}
                break
        if sha224_hash == True:
            if dsha224(x, u) == True:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha224&#34;)
                self.result = {u: [&#34;sha224:&#34; + x]}
                break
        if sha384_hash == True:
            if dsha384(x, u) == True:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha384&#34;)
                self.result = {u: [&#34;sha384:&#34; + x]}
                break
        if sha512_hash == True:
            if dsha512(x, u) == True:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: sha512&#34;)
                self.result = {u: [&#34;sha512:&#34; + x]}
                break
        if base64_string == True:
            if base64_decode(x) == u:
                if self.logs == True:
                    print(&#34;[+]Hash match found: &#34; + x + &#34; | Type: base64&#34;)
                self.result = {u: [&#34;base64:&#34; + x]}
                break
        if caesar_hash == True:
            for i in range(1, 27):
                if dcaesar(x, i) == True:
                    if self.logs == True:
                        print(
                            &#34;[+]Hash match found: &#34;
                            + x
                            + &#34; | Type: caesar | Key: &#34;
                            + str(i)
                        )
                    self.result = {u: [&#34;caesar&#34; + str(i) + &#34;:&#34; + x]}
                    break
    if self.result == {}:
        if self.logs == True:
            print(&#34;[-]No match found&#34;)
    self.finish = True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.decrypt.decrypt.done"><code class="name flex">
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
<h4><code><a title="bane.bruteforce.decrypt.decrypt" href="#bane.bruteforce.decrypt.decrypt">decrypt</a></code></h4>
<ul class="two-column">
<li><code><a title="bane.bruteforce.decrypt.decrypt.crack" href="#bane.bruteforce.decrypt.decrypt.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.decrypt.decrypt.done" href="#bane.bruteforce.decrypt.decrypt.done">done</a></code></li>
<li><code><a title="bane.bruteforce.decrypt.decrypt.finish" href="#bane.bruteforce.decrypt.decrypt.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.decrypt.decrypt.logs" href="#bane.bruteforce.decrypt.decrypt.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.decrypt.decrypt.result" href="#bane.bruteforce.decrypt.decrypt.result">result</a></code></li>
<li><code><a title="bane.bruteforce.decrypt.decrypt.stop" href="#bane.bruteforce.decrypt.decrypt.stop">stop</a></code></li>
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