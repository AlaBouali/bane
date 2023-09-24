from bane.scanners.vulnerabilities.utils import *

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
            c = requests.get(
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
            c = requests.post(
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
):
    """
    this function is for SSTI test with both POST and GET requests. it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.
    usage:

    >>>import bane
    >>>bane.ssti_forms('http://phptester.net/")
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
        u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True
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
                                    x = "parameter: '" + i + "' => [+] Vulnerable !!"
                                    vul.append({'parameter':i, 'context':_res[1]})
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
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
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
                            predefined_inputs=predefined_inputs))
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

