from bane.scanners.vulnerabilities.utils import *

def rce_submit(
    parsed,
    payload,
    based_on,
    replaceble_parameters,
    debug=False,
    enctype="application/x-www-form-urlencoded",
    type_injection="code",
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
    t = time.time()
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
            )
            if based_on[0] == "file":
                c = requests.Session().get(
                    parsed[0]["action"].replace(
                        parsed[0]["action"].split("/")[-1], based_on[1] + ".txt"
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
                        {"reflection":parsed[0]["action"].replace(
                            parsed[0]["action"].split("/")[-1], based_on[1]
                        )
                        + ".txt","p_o_c":p_o_c},
                        any(s in c.text for s in Common_Variables.sql_errors),
                        any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c
                    )
            if based_on[0] == "time":
                if type_injection == "command":
                    if (int(time.time() - t) >= based_on[1] - 2) or (
                        c.status_code == 504
                    ):
                        return (True, {"p_o_c":p_o_c},any(s in c.text for s in Common_Variables.sql_errors),any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) >= based_on[1]) or (c.status_code == 504):
                        return (True, {"p_o_c":p_o_c},any(s in c.text for s in Common_Variables.sql_errors),any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if "Read timed out" in str(e):
                #if based_on[0] == "time":
                    return (True, {"p_o_c":p_o_c},False,False,False,False)
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
            )
            if based_on[0] == "file":
                c = requests.Session().get(
                    parsed[0]["action"].replace(
                        parsed[0]["action"].split("/")[-1], based_on[1] + ".txt"
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
                        {"reflection":parsed[0]["action"].replace(
                            parsed[0]["action"].split("/")[-1], based_on[1]
                        )
                        + ".txt","p_o_c":p_o_c},
                        any(s in c.text for s in Common_Variables.sql_errors),
                        any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c
                    )
            if based_on[0] == "time":
                if (int(time.time() - t) >= based_on[1] - 2) or (c.status_code == 504):
                    return (True, {"p_o_c":p_o_c},any(s in c.text for s in Common_Variables.sql_errors),any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) >= based_on[1]) or (c.status_code == 504):
                        return (True, {"p_o_c":p_o_c},any(s in c.text for s in Common_Variables.sql_errors),any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if "Read timed out" in str(e):
                #if based_on[0] == "time":
                    return (True, {"p_o_c":p_o_c},any(s in c.text for s in Common_Variables.sql_errors),any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c)
    return (False, "",any(s in c.text for s in Common_Variables.sql_errors),any(s in c.text for s in Common_Variables.xml_parser_errors),any(s in c.text for s in Common_Variables.fetch_url_errors),any(s in c.text for s in Common_Variables.open_file_errors),p_o_c)


def rce_forms(
    u,
    payloads=Common_Variables.rce_payloads,
    payload_index=0,
    save_to_file=None,
    dont_change={},
    number=(1, 9),
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    injection={"code": "php"},
    code_operator_right="; ",
    code_operator_left="",
    command_operator_right="|",
    command_operator_left="&",
    sql_operator_right="or '",
    sql_operator_left="' or ",
    file_extension="png",
    replaceble_parameters={"phpvalue": ((".", ""),)},
    based_on="time",
    delay=10,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    timeout=120,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    predefined_inputs={},
    headers={},
    http_proxies=None,
    socks4_proxies=None,
    socks5_proxies=None
):
    proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
    payloads = payloads.copy()
    target_page = u
    xp = ""
    based_on_o = based_on
    if list(injection.keys())[0] == "command":
        xp += command_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == "file":
            based_on = ("file", random_string(random.randint(3, 10)))
        else:
            based_on = ("time", int(delay) + 2)
        xp = xp.format(based_on[1])
        xp += command_operator_right
    elif list(injection.keys())[0] == "code":
        xp += code_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == "file":
            based_on = ("file", random_string(random.randint(3, 10)))
        else:
            based_on = ("time", int(delay))
        xp = xp.format(based_on[1])
        xp += code_operator_right
    else:
        xp += sql_operator_left
        inject_type = list(injection.keys())[0]
        inject_target = injection[inject_type]
        xp += payloads[inject_type.lower()][inject_target.lower()][based_on.lower()][
            payload_index
        ]
        if based_on_o.lower() == "file":
            based_on = ("file", random_string(random.randint(3, 10)))
        else:
            based_on = ("time", int(delay))
        xp = xp.format(based_on[1])
        xp += sql_operator_right
    target_page = u
    form_index = -1
    dic = []
    if logs == True:
        print(Fore.WHITE + "[~]Getting forms..." + Style.RESET_ALL)
    hu = True
    fom = forms_parser(
        u, proxy=setup_proxy(proxies), timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + "[-]No forms were found!!!" + Style.RESET_ALL)
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
                    + xp.replace(
                        " {} ".format(int(delay) + 2), " {} ".format(int(delay))
                    )
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
                                    setup_proxy(proxies),
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
                                    enctype=l1["enctype"],
                                    type_injection=list(injection.keys())[0],
                                )
                                if _res[0] == True:
                                    x = "parameter: '" + i + "' => [+] Vulnerable !!"
                                    vul.append({'parameter':i, 'context': _res[1]})
                                    colr = Fore.GREEN
                                else:
                                    x = "parameter: '" + i + "' => [-] Not Vulnerable"
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
                            pass#raise(ex)
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
        if based_on_o == "time":
            final = {
                "payload": xp.replace(
                    " {} ".format(int(delay) + 2), " {} ".format(int(delay))
                ),
                "based_on": based_on_o,
                "injection": injection,
                "page": target_page,
                "result": dic,
            }
        else:
            final = {
                "payload": xp,
                "based_on": based_on_o,
                "injection": injection,
                "page": target_page,
                "result": dic,
            }
        if save_to_file:
            with open(save_to_file.split(".")[0] + ".json", "w") as outfile:
                json.dump(final, outfile, indent=4)
            outfile.close()
        return final



def rce(
    u,
    max_pages=5,
    pages=[],
    payloads=Common_Variables.rce_payloads,
    payload_index=0,
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    save_to_file=None,
    dont_change={},
    number=(1, 9),
    injection={"code": "php"},
    code_operator_right=" ; ",
    code_operator_left=" ",
    command_operator_right=" | ",
    command_operator_left=" & ",
    sql_operator_right=" or '",
    sql_operator_left="' or ",
    file_extension="png",
    replaceble_parameters={"phpvalue": ((".", ""),)},
    based_on="time",
    delay=10,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    timeout=120,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    predefined_inputs={},
    headers={},
    http_proxies=None,
    socks4_proxies=None,
    socks5_proxies=None
):
    proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=setup_proxy(proxies),headers=headers)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        l.append(rce_forms(x,
                            payload_index=payload_index,
                            payloads=payloads,
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
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type,
                            predefined_inputs=predefined_inputs,
                            headers=headers,
                            http_proxies=http_proxies,
                            socks4_proxies=socks4_proxies,
                            socks5_proxies=socks5_proxies))
    f=[]
    for x in l:
        if x !=None:
            n=x.copy()
            n['result']=[]
            for i in x['result']:
                if len(i['vulnerable']) > 0 or len(i['sql_errors']) > 0 or len(i['xml_parsing_errors'])>0 or len(i['fetching_url_errors'])>0 or len(i['reading_file_errors']) > 0:
                    n['result'].append(i)
            if n['result']!=[]:
                f.append(n)
    return f


