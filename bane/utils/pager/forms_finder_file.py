from .urls_parser import *

class FORMS_FINDER:

    @staticmethod
    def sort_inputs(l):
        a = []
        d = []
        for x in l:
            if x["type"] not in [u"radio", u"checkbox"]:
                d.append(x)
            if x["name"] not in a and (x["type"] == u"radio" or x["type"] == u"checkbox"):
                a.append(x["name"])
        for x in a:
            d.append(
                {
                    "type": [i["type"] for i in l if i["name"] == x][0],
                    "name": x,
                    "value": [i["value"] for i in l if i["name"] == x],
                }
            )
        return d


    @staticmethod
    def forms_parser(
        u,
        html_comments=False,
        user_agent=None,
        timeout=10,
        bypass=False,
        proxy=None,
        cookie=None,
        include_links=True,
        headers={}
    ):
        """
        same as "forms" function but it return detailed information about all forms in a given page
        """
        if urlparse(u).path == "":
            u += "/"
        domain=u.split('://')[1].split('/')[0]
        base_url=u.split('://')[0]+domain
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if bypass == True:
            u += "#"
        if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
        else:
            hea = {"User-Agent": us}
        hea.update(headers)
        l = []
        fom = []
        try:
            c = requests.Session().get(
                u, headers=hea, proxies=proxy, timeout=timeout, verify=False
            ).text
            if html_comments == False:
                c = remove_html_comments(c)
            soup = BeautifulSoup(c, "html.parser")
            i = soup.find_all("form")
            for f in i:
                form_id=f.get('id','')
                try:
                    tb_inputs = f.find_all("table")[0].find_all("input")
                except:
                    tb_inputs = []
                try:
                    tb_textareas = f.find_all("table")[0].find_all("textarea")
                except:
                    tb_textareas = []
                try:
                    tb_selects = f.find_all("table")[0].find_all("select")
                except:
                    tb_selects = []
                ac = urljoin(u, f.get("action",''))
                enc_ty = f.get("enctype", "application/x-www-form-urlencoded")
                if not ac:
                    ac = u
                """if len(ac)==0:
        ac=u
    if ac[0]=="/":
        url_o="/".join(u.split('/')[:-1])
        ac=url_o+ac
    if ac[:4]!="http":
        url_o="/".join(u.split('/')[:-1])
        ac=url_o+"/"+ac"""
                if "://" not in ac:
                    ur = u[: u.rfind("/")]
                    if ac[0] == "/":
                        ac = ac[1 : len(ac)]
                    ac = ur + "/" + ac
                me = f.get("method", "get")
                if not me:
                    me = "get"
                if len(me) == 0:
                    me = "get"
                me = me.lower()
                """radios={}
                checkxoes={}"""
                p = f.find_all("textarea") + tb_textareas
                for r in p:
                    required=False
                    if 'required' in r.attrs:
                        required=True
                    if r.has_attr("name"):
                        s = r.get("name")
                        v = r.renderContents().decode().split("</textarea>")[0]
                        typ = r.get("type", "textarea").lower()
                        max_size=r.get('maxlength',64)
                        if r.get('size',0)!=0:
                                max_size= r.get('size',64)
                        y = {"name": s, "value": v, "type": typ,'max':max_size,'min':r.get('minlength',1),'required':required}
                        if y not in l:
                            l.append(y)
                h_v = {}
                p = f.find_all("input") + tb_inputs
                for r in p:
                    required=False
                    if 'required' in r.attrs:
                        required=True
                    if r.has_attr("name"):
                        s = r.get("name")
                        v = r.get("value", "")
                        typ = r.get("type", "text").lower()
                        y = {"name": s, "value": v, "type": typ,'required':required}
                        if y['type'] in ['text','password','email','url','tel','search']:
                            max_size=r.get('maxlength',64)
                            if r.get('size',0)!=0:
                                max_size= r.get('size',64)
                            y.update({'max':int(max_size),'min':int(r.get('minlength',1))})
                        elif y['type']=='number':
                            y.update({'max':int(r.get('max',10)),'min':int(r.get('min',1))})
                        elif y['type']=='date':
                            y.update({'max':r.get('max',datetime.datetime.today().strftime("%Y-%m-%d")),'min':r.get('min',datetime.datetime.today().strftime("%Y-%m-%d"))})
                        elif y['type']=='file':
                            y.update({'accept':[ x.replace('.','').strip() for x in y.get('accept','.png').split(',')]})
                        """elif y['type']=='radio':
                            if y['name'] not in radios:
                                radios[y['name']]=[]
                            radios[y['name']].append(y)
                        elif y['type']=='checkbox':
                            if y['name'] not in checkxoes:
                                checkxoes[y['name']]=[]
                            checkxoes[y['name']].append(y)"""
                        if typ.lower() == "hidden":
                            h_v.update({s: v})
                        if y not in l :#and y['name'] not in radios and y['name'] not in checkxoes:
                            l.append(y)
                p = f.find_all("select") + tb_selects
                opts = []
                for r in p:
                    required=False
                    if 'required' in r.attrs:
                        required=True
                    if r.has_attr("name"):
                        s = r.get("name")
                        for x in r.find_all("option"):
                            opts.append(x.text)
                        y = {"name": s, "value": opts, "type": "select",'required':required}
                        if y not in l:
                            l.append(y)
                """for x in radios:
                    l.append({'name':x,'type':'radio','value':[i['value'] for i in radios[x]]})
                for x in checkxoes:
                    l.append({'name':x,'type':'checkbox','value':[i['value'] for i in checkxoes[x]]})"""
                fom.append(
                    {
                        'id':form_id,
                        "inputs": FORMS_FINDER.sort_inputs(l),
                        "action": ac.lower(),
                        "enctype": enc_ty.lower(),
                        "method": me.lower(),
                        "hidden_values": h_v,
                        "is_url":False
                    }
                )
                l = []
        except Exception as e:
            pass
        if include_links==True:
            fom+=URLS_Parser.get_links_from_page_source(soup,u,'')
        return fom


    @staticmethod
    def forms_parser_text(u, text, html_comments=False,include_links=True):
        """
        same as "forms" function but it return detailed information about all forms in a given page
        """
        if urlparse(u).path == "":
            u += "/"
        l = []
        fom = []
        try:
            c = text
            if html_comments == False:
                c = remove_html_comments(c)
            soup = BeautifulSoup(c, "html.parser")
            i = soup.find_all("form")
            for f in i:
                form_id=f.get('id','')
                try:
                    tb_inputs = f.find_all("table")[0].find_all("input")
                except:
                    tb_inputs = []
                try:
                    tb_textareas = f.find_all("table")[0].find_all("textarea")
                except:
                    tb_textareas = []
                try:
                    tb_selects = f.find_all("table")[0].find_all("select")
                except:
                    tb_selects = []
                ac = urljoin(u, f.get("action",''))
                enc_ty = f.get("enctype", "application/x-www-form-urlencoded").lower()
                if not ac:
                    ac = u
                """if len(ac)==0:
        ac=u
    if ac[0]=="/":
        url_o="/".join(u.split('/')[:-1])
        ac=url_o+ac
    if ac[:4]!="http":
        url_o="/".join(u.split('/')[:-1])
        ac=url_o+"/"+ac"""
                if "://" not in ac:
                    ur = u[: u.rfind("/")]
                    if ac[0] == "/":
                        ac = ac[1 : len(ac)]
                    ac = ur + "/" + ac
                me = f.get("method", "get").lower()
                if not me:
                    me = "get"
                if len(me) == 0:
                    me = "get"
                me = me.lower()
                """radios={}
                checkxoes={}"""
                p = f.find_all("textarea") + tb_textareas
                for r in p:
                    required=False
                    if 'required' in r.attrs:
                        required=True
                    if r.has_attr("name"):
                        s = r.get("name")
                        v = r.renderContents().decode().split("</textarea>")[0]
                        typ = r.get("type", "textarea").lower()
                        max_size=r.get('maxlength',64)
                        if r.get('size',0)!=0:
                                max_size= r.get('size',64)
                        y = {"name": s, "value": v, "type": typ,'max':max_size,'min':r.get('minlength',1),'required':required}
                        if y not in l:
                            l.append(y)
                h_v = {}
                p = f.find_all("input") + tb_inputs
                for r in p:
                    required=False
                    if 'required' in r.attrs:
                        required=True
                    if r.has_attr("name"):
                        s = r.get("name")
                        v = r.get("value", "")
                        typ = r.get("type", "text").lower()
                        y = {"name": s, "value": v, "type": typ,'required':required}
                        if y['type'] in ['text','password','email','url','tel','search']:
                            max_size=r.get('maxlength',64)
                            if r.get('size',0)!=0:
                                max_size= r.get('size',64)
                            y.update({'max':int(max_size),'min':int(r.get('minlength',1))})
                        elif y['type']=='number':
                            y.update({'max':int(r.get('max',64)),'min':int(r.get('min',1))})
                        elif y['type']=='date':
                            y.update({'max':r.get('max',datetime.datetime.today().strftime("%Y-%m-%d")),'min':r.get('min',datetime.datetime.today().strftime("%Y-%m-%d"))})
                        elif y['type']=='file':
                            y.update({'accept':[ x.replace('.','').strip() for x in y.get('accept','.png').split(',')]})
                        """elif y['type']=='radio':
                            if y['name'] not in radios:
                                radios[y['name']]=[]
                            radios[y['name']].append(y)
                        elif y['type']=='checkbox':
                            if y['name'] not in checkxoes:
                                checkxoes[y['name']]=[]
                            checkxoes[y['name']].append(y)"""
                        if typ.lower() == "hidden":
                            h_v.update({s: v})
                        if y not in l :#and y['name'] not in radios and y['name'] not in checkxoes:
                            l.append(y)
                p = f.find_all("select") + tb_selects
                opts = []
                for r in p:
                    required=False
                    if 'required' in r.attrs:
                        required=True
                    if r.has_attr("name"):
                        s = r.get("name")
                        for x in r.find_all("option"):
                            opts.append(x.text)
                        y = {"name": s, "value": opts, "type": "select",'required':required}
                        if y not in l:
                            l.append(y)
                """for x in radios:
                    l.append({'name':x,'type':'radio','value':[i['value'] for i in radios[x]]})
                for x in checkxoes:
                    l.append({'name':x,'type':'checkbox','value':[i['value'] for i in checkxoes[x]]})"""
                fom.append(
                    {
                        'id':form_id,
                        "inputs": FORMS_FINDER.sort_inputs(l),
                        "action": ac,
                        "enctype": enc_ty,
                        "method": me,
                        "hidden_values": h_v,
                        "is_url":False
                    }
                )
                l = []
        except Exception as e:
            raise(e)
        if include_links==True:
            fom+=URLS_Parser.get_links_from_page_source(soup,u,'')
        return fom

