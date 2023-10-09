<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.scanners.vulnerabilities.ssti API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.vulnerabilities.ssti</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *

def ssti_submit(
    parsed,
    payload,
    replaceble_parameters,
    debug=False,
    enctype="application/x-www-form-urlencoded",
    eval_value=1111111101,
):
    """"""
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
    if debug == True:
        for x in d:
            print("{}{} : {}{}".format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print("{}{} : {}{}".format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if "application/json" in enctype:
        d = json.dumps(d)
    if not fi:
        parsed[1].update(
            {
                "Content-Type": enctype,
                "Referer": parsed[0]["action"],
                "Origin": parsed[0]["action"].split("://")[0]
                + "://"
                + parsed[0]["action"].split("://")[1].split("/")[0],
            }
        )
    else:
        parsed[1].update(
            {
                "Referer": parsed[0]["action"],
                "Origin": parsed[0]["action"].split("://")[0]
                + "://"
                + parsed[0]["action"].split("://")[1].split("/")[0],
            }
        )
    c=''
    if parsed[0]["method"] == "get":
        try:
            c = requests.Session().get(
                parsed[0]["action"],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if "{}".format(eval_value) in c:
                return (True, {"p_o_c":p_o_c,"payload":payload, "result":"{}".format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    else:
        try:
            c = requests.Session().post(
                parsed[0]["action"],
                data=d,
                files=fi,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if "{}".format(eval_value) in c:
                return (True, {"p_o_c":p_o_c,"payload":payload, "result":"{}".format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, "",any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)


def safe_eval(a, o, b):
    if a.strip().isnumeric() == False or b.strip().isnumeric() == False:
        raise Exception("For security reasons, ONLY NUMERIC VALUES ARE EVALUATED !!")
    if o.strip() not in ["+", "-", "*", "/"]:
        raise Exception(
            "For security reasons, ONLY OPERATORS ALLOWED ARE: + , - , * , /!!"
        )
    return eval(a + o + b)


def ssti_forms(
    u,
    payload_index=0,
    values=(9, 123456789),
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    dont_change={},
    number=(1, 9),
    payload_keyword="payload",
    operator="*",
    save_to_file=None,
    file_extension="png",
    replaceble_parameters={"phpvalue": ((".", ""),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=120,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    """
    this function is for SSTI test with both POST and GET requests . it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.
    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.ssti_forms('http://phptester.net/")
    """
    target_page = u
    xp = ssti_list[payload_index].replace(
        payload_keyword, "{}{}{}".format(values[0], operator, values[1])
    )
    xp_eval = safe_eval("{}".format(values[0]), operator, "{}".format(values[1]))
    target_page = u
    form_index = -1
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    if logs == True:
        print(Fore.WHITE + "[~]Getting forms..." + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + "[-]No forms were found!!!" + Style.RESET_ALL)
        hu = False
    if hu == True:
        for l1 in fom:
            form_index += 1
            lst = {}
            vul = []
            sec = []
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            hu = True
            u = l1["action"]
            if logs == True:
                print(
                    Fore.BLUE
                    + "Form: "
                    + Fore.WHITE
                    + str(form_index)
                    + Fore.BLUE
                    + "\nAction: "
                    + Fore.WHITE
                    + u
                    + Fore.BLUE
                    + "\nMethod: "
                    + Fore.WHITE
                    + l1["method"]
                    + Fore.BLUE
                    + "\nPayload: "
                    + Fore.WHITE
                    + xp
                    + Style.RESET_ALL
                )
                """if len(inputs(u,proxy=proxy,timeout=timeout,value=True,cookie=cookie,user_agent=user_agent))==0:
     if logs==True:
      print(Fore.YELLOW+"[-]No parameters found on that page !! Moving on.."+Style.RESET_ALL)"""
            if True:
                extr = []
                l = []
                for x in l1["inputs"]:
                    if (
                        x["name"].strip() not in leave_empty
                        and x["name"].strip() not in dont_send
                    ):
                        try:
                            if (
                                x["type"]
                                in [
                                    "hidden",
                                    "file",
                                    "text",
                                    "textarea",
                                    "email",
                                    "tel",
                                    "search",
                                    "url",
                                    "password",
                                    "number",
                                    "select",
                                    "radio",
                                    "checkbox",
                                    "color"
                                ]
                                and x["name"] not in dont_change
                            ):  # any input type that accept direct input from keyboard
                                i = x["name"]
                                parsed_form = set_up_injection(
                                    target_page,
                                    form_index,
                                    i,
                                    xp,
                                    cookie,
                                    setup_ua(user_agent),
                                    setup_proxy(proxy, proxies),
                                    timeout,
                                    fill_empty,
                                    file_extension=file_extension,
                                    number=number,
                                    email_extension=email_extension,
                                    phone_pattern=phone_pattern,
                                    leave_empty=leave_empty,
                                    dont_send=dont_send,
                                    mime_type=mime_type,
                                    predefined_inputs=predefined_inputs,
                                    dont_change=dont_change,
                                    headers=headers
                                )
                                _res = ssti_submit(
                                    parsed_form,
                                    xp,
                                    replaceble_parameters,
                                    debug=debug,
                                    enctype=l1["enctype"],
                                    eval_value=xp_eval,
                                )
                                if _res[0] == True:
                                    x = "parameter: '" + i + "' =&gt; [+] Vulnerable !!"
                                    vul.append({'parameter':i, 'context':_res[1]})
                                    colr = Fore.GREEN
                                else:
                                    x = "parameter: '" + i + "' =&gt; [-] Not Vulnerable"
                                    #sec.append(i)
                                    colr = Fore.RED
                                if _res[2] == True:
                                    x+=Fore.YELLOW+"\n[i] SQL Error detected"
                                    sql_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if _res[3]==True:
                                    x+=Fore.YELLOW+"\n[i] XML parsing Error detected"
                                    xml_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if _res[4] == True:
                                    x+=Fore.YELLOW+"\n[i] Fetching URL Error detected (potential SSRF)"
                                    ssrf_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if _res[5] == True:
                                    x+=Fore.YELLOW+"\n[i] Reading file Error detected (potential path traversal)"
                                    p_t_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if logs == True:
                                    print(colr + x + Style.RESET_ALL)
                        except Exception as ex:
                            break
            dic.append(
                {
                    "action": u,
                    "method": l1["method"],
                    "vulnerable": vul,
                    #"safe": sec,
                    "sql_errors":sql_e,
                    "xml_parsing_errors":xml_e,
                    "fetching_url_errors":ssrf_e,
                    "reading_file_errors":p_t_e
                }
            )
        final = {"payload": xp, "page": target_page, "result": dic}
        if save_to_file:
            with open(save_to_file.split(".")[0] + ".json", "w") as outfile:
                json.dump(final, outfile, indent=4)
            outfile.close()
        return final

def ssti(
    u,
    max_pages=5,
    pages=[],
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    payload_index=0,
    values=(9, 123456789),
    dont_change={},
    number=(1, 9),
    payload_keyword="payload",
    operator="*",
    save_to_file=None,
    file_extension="png",
    replaceble_parameters={"phpvalue": ((".", ""),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=120,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers=headers)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        l.append(ssti_forms(x,
                            payload_index=payload_index,
                            values=values,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            dont_change=dont_change,
                            number=number,
                            payload_keyword=payload_keyword,
                            operator=operator,
                            save_to_file=save_to_file,
                            file_extension=file_extension,
                            replaceble_parameters=replaceble_parameters,
                            logs=logs,
                            fill_empty=fill_empty,
                            leave_empty=leave_empty,
                            dont_send=dont_send,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type,
                            predefined_inputs=predefined_inputs,
                            headers=headers))
    f=[]
    for x in l:
        if x !=None:
            n=x.copy()
            n['result']=[]
            for i in x['result']:
                if len(i['vulnerable']) &gt; 0 or len(i['sql_errors']) &gt; 0 or len(i['xml_parsing_errors'])&gt;0 or len(i['fetching_url_errors'])&gt;0 or len(i['reading_file_errors']) &gt; 0:
                    n['result'].append(i)
            if n['result']!=[]:
                f.append(n)
    return f</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.vulnerabilities.ssti.safe_eval"><code class="name flex">
<span>def <span class="ident">safe_eval</span></span>(<span>a, o, b)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def safe_eval(a, o, b):
    if a.strip().isnumeric() == False or b.strip().isnumeric() == False:
        raise Exception("For security reasons, ONLY NUMERIC VALUES ARE EVALUATED !!")
    if o.strip() not in ["+", "-", "*", "/"]:
        raise Exception(
            "For security reasons, ONLY OPERATORS ALLOWED ARE: + , - , * , /!!"
        )
    return eval(a + o + b)</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.ssti.ssti"><code class="name flex">
<span>def <span class="ident">ssti</span></span>(<span>u, max_pages=5, pages=[], email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', payload_index=0, values=(9, 123456789), dont_change={}, number=(1, 9), payload_keyword='payload', operator='*', save_to_file=None, file_extension='png', replaceble_parameters={'phpvalue': (('.', ''),)}, logs=True, fill_empty=10, leave_empty=[], dont_send=['btnClear'], proxy=None, proxies=None, timeout=120, user_agent=None, cookie=None, debug=False, mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssti(
    u,
    max_pages=5,
    pages=[],
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    payload_index=0,
    values=(9, 123456789),
    dont_change={},
    number=(1, 9),
    payload_keyword="payload",
    operator="*",
    save_to_file=None,
    file_extension="png",
    replaceble_parameters={"phpvalue": ((".", ""),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=120,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy,headers=headers)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        l.append(ssti_forms(x,
                            payload_index=payload_index,
                            values=values,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            dont_change=dont_change,
                            number=number,
                            payload_keyword=payload_keyword,
                            operator=operator,
                            save_to_file=save_to_file,
                            file_extension=file_extension,
                            replaceble_parameters=replaceble_parameters,
                            logs=logs,
                            fill_empty=fill_empty,
                            leave_empty=leave_empty,
                            dont_send=dont_send,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type,
                            predefined_inputs=predefined_inputs,
                            headers=headers))
    f=[]
    for x in l:
        if x !=None:
            n=x.copy()
            n['result']=[]
            for i in x['result']:
                if len(i['vulnerable']) &gt; 0 or len(i['sql_errors']) &gt; 0 or len(i['xml_parsing_errors'])&gt;0 or len(i['fetching_url_errors'])&gt;0 or len(i['reading_file_errors']) &gt; 0:
                    n['result'].append(i)
            if n['result']!=[]:
                f.append(n)
    return f</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.ssti.ssti_forms"><code class="name flex">
<span>def <span class="ident">ssti_forms</span></span>(<span>u, payload_index=0, values=(9, 123456789), email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', dont_change={}, number=(1, 9), payload_keyword='payload', operator='*', save_to_file=None, file_extension='png', replaceble_parameters={'phpvalue': (('.', ''),)}, logs=True, fill_empty=10, leave_empty=[], dont_send=['btnClear'], proxy=None, proxies=None, timeout=120, user_agent=None, cookie=None, debug=False, mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for SSTI test with both POST and GET requests . it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.
usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
bane.ssti_forms('http://phptester.net/")</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssti_forms(
    u,
    payload_index=0,
    values=(9, 123456789),
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    dont_change={},
    number=(1, 9),
    payload_keyword="payload",
    operator="*",
    save_to_file=None,
    file_extension="png",
    replaceble_parameters={"phpvalue": ((".", ""),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=120,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    """
    this function is for SSTI test with both POST and GET requests . it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.
    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.ssti_forms('http://phptester.net/")
    """
    target_page = u
    xp = ssti_list[payload_index].replace(
        payload_keyword, "{}{}{}".format(values[0], operator, values[1])
    )
    xp_eval = safe_eval("{}".format(values[0]), operator, "{}".format(values[1]))
    target_page = u
    form_index = -1
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    if logs == True:
        print(Fore.WHITE + "[~]Getting forms..." + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + "[-]No forms were found!!!" + Style.RESET_ALL)
        hu = False
    if hu == True:
        for l1 in fom:
            form_index += 1
            lst = {}
            vul = []
            sec = []
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            hu = True
            u = l1["action"]
            if logs == True:
                print(
                    Fore.BLUE
                    + "Form: "
                    + Fore.WHITE
                    + str(form_index)
                    + Fore.BLUE
                    + "\nAction: "
                    + Fore.WHITE
                    + u
                    + Fore.BLUE
                    + "\nMethod: "
                    + Fore.WHITE
                    + l1["method"]
                    + Fore.BLUE
                    + "\nPayload: "
                    + Fore.WHITE
                    + xp
                    + Style.RESET_ALL
                )
                """if len(inputs(u,proxy=proxy,timeout=timeout,value=True,cookie=cookie,user_agent=user_agent))==0:
     if logs==True:
      print(Fore.YELLOW+"[-]No parameters found on that page !! Moving on.."+Style.RESET_ALL)"""
            if True:
                extr = []
                l = []
                for x in l1["inputs"]:
                    if (
                        x["name"].strip() not in leave_empty
                        and x["name"].strip() not in dont_send
                    ):
                        try:
                            if (
                                x["type"]
                                in [
                                    "hidden",
                                    "file",
                                    "text",
                                    "textarea",
                                    "email",
                                    "tel",
                                    "search",
                                    "url",
                                    "password",
                                    "number",
                                    "select",
                                    "radio",
                                    "checkbox",
                                    "color"
                                ]
                                and x["name"] not in dont_change
                            ):  # any input type that accept direct input from keyboard
                                i = x["name"]
                                parsed_form = set_up_injection(
                                    target_page,
                                    form_index,
                                    i,
                                    xp,
                                    cookie,
                                    setup_ua(user_agent),
                                    setup_proxy(proxy, proxies),
                                    timeout,
                                    fill_empty,
                                    file_extension=file_extension,
                                    number=number,
                                    email_extension=email_extension,
                                    phone_pattern=phone_pattern,
                                    leave_empty=leave_empty,
                                    dont_send=dont_send,
                                    mime_type=mime_type,
                                    predefined_inputs=predefined_inputs,
                                    dont_change=dont_change,
                                    headers=headers
                                )
                                _res = ssti_submit(
                                    parsed_form,
                                    xp,
                                    replaceble_parameters,
                                    debug=debug,
                                    enctype=l1["enctype"],
                                    eval_value=xp_eval,
                                )
                                if _res[0] == True:
                                    x = "parameter: '" + i + "' =&gt; [+] Vulnerable !!"
                                    vul.append({'parameter':i, 'context':_res[1]})
                                    colr = Fore.GREEN
                                else:
                                    x = "parameter: '" + i + "' =&gt; [-] Not Vulnerable"
                                    #sec.append(i)
                                    colr = Fore.RED
                                if _res[2] == True:
                                    x+=Fore.YELLOW+"\n[i] SQL Error detected"
                                    sql_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if _res[3]==True:
                                    x+=Fore.YELLOW+"\n[i] XML parsing Error detected"
                                    xml_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if _res[4] == True:
                                    x+=Fore.YELLOW+"\n[i] Fetching URL Error detected (potential SSRF)"
                                    ssrf_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if _res[5] == True:
                                    x+=Fore.YELLOW+"\n[i] Reading file Error detected (potential path traversal)"
                                    p_t_e.append({'parameter':i, 'p_o_c': _res[-1]})
                                if logs == True:
                                    print(colr + x + Style.RESET_ALL)
                        except Exception as ex:
                            break
            dic.append(
                {
                    "action": u,
                    "method": l1["method"],
                    "vulnerable": vul,
                    #"safe": sec,
                    "sql_errors":sql_e,
                    "xml_parsing_errors":xml_e,
                    "fetching_url_errors":ssrf_e,
                    "reading_file_errors":p_t_e
                }
            )
        final = {"payload": xp, "page": target_page, "result": dic}
        if save_to_file:
            with open(save_to_file.split(".")[0] + ".json", "w") as outfile:
                json.dump(final, outfile, indent=4)
            outfile.close()
        return final</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.ssti.ssti_submit"><code class="name flex">
<span>def <span class="ident">ssti_submit</span></span>(<span>parsed, payload, replaceble_parameters, debug=False, enctype='application/x-www-form-urlencoded', eval_value=1111111101)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssti_submit(
    parsed,
    payload,
    replaceble_parameters,
    debug=False,
    enctype="application/x-www-form-urlencoded",
    eval_value=1111111101,
):
    """"""
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
    if debug == True:
        for x in d:
            print("{}{} : {}{}".format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print("{}{} : {}{}".format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if "application/json" in enctype:
        d = json.dumps(d)
    if not fi:
        parsed[1].update(
            {
                "Content-Type": enctype,
                "Referer": parsed[0]["action"],
                "Origin": parsed[0]["action"].split("://")[0]
                + "://"
                + parsed[0]["action"].split("://")[1].split("/")[0],
            }
        )
    else:
        parsed[1].update(
            {
                "Referer": parsed[0]["action"],
                "Origin": parsed[0]["action"].split("://")[0]
                + "://"
                + parsed[0]["action"].split("://")[1].split("/")[0],
            }
        )
    c=''
    if parsed[0]["method"] == "get":
        try:
            c = requests.Session().get(
                parsed[0]["action"],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if "{}".format(eval_value) in c:
                return (True, {"p_o_c":p_o_c,"payload":payload, "result":"{}".format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    else:
        try:
            c = requests.Session().post(
                parsed[0]["action"],
                data=d,
                files=fi,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if "{}".format(eval_value) in c:
                return (True, {"p_o_c":p_o_c,"payload":payload, "result":"{}".format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, "",any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)</code></pre>
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
<li><code><a href="#bane.scanners.vulnerabilities.ssti.safe_eval" title="bane.scanners.vulnerabilities.ssti.safe_eval">safe_eval</a></code></li>
<li><code><a href="#bane.scanners.vulnerabilities.ssti.ssti" title="bane.scanners.vulnerabilities.ssti.ssti">ssti</a></code></li>
<li><code><a href="#bane.scanners.vulnerabilities.ssti.ssti_forms" title="bane.scanners.vulnerabilities.ssti.ssti_forms">ssti_forms</a></code></li>
<li><code><a href="#bane.scanners.vulnerabilities.ssti.ssti_submit" title="bane.scanners.vulnerabilities.ssti.ssti_submit">ssti_submit</a></code></li>
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