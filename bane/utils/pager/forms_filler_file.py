from .forms_finder_file import *
from .rand_generator import *


class FORMS_FILLER:

    @staticmethod
    def set_up_injection(
        url,
        form_index,
        parameter,
        payload,
        cookie,
        user_agent,
        proxy,
        timeout,
        auto_fill,
        file_extension="png",
        email_extension='@gmail.com',
        phone_pattern='XXX-XXX-XXXX',
        dont_change={},
        number=(1, 9),
        leave_empty=[],
        dont_send=[],
        mime_type=None,
        predefined_inputs={},
        headers={}
    ):
        cookies = None
        h = {"User-Agent": user_agent}
        if cookie:
            h.update({"Cookie": cookie})
            cookies = cookie
        h.update(headers)
        
        try:
            r = requests.Session().get(url, proxies=proxy, headers=h, verify=False, timeout=timeout)
        except:
            return False
        cook = None
        try:
            cook = r.headers["Set-cookie"]
        except:
            pass
        cookies = Cookies_Manager.set_correct_cookies(cook, cookie=cookie)
        form = FORMS_FINDER.forms_parser_text(url, r.text)[form_index]
        h = {"User-Agent": user_agent}
        if cookies and len(cookies.strip()) > 0:
            h.update({"Cookie": cookies})
        h.update(headers)
        return (
            FORMS_FILLER.form_filler(
                form,
                parameter,
                payload,
                auto_fill=auto_fill,
                number=number,
                dont_change=dont_change,
                email_extension=email_extension,
                phone_pattern=phone_pattern,
                file_extension=file_extension,
                leave_empty=leave_empty,
                dont_send=dont_send,
                mime_type=mime_type,
                predefined_inputs=predefined_inputs,
            ),
            h,
            proxy,
            timeout,
        )


    @staticmethod
    def form_filler(
        form,
        param,
        payload,
        file_extension="png",
        email_extension='@gmail.com',
        phone_pattern='XXX-XXX-XXXX',
        dont_change={},
        number=(1, 9),
        auto_fill=10,
        leave_empty=[],
        dont_send=[],
        mime_type=None,
        predefined_inputs={},
    ):
        for x in form["inputs"]:
            if x["name"].strip() in dont_change:
                x["value"] = dont_change[x["name"]]
            else:
                if x["name"].strip() in dont_send:
                    form["inputs"].remove(x)
                else:
                    if x["name"].strip() not in leave_empty:
                        if x["name"].strip() == param:
                            if file_extension==None:
                                file_extension=random.choice(x["accept"])
                            if x["type"] == "file":
                                if not mime_type:
                                    x["value"] = (
                                        payload + "." + file_extension,
                                        Common_Variables.files_upload[file_extension],
                                    )
                                else:
                                    x["value"] = (
                                        payload + "." + file_extension,
                                        Common_Variables.files_upload[file_extension],
                                        mime_type,
                                    )
                            else:
                                x["value"] = payload
                        else:
                            if x["name"].strip() in predefined_inputs:
                                x["value"] = predefined_inputs[x["name"]]
                            else:
                                if x["value"] == "":
                                    if x["type"] == "file":
                                        if not mime_type:
                                            x["value"] = (
                                                "bane_test"
                                                + str(random.randint(100000, 999999))
                                                + "."
                                                + file_extension,
                                                Common_Variables.files_upload[file_extension],
                                            )
                                        else:
                                            x["value"] = (
                                                "bane_test"
                                                + str(random.randint(100000, 999999))
                                                + "."
                                                + file_extension,
                                                Common_Variables.files_upload[file_extension],
                                                mime_type,
                                            )
                                    else:
                                        #if x['value']=='':
                                            if x["type"] == "number":
                                                x["value"] += str(random.randint(int(float(x.get('min',0))), int(float(x.get('max',9)))))
                                            elif x['type'] in ['text','password','search','textarea']:
                                                leng=random.randint(int(float(x.get('min',1))), int(float(x.get('max',64)))+1)
                                                for i in range(leng):
                                                    x["value"] += random.choice(Common_Variables.source_string)
                                            elif x['type']=='email':
                                                leng=random.randint(int(float(x.get('min',1))), int(float(x.get('max',15)))-len(email_extension)+1)
                                                for i in range(leng):
                                                    x["value"] += random.choice(string.ascii_lowercase)
                                                x["value"]+=email_extension
                                            elif x['type']=='tel':
                                                x["value"]=RANDOM_GENERATOR.generate_random_phone_number(phone_pattern)
                                            elif x['type']=='url':
                                                x["value"]=RANDOM_GENERATOR.generate_random_url()
                                            elif x['type']=='date':
                                                x["value"]=RANDOM_GENERATOR.random_date(x['min'], x['max'])
                                            elif x['type']=='color':
                                                x['value']=RANDOM_GENERATOR.generate_random_html_input_color()      
                                if x["type"] in ["select", "radio", "checkbox"]:
                                    if len(x["value"]) == 0 or x["value"] == "":
                                        x["value"] = ""
                                        for i in range(auto_fill):
                                            x["value"] += random.choice(Common_Variables.source_string)
                                    else:
                                        x["value"] = random.choice(x["value"])
        #print(form)
        return form
