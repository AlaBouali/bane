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
<li><code><a title="bane.utils" href="index.md">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.utils.extrafun.escape_html" href="#bane.utils.extrafun.escape.md">escape_html</a></code></li>
<li><code><a title="bane.utils.extrafun.get_cf_cookie" href="#bane.utils.extrafun.get_cf_cookie">get_cf_cookie</a></code></li>
<li><code><a title="bane.utils.extrafun.set_general_dns_resolver" href="#bane.utils.extrafun.set_general_dns_resolver">set_general_dns_resolver</a></code></li>
<li><code><a title="bane.utils.extrafun.unescape_html" href="#bane.utils.extrafun.unescape.md">unescape_html</a></code></li>
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