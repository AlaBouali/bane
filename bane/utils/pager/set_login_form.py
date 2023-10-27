from .forms_filler_file import *

class LOGIN_FORM_FILLER:

    @staticmethod
    def get_login_form(url, text):
        a = FORMS_FINDER.forms_parser_text(url, text)
        for x in a:
            for i in x["inputs"]:
                if i["type"].lower().strip() == "password":
                    return x
        raise Exception("No login form")


    @staticmethod
    def set_login_form(url, text, username, password):
        a = LOGIN_FORM_FILLER.get_login_form(url, text)
        d = {}
        for x in a["inputs"]:
            if x["type"].lower().strip() == "password":
                d.update({x["name"]: password})
            elif (
                x["type"].lower().strip() == "text"
                or x["type"].lower().strip() == "email"
                or x["type"].lower().strip() == "tel"
            ):
                d.update({x["name"]: username})
            else:
                d.update({x["name"]: x["value"]})
        return [d, a["action"]]