<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.utils.pager API documentation</title>
<meta content="" name="description"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" rel="stylesheet preload"/>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script crossorigin="" defer="" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</meta></head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.utils.pager</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import requests, random, re, time, furl, sys, datetime , string,json,ast

try:
    import jsbeautifier
except:
    pass
if sys.version_info &lt; (3, 0):
    from urlparse import urlparse,urljoin
    from urllib import unquote as url_decode
else:
    from urllib.parse import urlparse,urljoin
    from urllib.parse import unquote as url_decode



import urllib3



from bane.cryptographers.hasher import base64_decode
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import bs4
from bs4 import BeautifulSoup
from bane.common.payloads import *
from bane.gather_info.info_s import extract_root_domain



def generate_random_url():
    protocols = ["http", "https"]
    protocol = random.choice(protocols)
    domain = random.choice(domainl)
    return "{}://{}/".format(protocol,domain)


def generate_random_phone_number(pattern):
    phone_number = ""
    for char in pattern:
        if char == "X":
            random_digit = str(random.randint(0, 9))
            phone_number += random_digit
        else:
            phone_number += char
    return phone_number

def generate_random_html_input_color():
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Convert RGB to hexadecimal
    color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return color_hex


def random_date(start_date, end_date):
    if start_date==end_date:
        return start_date
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")


def spider_url(base_url, include_id=False,max_pages=50,timeout=15,cookie=None,user_agent=None,proxy=None,headers={}):
    domain=base_url.split('://')[1].split('/')[0]
    h={}
    if cookie:
        h.update({'Cookie':cookie})
    if user_agent:
        h.update({'User-Agent':user_agent})
    else:
        h.update({'User-Agent':random.choice(ua)})
    h.update(headers)
    visited_urls = set()
    urls_to_visit = [base_url]
    collected_urls = set()
    root_urls=[]

    while urls_to_visit and len(collected_urls) &lt; max_pages:
        url = urls_to_visit.pop(0)
        try:
            response = requests.Session().get(url,headers=h,timeout=timeout,proxies=proxy,verify=False)
            response.raise_for_status()  # Check for any request errors

            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract all links from the page
            for anchor_tag in soup.find_all('a', href=True):
                href = anchor_tag['href']
                absolute_url = urljoin(url, href)
                try:
                    this_domain=absolute_url.split('://')[1].split('/')[0]
                except:
                    this_domain=''

                if absolute_url not in visited_urls and absolute_url.split('?')[0].split('#')[0] not in root_urls and domain == this_domain:
                    visited_urls.add(absolute_url)
                    urls_to_visit.append(absolute_url)
                    root_urls.append(absolute_url.split('?')[0].split('#')[0])
            if include_id==True:
                collected_urls.add({'url':url,'id':anchor_tag.get('id','')})
            else:
                collected_urls.add(url)
            #print(len(collected_urls))

        except requests.exceptions.RequestException as e:
            print("Error fetching URL: {}".format(e))

    return list(collected_urls)



def url_to_get_form(u,url_id):
    #print('&amp;'.join(u.split('?')[1:]).replace('?','&amp;').split('&amp;'))
    #print(u.split('?')[1].split('&amp;'))
    inputs=[]
    for x in '&amp;'.join(u.split('?')[1:]).replace('?','&amp;').split('&amp;'):
        try:
            inputs.append({'name':x.split('=')[0],'type':'text','value':x.split('=')[1]})
        except:
            inputs.append({'name':x.split('=')[0],'type':'text','value':''})
    #inputs=[ {'name':x.split('=')[0],'type':'text','value':x.split('=')[1]} for x in u.split('?')[1].split('&amp;')]
    return {
                    "inputs": inputs,
                    "action": u.split('?')[0],
                    "enctype": 'application/x-www-form-urlencoded',
                    "method": 'get',
                    "id":url_id,
                    "hidden_values": [],
                    "is_url":True
                }


def get_links_from_page_source(soup,url,url_id):
    if url.endswith('/')==False:
        url+='/'
    domain=url.split('/')[0] if url.startswith('http')==False else url.split('://')[1].split('/')[0]
    l=soup.find_all('a')
    links=[{'url':x['href'].replace('&amp;amp;','&amp;'),'id':x.get('id','')} for x in l if x.has_attr('href')]
    media_tags = soup.find_all(['img', 'audio', 'video', 'source','embed'])
    links+=[{'url':x['src'].replace('&amp;amp;','&amp;'),'id':x.get('id','') } for x in media_tags if x.has_attr('src')]
    links.append({'url':url,'id':url_id})
    #print(links)
    #links_list=[]
    root_links=[]
    forms=[]
    for l in links:
        x=l['url']
        l_id=l['id']
        if '?' in x and x.split('?')[0] not in root_links:
            a=urljoin(url, x)
            #print(a)
            if a.startswith(url.split(domain)[0]+domain)==True:
                forms.append(url_to_get_form(a,l_id))
                root_links.append(x.split('?')[0])
    return forms



def remove_html_comments(text):
    return re.sub(r"&lt;!--(.|\s|\n)*?--&gt;", "", text, flags=re.DOTALL)


def inputs(
    u,
    html_comments=False,
    value=False,
    timeout=10,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
):
    """
     this function is to get the names and values of input fields on a given webpage to scan.

     it takes 4 arguments:

     u: the page's link (http://...)
     value: (set by default to: False) to return the value of the fields set it to:True then the field's name and value will be string of 2
     values sperated by ":"
     timeout: (set by default to: 10) timeout flag for the request
     bypass: (set by default to: False) to bypass anti-crawlers

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;link='http://www.example.com'
    &gt;&gt;&gt;bane.inputs(link)
    ['email','password','rememberme']
    &gt;&gt;&gt;a=bane.inputs(link,value=True)
    ['email','password','rememberme:yes','rememberme:no']

    """
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += "#"
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    l = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        p = soup.find_all("textarea")
        for r in p:
            if r.has_attr("name"):
                s = r.get("name")
                v = r.get("value")
                if v == None:
                    v = ""
            if value == True:
                y = s + ":" + v
            else:
                y = s
            if y not in l:
                l.append(y)
        p = soup.find_all("input")
        for r in p:
            v = ""
            if r.has_attr("name"):
                s = str(r)
                s = s.split('name="')[1].split(",")[0]
                s = s.split('"')[0].split(",")[0]
                if r.has_attr("value") and (value == True):
                    v = str(r)
                    v = v.split('value="')[1].split(",")[0]
                    v = v.split('"')[0].split(",")[0]
            if value == True:
                y = s + ":" + v
            else:
                y = s
            if y not in l:
                l.append(y)
    except Exception as e:
        pass
    return l


def forms(
    u,
    value=True,
    html_comments=False,
    user_agent=None,
    timeout=10,
    bypass=False,
    proxy=None,
    cookie=None,
):
    """
    same as "inputs" function but it works on forms input fields only
    """
    if urlparse(u).path == "":
        u += "/"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += "#"
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
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
            ac = f.get("action")
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
            me = f.get("method")
            if not me:
                me = "get"
            if len(me) == 0:
                me = "get"
            me = me.lower()
            p = f.find_all("textarea")
            for r in p:
                if r.has_attr("name"):
                    s = r.get("name")
                    v = r.get("value")
                    if v == None:
                        v = ""
                if value == True:
                    y = s + ":" + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            p = f.find_all("input")
            for r in p:
                if r.has_attr("name"):
                    s = r.get("name")
                    v = r.get("value")
                    if v == None:
                        v = ""
                if value == True:
                    y = s + ":" + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            fom.append({"inputs": l, "action": ac, "method": me})
            l = []
    except Exception as e:
        pass
    return fom


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
        us = random.choice(ua)
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
                    v = r.renderContents().decode().split("&lt;/textarea&gt;")[0]
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
                    "inputs": sort_inputs(l),
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
        fom+=get_links_from_page_source(soup,u,'')
    return fom


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
                    v = r.renderContents().decode().split("&lt;/textarea&gt;")[0]
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
                    "inputs": sort_inputs(l),
                    "action": ac,
                    "enctype": enc_ty,
                    "method": me,
                    "hidden_values": h_v,
                    "is_url":False
                }
            )
            l = []
    except Exception as e:
        pass #raise(e)
    if include_links==True:
        fom+=get_links_from_page_source(soup,u,'')
    return fom


def cookies_to_dict(cookies):
    d = {}
    a = cookies.split(";")
    for x in a:
        if "=" in x:
            d.update({x.split("=")[0].strip(): x.split("=")[1].strip()})
    return d


def update_cookies(cookies, cook):
    c1 = {}
    c2 = {}
    if cookies:
        c1 = cookies_to_dict(cookies)
    if cook:
        c2 = cookies_to_dict(cook)
    c2.update(c1)
    cookie = ""
    for x in c2:
        cookie += x + "=" + c2[x] + ";"
    return cookie


def set_correct_cookies(new_cookies, cookie=None):
    if not cookie:
        cookie = ""
    if not new_cookies:
        new_cookies = ""
    if cookie and len(cookie) &gt; 0:
        if new_cookies and len(new_cookies) &gt; 0:
            cookies = update_cookies(new_cookies, cookie)
        else:
            cookies = cookie
    else:
        cookies = new_cookies
    return cookies


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
    cookies = set_correct_cookies(cook, cookie=cookie)
    form = forms_parser_text(url, r.text)[form_index]
    h = {"User-Agent": user_agent}
    if cookies and len(cookies.strip()) &gt; 0:
        h.update({"Cookie": cookies})
    h.update(headers)
    return (
        form_filler(
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
                                    files_upload[file_extension],
                                )
                            else:
                                x["value"] = (
                                    payload + "." + file_extension,
                                    files_upload[file_extension],
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
                                            files_upload[file_extension],
                                        )
                                    else:
                                        x["value"] = (
                                            "bane_test"
                                            + str(random.randint(100000, 999999))
                                            + "."
                                            + file_extension,
                                            files_upload[file_extension],
                                            mime_type,
                                        )
                                else:
                                    #if x['value']=='':
                                        if x["type"] == "number":
                                            x["value"] += str(random.randint(int(float(x.get('min',0))), int(float(x.get('max',9)))))
                                        elif x['type'] in ['text','password','search','textarea']:
                                            leng=random.randint(int(float(x.get('min',1))), int(float(x.get('max',64)))+1)
                                            for i in range(leng):
                                                x["value"] += random.choice(lis)
                                        elif x['type']=='email':
                                            leng=random.randint(int(float(x.get('min',1))), int(float(x.get('max',15)))-len(email_extension)+1)
                                            for i in range(leng):
                                                x["value"] += random.choice(string.ascii_lowercase)
                                            x["value"]+=email_extension
                                        elif x['type']=='tel':
                                            x["value"]=generate_random_phone_number(phone_pattern)
                                        elif x['type']=='url':
                                            x["value"]=generate_random_url()
                                        elif x['type']=='date':
                                            x["value"]=random_date(x['min'], x['max'])
                                        elif x['type']=='color':
                                            x['value']=generate_random_html_input_color()      
                            if x["type"] in ["select", "radio", "checkbox"]:
                                if len(x["value"]) == 0 or x["value"] == "":
                                    x["value"] = ""
                                    for i in range(auto_fill):
                                        x["value"] += random.choice(lis)
                                else:
                                    x["value"] = random.choice(x["value"])
    #print(form)
    return form


def get_login_form(url, text):
    a = forms_parser_text(url, text)
    for x in a:
        for i in x["inputs"]:
            if i["type"].lower().strip() == "password":
                return x
    raise Exception("No login form")


def set_login_form(url, text, username, password):
    a = get_login_form(url, text)
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


def get_upload_form(a):
    l=[]
    for x in a:
        for i in x["inputs"]:
            if i["type"].lower().strip() == "file":
                l.append(x)
    if l==[]:
        raise Exception("No file upload form")
    return l


def get_upload_form_text(url, text):
    l=[]
    a = forms_parser_text(url, text)
    for x in a:
        for i in x["inputs"]:
            if i["type"].lower().strip() == "file":
                l.append(x)
    if l==[]:
        raise Exception("No file upload form")
    return l


def crawl(
    u,
    timeout=10,
    html_comments=False,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
    headers={}
):
    """
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if bypass == True:
        u += "#"
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        ur = u.replace(u.split("/")[-1], "")
        """if ur[-1]=='/':
   ur=ur[:-1]"""
        index_link = 0
        h.update(
            {
                -1: (
                    "Source_url",
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all("a"):
            u = ur
            if a.has_attr("href"):
                try:
                    txt = a.text
                    a = str(a["href"])
                    if "://" not in a:
                        if a[0] == "/":
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + "/") and (a != u):
                            h.update(
                                {
                                    index_link: (
                                        txt,
                                        a,
                                        urlparse(a).path,
                                        [
                                            (x, furl.furl(a).args[x])
                                            for x in furl.furl(a).args
                                        ],
                                    )
                                }
                            )
                            index_link += 1
                except Exception as e:
                    pass
    except Exception as ex:
        pass
    return h


def crawl_text(u, text, html_comments=False):
    """
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    h={}
    try:
        c = text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        ur = u.replace(u.split("/")[-1], "")
        """if ur[-1]=='/':
   ur=ur[:-1]"""
        index_link = 0
        h.update(
            {
                -1: (
                    "Source_url",
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all("a"):
            u = ur
            if a.has_attr("href"):
                try:
                    txt = a.text
                    a = str(a["href"])
                    if "://" not in a:
                        if a[0] == "/":
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + "/") and (a != u):
                            h.update(
                                {
                                    index_link: (
                                        txt,
                                        a,
                                        urlparse(a).path,
                                        [
                                            (x, furl.furl(a).args[x])
                                            for x in furl.furl(a).args
                                        ],
                                    )
                                }
                            )
                            index_link += 1
                except Exception as e:
                    pass
    except Exception as ex:
        pass
    return h


def media(
    u,
    timeout=10,
    html_comments=False,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
    headers={}
):
    """
    this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram...).

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.media(url)

    &gt;&gt;&gt;bane.media(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    h = {}
    try:
        if bypass == True:
            u += "#"
        hea.update(headers)
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        ul = u.split("://")[1].split('"')[0]
        ur = ul.replace("www.", "")
        for a in soup.findAll("a"):
            try:
                if (
                    a.has_attr("href")
                    and (u not in a["href"])
                    and (ur not in a["href"])
                    and (a["href"][:4] == "http")
                ):
                    txt = a.text
                    if a["href"] not in h:
                        h.update({txt: a["href"]})
            except:
                pass
    except:
        pass
    return h


def subdomains_extract(
    u,
    timeout=10,
    html_comments=False,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
    headers={}
):
    """
    this function collects the subdomains found on the targeted webpage.

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.subdomains_extract(url)

    &gt;&gt;&gt;bane.subdomains_extract(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        if bypass == True:
            u += "#"
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        ul = u.split("://")[1].split("/")[0]
        soup = BeautifulSoup(c, "html.parser")
        for a in soup.findAll("a"):
            if (
                a.has_attr("href")
                and (ul.replace("www", "") in a["href"])
                and (ul not in a["href"])
                and (a["href"][:4] == "http")
            ):
                txt = a.text
                try:
                    hr = a["href"].split("://")[1].split("/")[0]
                    h.update({txt: hr})
                except Exception as e:
                    pass
    except Exception as e:
        pass
    return h




def extract_urls_from_js(js_content, base_url):
    # Regular expression to match URLs in JavaScript code
    url_pattern = re.compile(r'https?://\S+|/\S+')

    # Find all matches in the JavaScript code
    matches = re.findall(url_pattern, js_content)

    # Filter out URLs that start with '/'
    extracted_urls = [match if match.startswith('http') else base_url + match for match in matches]
    urls=[]
    for x in extracted_urls:
        x=x.split('"')[0]
        x=x.split(';')[0]
        x=x.split("'")[0]
        urls.append(x)
    return urls



def fetch_url(
        u,
        user_agent=None,
        timeout=10,
        proxy=None,
        cookie=None,
        headers={}
    ):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        return requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
    except:
        return ''



def extract_urls_from_js(js_content, base_url):
    # Regular expression to match URLs in JavaScript code
    url_pattern = re.compile(r'https?://\S+|/\S+')

    # Find all matches in the JavaScript code
    matches = re.findall(url_pattern, js_content)

    # Filter out URLs that start with '/'
    extracted_urls = [match if match.startswith('http') else base_url + match for match in matches]
    urls=[]
    for x in extracted_urls:
        x=x.split('"')[0]
        x=x.split(';')[0]
        x=x.split("'")[0]
        urls.append(x)
    return urls


def readable_js_code(code):
    return jsbeautifier.beautify(code)


def examine_js_code(u,
                    user_agent=None,
                    timeout=10,
                    proxy=None,
                    cookie=None,
                    headers={}
    ):
    domain=u.split('://')[1].split('/')[0]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        r= requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
        soup = BeautifulSoup(r, 'html.parser')
        script_tags = soup.find_all('script')
        code=''
        for script in script_tags:
            if script.has_attr('src'):
                pass
            else:
                code+=script.get_text()
        secrets=[]
        #print(code)
        secrets.append({'url':u,'secrets':extract_secrets_from_text(code)})#,'endpoints':extract_urls_from_js(code,u)})
        for script in script_tags:
            if script.has_attr('src'):
                url=urljoin(u,script['src'])
                url_domain=url.split('://')[1].split('/')[0]
                if extract_root_domain(url_domain)==extract_root_domain(domain):
                    #print(url_domain)
                    code=fetch_url(url,user_agent=user_agent,timeout=timeout,proxy=proxy,cookie=cookie,headers=headers)
                    secrets.append({'url':url,'secrets':extract_secrets_from_text(code)})#,'endpoints':extract_urls_from_js(code,url)})

    except Exception as ex:
        pass
    return [ x for x in secrets if len(list(x['secrets'].keys()))&gt;0]



def extract_secrets_from_text(js_content):
    tokens_dict = {}
    for key, pattern in js_exposed_secrets_regexs.items():
        #for pattern in x:
            l=[]
            try:
                if key=='firebase_config':
                    if matches:
                        for match in matches:
                            apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId, measurementId, vapidKey = match
                            d={
                                        "apiKey": apiKey,
                                        "authDomain": authDomain,
                                        "projectId": projectId,
                                        "storageBucket": storageBucket,
                                        "messagingSenderId": messagingSenderId,
                                        "appId": appId,
                                        "measurementId": measurementId,
                                        "vapidKey": vapidKey
                                    }
                            l.append(d)
                        tokens_dict[key] = l
                elif key=='json_configs':
                    matches=re.findall(pattern, js_content, re.DOTALL)
                    if matches:
                        l=[]
                        for match in matches:
                            if any(item in str(match).lower() for item in json_configs_signatures)==True and match not in l:
                                l.append(match)
                        if len(l)&gt;0:
                            tokens_dict[key] = l
                else:
                    if type(pattern)==tuple:
                        pattern=re.compile(pattern[0], re.IGNORECASE)
                    matches = re.findall(pattern, js_content)
                    if matches:
                        for x in matches:
                            if '"{}"'.format(x) in js_content or "'{}'".format(x) in js_content or "={}".format(x) in js_content or "= {}".format(x) in js_content or ":{}".format(x) in js_content or ": {}".format(x) in js_content:
                                l.append(x)
                        l=list(set(l))
                        if len(l)&gt;0:
                            tokens_dict[key] = l
            except Exception as ex:
                pass
    return tokens_dict




def generate_human_poc(data):
    if "is_url" not in data:
        raise ValueError("The 'is_url' key is missing in the input data")

    if data["is_url"]:
        # If is_url is True, generate a URL
        url = data.get("action", "")
        if not url:
            raise ValueError("Missing 'action' key for URL generation")
        
        query_parameters = []
        for input_field in data.get("inputs", []):
            name = input_field.get("name", "")
            value = input_field.get("value", "")
            query_parameters.append("{}={}".format(name,value))
        
        if query_parameters:
            url += "?" + "&amp;".join(query_parameters)

        return url

    else:
        # If is_url is False, generate an HTML form
        form_id = data.get("id", "")
        form_method = data.get("method", "post")
        form_action = data.get("action", "")
        form_enctype = data.get("enctype", "application/x-www-form-urlencoded")

        inputs = ""
        for input_field in data.get("inputs", []):
            name = input_field.get("name", "")
            value = input_field.get("value", "")
            input_type = input_field.get("type", "text")
            required = "required" if input_field.get("required", False) else ""
            input_element = "&lt;input type='{}' name='{}' value='{}' {}&gt;".format(input_type,name,value,required)
            inputs += input_element

        html_form = """
        &lt;form id='{}' method='{}' action='{}' enctype='{}'&gt;
            {}
        &lt;/form&gt;
        """.format(form_id,form_method,form_action,form_enctype,inputs)
        return html_form</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.utils.pager.cookies_to_dict"><code class="name flex">
<span>def <span class="ident">cookies_to_dict</span></span>(<span>cookies)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def cookies_to_dict(cookies):
    d = {}
    a = cookies.split(";")
    for x in a:
        if "=" in x:
            d.update({x.split("=")[0].strip(): x.split("=")[1].strip()})
    return d</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.crawl"><code class="name flex">
<span>def <span class="ident">crawl</span></span>(<span>u, timeout=10, html_comments=False, user_agent=None, bypass=False, proxy=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers</p>
<p>the function takes those arguments:</p>
<p>u: the targeted link
timeout: (set by default to 10) timeout flag for the request
bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
url='http://www.example.com'
bane.crawl(url)</p>
<p>bane.crawl(url,bypass=True)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crawl(
    u,
    timeout=10,
    html_comments=False,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
    headers={}
):
    """
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if bypass == True:
        u += "#"
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        ur = u.replace(u.split("/")[-1], "")
        """if ur[-1]=='/':
   ur=ur[:-1]"""
        index_link = 0
        h.update(
            {
                -1: (
                    "Source_url",
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all("a"):
            u = ur
            if a.has_attr("href"):
                try:
                    txt = a.text
                    a = str(a["href"])
                    if "://" not in a:
                        if a[0] == "/":
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + "/") and (a != u):
                            h.update(
                                {
                                    index_link: (
                                        txt,
                                        a,
                                        urlparse(a).path,
                                        [
                                            (x, furl.furl(a).args[x])
                                            for x in furl.furl(a).args
                                        ],
                                    )
                                }
                            )
                            index_link += 1
                except Exception as e:
                    pass
    except Exception as ex:
        pass
    return h</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.crawl_text"><code class="name flex">
<span>def <span class="ident">crawl_text</span></span>(<span>u, text, html_comments=False)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers</p>
<p>the function takes those arguments:</p>
<p>u: the targeted link
timeout: (set by default to 10) timeout flag for the request
bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
url='http://www.example.com'
bane.crawl(url)</p>
<p>bane.crawl(url,bypass=True)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crawl_text(u, text, html_comments=False):
    """
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if u.split("?")[0][-1] != "/" and "." not in u.split("?")[0].rsplit("/", 1)[-1]:
        u = u.replace("?", "/?")
    h={}
    try:
        c = text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        ur = u.replace(u.split("/")[-1], "")
        """if ur[-1]=='/':
   ur=ur[:-1]"""
        index_link = 0
        h.update(
            {
                -1: (
                    "Source_url",
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all("a"):
            u = ur
            if a.has_attr("href"):
                try:
                    txt = a.text
                    a = str(a["href"])
                    if "://" not in a:
                        if a[0] == "/":
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + "/") and (a != u):
                            h.update(
                                {
                                    index_link: (
                                        txt,
                                        a,
                                        urlparse(a).path,
                                        [
                                            (x, furl.furl(a).args[x])
                                            for x in furl.furl(a).args
                                        ],
                                    )
                                }
                            )
                            index_link += 1
                except Exception as e:
                    pass
    except Exception as ex:
        pass
    return h</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.examine_js_code"><code class="name flex">
<span>def <span class="ident">examine_js_code</span></span>(<span>u, user_agent=None, timeout=10, proxy=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def examine_js_code(u,
                    user_agent=None,
                    timeout=10,
                    proxy=None,
                    cookie=None,
                    headers={}
    ):
    domain=u.split('://')[1].split('/')[0]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        r= requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
        soup = BeautifulSoup(r, 'html.parser')
        script_tags = soup.find_all('script')
        code=''
        for script in script_tags:
            if script.has_attr('src'):
                pass
            else:
                code+=script.get_text()
        secrets=[]
        #print(code)
        secrets.append({'url':u,'secrets':extract_secrets_from_text(code)})#,'endpoints':extract_urls_from_js(code,u)})
        for script in script_tags:
            if script.has_attr('src'):
                url=urljoin(u,script['src'])
                url_domain=url.split('://')[1].split('/')[0]
                if extract_root_domain(url_domain)==extract_root_domain(domain):
                    #print(url_domain)
                    code=fetch_url(url,user_agent=user_agent,timeout=timeout,proxy=proxy,cookie=cookie,headers=headers)
                    secrets.append({'url':url,'secrets':extract_secrets_from_text(code)})#,'endpoints':extract_urls_from_js(code,url)})

    except Exception as ex:
        pass
    return [ x for x in secrets if len(list(x['secrets'].keys()))&gt;0]</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.extract_secrets_from_text"><code class="name flex">
<span>def <span class="ident">extract_secrets_from_text</span></span>(<span>js_content)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def extract_secrets_from_text(js_content):
    tokens_dict = {}
    for key, pattern in js_exposed_secrets_regexs.items():
        #for pattern in x:
            l=[]
            try:
                if key=='firebase_config':
                    if matches:
                        for match in matches:
                            apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId, measurementId, vapidKey = match
                            d={
                                        "apiKey": apiKey,
                                        "authDomain": authDomain,
                                        "projectId": projectId,
                                        "storageBucket": storageBucket,
                                        "messagingSenderId": messagingSenderId,
                                        "appId": appId,
                                        "measurementId": measurementId,
                                        "vapidKey": vapidKey
                                    }
                            l.append(d)
                        tokens_dict[key] = l
                elif key=='json_configs':
                    matches=re.findall(pattern, js_content, re.DOTALL)
                    if matches:
                        l=[]
                        for match in matches:
                            if any(item in str(match).lower() for item in json_configs_signatures)==True and match not in l:
                                l.append(match)
                        if len(l)&gt;0:
                            tokens_dict[key] = l
                else:
                    if type(pattern)==tuple:
                        pattern=re.compile(pattern[0], re.IGNORECASE)
                    matches = re.findall(pattern, js_content)
                    if matches:
                        for x in matches:
                            if '"{}"'.format(x) in js_content or "'{}'".format(x) in js_content or "={}".format(x) in js_content or "= {}".format(x) in js_content or ":{}".format(x) in js_content or ": {}".format(x) in js_content:
                                l.append(x)
                        l=list(set(l))
                        if len(l)&gt;0:
                            tokens_dict[key] = l
            except Exception as ex:
                pass
    return tokens_dict</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.extract_urls_from_js"><code class="name flex">
<span>def <span class="ident">extract_urls_from_js</span></span>(<span>js_content, base_url)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def extract_urls_from_js(js_content, base_url):
    # Regular expression to match URLs in JavaScript code
    url_pattern = re.compile(r'https?://\S+|/\S+')

    # Find all matches in the JavaScript code
    matches = re.findall(url_pattern, js_content)

    # Filter out URLs that start with '/'
    extracted_urls = [match if match.startswith('http') else base_url + match for match in matches]
    urls=[]
    for x in extracted_urls:
        x=x.split('"')[0]
        x=x.split(';')[0]
        x=x.split("'")[0]
        urls.append(x)
    return urls</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.fetch_url"><code class="name flex">
<span>def <span class="ident">fetch_url</span></span>(<span>u, user_agent=None, timeout=10, proxy=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def fetch_url(
        u,
        user_agent=None,
        timeout=10,
        proxy=None,
        cookie=None,
        headers={}
    ):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        return requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
    except:
        return ''</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.form_filler"><code class="name flex">
<span>def <span class="ident">form_filler</span></span>(<span>form, param, payload, file_extension='png', email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', dont_change={}, number=(1, 9), auto_fill=10, leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def form_filler(
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
                                    files_upload[file_extension],
                                )
                            else:
                                x["value"] = (
                                    payload + "." + file_extension,
                                    files_upload[file_extension],
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
                                            files_upload[file_extension],
                                        )
                                    else:
                                        x["value"] = (
                                            "bane_test"
                                            + str(random.randint(100000, 999999))
                                            + "."
                                            + file_extension,
                                            files_upload[file_extension],
                                            mime_type,
                                        )
                                else:
                                    #if x['value']=='':
                                        if x["type"] == "number":
                                            x["value"] += str(random.randint(int(float(x.get('min',0))), int(float(x.get('max',9)))))
                                        elif x['type'] in ['text','password','search','textarea']:
                                            leng=random.randint(int(float(x.get('min',1))), int(float(x.get('max',64)))+1)
                                            for i in range(leng):
                                                x["value"] += random.choice(lis)
                                        elif x['type']=='email':
                                            leng=random.randint(int(float(x.get('min',1))), int(float(x.get('max',15)))-len(email_extension)+1)
                                            for i in range(leng):
                                                x["value"] += random.choice(string.ascii_lowercase)
                                            x["value"]+=email_extension
                                        elif x['type']=='tel':
                                            x["value"]=generate_random_phone_number(phone_pattern)
                                        elif x['type']=='url':
                                            x["value"]=generate_random_url()
                                        elif x['type']=='date':
                                            x["value"]=random_date(x['min'], x['max'])
                                        elif x['type']=='color':
                                            x['value']=generate_random_html_input_color()      
                            if x["type"] in ["select", "radio", "checkbox"]:
                                if len(x["value"]) == 0 or x["value"] == "":
                                    x["value"] = ""
                                    for i in range(auto_fill):
                                        x["value"] += random.choice(lis)
                                else:
                                    x["value"] = random.choice(x["value"])
    #print(form)
    return form</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.forms"><code class="name flex">
<span>def <span class="ident">forms</span></span>(<span>u, value=True, html_comments=False, user_agent=None, timeout=10, bypass=False, proxy=None, cookie=None)</span>
</code></dt>
<dd>
<div class="desc"><p>same as "inputs" function but it works on forms input fields only</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def forms(
    u,
    value=True,
    html_comments=False,
    user_agent=None,
    timeout=10,
    bypass=False,
    proxy=None,
    cookie=None,
):
    """
    same as "inputs" function but it works on forms input fields only
    """
    if urlparse(u).path == "":
        u += "/"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += "#"
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
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
            ac = f.get("action")
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
            me = f.get("method")
            if not me:
                me = "get"
            if len(me) == 0:
                me = "get"
            me = me.lower()
            p = f.find_all("textarea")
            for r in p:
                if r.has_attr("name"):
                    s = r.get("name")
                    v = r.get("value")
                    if v == None:
                        v = ""
                if value == True:
                    y = s + ":" + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            p = f.find_all("input")
            for r in p:
                if r.has_attr("name"):
                    s = r.get("name")
                    v = r.get("value")
                    if v == None:
                        v = ""
                if value == True:
                    y = s + ":" + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            fom.append({"inputs": l, "action": ac, "method": me})
            l = []
    except Exception as e:
        pass
    return fom</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.forms_parser"><code class="name flex">
<span>def <span class="ident">forms_parser</span></span>(<span>u, html_comments=False, user_agent=None, timeout=10, bypass=False, proxy=None, cookie=None, include_links=True, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>same as "forms" function but it return detailed information about all forms in a given page</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def forms_parser(
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
        us = random.choice(ua)
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
                    v = r.renderContents().decode().split("&lt;/textarea&gt;")[0]
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
                    "inputs": sort_inputs(l),
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
        fom+=get_links_from_page_source(soup,u,'')
    return fom</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.forms_parser_text"><code class="name flex">
<span>def <span class="ident">forms_parser_text</span></span>(<span>u, text, html_comments=False, include_links=True)</span>
</code></dt>
<dd>
<div class="desc"><p>same as "forms" function but it return detailed information about all forms in a given page</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def forms_parser_text(u, text, html_comments=False,include_links=True):
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
                    v = r.renderContents().decode().split("&lt;/textarea&gt;")[0]
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
                    "inputs": sort_inputs(l),
                    "action": ac,
                    "enctype": enc_ty,
                    "method": me,
                    "hidden_values": h_v,
                    "is_url":False
                }
            )
            l = []
    except Exception as e:
        pass #raise(e)
    if include_links==True:
        fom+=get_links_from_page_source(soup,u,'')
    return fom</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.generate_human_poc"><code class="name flex">
<span>def <span class="ident">generate_human_poc</span></span>(<span>data)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def generate_human_poc(data):
    if "is_url" not in data:
        raise ValueError("The 'is_url' key is missing in the input data")

    if data["is_url"]:
        # If is_url is True, generate a URL
        url = data.get("action", "")
        if not url:
            raise ValueError("Missing 'action' key for URL generation")
        
        query_parameters = []
        for input_field in data.get("inputs", []):
            name = input_field.get("name", "")
            value = input_field.get("value", "")
            query_parameters.append("{}={}".format(name,value))
        
        if query_parameters:
            url += "?" + "&amp;".join(query_parameters)

        return url

    else:
        # If is_url is False, generate an HTML form
        form_id = data.get("id", "")
        form_method = data.get("method", "post")
        form_action = data.get("action", "")
        form_enctype = data.get("enctype", "application/x-www-form-urlencoded")

        inputs = ""
        for input_field in data.get("inputs", []):
            name = input_field.get("name", "")
            value = input_field.get("value", "")
            input_type = input_field.get("type", "text")
            required = "required" if input_field.get("required", False) else ""
            input_element = "&lt;input type='{}' name='{}' value='{}' {}&gt;".format(input_type,name,value,required)
            inputs += input_element

        html_form = """
        &lt;form id='{}' method='{}' action='{}' enctype='{}'&gt;
            {}
        &lt;/form&gt;
        """.format(form_id,form_method,form_action,form_enctype,inputs)
        return html_form</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.generate_random_html_input_color"><code class="name flex">
<span>def <span class="ident">generate_random_html_input_color</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def generate_random_html_input_color():
    # Generate random RGB values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # Convert RGB to hexadecimal
    color_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return color_hex</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.generate_random_phone_number"><code class="name flex">
<span>def <span class="ident">generate_random_phone_number</span></span>(<span>pattern)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def generate_random_phone_number(pattern):
    phone_number = ""
    for char in pattern:
        if char == "X":
            random_digit = str(random.randint(0, 9))
            phone_number += random_digit
        else:
            phone_number += char
    return phone_number</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.generate_random_url"><code class="name flex">
<span>def <span class="ident">generate_random_url</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def generate_random_url():
    protocols = ["http", "https"]
    protocol = random.choice(protocols)
    domain = random.choice(domainl)
    return "{}://{}/".format(protocol,domain)</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.get_links_from_page_source"><code class="name flex">
<span>def <span class="ident">get_links_from_page_source</span></span>(<span>soup, url, url_id)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_links_from_page_source(soup,url,url_id):
    if url.endswith('/')==False:
        url+='/'
    domain=url.split('/')[0] if url.startswith('http')==False else url.split('://')[1].split('/')[0]
    l=soup.find_all('a')
    links=[{'url':x['href'].replace('&amp;amp;','&amp;'),'id':x.get('id','')} for x in l if x.has_attr('href')]
    media_tags = soup.find_all(['img', 'audio', 'video', 'source','embed'])
    links+=[{'url':x['src'].replace('&amp;amp;','&amp;'),'id':x.get('id','') } for x in media_tags if x.has_attr('src')]
    links.append({'url':url,'id':url_id})
    #print(links)
    #links_list=[]
    root_links=[]
    forms=[]
    for l in links:
        x=l['url']
        l_id=l['id']
        if '?' in x and x.split('?')[0] not in root_links:
            a=urljoin(url, x)
            #print(a)
            if a.startswith(url.split(domain)[0]+domain)==True:
                forms.append(url_to_get_form(a,l_id))
                root_links.append(x.split('?')[0])
    return forms</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.get_login_form"><code class="name flex">
<span>def <span class="ident">get_login_form</span></span>(<span>url, text)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_login_form(url, text):
    a = forms_parser_text(url, text)
    for x in a:
        for i in x["inputs"]:
            if i["type"].lower().strip() == "password":
                return x
    raise Exception("No login form")</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.get_upload_form"><code class="name flex">
<span>def <span class="ident">get_upload_form</span></span>(<span>a)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_upload_form(a):
    l=[]
    for x in a:
        for i in x["inputs"]:
            if i["type"].lower().strip() == "file":
                l.append(x)
    if l==[]:
        raise Exception("No file upload form")
    return l</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.get_upload_form_text"><code class="name flex">
<span>def <span class="ident">get_upload_form_text</span></span>(<span>url, text)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_upload_form_text(url, text):
    l=[]
    a = forms_parser_text(url, text)
    for x in a:
        for i in x["inputs"]:
            if i["type"].lower().strip() == "file":
                l.append(x)
    if l==[]:
        raise Exception("No file upload form")
    return l</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.inputs"><code class="name flex">
<span>def <span class="ident">inputs</span></span>(<span>u, html_comments=False, value=False, timeout=10, user_agent=None, bypass=False, proxy=None, cookie=None)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to get the names and values of input fields on a given webpage to scan.</p>
<p>it takes 4 arguments:</p>
<p>u: the page's link (<a href="http://...">http://...</a>)
value: (set by default to: False) to return the value of the fields set it to:True then the field's name and value will be string of 2
values sperated by ":"
timeout: (set by default to: 10) timeout flag for the request
bypass: (set by default to: False) to bypass anti-crawlers</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
link='http://www.example.com'
bane.inputs(link)
['email','password','rememberme']
a=bane.inputs(link,value=True)
['email','password','rememberme:yes','rememberme:no']</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def inputs(
    u,
    html_comments=False,
    value=False,
    timeout=10,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
):
    """
     this function is to get the names and values of input fields on a given webpage to scan.

     it takes 4 arguments:

     u: the page's link (http://...)
     value: (set by default to: False) to return the value of the fields set it to:True then the field's name and value will be string of 2
     values sperated by ":"
     timeout: (set by default to: 10) timeout flag for the request
     bypass: (set by default to: False) to bypass anti-crawlers

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;link='http://www.example.com'
    &gt;&gt;&gt;bane.inputs(link)
    ['email','password','rememberme']
    &gt;&gt;&gt;a=bane.inputs(link,value=True)
    ['email','password','rememberme:yes','rememberme:no']

    """
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += "#"
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    l = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        p = soup.find_all("textarea")
        for r in p:
            if r.has_attr("name"):
                s = r.get("name")
                v = r.get("value")
                if v == None:
                    v = ""
            if value == True:
                y = s + ":" + v
            else:
                y = s
            if y not in l:
                l.append(y)
        p = soup.find_all("input")
        for r in p:
            v = ""
            if r.has_attr("name"):
                s = str(r)
                s = s.split('name="')[1].split(",")[0]
                s = s.split('"')[0].split(",")[0]
                if r.has_attr("value") and (value == True):
                    v = str(r)
                    v = v.split('value="')[1].split(",")[0]
                    v = v.split('"')[0].split(",")[0]
            if value == True:
                y = s + ":" + v
            else:
                y = s
            if y not in l:
                l.append(y)
    except Exception as e:
        pass
    return l</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.media"><code class="name flex">
<span>def <span class="ident">media</span></span>(<span>u, timeout=10, html_comments=False, user_agent=None, bypass=False, proxy=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram…).</p>
<p>the function takes those arguments:</p>
<p>u: the targeted link
timeout: (set by default to 10) timeout flag for the request
bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
url='http://www.example.com'
bane.media(url)</p>
<p>bane.media(url,bypass=True)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def media(
    u,
    timeout=10,
    html_comments=False,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
    headers={}
):
    """
    this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram...).

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.media(url)

    &gt;&gt;&gt;bane.media(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    h = {}
    try:
        if bypass == True:
            u += "#"
        hea.update(headers)
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, "html.parser")
        ul = u.split("://")[1].split('"')[0]
        ur = ul.replace("www.", "")
        for a in soup.findAll("a"):
            try:
                if (
                    a.has_attr("href")
                    and (u not in a["href"])
                    and (ur not in a["href"])
                    and (a["href"][:4] == "http")
                ):
                    txt = a.text
                    if a["href"] not in h:
                        h.update({txt: a["href"]})
            except:
                pass
    except:
        pass
    return h</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.random_date"><code class="name flex">
<span>def <span class="ident">random_date</span></span>(<span>start_date, end_date)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def random_date(start_date, end_date):
    if start_date==end_date:
        return start_date
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d")</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.readable_js_code"><code class="name flex">
<span>def <span class="ident">readable_js_code</span></span>(<span>code)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def readable_js_code(code):
    return jsbeautifier.beautify(code)</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.remove_html_comments"><code class="name flex">
<span>def <span class="ident">remove_html_comments</span></span>(<span>text)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def remove_html_comments(text):
    return re.sub(r"&lt;!--(.|\s|\n)*?--&gt;", "", text, flags=re.DOTALL)</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.set_correct_cookies"><code class="name flex">
<span>def <span class="ident">set_correct_cookies</span></span>(<span>new_cookies, cookie=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def set_correct_cookies(new_cookies, cookie=None):
    if not cookie:
        cookie = ""
    if not new_cookies:
        new_cookies = ""
    if cookie and len(cookie) &gt; 0:
        if new_cookies and len(new_cookies) &gt; 0:
            cookies = update_cookies(new_cookies, cookie)
        else:
            cookies = cookie
    else:
        cookies = new_cookies
    return cookies</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.set_login_form"><code class="name flex">
<span>def <span class="ident">set_login_form</span></span>(<span>url, text, username, password)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def set_login_form(url, text, username, password):
    a = get_login_form(url, text)
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
    return [d, a["action"]]</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.set_up_injection"><code class="name flex">
<span>def <span class="ident">set_up_injection</span></span>(<span>url, form_index, parameter, payload, cookie, user_agent, proxy, timeout, auto_fill, file_extension='png', email_extension='@gmail.com', phone_pattern='XXX-XXX-XXXX', dont_change={}, number=(1, 9), leave_empty=[], dont_send=[], mime_type=None, predefined_inputs={}, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def set_up_injection(
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
    cookies = set_correct_cookies(cook, cookie=cookie)
    form = forms_parser_text(url, r.text)[form_index]
    h = {"User-Agent": user_agent}
    if cookies and len(cookies.strip()) &gt; 0:
        h.update({"Cookie": cookies})
    h.update(headers)
    return (
        form_filler(
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
    )</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.sort_inputs"><code class="name flex">
<span>def <span class="ident">sort_inputs</span></span>(<span>l)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def sort_inputs(l):
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
    return d</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.spider_url"><code class="name flex">
<span>def <span class="ident">spider_url</span></span>(<span>base_url, include_id=False, max_pages=50, timeout=15, cookie=None, user_agent=None, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def spider_url(base_url, include_id=False,max_pages=50,timeout=15,cookie=None,user_agent=None,proxy=None,headers={}):
    domain=base_url.split('://')[1].split('/')[0]
    h={}
    if cookie:
        h.update({'Cookie':cookie})
    if user_agent:
        h.update({'User-Agent':user_agent})
    else:
        h.update({'User-Agent':random.choice(ua)})
    h.update(headers)
    visited_urls = set()
    urls_to_visit = [base_url]
    collected_urls = set()
    root_urls=[]

    while urls_to_visit and len(collected_urls) &lt; max_pages:
        url = urls_to_visit.pop(0)
        try:
            response = requests.Session().get(url,headers=h,timeout=timeout,proxies=proxy,verify=False)
            response.raise_for_status()  # Check for any request errors

            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract all links from the page
            for anchor_tag in soup.find_all('a', href=True):
                href = anchor_tag['href']
                absolute_url = urljoin(url, href)
                try:
                    this_domain=absolute_url.split('://')[1].split('/')[0]
                except:
                    this_domain=''

                if absolute_url not in visited_urls and absolute_url.split('?')[0].split('#')[0] not in root_urls and domain == this_domain:
                    visited_urls.add(absolute_url)
                    urls_to_visit.append(absolute_url)
                    root_urls.append(absolute_url.split('?')[0].split('#')[0])
            if include_id==True:
                collected_urls.add({'url':url,'id':anchor_tag.get('id','')})
            else:
                collected_urls.add(url)
            #print(len(collected_urls))

        except requests.exceptions.RequestException as e:
            print("Error fetching URL: {}".format(e))

    return list(collected_urls)</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.subdomains_extract"><code class="name flex">
<span>def <span class="ident">subdomains_extract</span></span>(<span>u, timeout=10, html_comments=False, user_agent=None, bypass=False, proxy=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function collects the subdomains found on the targeted webpage.</p>
<p>the function takes those arguments:</p>
<p>u: the targeted link
timeout: (set by default to 10) timeout flag for the request
bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)</p>
<p>usage:</p>
<blockquote>
<blockquote>
<blockquote>
<p>import bane
url='http://www.example.com'
bane.subdomains_extract(url)</p>
<p>bane.subdomains_extract(url,bypass=True)</p>
</blockquote>
</blockquote>
</blockquote></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def subdomains_extract(
    u,
    timeout=10,
    html_comments=False,
    user_agent=None,
    bypass=False,
    proxy=None,
    cookie=None,
    headers={}
):
    """
    this function collects the subdomains found on the targeted webpage.

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url='http://www.example.com'
    &gt;&gt;&gt;bane.subdomains_extract(url)

    &gt;&gt;&gt;bane.subdomains_extract(url,bypass=True)"""
    if urlparse(u).path == "":
        u += "/"
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if cookie:
        hea = {"User-Agent": us, "Cookie": cookie}
    else:
        hea = {"User-Agent": us}
    hea.update(headers)
    try:
        if bypass == True:
            u += "#"
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        ul = u.split("://")[1].split("/")[0]
        soup = BeautifulSoup(c, "html.parser")
        for a in soup.findAll("a"):
            if (
                a.has_attr("href")
                and (ul.replace("www", "") in a["href"])
                and (ul not in a["href"])
                and (a["href"][:4] == "http")
            ):
                txt = a.text
                try:
                    hr = a["href"].split("://")[1].split("/")[0]
                    h.update({txt: hr})
                except Exception as e:
                    pass
    except Exception as e:
        pass
    return h</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.update_cookies"><code class="name flex">
<span>def <span class="ident">update_cookies</span></span>(<span>cookies, cook)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def update_cookies(cookies, cook):
    c1 = {}
    c2 = {}
    if cookies:
        c1 = cookies_to_dict(cookies)
    if cook:
        c2 = cookies_to_dict(cook)
    c2.update(c1)
    cookie = ""
    for x in c2:
        cookie += x + "=" + c2[x] + ";"
    return cookie</code></pre>
</details>
</dd>
<dt id="bane.utils.pager.url_to_get_form"><code class="name flex">
<span>def <span class="ident">url_to_get_form</span></span>(<span>u, url_id)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def url_to_get_form(u,url_id):
    #print('&amp;'.join(u.split('?')[1:]).replace('?','&amp;').split('&amp;'))
    #print(u.split('?')[1].split('&amp;'))
    inputs=[]
    for x in '&amp;'.join(u.split('?')[1:]).replace('?','&amp;').split('&amp;'):
        try:
            inputs.append({'name':x.split('=')[0],'type':'text','value':x.split('=')[1]})
        except:
            inputs.append({'name':x.split('=')[0],'type':'text','value':''})
    #inputs=[ {'name':x.split('=')[0],'type':'text','value':x.split('=')[1]} for x in u.split('?')[1].split('&amp;')]
    return {
                    "inputs": inputs,
                    "action": u.split('?')[0],
                    "enctype": 'application/x-www-form-urlencoded',
                    "method": 'get',
                    "id":url_id,
                    "hidden_values": [],
                    "is_url":True
                }</code></pre>
</details>
</dd>
</dl>
</section>
<section>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3>Super-module</h3>
<ul>
<li><code><a href="index.md" title="bane.utils">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.utils.pager.cookies_to_dict" title="bane.utils.pager.cookies_to_dict">cookies_to_dict</a></code></li>
<li><code><a href="#bane.utils.pager.crawl" title="bane.utils.pager.crawl">crawl</a></code></li>
<li><code><a href="#bane.utils.pager.crawl_text" title="bane.utils.pager.crawl_text">crawl_text</a></code></li>
<li><code><a href="#bane.utils.pager.examine_js_code" title="bane.utils.pager.examine_js_code">examine_js_code</a></code></li>
<li><code><a href="#bane.utils.pager.extract_secrets_from_text" title="bane.utils.pager.extract_secrets_from_text">extract_secrets_from_text</a></code></li>
<li><code><a href="#bane.utils.pager.extract_urls_from_js" title="bane.utils.pager.extract_urls_from_js">extract_urls_from_js</a></code></li>
<li><code><a href="#bane.utils.pager.fetch_url" title="bane.utils.pager.fetch_url">fetch_url</a></code></li>
<li><code><a href="#bane.utils.pager.form_filler" title="bane.utils.pager.form_filler">form_filler</a></code></li>
<li><code><a href="#bane.utils.pager.forms" title="bane.utils.pager.forms">forms</a></code></li>
<li><code><a href="#bane.utils.pager.forms_parser" title="bane.utils.pager.forms_parser">forms_parser</a></code></li>
<li><code><a href="#bane.utils.pager.forms_parser_text" title="bane.utils.pager.forms_parser_text">forms_parser_text</a></code></li>
<li><code><a href="#bane.utils.pager.generate_human_poc" title="bane.utils.pager.generate_human_poc">generate_human_poc</a></code></li>
<li><code><a href="#bane.utils.pager.generate_random_html_input_color" title="bane.utils.pager.generate_random_html_input_color">generate_random_html_input_color</a></code></li>
<li><code><a href="#bane.utils.pager.generate_random_phone_number" title="bane.utils.pager.generate_random_phone_number">generate_random_phone_number</a></code></li>
<li><code><a href="#bane.utils.pager.generate_random_url" title="bane.utils.pager.generate_random_url">generate_random_url</a></code></li>
<li><code><a href="#bane.utils.pager.get_links_from_page_source" title="bane.utils.pager.get_links_from_page_source">get_links_from_page_source</a></code></li>
<li><code><a href="#bane.utils.pager.get_login_form" title="bane.utils.pager.get_login_form">get_login_form</a></code></li>
<li><code><a href="#bane.utils.pager.get_upload_form" title="bane.utils.pager.get_upload_form">get_upload_form</a></code></li>
<li><code><a href="#bane.utils.pager.get_upload_form_text" title="bane.utils.pager.get_upload_form_text">get_upload_form_text</a></code></li>
<li><code><a href="#bane.utils.pager.inputs" title="bane.utils.pager.inputs">inputs</a></code></li>
<li><code><a href="#bane.utils.pager.media" title="bane.utils.pager.media">media</a></code></li>
<li><code><a href="#bane.utils.pager.random_date" title="bane.utils.pager.random_date">random_date</a></code></li>
<li><code><a href="#bane.utils.pager.readable_js_code" title="bane.utils.pager.readable_js_code">readable_js_code</a></code></li>
<li><code><a href="#bane.utils.pager.remove_html_comments" title="bane.utils.pager.remove_html_comments">remove_html_comments</a></code></li>
<li><code><a href="#bane.utils.pager.set_correct_cookies" title="bane.utils.pager.set_correct_cookies">set_correct_cookies</a></code></li>
<li><code><a href="#bane.utils.pager.set_login_form" title="bane.utils.pager.set_login_form">set_login_form</a></code></li>
<li><code><a href="#bane.utils.pager.set_up_injection" title="bane.utils.pager.set_up_injection">set_up_injection</a></code></li>
<li><code><a href="#bane.utils.pager.sort_inputs" title="bane.utils.pager.sort_inputs">sort_inputs</a></code></li>
<li><code><a href="#bane.utils.pager.spider_url" title="bane.utils.pager.spider_url">spider_url</a></code></li>
<li><code><a href="#bane.utils.pager.subdomains_extract" title="bane.utils.pager.subdomains_extract">subdomains_extract</a></code></li>
<li><code><a href="#bane.utils.pager.update_cookies" title="bane.utils.pager.update_cookies">update_cookies</a></code></li>
<li><code><a href="#bane.utils.pager.url_to_get_form" title="bane.utils.pager.url_to_get_form">url_to_get_form</a></code></li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>