from bane.scanners.vulnerabilities.utils import *


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
    return  l#[x for x in l if x['result']['vulnerable']!=False]
