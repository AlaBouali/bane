from bane.scanners.vulnerabilities.utils import *


def is_valid_open_redirect(req,payload):
    return url_decode(payload)==req.headers['location']



def open_redirect_submit(
    parsed,
    payload,
    replaceble_parameters,
    debug=False,
    enctype="application/x-www-form-urlencoded",
):
    """"""
    p_o_c=parsed[0].copy()
    d, fi = setup_to_submit(parsed[0])
    for x in d:
        for y in replaceble_parameters:
            if x == y:
                for z in replaceble_parameters[y]:
                    d[x] = d[x].replace(z[0], z[1])
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
    if debug == True:
        for x in d:
            print("{}{} : {}{}".format(Fore.MAGENTA, x, Fore.WHITE, d[x]))
        for x in fi:
            print("{}{} : {}{}".format(Fore.MAGENTA, x, Fore.WHITE, fi[x]))
    if "application/json" in enctype:
        d = json.dumps(d)
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
                allow_redirects=False
            )
            if is_valid_open_redirect(c,payload):
                return (True, {"p_o_c":p_o_c},any(s in c for s in Common_Variables.sql_errors),any(s in c for s in Common_Variables.xml_parser_errors),any(s in c for s in Common_Variables.fetch_url_errors),any(s in c for s in Common_Variables.open_file_errors),p_o_c)
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
                allow_redirects=False
            )
            if is_valid_open_redirect(c,payload)==True:
                return (True, {"p_o_c":p_o_c},any(s in c for s in Common_Variables.sql_errors),any(s in c for s in Common_Variables.xml_parser_errors),any(s in c for s in Common_Variables.fetch_url_errors),any(s in c for s in Common_Variables.open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, "",any(s in c for s in Common_Variables.sql_errors),any(s in c for s in Common_Variables.xml_parser_errors),any(s in c for s in Common_Variables.fetch_url_errors),any(s in c for s in Common_Variables.open_file_errors),p_o_c)



def open_redirect_forms(
    u,
    payload='http://www.google.com',
    number=(1, 9),
    dont_change={},
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    predefined_inputs={},
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
    headers={},
    http_proxies=None,
    socks4_proxies=None,
    socks5_proxies=None
):
    proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
    target_page = u
    dic = []
    pre_apyload = True
    if logs == True:
        print(Fore.WHITE + "[~]Getting forms..." + Style.RESET_ALL)
    hu = True
    fom = FORMS_FINDER.forms_parser(
        u, proxy=setup_proxy(proxies), timeout=timeout, cookie=cookie, user_agent=user_agent,include_links=True,headers=headers
    )
    if len(fom) == 0:
        if logs == True:
            print(Fore.RED + "[-]No forms were found!!!" + Style.RESET_ALL)
        hu = False
    if hu == True:
        form_index = -1
        for l1 in fom:
            form_index += 1
            xp=payload
            lst = {}
            vul = []
            sec = []
            sql_e=[]
            xml_e=[]
            p_t_e=[]
            ssrf_e=[]
            p_t_erros=[]
            ssrf_errors=[]
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
     hu=False
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
                            parsed_form = FORMS_FILLER.set_up_injection(
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
                                dont_change=dont_change,
                                email_extension=email_extension,
                                phone_pattern=phone_pattern,
                                number=number,
                                leave_empty=leave_empty,
                                dont_send=dont_send,
                                mime_type=mime_type,
                                predefined_inputs=predefined_inputs,
                                headers=headers
                            )
                            xss_res = open_redirect_submit(
                                parsed_form,
                                xp,
                                replaceble_parameters,
                                debug=debug,
                                enctype=l1["enctype"],
                            )
                            if xss_res[0] == True:
                                x = "parameter: '" + i + "' => [+]Open redirect detected"
                                vul.append({'parameter':i, 'context':xss_res[1]})
                                colr = Fore.GREEN
                            else:
                                x = "parameter: '" + i + "' => [-]Failed"
                                #sec.append(i)
                                colr = Fore.RED
                            if xss_res[2] == True:
                                x+=Fore.YELLOW+"\n[i] SQL Error detected"
                                sql_e.append({'parameter':i, 'p_o_c': xss_res[-1]})
                            if xss_res[3]==True:
                                x+=Fore.YELLOW+"\n[i] XML parsing Error detected"
                                xml_e.append({'parameter':i, 'p_o_c': xss_res[-1]})
                            if xss_res[4] == True:
                                x+=Fore.YELLOW+"\n[i] Fetching URL Error detected (potential SSRF)"
                                ssrf_e.append({'parameter':i, 'p_o_c': xss_res[-1]})
                            if xss_res[5] == True:
                                x+=Fore.YELLOW+"\n[i] Reading file Error detected (potential path traversal)"
                                p_t_e.append({'parameter':i, 'p_o_c': xss_res[-1]})
                            if logs == True:
                                print(colr + x + Style.RESET_ALL)
            dic.append(
                {
                    "form": u,
                    "method": l1["method"],
                    "vulnerable": vul,
                    #"safe": sec,
                    "sql_errors":sql_e,
                    "xml_parsing_errors":xml_e,
                    "fetching_url_errors":ssrf_e,
                    "reading_file_errors":p_t_e
                }
            )
        if save_to_file:
            with open(save_to_file.split(".")[0] + ".json", "w") as outfile:
                json.dump(
                    {"payload": xp, "page": target_page, "result": dic},
                    outfile,
                    indent=4,
                )
            outfile.close()
        return {"payload": xp, "page": target_page, "result": dic}




def open_redirect(
    u,
    max_pages=5,
    pages=[],
    payload='http://www.google.com',
    number=(1, 9),
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
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
        l.append(open_redirect_forms(x,
                           payload=payload,
                            number=number,
                            dont_change=dont_change,
                            predefined_inputs=predefined_inputs,
                            replaceble_parameters=replaceble_parameters,
                            file_extension=file_extension,
                            save_to_file=save_to_file,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            logs=logs,
                            fill_empty=fill_empty,
                            leave_empty=leave_empty,
                            dont_send=dont_send,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type,
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


