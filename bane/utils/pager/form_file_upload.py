from .forms_filler_file import *


class FORM_FILE_UPLOAD:

    
    @staticmethod
    def get_upload_form(a):
        l=[]
        for x in a:
            for i in x["inputs"]:
                if i["type"].lower().strip() == "file":
                    l.append(x)
        if l==[]:
            raise Exception("No file upload form")
        return l


    @staticmethod
    def get_upload_form_text(url, text):
        l=[]
        a = FORMS_FINDER.forms_parser_text(url, text)
        for x in a:
            for i in x["inputs"]:
                if i["type"].lower().strip() == "file":
                    l.append(x)
        if l==[]:
            raise Exception("No file upload form")
        return l

