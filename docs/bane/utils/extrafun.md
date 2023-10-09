<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.utils.extrafun API documentation</title>
<meta content="" name="description"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" rel="stylesheet preload"/>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script crossorigin="" defer="" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</meta></head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.utils.extrafun</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import cgi, requests, os, random, re, hashlib, urllib, sys, cfscrape, json, gc
from bane.cryptographers import *
from bane.utils import *
if sys.version_info &lt; (3, 0):
    import HTMLParser
else:
    import html.parser as HTMLParser
import bs4
from bs4 import BeautifulSoup
from bane.common import *
from bane.utils.pager import crawl



def set_general_dns_resolver(host,port):
    socket.setdns()

def get_cf_cookie(domain, user_agent):
    try:
        s = cfscrape.create_scraper()
        c = s.get_cookie_string("http://" + domain, user_agent=user_agent)
        return c[0]
    except:
        return {}




def escape_html(s):
    """
    function to return escaped html string
    """
    return cgi.escape(s, quote=True)


def unescape_html(s):
    """
    function to return unescaped html string
    """
    return HTMLParser.HTMLParser().unescape(s).encode("utf-8")



def youtube_search(q, proxy=None, timeout=10):
    """
    this function is for searching on youtub and returning a links of related videos."""
    q = q.replace(" ", "+")
    u = "https://www.youtube.com/results"
    params = {"search_query": q}
    l = []
    try:
        r = requests.Session().get(
            u,
            params,
            headers={"User-Agent": random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(r, "html.parser")
        yt = soup.find_all(attrs={"class": "yt-uix-tile-link"})
        for vi in yt:
            try:
                vi = "https://www.youtube.com" + str(vi["href"])
                if vi not in l:
                    l.append(vi)
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return l


def webcams(count=10, by={"country": "us"}, timeout=10):
    a = 0
    f = {}
    x = 1
    if by:
        key = list(by.keys())[0]
        if key not in ["country", "tag", "city", "timezone", "type"]:
            raise Exception(
                "Your search must be in one of these categories: country, city, timezone, type, tag"
            )
        value = by[key].lower()
        if "country" in by:
            if by["country"].lower() not in [
                "af",
                "ax",
                "al",
                "dz",
                "as",
                "ad",
                "ao",
                "ai",
                "aq",
                "ag",
                "ar",
                "am",
                "aw",
                "au",
                "at",
                "az",
                "bs",
                "bh",
                "bd",
                "bb",
                "by",
                "be",
                "bz",
                "bj",
                "bm",
                "bt",
                "bo",
                "bq",
                "ba",
                "bw",
                "br",
                "io",
                "bn",
                "bg",
                "bf",
                "bi",
                "cv",
                "kh",
                "cm",
                "ca",
                "ky",
                "cf",
                "td",
                "cl",
                "cn",
                "cx",
                "cc",
                "co",
                "km",
                "cd",
                "cg",
                "ck",
                "cr",
                "ci",
                "hr",
                "cu",
                "cw",
                "cy",
                "cz",
                "dk",
                "dj",
                "dm",
                "do",
                "ec",
                "eg",
                "sv",
                "gq",
                "er",
                "ee",
                "sz",
                "et",
                "fk",
                "fo",
                "fj",
                "fi",
                "fr",
                "gf",
                "pf",
                "tf",
                "ga",
                "gm",
                "ge",
                "de",
                "gh",
                "gi",
                "gr",
                "gl",
                "gd",
                "gp",
                "gu",
                "gt",
                "gg",
                "gn",
                "gw",
                "gy",
                "ht",
                "hm",
                "va",
                "hn",
                "hk",
                "hu",
                "is",
                "in",
                "id",
                "ir",
                "iq",
                "ie",
                "im",
                "il",
                "it",
                "jm",
                "jp",
                "je",
                "jo",
                "kz",
                "ke",
                "ki",
                "kp",
                "kr",
                "kw",
                "kg",
                "la",
                "lv",
                "lb",
                "ls",
                "lr",
                "ly",
                "li",
                "lt",
                "lu",
                "mo",
                "mk",
                "mg",
                "mw",
                "my",
                "mv",
                "ml",
                "mt",
                "mh",
                "mq",
                "mr",
                "mu",
                "yt",
                "mx",
                "fm",
                "md",
                "mc",
                "mn",
                "me",
                "ms",
                "ma",
                "mz",
                "mm",
                "na",
                "nr",
                "np",
                "nl",
                "nc",
                "nz",
                "ni",
                "ne",
                "ng",
                "nu",
                "nf",
                "mp",
                "no",
                "om",
                "pk",
                "pw",
                "ps",
                "pa",
                "pg",
                "py",
                "pe",
                "ph",
                "pn",
                "pl",
                "pt",
                "pr",
                "qa",
                "re",
                "ro",
                "ru",
                "rw",
                "bl",
                "sh",
                "kn",
                "lc",
                "mf",
                "pm",
                "vc",
                "ws",
                "sm",
                "st",
                "sa",
                "sn",
                "rs",
                "sc",
                "sl",
                "sg",
                "sx",
                "sk",
                "si",
                "sb",
                "so",
                "za",
                "gs",
                "ss",
                "es",
                "lk",
                "sd",
                "sr",
                "se",
                "ch",
                "sy",
                "tw",
                "tj",
                "tz",
                "th",
                "tl",
                "tg",
                "tk",
                "to",
                "tt",
                "tn",
                "tr",
                "tm",
                "tc",
                "tv",
                "ug",
                "ua",
                "ae",
                "gb",
                "us",
                "uy",
                "uz",
                "vu",
                "ve",
                "vn",
                "vg",
                "vi",
                "wf",
                "ye",
                "zm",
                "zw",
            ]:
                raise Exception("Unexisting Country code")
        url = "https://www.insecam.org/en/by{}/{}/?page=".format(key, value)
    else:
        url = "https://www.insecam.org/en/byrating/?page="
    while True:
        try:
            soup = BeautifulSoup(
                requests.Session().get(
                    url + str(x),
                    headers={"User-Agent": random.choice(ua)},
                    timeout=timeout,
                ).text,
                "html.parser",
            )
            fi = soup.findAll("img", {"class": "thumbnail-item__img img-responsive"})
            for i in fi:
                j = HTMLParser.HTMLParser().unescape(i["src"])
                o = HTMLParser.HTMLParser().unescape(i["title"])
                f.update({j: o})
            if (len(fi) == 0) or (a == len(f)):
                break
            a = len(f)
        except Exception as e:
            break
        if len(f) &gt;= int(count):
            break
        x += 1
    return {k: f[k] for k in list(f.keys())[: int(count)]}</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.utils.extrafun.escape_html"><code class="name flex">
<span>def <span class="ident">escape_html</span></span>(<span>s)</span>
</code></dt>
<dd>
<div class="desc"><p>function to return escaped html string</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def escape_html(s):
    """
    function to return escaped html string
    """
    return cgi.escape(s, quote=True)</code></pre>
</details>
</dd>
<dt id="bane.utils.extrafun.get_cf_cookie"><code class="name flex">
<span>def <span class="ident">get_cf_cookie</span></span>(<span>domain, user_agent)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_cf_cookie(domain, user_agent):
    try:
        s = cfscrape.create_scraper()
        c = s.get_cookie_string("http://" + domain, user_agent=user_agent)
        return c[0]
    except:
        return {}</code></pre>
</details>
</dd>
<dt id="bane.utils.extrafun.set_general_dns_resolver"><code class="name flex">
<span>def <span class="ident">set_general_dns_resolver</span></span>(<span>host, port)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def set_general_dns_resolver(host,port):
    socket.setdns()</code></pre>
</details>
</dd>
<dt id="bane.utils.extrafun.unescape_html"><code class="name flex">
<span>def <span class="ident">unescape_html</span></span>(<span>s)</span>
</code></dt>
<dd>
<div class="desc"><p>function to return unescaped html string</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def unescape_html(s):
    """
    function to return unescaped html string
    """
    return HTMLParser.HTMLParser().unescape(s).encode("utf-8")</code></pre>
</details>
</dd>
<dt id="bane.utils.extrafun.webcams"><code class="name flex">
<span>def <span class="ident">webcams</span></span>(<span>count=10, by={'country': 'us'}, timeout=10)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def webcams(count=10, by={"country": "us"}, timeout=10):
    a = 0
    f = {}
    x = 1
    if by:
        key = list(by.keys())[0]
        if key not in ["country", "tag", "city", "timezone", "type"]:
            raise Exception(
                "Your search must be in one of these categories: country, city, timezone, type, tag"
            )
        value = by[key].lower()
        if "country" in by:
            if by["country"].lower() not in [
                "af",
                "ax",
                "al",
                "dz",
                "as",
                "ad",
                "ao",
                "ai",
                "aq",
                "ag",
                "ar",
                "am",
                "aw",
                "au",
                "at",
                "az",
                "bs",
                "bh",
                "bd",
                "bb",
                "by",
                "be",
                "bz",
                "bj",
                "bm",
                "bt",
                "bo",
                "bq",
                "ba",
                "bw",
                "br",
                "io",
                "bn",
                "bg",
                "bf",
                "bi",
                "cv",
                "kh",
                "cm",
                "ca",
                "ky",
                "cf",
                "td",
                "cl",
                "cn",
                "cx",
                "cc",
                "co",
                "km",
                "cd",
                "cg",
                "ck",
                "cr",
                "ci",
                "hr",
                "cu",
                "cw",
                "cy",
                "cz",
                "dk",
                "dj",
                "dm",
                "do",
                "ec",
                "eg",
                "sv",
                "gq",
                "er",
                "ee",
                "sz",
                "et",
                "fk",
                "fo",
                "fj",
                "fi",
                "fr",
                "gf",
                "pf",
                "tf",
                "ga",
                "gm",
                "ge",
                "de",
                "gh",
                "gi",
                "gr",
                "gl",
                "gd",
                "gp",
                "gu",
                "gt",
                "gg",
                "gn",
                "gw",
                "gy",
                "ht",
                "hm",
                "va",
                "hn",
                "hk",
                "hu",
                "is",
                "in",
                "id",
                "ir",
                "iq",
                "ie",
                "im",
                "il",
                "it",
                "jm",
                "jp",
                "je",
                "jo",
                "kz",
                "ke",
                "ki",
                "kp",
                "kr",
                "kw",
                "kg",
                "la",
                "lv",
                "lb",
                "ls",
                "lr",
                "ly",
                "li",
                "lt",
                "lu",
                "mo",
                "mk",
                "mg",
                "mw",
                "my",
                "mv",
                "ml",
                "mt",
                "mh",
                "mq",
                "mr",
                "mu",
                "yt",
                "mx",
                "fm",
                "md",
                "mc",
                "mn",
                "me",
                "ms",
                "ma",
                "mz",
                "mm",
                "na",
                "nr",
                "np",
                "nl",
                "nc",
                "nz",
                "ni",
                "ne",
                "ng",
                "nu",
                "nf",
                "mp",
                "no",
                "om",
                "pk",
                "pw",
                "ps",
                "pa",
                "pg",
                "py",
                "pe",
                "ph",
                "pn",
                "pl",
                "pt",
                "pr",
                "qa",
                "re",
                "ro",
                "ru",
                "rw",
                "bl",
                "sh",
                "kn",
                "lc",
                "mf",
                "pm",
                "vc",
                "ws",
                "sm",
                "st",
                "sa",
                "sn",
                "rs",
                "sc",
                "sl",
                "sg",
                "sx",
                "sk",
                "si",
                "sb",
                "so",
                "za",
                "gs",
                "ss",
                "es",
                "lk",
                "sd",
                "sr",
                "se",
                "ch",
                "sy",
                "tw",
                "tj",
                "tz",
                "th",
                "tl",
                "tg",
                "tk",
                "to",
                "tt",
                "tn",
                "tr",
                "tm",
                "tc",
                "tv",
                "ug",
                "ua",
                "ae",
                "gb",
                "us",
                "uy",
                "uz",
                "vu",
                "ve",
                "vn",
                "vg",
                "vi",
                "wf",
                "ye",
                "zm",
                "zw",
            ]:
                raise Exception("Unexisting Country code")
        url = "https://www.insecam.org/en/by{}/{}/?page=".format(key, value)
    else:
        url = "https://www.insecam.org/en/byrating/?page="
    while True:
        try:
            soup = BeautifulSoup(
                requests.Session().get(
                    url + str(x),
                    headers={"User-Agent": random.choice(ua)},
                    timeout=timeout,
                ).text,
                "html.parser",
            )
            fi = soup.findAll("img", {"class": "thumbnail-item__img img-responsive"})
            for i in fi:
                j = HTMLParser.HTMLParser().unescape(i["src"])
                o = HTMLParser.HTMLParser().unescape(i["title"])
                f.update({j: o})
            if (len(fi) == 0) or (a == len(f)):
                break
            a = len(f)
        except Exception as e:
            break
        if len(f) &gt;= int(count):
            break
        x += 1
    return {k: f[k] for k in list(f.keys())[: int(count)]}</code></pre>
</details>
</dd>
<dt id="bane.utils.extrafun.youtube_search"><code class="name flex">
<span>def <span class="ident">youtube_search</span></span>(<span>q, proxy=None, timeout=10)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for searching on youtub and returning a links of related videos.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def youtube_search(q, proxy=None, timeout=10):
    """
    this function is for searching on youtub and returning a links of related videos."""
    q = q.replace(" ", "+")
    u = "https://www.youtube.com/results"
    params = {"search_query": q}
    l = []
    try:
        r = requests.Session().get(
            u,
            params,
            headers={"User-Agent": random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(r, "html.parser")
        yt = soup.find_all(attrs={"class": "yt-uix-tile-link"})
        for vi in yt:
            try:
                vi = "https://www.youtube.com" + str(vi["href"])
                if vi not in l:
                    l.append(vi)
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return l</code></pre>
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
<li><code><a href="index.md" title="bane.utils">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.utils.extrafun.escape_html" title="bane.utils.extrafun.escape_html">escape_html</a></code></li>
<li><code><a href="#bane.utils.extrafun.get_cf_cookie" title="bane.utils.extrafun.get_cf_cookie">get_cf_cookie</a></code></li>
<li><code><a href="#bane.utils.extrafun.set_general_dns_resolver" title="bane.utils.extrafun.set_general_dns_resolver">set_general_dns_resolver</a></code></li>
<li><code><a href="#bane.utils.extrafun.unescape_html" title="bane.utils.extrafun.unescape_html">unescape_html</a></code></li>
<li><code><a href="#bane.utils.extrafun.webcams" title="bane.utils.extrafun.webcams">webcams</a></code></li>
<li><code><a href="#bane.utils.extrafun.youtube_search" title="bane.utils.extrafun.youtube_search">youtube_search</a></code></li>
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