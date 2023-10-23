<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.vulner_search</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *

def vulners_search(
    software,
    url=&#34;https://vulners.com/api/v3/burp/software/&#34;,
    file_name=&#34;&#34;,
    save_to_file=False,
    max_vulnerabilities=100,
    version=&#34;&#34;,
    software_type=&#34;software&#34;,
    user_agent=None,
    cookie=None,
    api_key=&#39;&#39;,
    proxy=None,
    timeout=20,
):
    if api_key==None:
        api_key=&#39;&#39;
    if not file_name:
        if version:
            file_name = software + &#34;_&#34; + version.replace(&#34;.&#34;, &#34;-&#34;)
        else:
            file_name = software
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    try:
        ver = &#34;&#34;
        if version:
            ver = version
        max_vuln = 100
        if max_vulnerabilities:
            max_vuln = max_vulnerabilities
        ty = &#34;software&#34;
        if software_type:
            ty = software_type
        if ty not in [&#34;software&#34;, &#34;cpe&#34;]:
            raise Exception(&#39;type must be: &#34;software&#34; or &#34;cpe&#34;&#39;)
        d = {
            &#34;maxVulnerabilities&#34;: max_vuln,
            &#34;version&#34;: ver,
            &#34;type&#34;: ty,
            &#34;software&#34;: software,
            &#39;apikey&#39;:api_key
        }
        r = requests.Session().get(
            url,
            params=d,
            headers=hea,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        c = json.loads(r.text)
        if c[&#34;result&#34;] == &#34;OK&#34;:
            if save_to_file==True:
                with open(file_name.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                    json.dump(c, outfile, indent=4)
                outfile.close()
            l = []
            m = c[&#34;data&#34;][&#34;search&#34;]
            i = 0
            for x in m:
                #print(x)
                l.append(
                     x[
                            &#34;_source&#34;
                        ]
                )
                i += 1
            return l
        else:
            return {&#39;error&#39;:&#34;couldn&#39;t find vulnerabilities for this version&#34;}
    except:
        pass
    return []</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.vulner_search.vulners_search"><code class="name flex">
<span>def <span class="ident">vulners_search</span></span>(<span>software, url='https://vulners.com/api/v3/burp/software/', file_name='', save_to_file=False, max_vulnerabilities=100, version='', software_type='software', user_agent=None, cookie=None, api_key='', proxy=None, timeout=20)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def vulners_search(
    software,
    url=&#34;https://vulners.com/api/v3/burp/software/&#34;,
    file_name=&#34;&#34;,
    save_to_file=False,
    max_vulnerabilities=100,
    version=&#34;&#34;,
    software_type=&#34;software&#34;,
    user_agent=None,
    cookie=None,
    api_key=&#39;&#39;,
    proxy=None,
    timeout=20,
):
    if api_key==None:
        api_key=&#39;&#39;
    if not file_name:
        if version:
            file_name = software + &#34;_&#34; + version.replace(&#34;.&#34;, &#34;-&#34;)
        else:
            file_name = software
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    try:
        ver = &#34;&#34;
        if version:
            ver = version
        max_vuln = 100
        if max_vulnerabilities:
            max_vuln = max_vulnerabilities
        ty = &#34;software&#34;
        if software_type:
            ty = software_type
        if ty not in [&#34;software&#34;, &#34;cpe&#34;]:
            raise Exception(&#39;type must be: &#34;software&#34; or &#34;cpe&#34;&#39;)
        d = {
            &#34;maxVulnerabilities&#34;: max_vuln,
            &#34;version&#34;: ver,
            &#34;type&#34;: ty,
            &#34;software&#34;: software,
            &#39;apikey&#39;:api_key
        }
        r = requests.Session().get(
            url,
            params=d,
            headers=hea,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        c = json.loads(r.text)
        if c[&#34;result&#34;] == &#34;OK&#34;:
            if save_to_file==True:
                with open(file_name.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                    json.dump(c, outfile, indent=4)
                outfile.close()
            l = []
            m = c[&#34;data&#34;][&#34;search&#34;]
            i = 0
            for x in m:
                #print(x)
                l.append(
                     x[
                            &#34;_source&#34;
                        ]
                )
                i += 1
            return l
        else:
            return {&#39;error&#39;:&#34;couldn&#39;t find vulnerabilities for this version&#34;}
    except:
        pass
    return []</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.vulner_search.vulners_search" href="#bane.scanners.vulnerabilities.vulner_search.vulners_search">vulners_search</a></code></li>
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