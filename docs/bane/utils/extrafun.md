<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.utils.extrafun API documentation</title>
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



def get_cf_cookie(domain, user_agent):
    try:
        s = cfscrape.create_scraper()
        c = s.get_cookie_string(&#34;http://&#34; + domain, user_agent=user_agent)
        return c[0]
    except:
        return {}




def escape_html(s):
    &#34;&#34;&#34;
    function to return escaped html string
    &#34;&#34;&#34;
    return cgi.escape(s, quote=True)


def unescape_html(s):
    &#34;&#34;&#34;
    function to return unescaped html string
    &#34;&#34;&#34;
    return HTMLParser.HTMLParser().unescape(s).encode(&#34;utf-8&#34;)



def youtube_search(q, proxy=None, timeout=10):
    &#34;&#34;&#34;
    this function is for searching on youtub and returning a links of related videos.&#34;&#34;&#34;
    q = q.replace(&#34; &#34;, &#34;+&#34;)
    u = &#34;https://www.youtube.com/results&#34;
    params = {&#34;search_query&#34;: q}
    l = []
    try:
        r = requests.Session().get(
            u,
            params,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(r, &#34;html.parser&#34;)
        yt = soup.find_all(attrs={&#34;class&#34;: &#34;yt-uix-tile-link&#34;})
        for vi in yt:
            try:
                vi = &#34;https://www.youtube.com&#34; + str(vi[&#34;href&#34;])
                if vi not in l:
                    l.append(vi)
            except Exception as ex:
                pass
    except Exception as e:
        pass
    return l


def webcams(count=10, by={&#34;country&#34;: &#34;us&#34;}, timeout=10):
    a = 0
    f = {}
    x = 1
    if by:
        key = list(by.keys())[0]
        if key not in [&#34;country&#34;, &#34;tag&#34;, &#34;city&#34;, &#34;timezone&#34;, &#34;type&#34;]:
            raise Exception(
                &#34;Your search must be in one of these categories: country, city, timezone, type, tag&#34;
            )
        value = by[key].lower()
        if &#34;country&#34; in by:
            if by[&#34;country&#34;].lower() not in [
                &#34;af&#34;,
                &#34;ax&#34;,
                &#34;al&#34;,
                &#34;dz&#34;,
                &#34;as&#34;,
                &#34;ad&#34;,
                &#34;ao&#34;,
                &#34;ai&#34;,
                &#34;aq&#34;,
                &#34;ag&#34;,
                &#34;ar&#34;,
                &#34;am&#34;,
                &#34;aw&#34;,
                &#34;au&#34;,
                &#34;at&#34;,
                &#34;az&#34;,
                &#34;bs&#34;,
                &#34;bh&#34;,
                &#34;bd&#34;,
                &#34;bb&#34;,
                &#34;by&#34;,
                &#34;be&#34;,
                &#34;bz&#34;,
                &#34;bj&#34;,
                &#34;bm&#34;,
                &#34;bt&#34;,
                &#34;bo&#34;,
                &#34;bq&#34;,
                &#34;ba&#34;,
                &#34;bw&#34;,
                &#34;br&#34;,
                &#34;io&#34;,
                &#34;bn&#34;,
                &#34;bg&#34;,
                &#34;bf&#34;,
                &#34;bi&#34;,
                &#34;cv&#34;,
                &#34;kh&#34;,
                &#34;cm&#34;,
                &#34;ca&#34;,
                &#34;ky&#34;,
                &#34;cf&#34;,
                &#34;td&#34;,
                &#34;cl&#34;,
                &#34;cn&#34;,
                &#34;cx&#34;,
                &#34;cc&#34;,
                &#34;co&#34;,
                &#34;km&#34;,
                &#34;cd&#34;,
                &#34;cg&#34;,
                &#34;ck&#34;,
                &#34;cr&#34;,
                &#34;ci&#34;,
                &#34;hr&#34;,
                &#34;cu&#34;,
                &#34;cw&#34;,
                &#34;cy&#34;,
                &#34;cz&#34;,
                &#34;dk&#34;,
                &#34;dj&#34;,
                &#34;dm&#34;,
                &#34;do&#34;,
                &#34;ec&#34;,
                &#34;eg&#34;,
                &#34;sv&#34;,
                &#34;gq&#34;,
                &#34;er&#34;,
                &#34;ee&#34;,
                &#34;sz&#34;,
                &#34;et&#34;,
                &#34;fk&#34;,
                &#34;fo&#34;,
                &#34;fj&#34;,
                &#34;fi&#34;,
                &#34;fr&#34;,
                &#34;gf&#34;,
                &#34;pf&#34;,
                &#34;tf&#34;,
                &#34;ga&#34;,
                &#34;gm&#34;,
                &#34;ge&#34;,
                &#34;de&#34;,
                &#34;gh&#34;,
                &#34;gi&#34;,
                &#34;gr&#34;,
                &#34;gl&#34;,
                &#34;gd&#34;,
                &#34;gp&#34;,
                &#34;gu&#34;,
                &#34;gt&#34;,
                &#34;gg&#34;,
                &#34;gn&#34;,
                &#34;gw&#34;,
                &#34;gy&#34;,
                &#34;ht&#34;,
                &#34;hm&#34;,
                &#34;va&#34;,
                &#34;hn&#34;,
                &#34;hk&#34;,
                &#34;hu&#34;,
                &#34;is&#34;,
                &#34;in&#34;,
                &#34;id&#34;,
                &#34;ir&#34;,
                &#34;iq&#34;,
                &#34;ie&#34;,
                &#34;im&#34;,
                &#34;il&#34;,
                &#34;it&#34;,
                &#34;jm&#34;,
                &#34;jp&#34;,
                &#34;je&#34;,
                &#34;jo&#34;,
                &#34;kz&#34;,
                &#34;ke&#34;,
                &#34;ki&#34;,
                &#34;kp&#34;,
                &#34;kr&#34;,
                &#34;kw&#34;,
                &#34;kg&#34;,
                &#34;la&#34;,
                &#34;lv&#34;,
                &#34;lb&#34;,
                &#34;ls&#34;,
                &#34;lr&#34;,
                &#34;ly&#34;,
                &#34;li&#34;,
                &#34;lt&#34;,
                &#34;lu&#34;,
                &#34;mo&#34;,
                &#34;mk&#34;,
                &#34;mg&#34;,
                &#34;mw&#34;,
                &#34;my&#34;,
                &#34;mv&#34;,
                &#34;ml&#34;,
                &#34;mt&#34;,
                &#34;mh&#34;,
                &#34;mq&#34;,
                &#34;mr&#34;,
                &#34;mu&#34;,
                &#34;yt&#34;,
                &#34;mx&#34;,
                &#34;fm&#34;,
                &#34;md&#34;,
                &#34;mc&#34;,
                &#34;mn&#34;,
                &#34;me&#34;,
                &#34;ms&#34;,
                &#34;ma&#34;,
                &#34;mz&#34;,
                &#34;mm&#34;,
                &#34;na&#34;,
                &#34;nr&#34;,
                &#34;np&#34;,
                &#34;nl&#34;,
                &#34;nc&#34;,
                &#34;nz&#34;,
                &#34;ni&#34;,
                &#34;ne&#34;,
                &#34;ng&#34;,
                &#34;nu&#34;,
                &#34;nf&#34;,
                &#34;mp&#34;,
                &#34;no&#34;,
                &#34;om&#34;,
                &#34;pk&#34;,
                &#34;pw&#34;,
                &#34;ps&#34;,
                &#34;pa&#34;,
                &#34;pg&#34;,
                &#34;py&#34;,
                &#34;pe&#34;,
                &#34;ph&#34;,
                &#34;pn&#34;,
                &#34;pl&#34;,
                &#34;pt&#34;,
                &#34;pr&#34;,
                &#34;qa&#34;,
                &#34;re&#34;,
                &#34;ro&#34;,
                &#34;ru&#34;,
                &#34;rw&#34;,
                &#34;bl&#34;,
                &#34;sh&#34;,
                &#34;kn&#34;,
                &#34;lc&#34;,
                &#34;mf&#34;,
                &#34;pm&#34;,
                &#34;vc&#34;,
                &#34;ws&#34;,
                &#34;sm&#34;,
                &#34;st&#34;,
                &#34;sa&#34;,
                &#34;sn&#34;,
                &#34;rs&#34;,
                &#34;sc&#34;,
                &#34;sl&#34;,
                &#34;sg&#34;,
                &#34;sx&#34;,
                &#34;sk&#34;,
                &#34;si&#34;,
                &#34;sb&#34;,
                &#34;so&#34;,
                &#34;za&#34;,
                &#34;gs&#34;,
                &#34;ss&#34;,
                &#34;es&#34;,
                &#34;lk&#34;,
                &#34;sd&#34;,
                &#34;sr&#34;,
                &#34;se&#34;,
                &#34;ch&#34;,
                &#34;sy&#34;,
                &#34;tw&#34;,
                &#34;tj&#34;,
                &#34;tz&#34;,
                &#34;th&#34;,
                &#34;tl&#34;,
                &#34;tg&#34;,
                &#34;tk&#34;,
                &#34;to&#34;,
                &#34;tt&#34;,
                &#34;tn&#34;,
                &#34;tr&#34;,
                &#34;tm&#34;,
                &#34;tc&#34;,
                &#34;tv&#34;,
                &#34;ug&#34;,
                &#34;ua&#34;,
                &#34;ae&#34;,
                &#34;gb&#34;,
                &#34;us&#34;,
                &#34;uy&#34;,
                &#34;uz&#34;,
                &#34;vu&#34;,
                &#34;ve&#34;,
                &#34;vn&#34;,
                &#34;vg&#34;,
                &#34;vi&#34;,
                &#34;wf&#34;,
                &#34;ye&#34;,
                &#34;zm&#34;,
                &#34;zw&#34;,
            ]:
                raise Exception(&#34;Unexisting Country code&#34;)
        url = &#34;https://www.insecam.org/en/by{}/{}/?page=&#34;.format(key, value)
    else:
        url = &#34;https://www.insecam.org/en/byrating/?page=&#34;
    while True:
        try:
            soup = BeautifulSoup(
                requests.Session().get(
                    url + str(x),
                    headers={&#34;User-Agent&#34;: random.choice(ua)},
                    timeout=timeout,
                ).text,
                &#34;html.parser&#34;,
            )
            fi = soup.findAll(&#34;img&#34;, {&#34;class&#34;: &#34;thumbnail-item__img img-responsive&#34;})
            for i in fi:
                j = HTMLParser.HTMLParser().unescape(i[&#34;src&#34;])
                o = HTMLParser.HTMLParser().unescape(i[&#34;title&#34;])
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
    &#34;&#34;&#34;
    function to return escaped html string
    &#34;&#34;&#34;
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
        c = s.get_cookie_string(&#34;http://&#34; + domain, user_agent=user_agent)
        return c[0]
    except:
        return {}</code></pre>
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
    &#34;&#34;&#34;
    function to return unescaped html string
    &#34;&#34;&#34;
    return HTMLParser.HTMLParser().unescape(s).encode(&#34;utf-8&#34;)</code></pre>
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
<pre><code class="python">def webcams(count=10, by={&#34;country&#34;: &#34;us&#34;}, timeout=10):
    a = 0
    f = {}
    x = 1
    if by:
        key = list(by.keys())[0]
        if key not in [&#34;country&#34;, &#34;tag&#34;, &#34;city&#34;, &#34;timezone&#34;, &#34;type&#34;]:
            raise Exception(
                &#34;Your search must be in one of these categories: country, city, timezone, type, tag&#34;
            )
        value = by[key].lower()
        if &#34;country&#34; in by:
            if by[&#34;country&#34;].lower() not in [
                &#34;af&#34;,
                &#34;ax&#34;,
                &#34;al&#34;,
                &#34;dz&#34;,
                &#34;as&#34;,
                &#34;ad&#34;,
                &#34;ao&#34;,
                &#34;ai&#34;,
                &#34;aq&#34;,
                &#34;ag&#34;,
                &#34;ar&#34;,
                &#34;am&#34;,
                &#34;aw&#34;,
                &#34;au&#34;,
                &#34;at&#34;,
                &#34;az&#34;,
                &#34;bs&#34;,
                &#34;bh&#34;,
                &#34;bd&#34;,
                &#34;bb&#34;,
                &#34;by&#34;,
                &#34;be&#34;,
                &#34;bz&#34;,
                &#34;bj&#34;,
                &#34;bm&#34;,
                &#34;bt&#34;,
                &#34;bo&#34;,
                &#34;bq&#34;,
                &#34;ba&#34;,
                &#34;bw&#34;,
                &#34;br&#34;,
                &#34;io&#34;,
                &#34;bn&#34;,
                &#34;bg&#34;,
                &#34;bf&#34;,
                &#34;bi&#34;,
                &#34;cv&#34;,
                &#34;kh&#34;,
                &#34;cm&#34;,
                &#34;ca&#34;,
                &#34;ky&#34;,
                &#34;cf&#34;,
                &#34;td&#34;,
                &#34;cl&#34;,
                &#34;cn&#34;,
                &#34;cx&#34;,
                &#34;cc&#34;,
                &#34;co&#34;,
                &#34;km&#34;,
                &#34;cd&#34;,
                &#34;cg&#34;,
                &#34;ck&#34;,
                &#34;cr&#34;,
                &#34;ci&#34;,
                &#34;hr&#34;,
                &#34;cu&#34;,
                &#34;cw&#34;,
                &#34;cy&#34;,
                &#34;cz&#34;,
                &#34;dk&#34;,
                &#34;dj&#34;,
                &#34;dm&#34;,
                &#34;do&#34;,
                &#34;ec&#34;,
                &#34;eg&#34;,
                &#34;sv&#34;,
                &#34;gq&#34;,
                &#34;er&#34;,
                &#34;ee&#34;,
                &#34;sz&#34;,
                &#34;et&#34;,
                &#34;fk&#34;,
                &#34;fo&#34;,
                &#34;fj&#34;,
                &#34;fi&#34;,
                &#34;fr&#34;,
                &#34;gf&#34;,
                &#34;pf&#34;,
                &#34;tf&#34;,
                &#34;ga&#34;,
                &#34;gm&#34;,
                &#34;ge&#34;,
                &#34;de&#34;,
                &#34;gh&#34;,
                &#34;gi&#34;,
                &#34;gr&#34;,
                &#34;gl&#34;,
                &#34;gd&#34;,
                &#34;gp&#34;,
                &#34;gu&#34;,
                &#34;gt&#34;,
                &#34;gg&#34;,
                &#34;gn&#34;,
                &#34;gw&#34;,
                &#34;gy&#34;,
                &#34;ht&#34;,
                &#34;hm&#34;,
                &#34;va&#34;,
                &#34;hn&#34;,
                &#34;hk&#34;,
                &#34;hu&#34;,
                &#34;is&#34;,
                &#34;in&#34;,
                &#34;id&#34;,
                &#34;ir&#34;,
                &#34;iq&#34;,
                &#34;ie&#34;,
                &#34;im&#34;,
                &#34;il&#34;,
                &#34;it&#34;,
                &#34;jm&#34;,
                &#34;jp&#34;,
                &#34;je&#34;,
                &#34;jo&#34;,
                &#34;kz&#34;,
                &#34;ke&#34;,
                &#34;ki&#34;,
                &#34;kp&#34;,
                &#34;kr&#34;,
                &#34;kw&#34;,
                &#34;kg&#34;,
                &#34;la&#34;,
                &#34;lv&#34;,
                &#34;lb&#34;,
                &#34;ls&#34;,
                &#34;lr&#34;,
                &#34;ly&#34;,
                &#34;li&#34;,
                &#34;lt&#34;,
                &#34;lu&#34;,
                &#34;mo&#34;,
                &#34;mk&#34;,
                &#34;mg&#34;,
                &#34;mw&#34;,
                &#34;my&#34;,
                &#34;mv&#34;,
                &#34;ml&#34;,
                &#34;mt&#34;,
                &#34;mh&#34;,
                &#34;mq&#34;,
                &#34;mr&#34;,
                &#34;mu&#34;,
                &#34;yt&#34;,
                &#34;mx&#34;,
                &#34;fm&#34;,
                &#34;md&#34;,
                &#34;mc&#34;,
                &#34;mn&#34;,
                &#34;me&#34;,
                &#34;ms&#34;,
                &#34;ma&#34;,
                &#34;mz&#34;,
                &#34;mm&#34;,
                &#34;na&#34;,
                &#34;nr&#34;,
                &#34;np&#34;,
                &#34;nl&#34;,
                &#34;nc&#34;,
                &#34;nz&#34;,
                &#34;ni&#34;,
                &#34;ne&#34;,
                &#34;ng&#34;,
                &#34;nu&#34;,
                &#34;nf&#34;,
                &#34;mp&#34;,
                &#34;no&#34;,
                &#34;om&#34;,
                &#34;pk&#34;,
                &#34;pw&#34;,
                &#34;ps&#34;,
                &#34;pa&#34;,
                &#34;pg&#34;,
                &#34;py&#34;,
                &#34;pe&#34;,
                &#34;ph&#34;,
                &#34;pn&#34;,
                &#34;pl&#34;,
                &#34;pt&#34;,
                &#34;pr&#34;,
                &#34;qa&#34;,
                &#34;re&#34;,
                &#34;ro&#34;,
                &#34;ru&#34;,
                &#34;rw&#34;,
                &#34;bl&#34;,
                &#34;sh&#34;,
                &#34;kn&#34;,
                &#34;lc&#34;,
                &#34;mf&#34;,
                &#34;pm&#34;,
                &#34;vc&#34;,
                &#34;ws&#34;,
                &#34;sm&#34;,
                &#34;st&#34;,
                &#34;sa&#34;,
                &#34;sn&#34;,
                &#34;rs&#34;,
                &#34;sc&#34;,
                &#34;sl&#34;,
                &#34;sg&#34;,
                &#34;sx&#34;,
                &#34;sk&#34;,
                &#34;si&#34;,
                &#34;sb&#34;,
                &#34;so&#34;,
                &#34;za&#34;,
                &#34;gs&#34;,
                &#34;ss&#34;,
                &#34;es&#34;,
                &#34;lk&#34;,
                &#34;sd&#34;,
                &#34;sr&#34;,
                &#34;se&#34;,
                &#34;ch&#34;,
                &#34;sy&#34;,
                &#34;tw&#34;,
                &#34;tj&#34;,
                &#34;tz&#34;,
                &#34;th&#34;,
                &#34;tl&#34;,
                &#34;tg&#34;,
                &#34;tk&#34;,
                &#34;to&#34;,
                &#34;tt&#34;,
                &#34;tn&#34;,
                &#34;tr&#34;,
                &#34;tm&#34;,
                &#34;tc&#34;,
                &#34;tv&#34;,
                &#34;ug&#34;,
                &#34;ua&#34;,
                &#34;ae&#34;,
                &#34;gb&#34;,
                &#34;us&#34;,
                &#34;uy&#34;,
                &#34;uz&#34;,
                &#34;vu&#34;,
                &#34;ve&#34;,
                &#34;vn&#34;,
                &#34;vg&#34;,
                &#34;vi&#34;,
                &#34;wf&#34;,
                &#34;ye&#34;,
                &#34;zm&#34;,
                &#34;zw&#34;,
            ]:
                raise Exception(&#34;Unexisting Country code&#34;)
        url = &#34;https://www.insecam.org/en/by{}/{}/?page=&#34;.format(key, value)
    else:
        url = &#34;https://www.insecam.org/en/byrating/?page=&#34;
    while True:
        try:
            soup = BeautifulSoup(
                requests.Session().get(
                    url + str(x),
                    headers={&#34;User-Agent&#34;: random.choice(ua)},
                    timeout=timeout,
                ).text,
                &#34;html.parser&#34;,
            )
            fi = soup.findAll(&#34;img&#34;, {&#34;class&#34;: &#34;thumbnail-item__img img-responsive&#34;})
            for i in fi:
                j = HTMLParser.HTMLParser().unescape(i[&#34;src&#34;])
                o = HTMLParser.HTMLParser().unescape(i[&#34;title&#34;])
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
    &#34;&#34;&#34;
    this function is for searching on youtub and returning a links of related videos.&#34;&#34;&#34;
    q = q.replace(&#34; &#34;, &#34;+&#34;)
    u = &#34;https://www.youtube.com/results&#34;
    params = {&#34;search_query&#34;: q}
    l = []
    try:
        r = requests.Session().get(
            u,
            params,
            headers={&#34;User-Agent&#34;: random.choice(ua)},
            proxies=proxy,
            timeout=timeout,
        ).text
        soup = BeautifulSoup(r, &#34;html.parser&#34;)
        yt = soup.find_all(attrs={&#34;class&#34;: &#34;yt-uix-tile-link&#34;})
        for vi in yt:
            try:
                vi = &#34;https://www.youtube.com&#34; + str(vi[&#34;href&#34;])
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
<li><code><a title="bane.utils" href="index.html">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.utils.extrafun.escape_html" href="#bane.utils.extrafun.escape_html">escape_html</a></code></li>
<li><code><a title="bane.utils.extrafun.get_cf_cookie" href="#bane.utils.extrafun.get_cf_cookie">get_cf_cookie</a></code></li>
<li><code><a title="bane.utils.extrafun.unescape_html" href="#bane.utils.extrafun.unescape_html">unescape_html</a></code></li>
<li><code><a title="bane.utils.extrafun.webcams" href="#bane.utils.extrafun.webcams">webcams</a></code></li>
<li><code><a title="bane.utils.extrafun.youtube_search" href="#bane.utils.extrafun.youtube_search">youtube_search</a></code></li>
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