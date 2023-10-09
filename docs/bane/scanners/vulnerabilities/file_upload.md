<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.scanners.vulnerabilities.file_upload API documentation</title>
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
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
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
                "",
                "",
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
            h = {"User-Agent": user_agent}
        else:
            h = {"User-Agent": random.choice(ua)}
        if "application/json" in fo["enctype"]:
            d = json.dumps(d)
        h.update({"cookie": cookie})
        h.update(
            {
                "Referer": referer,
                "Origin": referer.split("://")[0]
                + "://"
                + referer.split("://")[1].split("/")[0],
            }
        )
        h.update(headers)
        try:
            r = requests.Session().post(
                fo["action"], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
            if (
                r.status_code == 200
                and not any(i in r.text for i in l)
                and any(
                    i in r.text.lower() for i in ["only accept", "invalid","not valid","not a valid", "unacceptable","not allowed","not accepted","not acceptable"]
                )
            ):
                pass#result.append({"form":fo,"vulnerable": False, 'status':"Unacceptable file extension"})
            elif all(i in r.text for i in l):
                result.append({"form":fo,"vulnerable":True, 'status':"Found all data"})
            elif r.status_code == 200 and any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        "Warning: HTTP Status Code: 200 , but we didn't find some of our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                    )
                result.append({"form":fo,"vulnerable":True, 'status':"HTTP Status Code: 200 , but we didn't find some of our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                    })
            elif r.status_code == 200 and not any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        "Warning: HTTP Status Code: 200 , but we didn't find our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                    )
                result.append({"form":fo,"vulnerable": True, 'status':"HTTP Status Code: 200 , but we didn't find our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"})
        except Exception as ex:
            #raise(ex)
            pass#result.append({"form":fo,"vulnerable": False, 'status':"Found no data and Status Code NOT: 200"})
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
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
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
            print('\n\nPage: {}\n'.format(x))
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
        #result={'vulnerable':result[0],'status':result[1]}
        if logs==True:
            for r in result:
                print(r)
        if result!=[]:
            l.append({'page':x,'result':result})
    return  l#[x for x in l if x['result']['vulnerable']!=False]</code></pre>
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
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
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
            print('\n\nPage: {}\n'.format(x))
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
        #result={'vulnerable':result[0],'status':result[1]}
        if logs==True:
            for r in result:
                print(r)
        if result!=[]:
            l.append({'page':x,'result':result})
    return  l#[x for x in l if x['result']['vulnerable']!=False]</code></pre>
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
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
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
                "",
                "",
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
            h = {"User-Agent": user_agent}
        else:
            h = {"User-Agent": random.choice(ua)}
        if "application/json" in fo["enctype"]:
            d = json.dumps(d)
        h.update({"cookie": cookie})
        h.update(
            {
                "Referer": referer,
                "Origin": referer.split("://")[0]
                + "://"
                + referer.split("://")[1].split("/")[0],
            }
        )
        h.update(headers)
        try:
            r = requests.Session().post(
                fo["action"], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
            if (
                r.status_code == 200
                and not any(i in r.text for i in l)
                and any(
                    i in r.text.lower() for i in ["only accept", "invalid","not valid","not a valid", "unacceptable","not allowed","not accepted","not acceptable"]
                )
            ):
                pass#result.append({"form":fo,"vulnerable": False, 'status':"Unacceptable file extension"})
            elif all(i in r.text for i in l):
                result.append({"form":fo,"vulnerable":True, 'status':"Found all data"})
            elif r.status_code == 200 and any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        "Warning: HTTP Status Code: 200 , but we didn't find some of our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                    )
                result.append({"form":fo,"vulnerable":True, 'status':"HTTP Status Code: 200 , but we didn't find some of our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                    })
            elif r.status_code == 200 and not any(i in r.text for i in l):
                if show_warnings == True:
                    print(
                        "Warning: HTTP Status Code: 200 , but we didn't find our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                    )
                result.append({"form":fo,"vulnerable": True, 'status':"HTTP Status Code: 200 , but we didn't find our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"})
        except Exception as ex:
            #raise(ex)
            pass#result.append({"form":fo,"vulnerable": False, 'status':"Found no data and Status Code NOT: 200"})
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
<li><code><a href="index.md" title="bane.scanners.vulnerabilities">bane.scanners.vulnerabilities</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.scanners.vulnerabilities.file_upload.file_upload" title="bane.scanners.vulnerabilities.file_upload.file_upload">file_upload</a></code></li>
<li><code><a href="#bane.scanners.vulnerabilities.file_upload.file_upload_forms" title="bane.scanners.vulnerabilities.file_upload.file_upload_forms">file_upload_forms</a></code></li>
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