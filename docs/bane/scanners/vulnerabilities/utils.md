<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.utils</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import subprocess, os, xtelnet, sys, cgi, re, json,platform
from colorama import Fore, Back, Style

if platform.system()==&#39;Java&#39;:
        Fore.WHITE = &#34;&#34;
        Fore.GREEN = &#34;&#34;
        Fore.RED = &#34;&#34;
        Fore.YELLOW = &#34;&#34;
        Fore.BLUE = &#34;&#34;
        Fore.MAGENTA = &#34;&#34;
        Style.RESET_ALL = &#34;&#34;

if sys.version_info &lt; (3, 0):
    if (sys.platform.lower() == &#34;win32&#34;) or (sys.platform.lower() == &#34;win64&#34;):
        Fore.WHITE = &#34;&#34;
        Fore.GREEN = &#34;&#34;
        Fore.RED = &#34;&#34;
        Fore.YELLOW = &#34;&#34;
        Fore.BLUE = &#34;&#34;
        Fore.MAGENTA = &#34;&#34;
        Style.RESET_ALL = &#34;&#34;
    import urllib, HTMLParser
    from urlparse import urlparse
    from urllib import unquote as url_decode
else:
    from urllib.parse import urlparse
    from urllib.parse import unquote as url_decode
    import urllib.parse as urllib
    import html.parser as HTMLParser

unicode = str
import requests, socket, random, time, ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import bs4,socks
from bs4 import BeautifulSoup
from bane.common.payloads import *
from bane.utils.pager import *
from bane.utils.js_fuck import js_fuck
from bane.utils.handle_files import write_file, delete_file
from bane.gather_info.info_s import extract_root_domain


def random_string(size):
    s = &#34;&#34;
    for x in range(size):
        s += random.choice(lis)
    return s


def setup_to_submit(form):
    d = {}
    f = {}
    for x in form[&#34;inputs&#34;]:
        if x[&#34;type&#34;] == &#34;file&#34;:
            f.update({x[&#34;name&#34;]: x[&#34;value&#34;]})
        else:
            d.update({x[&#34;name&#34;]: x[&#34;value&#34;]})
    return d, f


def setup_proxy(pr, prs):
    if pr:
        return pr
    if prs:
        return random.choice(prs)
    return None


def setup_ua(usra):
    if usra:
        return usra
    return random.choice(ua)


def valid_parameter(parm):
    try:
        float(parm)
        return False
    except:
        return True</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.utils.random_string"><code class="name flex">
<span>def <span class="ident">random_string</span></span>(<span>size)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def random_string(size):
    s = &#34;&#34;
    for x in range(size):
        s += random.choice(lis)
    return s</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.utils.setup_proxy"><code class="name flex">
<span>def <span class="ident">setup_proxy</span></span>(<span>pr, prs)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def setup_proxy(pr, prs):
    if pr:
        return pr
    if prs:
        return random.choice(prs)
    return None</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.utils.setup_to_submit"><code class="name flex">
<span>def <span class="ident">setup_to_submit</span></span>(<span>form)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def setup_to_submit(form):
    d = {}
    f = {}
    for x in form[&#34;inputs&#34;]:
        if x[&#34;type&#34;] == &#34;file&#34;:
            f.update({x[&#34;name&#34;]: x[&#34;value&#34;]})
        else:
            d.update({x[&#34;name&#34;]: x[&#34;value&#34;]})
    return d, f</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.utils.setup_ua"><code class="name flex">
<span>def <span class="ident">setup_ua</span></span>(<span>usra)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def setup_ua(usra):
    if usra:
        return usra
    return random.choice(ua)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.utils.valid_parameter"><code class="name flex">
<span>def <span class="ident">valid_parameter</span></span>(<span>parm)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def valid_parameter(parm):
    try:
        float(parm)
        return False
    except:
        return True</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities" href="index.md">bane.scanners.vulnerabilities</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.vulnerabilities.utils.random_string" href="#bane.scanners.vulnerabilities.utils.random_string">random_string</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.utils.setup_proxy" href="#bane.scanners.vulnerabilities.utils.setup_proxy">setup_proxy</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.utils.setup_to_submit" href="#bane.scanners.vulnerabilities.utils.setup_to_submit">setup_to_submit</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.utils.setup_ua" href="#bane.scanners.vulnerabilities.utils.setup_ua">setup_ua</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.utils.valid_parameter" href="#bane.scanners.vulnerabilities.utils.valid_parameter">valid_parameter</a></code></li>
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