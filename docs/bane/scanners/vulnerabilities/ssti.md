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
    enctype=&#34;application/x-www-form-urlencoded&#34;,
    eval_value=1111111101,
):
    &#34;&#34;&#34;&#34;&#34;&#34;
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
    if debug == True:
        for x in d:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if &#34;application/json&#34; in enctype:
        d = json.dumps(d)
    if not fi:
        parsed[1].update(
            {
                &#34;Content-Type&#34;: enctype,
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    else:
        parsed[1].update(
            {
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    c=&#39;&#39;
    if parsed[0][&#34;method&#34;] == &#34;get&#34;:
        try:
            c = requests.Session().get(
                parsed[0][&#34;action&#34;],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if &#34;{}&#34;.format(eval_value) in c:
                return (True, {&#34;p_o_c&#34;:p_o_c,&#34;payload&#34;:payload, &#34;result&#34;:&#34;{}&#34;.format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    else:
        try:
            c = requests.Session().post(
                parsed[0][&#34;action&#34;],
                data=d,
                files=fi,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if &#34;{}&#34;.format(eval_value) in c:
                return (True, {&#34;p_o_c&#34;:p_o_c,&#34;payload&#34;:payload, &#34;result&#34;:&#34;{}&#34;.format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, &#34;&#34;,any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)


def safe_eval(a, o, b):
    if a.strip().isnumeric() == False or b.strip().isnumeric() == False:
        raise Exception(&#34;For security reasons, ONLY NUMERIC VALUES ARE EVALUATED !!&#34;)
    if o.strip() not in [&#34;+&#34;, &#34;-&#34;, &#34;*&#34;, &#34;/&#34;]:
        raise Exception(
            &#34;For security reasons, ONLY OPERATORS ALLOWED ARE: + , - , * , /!!&#34;
        )
    return eval(a + o + b)


def ssti_forms(
    u,
    payload_index=0,
    values=(9, 123456789),
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    number=(1, 9),
    payload_keyword=&#34;payload&#34;,
    operator=&#34;*&#34;,
    save_to_file=None,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
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
    &#34;&#34;&#34;
    this function is for SSTI test with both POST and GET requests . it extracts the input fields names using the &#34;inputs&#34; function then test each input using POST and GET methods.
    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.ssti_forms(&#39;http://phptester.net/&#34;)
    &#34;&#34;&#34;
    target_page = u
    xp = ssti_list[payload_index].replace(
        payload_keyword, &#34;{}{}{}&#34;.format(values[0], operator, values[1])
    )
    xp_eval = safe_eval(&#34;{}&#34;.format(values[0]), operator, &#34;{}&#34;.format(values[1]))
    target_page = u
    form_index = -1
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    if logs == True:
        print(Fore.WHITE + &#34;[~]Getting forms...&#34; + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + &#34;[-]No forms were found!!!&#34; + Style.RESET_ALL)
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
            u = l1[&#34;action&#34;]
            if logs == True:
                print(
                    Fore.BLUE
                    + &#34;Form: &#34;
                    + Fore.WHITE
                    + str(form_index)
                    + Fore.BLUE
                    + &#34;\nAction: &#34;
                    + Fore.WHITE
                    + u
                    + Fore.BLUE
                    + &#34;\nMethod: &#34;
                    + Fore.WHITE
                    + l1[&#34;method&#34;]
                    + Fore.BLUE
                    + &#34;\nPayload: &#34;
                    + Fore.WHITE
                    + xp
                    + Style.RESET_ALL
                )
                &#34;&#34;&#34;if len(inputs(u,proxy=proxy,timeout=timeout,value=True,cookie=cookie,user_agent=user_agent))==0:
     if logs==True:
      print(Fore.YELLOW+&#34;[-]No parameters found on that page !! Moving on..&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            if True:
                extr = []
                l = []
                for x in l1[&#34;inputs&#34;]:
                    if (
                        x[&#34;name&#34;].strip() not in leave_empty
                        and x[&#34;name&#34;].strip() not in dont_send
                    ):
                        try:
                            if (
                                x[&#34;type&#34;]
                                in [
                                    &#34;hidden&#34;,
                                    &#34;file&#34;,
                                    &#34;text&#34;,
                                    &#34;textarea&#34;,
                                    &#34;email&#34;,
                                    &#34;tel&#34;,
                                    &#34;search&#34;,
                                    &#34;url&#34;,
                                    &#34;password&#34;,
                                    &#34;number&#34;,
                                    &#34;select&#34;,
                                    &#34;radio&#34;,
                                    &#34;checkbox&#34;,
                                    &#34;color&#34;
                                ]
                                and x[&#34;name&#34;] not in dont_change
                            ):  # any input type that accept direct input from keyboard
                                i = x[&#34;name&#34;]
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
                                    enctype=l1[&#34;enctype&#34;],
                                    eval_value=xp_eval,
                                )
                                if _res[0] == True:
                                    x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [+] Vulnerable !!&#34;
                                    vul.append({&#39;parameter&#39;:i, &#39;context&#39;:_res[1]})
                                    colr = Fore.GREEN
                                else:
                                    x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [-] Not Vulnerable&#34;
                                    #sec.append(i)
                                    colr = Fore.RED
                                if _res[2] == True:
                                    x+=Fore.YELLOW+&#34;\n[i] SQL Error detected&#34;
                                    sql_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if _res[3]==True:
                                    x+=Fore.YELLOW+&#34;\n[i] XML parsing Error detected&#34;
                                    xml_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if _res[4] == True:
                                    x+=Fore.YELLOW+&#34;\n[i] Fetching URL Error detected (potential SSRF)&#34;
                                    ssrf_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if _res[5] == True:
                                    x+=Fore.YELLOW+&#34;\n[i] Reading file Error detected (potential path traversal)&#34;
                                    p_t_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if logs == True:
                                    print(colr + x + Style.RESET_ALL)
                        except Exception as ex:
                            break
            dic.append(
                {
                    &#34;action&#34;: u,
                    &#34;method&#34;: l1[&#34;method&#34;],
                    &#34;vulnerable&#34;: vul,
                    #&#34;safe&#34;: sec,
                    &#34;sql_errors&#34;:sql_e,
                    &#34;xml_parsing_errors&#34;:xml_e,
                    &#34;fetching_url_errors&#34;:ssrf_e,
                    &#34;reading_file_errors&#34;:p_t_e
                }
            )
        final = {&#34;payload&#34;: xp, &#34;page&#34;: target_page, &#34;result&#34;: dic}
        if save_to_file:
            with open(save_to_file.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                json.dump(final, outfile, indent=4)
            outfile.close()
        return final

def ssti(
    u,
    max_pages=5,
    pages=[],
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    payload_index=0,
    values=(9, 123456789),
    dont_change={},
    number=(1, 9),
    payload_keyword=&#34;payload&#34;,
    operator=&#34;*&#34;,
    save_to_file=None,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
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
            print(&#39;\n\nPage: {}\n&#39;.format(x))
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
            n[&#39;result&#39;]=[]
            for i in x[&#39;result&#39;]:
                if len(i[&#39;vulnerable&#39;]) &gt; 0 or len(i[&#39;sql_errors&#39;]) &gt; 0 or len(i[&#39;xml_parsing_errors&#39;])&gt;0 or len(i[&#39;fetching_url_errors&#39;])&gt;0 or len(i[&#39;reading_file_errors&#39;]) &gt; 0:
                    n[&#39;result&#39;].append(i)
            if n[&#39;result&#39;]!=[]:
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
        raise Exception(&#34;For security reasons, ONLY NUMERIC VALUES ARE EVALUATED !!&#34;)
    if o.strip() not in [&#34;+&#34;, &#34;-&#34;, &#34;*&#34;, &#34;/&#34;]:
        raise Exception(
            &#34;For security reasons, ONLY OPERATORS ALLOWED ARE: + , - , * , /!!&#34;
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
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    payload_index=0,
    values=(9, 123456789),
    dont_change={},
    number=(1, 9),
    payload_keyword=&#34;payload&#34;,
    operator=&#34;*&#34;,
    save_to_file=None,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
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
            print(&#39;\n\nPage: {}\n&#39;.format(x))
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
            n[&#39;result&#39;]=[]
            for i in x[&#39;result&#39;]:
                if len(i[&#39;vulnerable&#39;]) &gt; 0 or len(i[&#39;sql_errors&#39;]) &gt; 0 or len(i[&#39;xml_parsing_errors&#39;])&gt;0 or len(i[&#39;fetching_url_errors&#39;])&gt;0 or len(i[&#39;reading_file_errors&#39;]) &gt; 0:
                    n[&#39;result&#39;].append(i)
            if n[&#39;result&#39;]!=[]:
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
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    number=(1, 9),
    payload_keyword=&#34;payload&#34;,
    operator=&#34;*&#34;,
    save_to_file=None,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=[&#34;btnClear&#34;],
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
    &#34;&#34;&#34;
    this function is for SSTI test with both POST and GET requests . it extracts the input fields names using the &#34;inputs&#34; function then test each input using POST and GET methods.
    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.ssti_forms(&#39;http://phptester.net/&#34;)
    &#34;&#34;&#34;
    target_page = u
    xp = ssti_list[payload_index].replace(
        payload_keyword, &#34;{}{}{}&#34;.format(values[0], operator, values[1])
    )
    xp_eval = safe_eval(&#34;{}&#34;.format(values[0]), operator, &#34;{}&#34;.format(values[1]))
    target_page = u
    form_index = -1
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    if logs == True:
        print(Fore.WHITE + &#34;[~]Getting forms...&#34; + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + &#34;[-]No forms were found!!!&#34; + Style.RESET_ALL)
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
            u = l1[&#34;action&#34;]
            if logs == True:
                print(
                    Fore.BLUE
                    + &#34;Form: &#34;
                    + Fore.WHITE
                    + str(form_index)
                    + Fore.BLUE
                    + &#34;\nAction: &#34;
                    + Fore.WHITE
                    + u
                    + Fore.BLUE
                    + &#34;\nMethod: &#34;
                    + Fore.WHITE
                    + l1[&#34;method&#34;]
                    + Fore.BLUE
                    + &#34;\nPayload: &#34;
                    + Fore.WHITE
                    + xp
                    + Style.RESET_ALL
                )
                &#34;&#34;&#34;if len(inputs(u,proxy=proxy,timeout=timeout,value=True,cookie=cookie,user_agent=user_agent))==0:
     if logs==True:
      print(Fore.YELLOW+&#34;[-]No parameters found on that page !! Moving on..&#34;+Style.RESET_ALL)&#34;&#34;&#34;
            if True:
                extr = []
                l = []
                for x in l1[&#34;inputs&#34;]:
                    if (
                        x[&#34;name&#34;].strip() not in leave_empty
                        and x[&#34;name&#34;].strip() not in dont_send
                    ):
                        try:
                            if (
                                x[&#34;type&#34;]
                                in [
                                    &#34;hidden&#34;,
                                    &#34;file&#34;,
                                    &#34;text&#34;,
                                    &#34;textarea&#34;,
                                    &#34;email&#34;,
                                    &#34;tel&#34;,
                                    &#34;search&#34;,
                                    &#34;url&#34;,
                                    &#34;password&#34;,
                                    &#34;number&#34;,
                                    &#34;select&#34;,
                                    &#34;radio&#34;,
                                    &#34;checkbox&#34;,
                                    &#34;color&#34;
                                ]
                                and x[&#34;name&#34;] not in dont_change
                            ):  # any input type that accept direct input from keyboard
                                i = x[&#34;name&#34;]
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
                                    enctype=l1[&#34;enctype&#34;],
                                    eval_value=xp_eval,
                                )
                                if _res[0] == True:
                                    x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [+] Vulnerable !!&#34;
                                    vul.append({&#39;parameter&#39;:i, &#39;context&#39;:_res[1]})
                                    colr = Fore.GREEN
                                else:
                                    x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [-] Not Vulnerable&#34;
                                    #sec.append(i)
                                    colr = Fore.RED
                                if _res[2] == True:
                                    x+=Fore.YELLOW+&#34;\n[i] SQL Error detected&#34;
                                    sql_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if _res[3]==True:
                                    x+=Fore.YELLOW+&#34;\n[i] XML parsing Error detected&#34;
                                    xml_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if _res[4] == True:
                                    x+=Fore.YELLOW+&#34;\n[i] Fetching URL Error detected (potential SSRF)&#34;
                                    ssrf_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if _res[5] == True:
                                    x+=Fore.YELLOW+&#34;\n[i] Reading file Error detected (potential path traversal)&#34;
                                    p_t_e.append({&#39;parameter&#39;:i, &#39;p_o_c&#39;: _res[-1]})
                                if logs == True:
                                    print(colr + x + Style.RESET_ALL)
                        except Exception as ex:
                            break
            dic.append(
                {
                    &#34;action&#34;: u,
                    &#34;method&#34;: l1[&#34;method&#34;],
                    &#34;vulnerable&#34;: vul,
                    #&#34;safe&#34;: sec,
                    &#34;sql_errors&#34;:sql_e,
                    &#34;xml_parsing_errors&#34;:xml_e,
                    &#34;fetching_url_errors&#34;:ssrf_e,
                    &#34;reading_file_errors&#34;:p_t_e
                }
            )
        final = {&#34;payload&#34;: xp, &#34;page&#34;: target_page, &#34;result&#34;: dic}
        if save_to_file:
            with open(save_to_file.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
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
    enctype=&#34;application/x-www-form-urlencoded&#34;,
    eval_value=1111111101,
):
    &#34;&#34;&#34;&#34;&#34;&#34;
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
    if debug == True:
        for x in d:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print(&#34;{}{} : {}{}&#34;.format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if &#34;application/json&#34; in enctype:
        d = json.dumps(d)
    if not fi:
        parsed[1].update(
            {
                &#34;Content-Type&#34;: enctype,
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    else:
        parsed[1].update(
            {
                &#34;Referer&#34;: parsed[0][&#34;action&#34;],
                &#34;Origin&#34;: parsed[0][&#34;action&#34;].split(&#34;://&#34;)[0]
                + &#34;://&#34;
                + parsed[0][&#34;action&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0],
            }
        )
    c=&#39;&#39;
    if parsed[0][&#34;method&#34;] == &#34;get&#34;:
        try:
            c = requests.Session().get(
                parsed[0][&#34;action&#34;],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if &#34;{}&#34;.format(eval_value) in c:
                return (True, {&#34;p_o_c&#34;:p_o_c,&#34;payload&#34;:payload, &#34;result&#34;:&#34;{}&#34;.format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    else:
        try:
            c = requests.Session().post(
                parsed[0][&#34;action&#34;],
                data=d,
                files=fi,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if &#34;{}&#34;.format(eval_value) in c:
                return (True, {&#34;p_o_c&#34;:p_o_c,&#34;payload&#34;:payload, &#34;result&#34;:&#34;{}&#34;.format(eval_value)},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, &#34;&#34;,any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.ssti.safe_eval" href="#bane.scanners.vulnerabilities.ssti.safe_eval">safe_eval</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssti.ssti" href="#bane.scanners.vulnerabilities.ssti.ssti">ssti</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssti.ssti_forms" href="#bane.scanners.vulnerabilities.ssti.ssti_forms">ssti_forms</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.ssti.ssti_submit" href="#bane.scanners.vulnerabilities.ssti.ssti_submit">ssti_submit</a></code></li>
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