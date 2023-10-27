from bane.scanners.vulnerabilities.utils import *


def csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None,headers={}):
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            "This attack requires authentication !! You need to set a Cookie"
        )
    res = {"Vulnerable": [], "Safe": []}
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
        # print(Fore.BLUE+"Form: "+Fore.WHITE+str(f.index(x))+Fore.BLUE+"\nAction: "+Fore.WHITE+x['action']+Fore.BLUE+"\nMethod: "+Fore.WHITE+x['method']+Style.RESET_ALL)
        for y in x["inputs"]:
            # print("Name: {} | Type: {} | Value: {}".format(y["name"],y["type"],y["value"]))
            if y["type"].lower() == "hidden":
                hd_v = True
            if y["type"].lower() == "hidden" and any(
                ele in y["name"].lower() for ele in Common_Variables.csrf_strings
            ):  # and y["value"]==f1f["inputs"][con]["value"]:
                vuln = False
        if vuln == True:
            if (
                hd_v == True
            ):  # if there is no Anti-CSRF Tokens then we check if the Hidden fields can be predicted or not (keep their values or change them by request)
                # print(Fore.YELLOW+"[i] Validating hidden values' prediction..."+Style.RESET_ALL)
                for i in x["hidden_values"]:
                    if len(x["hidden_values"][i]) > 0:
                        if x["hidden_values"][i] != f1[coun]["hidden_values"][i]:
                            vuln = False
        if vuln == True:
            colr = Fore.GREEN
            """if logs==True:
    print (colr+"[+] Vulnerable"+Style.RESET_ALL)"""
            res["Vulnerable"].append(x)
        else:
            colr = Fore.RED
            """if logs==True:
    print (colr+"[-] Not vulnerable"+Style.RESET_ALL)"""
            res["Safe"].append(x)
    return res


def csrf_forms(
    u,
    proxy=None,
    timeout=10,
    show_warnings=True,
    user_agent=None,
    cookie=None,
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    fill_empty=10,
    referer="http://www.evil.com",
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={},
    http_proxies=None,
    socks4_proxies=None,
    socks5_proxies=None
    ):
    proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
    vu = []
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            "This attack requires authentication !! You need to set a Cookie"
        )
    v = csrf_filter_tokens(
        u, proxy=setup_proxy(proxies), timeout=timeout, user_agent=user_agent, cookie=cookie, headers=headers
    )["Vulnerable"]
    if user_agent:
        h = {"User-Agent": user_agent}
    else:
        h = {"User-Agent": random.choice(Common_Variables.user_agents_list)}
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
    for x in v:
        x = form_filler(
            x,
            "",
            "",
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
        if x["method"] == "get":
            r = requests.Session().get(
                x["action"], params=d, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        else:
            if "application/json" in x["enctype"]:
                d = json.dumps(d)
            r = requests.Session().post(
                x["action"], data=d, files=f, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        if all(i in r.text for i in l):
            vu.append({'form':x, 'status':"Found all data"})
        elif r.status_code == 200 and any(i in r.text for i in l):
            vu.append({'form':x, 'status':"Found some data"})
            if show_warnings == True:
                print(
                    "Warning: HTTP Status Code: 200 , but we didn't find some of our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                )
        elif (
            r.status_code == 200
            and not any(i in r.text for i in l)
            and any(
                i in r.text.lower() for i in ["unauthorized", "invalid", "unacceptable"]
            )
        ):
            return False
        elif r.status_code == 200 and not any(i in r.text for i in l):
            if show_warnings == True:
                print(
                    "Warning: HTTP Status Code: 200 , but we didn't find any of our submitted data, so it's probably vulnerable but they are saved somewhere else..\nPlease check manually by visiting the form again"
                )
            vu.append({'form':x, 'status':"Found no data but Status Code: 200"})
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
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    fill_empty=10,
    referer="http://www.evil.com",
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    pages=[],
    headers={},
    http_proxies=None,
    socks4_proxies=None,
    socks5_proxies=None
    ):
    proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=setup_proxy(proxies))
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=csrf_forms(x,
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
                        headers=headers,
                        http_proxies=http_proxies,
                        socks4_proxies=socks4_proxies,
                        socks5_proxies=socks5_proxies)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]

