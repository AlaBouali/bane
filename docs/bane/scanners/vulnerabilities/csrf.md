<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.csrf</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None,headers={}):
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    res = {&#34;Vulnerable&#34;: [], &#34;Safe&#34;: []}
    f = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    f1 = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    coun = -1
    for x in f:
        coun += 1
        vuln = True
        hd_v = False
        # print(Fore.BLUE+&#34;Form: &#34;+Fore.WHITE+str(f.index(x))+Fore.BLUE+&#34;\nAction: &#34;+Fore.WHITE+x[&#39;action&#39;]+Fore.BLUE+&#34;\nMethod: &#34;+Fore.WHITE+x[&#39;method&#39;]+Style.RESET_ALL)
        for y in x[&#34;inputs&#34;]:
            # print(&#34;Name: {} | Type: {} | Value: {}&#34;.format(y[&#34;name&#34;],y[&#34;type&#34;],y[&#34;value&#34;]))
            if y[&#34;type&#34;].lower() == &#34;hidden&#34;:
                hd_v = True
            if y[&#34;type&#34;].lower() == &#34;hidden&#34; and any(
                ele in y[&#34;name&#34;].lower() for ele in csrf_strings
            ):  # and y[&#34;value&#34;]==f1f[&#34;inputs&#34;][con][&#34;value&#34;]:
                vuln = False
        if vuln == True:
            if (
                hd_v == True
            ):  # if there is no Anti-CSRF Tokens then we check if the Hidden fields can be predicted or not (keep their values or change them by request)
                # print(Fore.YELLOW+&#34;[i] Validating hidden values&#39; prediction...&#34;+Style.RESET_ALL)
                for i in x[&#34;hidden_values&#34;]:
                    if len(x[&#34;hidden_values&#34;][i]) &gt; 0:
                        if x[&#34;hidden_values&#34;][i] != f1[coun][&#34;hidden_values&#34;][i]:
                            vuln = False
        if vuln == True:
            colr = Fore.GREEN
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[+] Vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Vulnerable&#34;].append(x)
        else:
            colr = Fore.RED
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[-] Not vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Safe&#34;].append(x)
    return res


def csrf_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    vu = []
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    v = csrf_filter_tokens(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie, headers=headers
    )[&#34;Vulnerable&#34;]
    if user_agent:
        h = {&#34;User-Agent&#34;: user_agent}
    else:
        h = {&#34;User-Agent&#34;: random.choice(ua)}
    h.update({&#34;cookie&#34;: cookie})
    h.update(
        {
            &#34;Referer&#34;: referer,
            &#34;Origin&#34;: referer.split(&#34;://&#34;)[0]
            + &#34;://&#34;
            + referer.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    h.update(headers)
    for x in v:
        x = form_filler(
            x,
            &#34;&#34;,
            &#34;&#34;,
            file_extension=file_extension,
            auto_fill=fill_empty,
            leave_empty=leave_empty,
            dont_send=dont_send,
            mime_type=mime_type,
            predefined_inputs=predefined_inputs,
        )
        d, f = setup_to_submit(x)
        for g in d:
            for y in replaceble_parameters:
                if x == y:
                    for z in replaceble_parameters[y]:
                        d[g] = d[g].replace(z[0], z[1])
        l = [d[y] for y in d]
        for j in f:
            l.append(f[j][0])
        if x[&#34;method&#34;] == &#34;get&#34;:
            r = requests.Session().get(
                x[&#34;action&#34;], params=d, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        else:
            if &#34;application/json&#34; in x[&#34;enctype&#34;]:
                d = json.dumps(d)
            r = requests.Session().post(
                x[&#34;action&#34;], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        if all(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found all data&#34;})
        elif r.status_code == 200 and any(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found some data&#34;})
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
        elif (
            r.status_code == 200
            and not any(i in r.text for i in l)
            and any(
                i in r.text.lower() for i in [&#34;unauthorized&#34;, &#34;invalid&#34;, &#34;unacceptable&#34;]
            )
        ):
            return False
        elif r.status_code == 200 and not any(i in r.text for i in l):
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find any of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found no data but Status Code: 200&#34;})
    return vu


def csrf(
    u,
    max_pages=5,
    logs=True,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=csrf_forms(x,
                        proxy=proxy,
                        timeout=timeout,
                        show_warnings=show_warnings,
                        user_agent=user_agent,
                        cookie=cookie,
                        replaceble_parameters=replaceble_parameters,
                        file_extension=file_extension,
                        fill_empty=fill_empty,
                        referer=referer,
                        leave_empty=leave_empty,
                        dont_send=dont_send,
                        mime_type=mime_type,
                        predefined_inputs=predefined_inputs,
                        headers=headers)
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.csrf.csrf"><code class="name flex">
<span>def <span class="ident">csrf</span></span>(<span>u, max_pages=5, logs=True, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', fill_empty=10, referer='http://www.evil.com', leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, pages=[], headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def csrf(
    u,
    max_pages=5,
    logs=True,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    pages=[],
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print(&#39;\n\nPage: {}\n&#39;.format(x))
        result=csrf_forms(x,
                        proxy=proxy,
                        timeout=timeout,
                        show_warnings=show_warnings,
                        user_agent=user_agent,
                        cookie=cookie,
                        replaceble_parameters=replaceble_parameters,
                        file_extension=file_extension,
                        fill_empty=fill_empty,
                        referer=referer,
                        leave_empty=leave_empty,
                        dont_send=dont_send,
                        mime_type=mime_type,
                        predefined_inputs=predefined_inputs,
                        headers=headers)
        if logs==True:
            for r in result:
                print(r)
        l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  [x for x in l if x[&#39;result&#39;]!=[]]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.csrf.csrf_filter_tokens"><code class="name flex">
<span>def <span class="ident">csrf_filter_tokens</span></span>(<span>u, proxy=None, timeout=10, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None,headers={}):
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    res = {&#34;Vulnerable&#34;: [], &#34;Safe&#34;: []}
    f = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    f1 = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy, headers=headers
    )
    coun = -1
    for x in f:
        coun += 1
        vuln = True
        hd_v = False
        # print(Fore.BLUE+&#34;Form: &#34;+Fore.WHITE+str(f.index(x))+Fore.BLUE+&#34;\nAction: &#34;+Fore.WHITE+x[&#39;action&#39;]+Fore.BLUE+&#34;\nMethod: &#34;+Fore.WHITE+x[&#39;method&#39;]+Style.RESET_ALL)
        for y in x[&#34;inputs&#34;]:
            # print(&#34;Name: {} | Type: {} | Value: {}&#34;.format(y[&#34;name&#34;],y[&#34;type&#34;],y[&#34;value&#34;]))
            if y[&#34;type&#34;].lower() == &#34;hidden&#34;:
                hd_v = True
            if y[&#34;type&#34;].lower() == &#34;hidden&#34; and any(
                ele in y[&#34;name&#34;].lower() for ele in csrf_strings
            ):  # and y[&#34;value&#34;]==f1f[&#34;inputs&#34;][con][&#34;value&#34;]:
                vuln = False
        if vuln == True:
            if (
                hd_v == True
            ):  # if there is no Anti-CSRF Tokens then we check if the Hidden fields can be predicted or not (keep their values or change them by request)
                # print(Fore.YELLOW+&#34;[i] Validating hidden values&#39; prediction...&#34;+Style.RESET_ALL)
                for i in x[&#34;hidden_values&#34;]:
                    if len(x[&#34;hidden_values&#34;][i]) &gt; 0:
                        if x[&#34;hidden_values&#34;][i] != f1[coun][&#34;hidden_values&#34;][i]:
                            vuln = False
        if vuln == True:
            colr = Fore.GREEN
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[+] Vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Vulnerable&#34;].append(x)
        else:
            colr = Fore.RED
            &#34;&#34;&#34;if logs==True:
    print (colr+&#34;[-] Not vulnerable&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            res[&#34;Safe&#34;].append(x)
    return res</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.csrf.csrf_forms"><code class="name flex">
<span>def <span class="ident">csrf_forms</span></span>(<span>u, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', fill_empty=10, referer='http://www.evil.com', leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def csrf_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    referer=&#34;http://www.evil.com&#34;,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    vu = []
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            &#34;This attack requires authentication !! You need to set a Cookie&#34;
        )
    v = csrf_filter_tokens(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie, headers=headers
    )[&#34;Vulnerable&#34;]
    if user_agent:
        h = {&#34;User-Agent&#34;: user_agent}
    else:
        h = {&#34;User-Agent&#34;: random.choice(ua)}
    h.update({&#34;cookie&#34;: cookie})
    h.update(
        {
            &#34;Referer&#34;: referer,
            &#34;Origin&#34;: referer.split(&#34;://&#34;)[0]
            + &#34;://&#34;
            + referer.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
        }
    )
    h.update(headers)
    for x in v:
        x = form_filler(
            x,
            &#34;&#34;,
            &#34;&#34;,
            file_extension=file_extension,
            auto_fill=fill_empty,
            leave_empty=leave_empty,
            dont_send=dont_send,
            mime_type=mime_type,
            predefined_inputs=predefined_inputs,
        )
        d, f = setup_to_submit(x)
        for g in d:
            for y in replaceble_parameters:
                if x == y:
                    for z in replaceble_parameters[y]:
                        d[g] = d[g].replace(z[0], z[1])
        l = [d[y] for y in d]
        for j in f:
            l.append(f[j][0])
        if x[&#34;method&#34;] == &#34;get&#34;:
            r = requests.Session().get(
                x[&#34;action&#34;], params=d, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        else:
            if &#34;application/json&#34; in x[&#34;enctype&#34;]:
                d = json.dumps(d)
            r = requests.Session().post(
                x[&#34;action&#34;], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        if all(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found all data&#34;})
        elif r.status_code == 200 and any(i in r.text for i in l):
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found some data&#34;})
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
        elif (
            r.status_code == 200
            and not any(i in r.text for i in l)
            and any(
                i in r.text.lower() for i in [&#34;unauthorized&#34;, &#34;invalid&#34;, &#34;unacceptable&#34;]
            )
        ):
            return False
        elif r.status_code == 200 and not any(i in r.text for i in l):
            if show_warnings == True:
                print(
                    &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find any of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                )
            vu.append({&#39;form&#39;:x, &#39;status&#39;:&#34;Found no data but Status Code: 200&#34;})
    return vu</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.csrf.csrf" href="#bane.scanners.vulnerabilities.csrf.csrf">csrf</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.csrf.csrf_filter_tokens" href="#bane.scanners.vulnerabilities.csrf.csrf_filter_tokens">csrf_filter_tokens</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.csrf.csrf_forms" href="#bane.scanners.vulnerabilities.csrf.csrf_forms">csrf_forms</a></code></li>
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