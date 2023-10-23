<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.utils.swtch</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import os, sys, time

try:
    import stem
    from stem import Signal
    from stem.control import Controller
except:
    stem=None


def tor_switch_no_password(interval=30, logs=True):
    &#34;&#34;&#34;
     this function is for auto ip switching of tor&#39;s nodes, it doesnt work on windows because it use the command on linux to restart tor&#39; service in a chosen interval.

    it takes the following parameters:

    new: (set by default to: 30) the interval in seconds between switching tor&#39;s nodes
    logs: (set by default to: True) showing the screen prints

    example:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.torswitch1(new=15)
    &#34;&#34;&#34;
    i = True
    if (sys.platform == &#34;win32&#34;) or (sys.platform == &#34;win64&#34;) or stem==None or os.name==os.PyShadowString(&#39;java&#39;, &#39;nt&#39;):
        print(&#34;[-]This option is not for windows&#34;)
        i = False
    if i == True:
        while True:
            try:
                os.system(&#34;systemctl reload tor&#34;)
                if logs == True:
                    print(&#34;IP changed, sleeping for {} seconds...&#34;.format(interval))
                time.sleep(interval)
            except KeyboardInterrupt:
                break


def tor_switch_with_password(interval=30, password=None, p=9051, logs=True):
    &#34;&#34;&#34;
    this one does work on any OS, you just need to activate tor&#39;s control port 9051 and set the password.

    it takes the next parameters:

    new: (set by default to: 30) the interval in seconds between switching tor&#39;s nodes
    password: your password
    p: (set by default to: 9051) tor&#39;s control port
    logs: (set by default to: True) showing the screen prints&#34;&#34;&#34;
    if password == None:
        print(&#34;[-]you need to put your control port&#39;s password for authentication!!!&#34;)
    else:
        while True:
            try:
                with Controller.from_port(port=p) as controller:
                    controller.authenticate(password=password)
                    controller.signal(Signal.NEWNYM)
                    controller.close()
                if logs == True:
                    print(&#34;IP changed, sleeping for {} seconds...&#34;.format(interval))
                time.sleep(interval)
            except KeyboardInterrupt:
                break</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.utils.swtch.tor_switch_no_password"><code class="name flex">
<span>def <span class="ident">tor_switch_no_password</span></span>(<span>interval=30, logs=True)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for auto ip switching of tor's nodes, it doesnt work on windows because it use the command on linux to restart tor' service in a chosen interval.</p>
<p>it takes the following parameters:</p>
<p>new: (set by default to: 30) the interval in seconds between switching tor's nodes
logs: (set by default to: True) showing the screen prints</p>
<p>example:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
bane.torswitch1(new=15)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def tor_switch_no_password(interval=30, logs=True):
    &#34;&#34;&#34;
     this function is for auto ip switching of tor&#39;s nodes, it doesnt work on windows because it use the command on linux to restart tor&#39; service in a chosen interval.

    it takes the following parameters:

    new: (set by default to: 30) the interval in seconds between switching tor&#39;s nodes
    logs: (set by default to: True) showing the screen prints

    example:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.torswitch1(new=15)
    &#34;&#34;&#34;
    i = True
    if (sys.platform == &#34;win32&#34;) or (sys.platform == &#34;win64&#34;) or stem==None or os.name==os.PyShadowString(&#39;java&#39;, &#39;nt&#39;):
        print(&#34;[-]This option is not for windows&#34;)
        i = False
    if i == True:
        while True:
            try:
                os.system(&#34;systemctl reload tor&#34;)
                if logs == True:
                    print(&#34;IP changed, sleeping for {} seconds...&#34;.format(interval))
                time.sleep(interval)
            except KeyboardInterrupt:
                break</code></pre>
</details>
</dd>
<dt id="bane.utils.swtch.tor_switch_with_password"><code class="name flex">
<span>def <span class="ident">tor_switch_with_password</span></span>(<span>interval=30, password=None, p=9051, logs=True)</span>
</code></dt>
<dd>
<div class="desc"><p>this one does work on any OS, you just need to activate tor's control port 9051 and set the password.</p>
<p>it takes the next parameters:</p>
<p>new: (set by default to: 30) the interval in seconds between switching tor's nodes
password: your password
p: (set by default to: 9051) tor's control port
logs: (set by default to: True) showing the screen prints</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def tor_switch_with_password(interval=30, password=None, p=9051, logs=True):
    &#34;&#34;&#34;
    this one does work on any OS, you just need to activate tor&#39;s control port 9051 and set the password.

    it takes the next parameters:

    new: (set by default to: 30) the interval in seconds between switching tor&#39;s nodes
    password: your password
    p: (set by default to: 9051) tor&#39;s control port
    logs: (set by default to: True) showing the screen prints&#34;&#34;&#34;
    if password == None:
        print(&#34;[-]you need to put your control port&#39;s password for authentication!!!&#34;)
    else:
        while True:
            try:
                with Controller.from_port(port=p) as controller:
                    controller.authenticate(password=password)
                    controller.signal(Signal.NEWNYM)
                    controller.close()
                if logs == True:
                    print(&#34;IP changed, sleeping for {} seconds...&#34;.format(interval))
                time.sleep(interval)
            except KeyboardInterrupt:
                break</code></pre>
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
<li><code><a title="bane.utils" href="index.md">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.utils.swtch.tor_switch_no_password" href="#bane.utils.swtch.tor_switch_no_password">tor_switch_no_password</a></code></li>
<li><code><a title="bane.utils.swtch.tor_switch_with_password" href="#bane.utils.swtch.tor_switch_with_password">tor_switch_with_password</a></code></li>
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