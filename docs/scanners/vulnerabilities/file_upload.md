<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.file_upload</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *


def file_upload_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    dont_change=[],
    referer=None,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    l = []
    result=[]
    x = forms_parser(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie
    )
    fos = get_upload_form(x)
    for fo in fos:
        d, f = setup_to_submit(
            form_filler(
                fo,
                &#34;&#34;,
                &#34;&#34;,
                mime_type=mime_type,
                file_extension=file_extension,
                predefined_inputs=predefined_inputs,
                leave_empty=leave_empty,
                dont_change=dont_change,
                dont_send=dont_send
            )
        )
        for x in d:
            for y in replaceble_parameters:
                if x == y:
                    for z in replaceble_parameters[y]:
                        d[x] = d[x].replace(z[0], z[1])
        if not referer or len(referer) == 0:
            referer = u
        for j in f:
            l.append(f[j][0])
        if user_agent:
            h = {&#34;User-Agent&#34;: user_agent}
        else:
            h = {&#34;User-Agent&#34;: random.choice(ua)}
        if &#34;application/json&#34; in fo[&#34;enctype&#34;]:
            d = json.dumps(d)
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
        try:
            r = requests.Session().post(
                fo[&#34;action&#34;], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
            if (
                r.status_code == 200
                and not any(i in r.text for i in l)
                and any(
                    i in r.text.lower() for i in [&#34;only accept&#34;, &#34;invalid&#34;,&#34;not valid&#34;,&#34;not a valid&#34;, &#34;unacceptable&#34;,&#34;not allowed&#34;,&#34;not accepted&#34;,&#34;not acceptable&#34;]
                )
            ):
                pass#result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;: False, &#39;status&#39;:&#34;Unacceptable file extension&#34;})
            elif all(i in r.text for i in l):
                result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;:True, &#39;status&#39;:&#34;Found all data&#34;})
            elif r.status_code == 200 and any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                    )
                result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;:True, &#39;status&#39;:&#34;HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                    })
            elif r.status_code == 200 and not any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                    )
                result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;: True, &#39;status&#39;:&#34;HTTP Status Code: 200 , but we didn&#39;t find our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;})
        except Exception as ex:
            #raise(ex)
            pass#result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;: False, &#39;status&#39;:&#34;Found no data and Status Code NOT: 200&#34;})
    return result



def file_upload(
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
    referer=None,
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
        result=file_upload_forms(x,
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
        #result={&#39;vulnerable&#39;:result[0],&#39;status&#39;:result[1]}
        if logs==True:
            for r in result:
                print(r)
        if result!=[]:
            l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  l#[x for x in l if x[&#39;result&#39;][&#39;vulnerable&#39;]!=False]</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.file_upload.file_upload"><code class="name flex">
<span>def <span class="ident">file_upload</span></span>(<span>u, max_pages=5, logs=True, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', fill_empty=10, referer=None, leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, pages=[], headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def file_upload(
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
    referer=None,
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
        result=file_upload_forms(x,
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
        #result={&#39;vulnerable&#39;:result[0],&#39;status&#39;:result[1]}
        if logs==True:
            for r in result:
                print(r)
        if result!=[]:
            l.append({&#39;page&#39;:x,&#39;result&#39;:result})
    return  l#[x for x in l if x[&#39;result&#39;][&#39;vulnerable&#39;]!=False]</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.file_upload.file_upload_forms"><code class="name flex">
<span>def <span class="ident">file_upload_forms</span></span>(<span>u, proxy=None, timeout=10, show_warnings=True, user_agent=None, cookie=None, replaceble_parameters={'phpvalue': (('.', ''),)}, file_extension='png', fill_empty=10, dont_change=[], referer=None, leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def file_upload_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    file_extension=&#34;png&#34;,
    fill_empty=10,
    dont_change=[],
    referer=None,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    l = []
    result=[]
    x = forms_parser(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie
    )
    fos = get_upload_form(x)
    for fo in fos:
        d, f = setup_to_submit(
            form_filler(
                fo,
                &#34;&#34;,
                &#34;&#34;,
                mime_type=mime_type,
                file_extension=file_extension,
                predefined_inputs=predefined_inputs,
                leave_empty=leave_empty,
                dont_change=dont_change,
                dont_send=dont_send
            )
        )
        for x in d:
            for y in replaceble_parameters:
                if x == y:
                    for z in replaceble_parameters[y]:
                        d[x] = d[x].replace(z[0], z[1])
        if not referer or len(referer) == 0:
            referer = u
        for j in f:
            l.append(f[j][0])
        if user_agent:
            h = {&#34;User-Agent&#34;: user_agent}
        else:
            h = {&#34;User-Agent&#34;: random.choice(ua)}
        if &#34;application/json&#34; in fo[&#34;enctype&#34;]:
            d = json.dumps(d)
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
        try:
            r = requests.Session().post(
                fo[&#34;action&#34;], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
            if (
                r.status_code == 200
                and not any(i in r.text for i in l)
                and any(
                    i in r.text.lower() for i in [&#34;only accept&#34;, &#34;invalid&#34;,&#34;not valid&#34;,&#34;not a valid&#34;, &#34;unacceptable&#34;,&#34;not allowed&#34;,&#34;not accepted&#34;,&#34;not acceptable&#34;]
                )
            ):
                pass#result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;: False, &#39;status&#39;:&#34;Unacceptable file extension&#34;})
            elif all(i in r.text for i in l):
                result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;:True, &#39;status&#39;:&#34;Found all data&#34;})
            elif r.status_code == 200 and any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                    )
                result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;:True, &#39;status&#39;:&#34;HTTP Status Code: 200 , but we didn&#39;t find some of our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                    })
            elif r.status_code == 200 and not any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        &#34;Warning: HTTP Status Code: 200 , but we didn&#39;t find our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;
                    )
                result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;: True, &#39;status&#39;:&#34;HTTP Status Code: 200 , but we didn&#39;t find our submitted data, so it&#39;s probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again&#34;})
        except Exception as ex:
            #raise(ex)
            pass#result.append({&#34;form&#34;:fo,&#34;vulnerable&#34;: False, &#39;status&#39;:&#34;Found no data and Status Code NOT: 200&#34;})
    return result</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.file_upload.file_upload" href="#bane.scanners.vulnerabilities.file_upload.file_upload">file_upload</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.file_upload.file_upload_forms" href="#bane.scanners.vulnerabilities.file_upload.file_upload_forms">file_upload_forms</a></code></li>
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