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
    protocols = [&#34;http&#34;, &#34;https&#34;]
    protocol = random.choice(protocols)
    domain = random.choice(domainl)
    return &#34;{}://{}/&#34;.format(protocol,domain)


def generate_random_phone_number(pattern):
    phone_number = &#34;&#34;
    for char in pattern:
        if char == &#34;X&#34;:
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
    color_hex = &#34;#{:02X}{:02X}{:02X}&#34;.format(r, g, b)
    return color_hex


def random_date(start_date, end_date):
    if start_date==end_date:
        return start_date
    start_date = datetime.datetime.strptime(start_date, &#34;%Y-%m-%d&#34;)
    end_date = datetime.datetime.strptime(end_date, &#34;%Y-%m-%d&#34;)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime(&#34;%Y-%m-%d&#34;)


def spider_url(base_url, include_id=False,max_pages=50,timeout=15,cookie=None,user_agent=None,proxy=None,headers={}):
    domain=base_url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    h={}
    if cookie:
        h.update({&#39;Cookie&#39;:cookie})
    if user_agent:
        h.update({&#39;User-Agent&#39;:user_agent})
    else:
        h.update({&#39;User-Agent&#39;:random.choice(ua)})
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
            soup = BeautifulSoup(response.content, &#39;html.parser&#39;)

            # Extract all links from the page
            for anchor_tag in soup.find_all(&#39;a&#39;, href=True):
                href = anchor_tag[&#39;href&#39;]
                absolute_url = urljoin(url, href)
                try:
                    this_domain=absolute_url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
                except:
                    this_domain=&#39;&#39;

                if absolute_url not in visited_urls and absolute_url.split(&#39;?&#39;)[0].split(&#39;#&#39;)[0] not in root_urls and domain == this_domain:
                    visited_urls.add(absolute_url)
                    urls_to_visit.append(absolute_url)
                    root_urls.append(absolute_url.split(&#39;?&#39;)[0].split(&#39;#&#39;)[0])
            if include_id==True:
                collected_urls.add({&#39;url&#39;:url,&#39;id&#39;:anchor_tag.get(&#39;id&#39;,&#39;&#39;)})
            else:
                collected_urls.add(url)
            #print(len(collected_urls))

        except requests.exceptions.RequestException as e:
            print(&#34;Error fetching URL: {}&#34;.format(e))

    return list(collected_urls)



def url_to_get_form(u,url_id):
    #print(&#39;&amp;&#39;.join(u.split(&#39;?&#39;)[1:]).replace(&#39;?&#39;,&#39;&amp;&#39;).split(&#39;&amp;&#39;))
    #print(u.split(&#39;?&#39;)[1].split(&#39;&amp;&#39;))
    inputs=[]
    for x in &#39;&amp;&#39;.join(u.split(&#39;?&#39;)[1:]).replace(&#39;?&#39;,&#39;&amp;&#39;).split(&#39;&amp;&#39;):
        try:
            inputs.append({&#39;name&#39;:x.split(&#39;=&#39;)[0],&#39;type&#39;:&#39;text&#39;,&#39;value&#39;:x.split(&#39;=&#39;)[1]})
        except:
            inputs.append({&#39;name&#39;:x.split(&#39;=&#39;)[0],&#39;type&#39;:&#39;text&#39;,&#39;value&#39;:&#39;&#39;})
    #inputs=[ {&#39;name&#39;:x.split(&#39;=&#39;)[0],&#39;type&#39;:&#39;text&#39;,&#39;value&#39;:x.split(&#39;=&#39;)[1]} for x in u.split(&#39;?&#39;)[1].split(&#39;&amp;&#39;)]
    return {
                    &#34;inputs&#34;: inputs,
                    &#34;action&#34;: u.split(&#39;?&#39;)[0],
                    &#34;enctype&#34;: &#39;application/x-www-form-urlencoded&#39;,
                    &#34;method&#34;: &#39;get&#39;,
                    &#34;id&#34;:url_id,
                    &#34;hidden_values&#34;: [],
                    &#34;is_url&#34;:True
                }


def get_links_from_page_source(soup,url,url_id):
    if url.endswith(&#39;/&#39;)==False:
        url+=&#39;/&#39;
    domain=url.split(&#39;/&#39;)[0] if url.startswith(&#39;http&#39;)==False else url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    l=soup.find_all(&#39;a&#39;)
    links=[{&#39;url&#39;:x[&#39;href&#39;].replace(&#39;&amp;amp;&#39;,&#39;&amp;&#39;),&#39;id&#39;:x.get(&#39;id&#39;,&#39;&#39;)} for x in l if x.has_attr(&#39;href&#39;)]
    media_tags = soup.find_all([&#39;img&#39;, &#39;audio&#39;, &#39;video&#39;, &#39;source&#39;,&#39;embed&#39;])
    links+=[{&#39;url&#39;:x[&#39;src&#39;].replace(&#39;&amp;amp;&#39;,&#39;&amp;&#39;),&#39;id&#39;:x.get(&#39;id&#39;,&#39;&#39;) } for x in media_tags if x.has_attr(&#39;src&#39;)]
    links.append({&#39;url&#39;:url,&#39;id&#39;:url_id})
    #print(links)
    #links_list=[]
    root_links=[]
    forms=[]
    for l in links:
        x=l[&#39;url&#39;]
        l_id=l[&#39;id&#39;]
        if &#39;?&#39; in x and x.split(&#39;?&#39;)[0] not in root_links:
            a=urljoin(url, x)
            #print(a)
            if a.startswith(url.split(domain)[0]+domain)==True:
                forms.append(url_to_get_form(a,l_id))
                root_links.append(x.split(&#39;?&#39;)[0])
    return forms



def remove_html_comments(text):
    return re.sub(r&#34;&lt;!--(.|\s|\n)*?--&gt;&#34;, &#34;&#34;, text, flags=re.DOTALL)


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
    &#34;&#34;&#34;
     this function is to get the names and values of input fields on a given webpage to scan.

     it takes 4 arguments:

     u: the page&#39;s link (http://...)
     value: (set by default to: False) to return the value of the fields set it to:True then the field&#39;s name and value will be string of 2
     values sperated by &#34;:&#34;
     timeout: (set by default to: 10) timeout flag for the request
     bypass: (set by default to: False) to bypass anti-crawlers

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;link=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.inputs(link)
    [&#39;email&#39;,&#39;password&#39;,&#39;rememberme&#39;]
    &gt;&gt;&gt;a=bane.inputs(link,value=True)
    [&#39;email&#39;,&#39;password&#39;,&#39;rememberme:yes&#39;,&#39;rememberme:no&#39;]

    &#34;&#34;&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    l = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        p = soup.find_all(&#34;textarea&#34;)
        for r in p:
            if r.has_attr(&#34;name&#34;):
                s = r.get(&#34;name&#34;)
                v = r.get(&#34;value&#34;)
                if v == None:
                    v = &#34;&#34;
            if value == True:
                y = s + &#34;:&#34; + v
            else:
                y = s
            if y not in l:
                l.append(y)
        p = soup.find_all(&#34;input&#34;)
        for r in p:
            v = &#34;&#34;
            if r.has_attr(&#34;name&#34;):
                s = str(r)
                s = s.split(&#39;name=&#34;&#39;)[1].split(&#34;,&#34;)[0]
                s = s.split(&#39;&#34;&#39;)[0].split(&#34;,&#34;)[0]
                if r.has_attr(&#34;value&#34;) and (value == True):
                    v = str(r)
                    v = v.split(&#39;value=&#34;&#39;)[1].split(&#34;,&#34;)[0]
                    v = v.split(&#39;&#34;&#39;)[0].split(&#34;,&#34;)[0]
            if value == True:
                y = s + &#34;:&#34; + v
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
    &#34;&#34;&#34;
    same as &#34;inputs&#34; function but it works on forms input fields only
    &#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    l = []
    fom = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        i = soup.find_all(&#34;form&#34;)
        for f in i:
            ac = f.get(&#34;action&#34;)
            if not ac:
                ac = u
            &#34;&#34;&#34;if len(ac)==0:
    ac=u
   if ac[0]==&#34;/&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+ac
   if ac[:4]!=&#34;http&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+&#34;/&#34;+ac&#34;&#34;&#34;
            if &#34;://&#34; not in ac:
                ur = u[: u.rfind(&#34;/&#34;)]
                if ac[0] == &#34;/&#34;:
                    ac = ac[1 : len(ac)]
                ac = ur + &#34;/&#34; + ac
            me = f.get(&#34;method&#34;)
            if not me:
                me = &#34;get&#34;
            if len(me) == 0:
                me = &#34;get&#34;
            me = me.lower()
            p = f.find_all(&#34;textarea&#34;)
            for r in p:
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;)
                    if v == None:
                        v = &#34;&#34;
                if value == True:
                    y = s + &#34;:&#34; + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            p = f.find_all(&#34;input&#34;)
            for r in p:
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;)
                    if v == None:
                        v = &#34;&#34;
                if value == True:
                    y = s + &#34;:&#34; + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            fom.append({&#34;inputs&#34;: l, &#34;action&#34;: ac, &#34;method&#34;: me})
            l = []
    except Exception as e:
        pass
    return fom


def sort_inputs(l):
    a = []
    d = []
    for x in l:
        if x[&#34;type&#34;] not in [u&#34;radio&#34;, u&#34;checkbox&#34;]:
            d.append(x)
        if x[&#34;name&#34;] not in a and (x[&#34;type&#34;] == u&#34;radio&#34; or x[&#34;type&#34;] == u&#34;checkbox&#34;):
            a.append(x[&#34;name&#34;])
    for x in a:
        d.append(
            {
                &#34;type&#34;: [i[&#34;type&#34;] for i in l if i[&#34;name&#34;] == x][0],
                &#34;name&#34;: x,
                &#34;value&#34;: [i[&#34;value&#34;] for i in l if i[&#34;name&#34;] == x],
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
    &#34;&#34;&#34;
    same as &#34;forms&#34; function but it return detailed information about all forms in a given page
    &#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    base_url=u.split(&#39;://&#39;)[0]+domain
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    l = []
    fom = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        i = soup.find_all(&#34;form&#34;)
        for f in i:
            form_id=f.get(&#39;id&#39;,&#39;&#39;)
            try:
                tb_inputs = f.find_all(&#34;table&#34;)[0].find_all(&#34;input&#34;)
            except:
                tb_inputs = []
            try:
                tb_textareas = f.find_all(&#34;table&#34;)[0].find_all(&#34;textarea&#34;)
            except:
                tb_textareas = []
            try:
                tb_selects = f.find_all(&#34;table&#34;)[0].find_all(&#34;select&#34;)
            except:
                tb_selects = []
            ac = urljoin(u, f.get(&#34;action&#34;,&#39;&#39;))
            enc_ty = f.get(&#34;enctype&#34;, &#34;application/x-www-form-urlencoded&#34;)
            if not ac:
                ac = u
            &#34;&#34;&#34;if len(ac)==0:
    ac=u
   if ac[0]==&#34;/&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+ac
   if ac[:4]!=&#34;http&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+&#34;/&#34;+ac&#34;&#34;&#34;
            if &#34;://&#34; not in ac:
                ur = u[: u.rfind(&#34;/&#34;)]
                if ac[0] == &#34;/&#34;:
                    ac = ac[1 : len(ac)]
                ac = ur + &#34;/&#34; + ac
            me = f.get(&#34;method&#34;, &#34;get&#34;)
            if not me:
                me = &#34;get&#34;
            if len(me) == 0:
                me = &#34;get&#34;
            me = me.lower()
            &#34;&#34;&#34;radios={}
            checkxoes={}&#34;&#34;&#34;
            p = f.find_all(&#34;textarea&#34;) + tb_textareas
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.renderContents().decode().split(&#34;&lt;/textarea&gt;&#34;)[0]
                    typ = r.get(&#34;type&#34;, &#34;textarea&#34;).lower()
                    max_size=r.get(&#39;maxlength&#39;,64)
                    if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;max&#39;:max_size,&#39;min&#39;:r.get(&#39;minlength&#39;,1),&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            h_v = {}
            p = f.find_all(&#34;input&#34;) + tb_inputs
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;, &#34;&#34;)
                    typ = r.get(&#34;type&#34;, &#34;text&#34;).lower()
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;required&#39;:required}
                    if y[&#39;type&#39;] in [&#39;text&#39;,&#39;password&#39;,&#39;email&#39;,&#39;url&#39;,&#39;tel&#39;,&#39;search&#39;]:
                        max_size=r.get(&#39;maxlength&#39;,64)
                        if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                        y.update({&#39;max&#39;:int(max_size),&#39;min&#39;:int(r.get(&#39;minlength&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;number&#39;:
                        y.update({&#39;max&#39;:int(r.get(&#39;max&#39;,10)),&#39;min&#39;:int(r.get(&#39;min&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;date&#39;:
                        y.update({&#39;max&#39;:r.get(&#39;max&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;)),&#39;min&#39;:r.get(&#39;min&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;))})
                    elif y[&#39;type&#39;]==&#39;file&#39;:
                        y.update({&#39;accept&#39;:[ x.replace(&#39;.&#39;,&#39;&#39;).strip() for x in y.get(&#39;accept&#39;,&#39;.png&#39;).split(&#39;,&#39;)]})
                    &#34;&#34;&#34;elif y[&#39;type&#39;]==&#39;radio&#39;:
                        if y[&#39;name&#39;] not in radios:
                            radios[y[&#39;name&#39;]]=[]
                        radios[y[&#39;name&#39;]].append(y)
                    elif y[&#39;type&#39;]==&#39;checkbox&#39;:
                        if y[&#39;name&#39;] not in checkxoes:
                            checkxoes[y[&#39;name&#39;]]=[]
                        checkxoes[y[&#39;name&#39;]].append(y)&#34;&#34;&#34;
                    if typ.lower() == &#34;hidden&#34;:
                        h_v.update({s: v})
                    if y not in l :#and y[&#39;name&#39;] not in radios and y[&#39;name&#39;] not in checkxoes:
                        l.append(y)
            p = f.find_all(&#34;select&#34;) + tb_selects
            opts = []
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    for x in r.find_all(&#34;option&#34;):
                        opts.append(x.text)
                    y = {&#34;name&#34;: s, &#34;value&#34;: opts, &#34;type&#34;: &#34;select&#34;,&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            &#34;&#34;&#34;for x in radios:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;radio&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in radios[x]]})
            for x in checkxoes:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;checkbox&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in checkxoes[x]]})&#34;&#34;&#34;
            fom.append(
                {
                    &#39;id&#39;:form_id,
                    &#34;inputs&#34;: sort_inputs(l),
                    &#34;action&#34;: ac.lower(),
                    &#34;enctype&#34;: enc_ty.lower(),
                    &#34;method&#34;: me.lower(),
                    &#34;hidden_values&#34;: h_v,
                    &#34;is_url&#34;:False
                }
            )
            l = []
    except Exception as e:
        pass
    if include_links==True:
        fom+=get_links_from_page_source(soup,u,&#39;&#39;)
    return fom


def forms_parser_text(u, text, html_comments=False,include_links=True):
    &#34;&#34;&#34;
    same as &#34;forms&#34; function but it return detailed information about all forms in a given page
    &#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    l = []
    fom = []
    try:
        c = text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        i = soup.find_all(&#34;form&#34;)
        for f in i:
            form_id=f.get(&#39;id&#39;,&#39;&#39;)
            try:
                tb_inputs = f.find_all(&#34;table&#34;)[0].find_all(&#34;input&#34;)
            except:
                tb_inputs = []
            try:
                tb_textareas = f.find_all(&#34;table&#34;)[0].find_all(&#34;textarea&#34;)
            except:
                tb_textareas = []
            try:
                tb_selects = f.find_all(&#34;table&#34;)[0].find_all(&#34;select&#34;)
            except:
                tb_selects = []
            ac = urljoin(u, f.get(&#34;action&#34;,&#39;&#39;))
            enc_ty = f.get(&#34;enctype&#34;, &#34;application/x-www-form-urlencoded&#34;).lower()
            if not ac:
                ac = u
            &#34;&#34;&#34;if len(ac)==0:
    ac=u
   if ac[0]==&#34;/&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+ac
   if ac[:4]!=&#34;http&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+&#34;/&#34;+ac&#34;&#34;&#34;
            if &#34;://&#34; not in ac:
                ur = u[: u.rfind(&#34;/&#34;)]
                if ac[0] == &#34;/&#34;:
                    ac = ac[1 : len(ac)]
                ac = ur + &#34;/&#34; + ac
            me = f.get(&#34;method&#34;, &#34;get&#34;).lower()
            if not me:
                me = &#34;get&#34;
            if len(me) == 0:
                me = &#34;get&#34;
            me = me.lower()
            &#34;&#34;&#34;radios={}
            checkxoes={}&#34;&#34;&#34;
            p = f.find_all(&#34;textarea&#34;) + tb_textareas
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.renderContents().decode().split(&#34;&lt;/textarea&gt;&#34;)[0]
                    typ = r.get(&#34;type&#34;, &#34;textarea&#34;).lower()
                    max_size=r.get(&#39;maxlength&#39;,64)
                    if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;max&#39;:max_size,&#39;min&#39;:r.get(&#39;minlength&#39;,1),&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            h_v = {}
            p = f.find_all(&#34;input&#34;) + tb_inputs
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;, &#34;&#34;)
                    typ = r.get(&#34;type&#34;, &#34;text&#34;).lower()
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;required&#39;:required}
                    if y[&#39;type&#39;] in [&#39;text&#39;,&#39;password&#39;,&#39;email&#39;,&#39;url&#39;,&#39;tel&#39;,&#39;search&#39;]:
                        max_size=r.get(&#39;maxlength&#39;,64)
                        if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                        y.update({&#39;max&#39;:int(max_size),&#39;min&#39;:int(r.get(&#39;minlength&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;number&#39;:
                        y.update({&#39;max&#39;:int(r.get(&#39;max&#39;,64)),&#39;min&#39;:int(r.get(&#39;min&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;date&#39;:
                        y.update({&#39;max&#39;:r.get(&#39;max&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;)),&#39;min&#39;:r.get(&#39;min&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;))})
                    elif y[&#39;type&#39;]==&#39;file&#39;:
                        y.update({&#39;accept&#39;:[ x.replace(&#39;.&#39;,&#39;&#39;).strip() for x in y.get(&#39;accept&#39;,&#39;.png&#39;).split(&#39;,&#39;)]})
                    &#34;&#34;&#34;elif y[&#39;type&#39;]==&#39;radio&#39;:
                        if y[&#39;name&#39;] not in radios:
                            radios[y[&#39;name&#39;]]=[]
                        radios[y[&#39;name&#39;]].append(y)
                    elif y[&#39;type&#39;]==&#39;checkbox&#39;:
                        if y[&#39;name&#39;] not in checkxoes:
                            checkxoes[y[&#39;name&#39;]]=[]
                        checkxoes[y[&#39;name&#39;]].append(y)&#34;&#34;&#34;
                    if typ.lower() == &#34;hidden&#34;:
                        h_v.update({s: v})
                    if y not in l :#and y[&#39;name&#39;] not in radios and y[&#39;name&#39;] not in checkxoes:
                        l.append(y)
            p = f.find_all(&#34;select&#34;) + tb_selects
            opts = []
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    for x in r.find_all(&#34;option&#34;):
                        opts.append(x.text)
                    y = {&#34;name&#34;: s, &#34;value&#34;: opts, &#34;type&#34;: &#34;select&#34;,&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            &#34;&#34;&#34;for x in radios:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;radio&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in radios[x]]})
            for x in checkxoes:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;checkbox&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in checkxoes[x]]})&#34;&#34;&#34;
            fom.append(
                {
                    &#39;id&#39;:form_id,
                    &#34;inputs&#34;: sort_inputs(l),
                    &#34;action&#34;: ac,
                    &#34;enctype&#34;: enc_ty,
                    &#34;method&#34;: me,
                    &#34;hidden_values&#34;: h_v,
                    &#34;is_url&#34;:False
                }
            )
            l = []
    except Exception as e:
        pass #raise(e)
    if include_links==True:
        fom+=get_links_from_page_source(soup,u,&#39;&#39;)
    return fom


def cookies_to_dict(cookies):
    d = {}
    a = cookies.split(&#34;;&#34;)
    for x in a:
        if &#34;=&#34; in x:
            d.update({x.split(&#34;=&#34;)[0].strip(): x.split(&#34;=&#34;)[1].strip()})
    return d


def update_cookies(cookies, cook):
    c1 = {}
    c2 = {}
    if cookies:
        c1 = cookies_to_dict(cookies)
    if cook:
        c2 = cookies_to_dict(cook)
    c2.update(c1)
    cookie = &#34;&#34;
    for x in c2:
        cookie += x + &#34;=&#34; + c2[x] + &#34;;&#34;
    return cookie


def set_correct_cookies(new_cookies, cookie=None):
    if not cookie:
        cookie = &#34;&#34;
    if not new_cookies:
        new_cookies = &#34;&#34;
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
    file_extension=&#34;png&#34;,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    number=(1, 9),
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    cookies = None
    h = {&#34;User-Agent&#34;: user_agent}
    if cookie:
        h.update({&#34;Cookie&#34;: cookie})
        cookies = cookie
    h.update(headers)
    
    try:
        r = requests.Session().get(url, proxies=proxy, headers=h, verify=False, timeout=timeout)
    except:
        return False
    cook = None
    try:
        cook = r.headers[&#34;Set-cookie&#34;]
    except:
        pass
    cookies = set_correct_cookies(cook, cookie=cookie)
    form = forms_parser_text(url, r.text)[form_index]
    h = {&#34;User-Agent&#34;: user_agent}
    if cookies and len(cookies.strip()) &gt; 0:
        h.update({&#34;Cookie&#34;: cookies})
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
    file_extension=&#34;png&#34;,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    number=(1, 9),
    auto_fill=10,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
):
    for x in form[&#34;inputs&#34;]:
        if x[&#34;name&#34;].strip() in dont_change:
            x[&#34;value&#34;] = dont_change[x[&#34;name&#34;]]
        else:
            if x[&#34;name&#34;].strip() in dont_send:
                form[&#34;inputs&#34;].remove(x)
            else:
                if x[&#34;name&#34;].strip() not in leave_empty:
                    if x[&#34;name&#34;].strip() == param:
                        if file_extension==None:
                            file_extension=random.choice(x[&#34;accept&#34;])
                        if x[&#34;type&#34;] == &#34;file&#34;:
                            if not mime_type:
                                x[&#34;value&#34;] = (
                                    payload + &#34;.&#34; + file_extension,
                                    files_upload[file_extension],
                                )
                            else:
                                x[&#34;value&#34;] = (
                                    payload + &#34;.&#34; + file_extension,
                                    files_upload[file_extension],
                                    mime_type,
                                )
                        else:
                            x[&#34;value&#34;] = payload
                    else:
                        if x[&#34;name&#34;].strip() in predefined_inputs:
                            x[&#34;value&#34;] = predefined_inputs[x[&#34;name&#34;]]
                        else:
                            if x[&#34;value&#34;] == &#34;&#34;:
                                if x[&#34;type&#34;] == &#34;file&#34;:
                                    if not mime_type:
                                        x[&#34;value&#34;] = (
                                            &#34;bane_test&#34;
                                            + str(random.randint(100000, 999999))
                                            + &#34;.&#34;
                                            + file_extension,
                                            files_upload[file_extension],
                                        )
                                    else:
                                        x[&#34;value&#34;] = (
                                            &#34;bane_test&#34;
                                            + str(random.randint(100000, 999999))
                                            + &#34;.&#34;
                                            + file_extension,
                                            files_upload[file_extension],
                                            mime_type,
                                        )
                                else:
                                    #if x[&#39;value&#39;]==&#39;&#39;:
                                        if x[&#34;type&#34;] == &#34;number&#34;:
                                            x[&#34;value&#34;] += str(random.randint(int(float(x.get(&#39;min&#39;,0))), int(float(x.get(&#39;max&#39;,9)))))
                                        elif x[&#39;type&#39;] in [&#39;text&#39;,&#39;password&#39;,&#39;search&#39;,&#39;textarea&#39;]:
                                            leng=random.randint(int(float(x.get(&#39;min&#39;,1))), int(float(x.get(&#39;max&#39;,64)))+1)
                                            for i in range(leng):
                                                x[&#34;value&#34;] += random.choice(lis)
                                        elif x[&#39;type&#39;]==&#39;email&#39;:
                                            leng=random.randint(int(float(x.get(&#39;min&#39;,1))), int(float(x.get(&#39;max&#39;,15)))-len(email_extension)+1)
                                            for i in range(leng):
                                                x[&#34;value&#34;] += random.choice(string.ascii_lowercase)
                                            x[&#34;value&#34;]+=email_extension
                                        elif x[&#39;type&#39;]==&#39;tel&#39;:
                                            x[&#34;value&#34;]=generate_random_phone_number(phone_pattern)
                                        elif x[&#39;type&#39;]==&#39;url&#39;:
                                            x[&#34;value&#34;]=generate_random_url()
                                        elif x[&#39;type&#39;]==&#39;date&#39;:
                                            x[&#34;value&#34;]=random_date(x[&#39;min&#39;], x[&#39;max&#39;])
                                        elif x[&#39;type&#39;]==&#39;color&#39;:
                                            x[&#39;value&#39;]=generate_random_html_input_color()      
                            if x[&#34;type&#34;] in [&#34;select&#34;, &#34;radio&#34;, &#34;checkbox&#34;]:
                                if len(x[&#34;value&#34;]) == 0 or x[&#34;value&#34;] == &#34;&#34;:
                                    x[&#34;value&#34;] = &#34;&#34;
                                    for i in range(auto_fill):
                                        x[&#34;value&#34;] += random.choice(lis)
                                else:
                                    x[&#34;value&#34;] = random.choice(x[&#34;value&#34;])
    #print(form)
    return form


def get_login_form(url, text):
    a = forms_parser_text(url, text)
    for x in a:
        for i in x[&#34;inputs&#34;]:
            if i[&#34;type&#34;].lower().strip() == &#34;password&#34;:
                return x
    raise Exception(&#34;No login form&#34;)


def set_login_form(url, text, username, password):
    a = get_login_form(url, text)
    d = {}
    for x in a[&#34;inputs&#34;]:
        if x[&#34;type&#34;].lower().strip() == &#34;password&#34;:
            d.update({x[&#34;name&#34;]: password})
        elif (
            x[&#34;type&#34;].lower().strip() == &#34;text&#34;
            or x[&#34;type&#34;].lower().strip() == &#34;email&#34;
            or x[&#34;type&#34;].lower().strip() == &#34;tel&#34;
        ):
            d.update({x[&#34;name&#34;]: username})
        else:
            d.update({x[&#34;name&#34;]: x[&#34;value&#34;]})
    return [d, a[&#34;action&#34;]]


def get_upload_form(a):
    l=[]
    for x in a:
        for i in x[&#34;inputs&#34;]:
            if i[&#34;type&#34;].lower().strip() == &#34;file&#34;:
                l.append(x)
    if l==[]:
        raise Exception(&#34;No file upload form&#34;)
    return l


def get_upload_form_text(url, text):
    l=[]
    a = forms_parser_text(url, text)
    for x in a:
        for i in x[&#34;inputs&#34;]:
            if i[&#34;type&#34;].lower().strip() == &#34;file&#34;:
                l.append(x)
    if l==[]:
        raise Exception(&#34;No file upload form&#34;)
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
    &#34;&#34;&#34;
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        ur = u.replace(u.split(&#34;/&#34;)[-1], &#34;&#34;)
        &#34;&#34;&#34;if ur[-1]==&#39;/&#39;:
   ur=ur[:-1]&#34;&#34;&#34;
        index_link = 0
        h.update(
            {
                -1: (
                    &#34;Source_url&#34;,
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all(&#34;a&#34;):
            u = ur
            if a.has_attr(&#34;href&#34;):
                try:
                    txt = a.text
                    a = str(a[&#34;href&#34;])
                    if &#34;://&#34; not in a:
                        if a[0] == &#34;/&#34;:
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + &#34;/&#34;) and (a != u):
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
    &#34;&#34;&#34;
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    h={}
    try:
        c = text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        ur = u.replace(u.split(&#34;/&#34;)[-1], &#34;&#34;)
        &#34;&#34;&#34;if ur[-1]==&#39;/&#39;:
   ur=ur[:-1]&#34;&#34;&#34;
        index_link = 0
        h.update(
            {
                -1: (
                    &#34;Source_url&#34;,
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all(&#34;a&#34;):
            u = ur
            if a.has_attr(&#34;href&#34;):
                try:
                    txt = a.text
                    a = str(a[&#34;href&#34;])
                    if &#34;://&#34; not in a:
                        if a[0] == &#34;/&#34;:
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + &#34;/&#34;) and (a != u):
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
    &#34;&#34;&#34;
    this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram...).

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.media(url)

    &gt;&gt;&gt;bane.media(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    h = {}
    try:
        if bypass == True:
            u += &#34;#&#34;
        hea.update(headers)
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        ul = u.split(&#34;://&#34;)[1].split(&#39;&#34;&#39;)[0]
        ur = ul.replace(&#34;www.&#34;, &#34;&#34;)
        for a in soup.findAll(&#34;a&#34;):
            try:
                if (
                    a.has_attr(&#34;href&#34;)
                    and (u not in a[&#34;href&#34;])
                    and (ur not in a[&#34;href&#34;])
                    and (a[&#34;href&#34;][:4] == &#34;http&#34;)
                ):
                    txt = a.text
                    if a[&#34;href&#34;] not in h:
                        h.update({txt: a[&#34;href&#34;]})
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
    &#34;&#34;&#34;
    this function collects the subdomains found on the targeted webpage.

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.subdomains_extract(url)

    &gt;&gt;&gt;bane.subdomains_extract(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        if bypass == True:
            u += &#34;#&#34;
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        ul = u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        for a in soup.findAll(&#34;a&#34;):
            if (
                a.has_attr(&#34;href&#34;)
                and (ul.replace(&#34;www&#34;, &#34;&#34;) in a[&#34;href&#34;])
                and (ul not in a[&#34;href&#34;])
                and (a[&#34;href&#34;][:4] == &#34;http&#34;)
            ):
                txt = a.text
                try:
                    hr = a[&#34;href&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
                    h.update({txt: hr})
                except Exception as e:
                    pass
    except Exception as e:
        pass
    return h




def extract_urls_from_js(js_content, base_url):
    # Regular expression to match URLs in JavaScript code
    url_pattern = re.compile(r&#39;https?://\S+|/\S+&#39;)

    # Find all matches in the JavaScript code
    matches = re.findall(url_pattern, js_content)

    # Filter out URLs that start with &#39;/&#39;
    extracted_urls = [match if match.startswith(&#39;http&#39;) else base_url + match for match in matches]
    urls=[]
    for x in extracted_urls:
        x=x.split(&#39;&#34;&#39;)[0]
        x=x.split(&#39;;&#39;)[0]
        x=x.split(&#34;&#39;&#34;)[0]
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
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        return requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
    except:
        return &#39;&#39;



def extract_urls_from_js(js_content, base_url):
    # Regular expression to match URLs in JavaScript code
    url_pattern = re.compile(r&#39;https?://\S+|/\S+&#39;)

    # Find all matches in the JavaScript code
    matches = re.findall(url_pattern, js_content)

    # Filter out URLs that start with &#39;/&#39;
    extracted_urls = [match if match.startswith(&#39;http&#39;) else base_url + match for match in matches]
    urls=[]
    for x in extracted_urls:
        x=x.split(&#39;&#34;&#39;)[0]
        x=x.split(&#39;;&#39;)[0]
        x=x.split(&#34;&#39;&#34;)[0]
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
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        r= requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
        soup = BeautifulSoup(r, &#39;html.parser&#39;)
        script_tags = soup.find_all(&#39;script&#39;)
        code=&#39;&#39;
        for script in script_tags:
            if script.has_attr(&#39;src&#39;):
                pass
            else:
                code+=script.get_text()
        secrets=[]
        #print(code)
        secrets.append({&#39;url&#39;:u,&#39;secrets&#39;:extract_secrets_from_text(code)})#,&#39;endpoints&#39;:extract_urls_from_js(code,u)})
        for script in script_tags:
            if script.has_attr(&#39;src&#39;):
                url=urljoin(u,script[&#39;src&#39;])
                url_domain=url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
                if extract_root_domain(url_domain)==extract_root_domain(domain):
                    #print(url_domain)
                    code=fetch_url(url,user_agent=user_agent,timeout=timeout,proxy=proxy,cookie=cookie,headers=headers)
                    secrets.append({&#39;url&#39;:url,&#39;secrets&#39;:extract_secrets_from_text(code)})#,&#39;endpoints&#39;:extract_urls_from_js(code,url)})

    except Exception as ex:
        pass
    return [ x for x in secrets if len(list(x[&#39;secrets&#39;].keys()))&gt;0]



def extract_secrets_from_text(js_content):
    tokens_dict = {}
    for key, pattern in js_exposed_secrets_regexs.items():
        #for pattern in x:
            l=[]
            try:
                if key==&#39;firebase_config&#39;:
                    if matches:
                        for match in matches:
                            apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId, measurementId, vapidKey = match
                            d={
                                        &#34;apiKey&#34;: apiKey,
                                        &#34;authDomain&#34;: authDomain,
                                        &#34;projectId&#34;: projectId,
                                        &#34;storageBucket&#34;: storageBucket,
                                        &#34;messagingSenderId&#34;: messagingSenderId,
                                        &#34;appId&#34;: appId,
                                        &#34;measurementId&#34;: measurementId,
                                        &#34;vapidKey&#34;: vapidKey
                                    }
                            l.append(d)
                        tokens_dict[key] = l
                elif key==&#39;json_configs&#39;:
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
                            if &#39;&#34;{}&#34;&#39;.format(x) in js_content or &#34;&#39;{}&#39;&#34;.format(x) in js_content or &#34;={}&#34;.format(x) in js_content or &#34;= {}&#34;.format(x) in js_content or &#34;:{}&#34;.format(x) in js_content or &#34;: {}&#34;.format(x) in js_content:
                                l.append(x)
                        l=list(set(l))
                        if len(l)&gt;0:
                            tokens_dict[key] = l
            except Exception as ex:
                pass
    return tokens_dict




def generate_human_poc(data):
    if &#34;is_url&#34; not in data:
        raise ValueError(&#34;The &#39;is_url&#39; key is missing in the input data&#34;)

    if data[&#34;is_url&#34;]:
        # If is_url is True, generate a URL
        url = data.get(&#34;action&#34;, &#34;&#34;)
        if not url:
            raise ValueError(&#34;Missing &#39;action&#39; key for URL generation&#34;)
        
        query_parameters = []
        for input_field in data.get(&#34;inputs&#34;, []):
            name = input_field.get(&#34;name&#34;, &#34;&#34;)
            value = input_field.get(&#34;value&#34;, &#34;&#34;)
            query_parameters.append(&#34;{}={}&#34;.format(name,value))
        
        if query_parameters:
            url += &#34;?&#34; + &#34;&amp;&#34;.join(query_parameters)

        return url

    else:
        # If is_url is False, generate an HTML form
        form_id = data.get(&#34;id&#34;, &#34;&#34;)
        form_method = data.get(&#34;method&#34;, &#34;post&#34;)
        form_action = data.get(&#34;action&#34;, &#34;&#34;)
        form_enctype = data.get(&#34;enctype&#34;, &#34;application/x-www-form-urlencoded&#34;)

        inputs = &#34;&#34;
        for input_field in data.get(&#34;inputs&#34;, []):
            name = input_field.get(&#34;name&#34;, &#34;&#34;)
            value = input_field.get(&#34;value&#34;, &#34;&#34;)
            input_type = input_field.get(&#34;type&#34;, &#34;text&#34;)
            required = &#34;required&#34; if input_field.get(&#34;required&#34;, False) else &#34;&#34;
            input_element = &#34;&lt;input type=&#39;{}&#39; name=&#39;{}&#39; value=&#39;{}&#39; {}&gt;&#34;.format(input_type,name,value,required)
            inputs += input_element

        html_form = &#34;&#34;&#34;
        &lt;form id=&#39;{}&#39; method=&#39;{}&#39; action=&#39;{}&#39; enctype=&#39;{}&#39;&gt;
            {}
        &lt;/form&gt;
        &#34;&#34;&#34;.format(form_id,form_method,form_action,form_enctype,inputs)
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
    a = cookies.split(&#34;;&#34;)
    for x in a:
        if &#34;=&#34; in x:
            d.update({x.split(&#34;=&#34;)[0].strip(): x.split(&#34;=&#34;)[1].strip()})
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
    &#34;&#34;&#34;
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        ur = u.replace(u.split(&#34;/&#34;)[-1], &#34;&#34;)
        &#34;&#34;&#34;if ur[-1]==&#39;/&#39;:
   ur=ur[:-1]&#34;&#34;&#34;
        index_link = 0
        h.update(
            {
                -1: (
                    &#34;Source_url&#34;,
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all(&#34;a&#34;):
            u = ur
            if a.has_attr(&#34;href&#34;):
                try:
                    txt = a.text
                    a = str(a[&#34;href&#34;])
                    if &#34;://&#34; not in a:
                        if a[0] == &#34;/&#34;:
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + &#34;/&#34;) and (a != u):
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
    &#34;&#34;&#34;
    this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.crawl(url)

    &gt;&gt;&gt;bane.crawl(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if u.split(&#34;?&#34;)[0][-1] != &#34;/&#34; and &#34;.&#34; not in u.split(&#34;?&#34;)[0].rsplit(&#34;/&#34;, 1)[-1]:
        u = u.replace(&#34;?&#34;, &#34;/?&#34;)
    h={}
    try:
        c = text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        ur = u.replace(u.split(&#34;/&#34;)[-1], &#34;&#34;)
        &#34;&#34;&#34;if ur[-1]==&#39;/&#39;:
   ur=ur[:-1]&#34;&#34;&#34;
        index_link = 0
        h.update(
            {
                -1: (
                    &#34;Source_url&#34;,
                    u,
                    urlparse(u).path,
                    [(x, furl.furl(u).args[x]) for x in furl.furl(u).args],
                )
            }
        )
        for a in soup.find_all(&#34;a&#34;):
            u = ur
            if a.has_attr(&#34;href&#34;):
                try:
                    txt = a.text
                    a = str(a[&#34;href&#34;])
                    if &#34;://&#34; not in a:
                        if a[0] == &#34;/&#34;:
                            a = a[1 : len(a)]
                        a = u + a
                    if (a not in h.values()) and (u in a):
                        if (a != u + &#34;/&#34;) and (a != u):
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
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        r= requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
        soup = BeautifulSoup(r, &#39;html.parser&#39;)
        script_tags = soup.find_all(&#39;script&#39;)
        code=&#39;&#39;
        for script in script_tags:
            if script.has_attr(&#39;src&#39;):
                pass
            else:
                code+=script.get_text()
        secrets=[]
        #print(code)
        secrets.append({&#39;url&#39;:u,&#39;secrets&#39;:extract_secrets_from_text(code)})#,&#39;endpoints&#39;:extract_urls_from_js(code,u)})
        for script in script_tags:
            if script.has_attr(&#39;src&#39;):
                url=urljoin(u,script[&#39;src&#39;])
                url_domain=url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
                if extract_root_domain(url_domain)==extract_root_domain(domain):
                    #print(url_domain)
                    code=fetch_url(url,user_agent=user_agent,timeout=timeout,proxy=proxy,cookie=cookie,headers=headers)
                    secrets.append({&#39;url&#39;:url,&#39;secrets&#39;:extract_secrets_from_text(code)})#,&#39;endpoints&#39;:extract_urls_from_js(code,url)})

    except Exception as ex:
        pass
    return [ x for x in secrets if len(list(x[&#39;secrets&#39;].keys()))&gt;0]</code></pre>
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
                if key==&#39;firebase_config&#39;:
                    if matches:
                        for match in matches:
                            apiKey, authDomain, projectId, storageBucket, messagingSenderId, appId, measurementId, vapidKey = match
                            d={
                                        &#34;apiKey&#34;: apiKey,
                                        &#34;authDomain&#34;: authDomain,
                                        &#34;projectId&#34;: projectId,
                                        &#34;storageBucket&#34;: storageBucket,
                                        &#34;messagingSenderId&#34;: messagingSenderId,
                                        &#34;appId&#34;: appId,
                                        &#34;measurementId&#34;: measurementId,
                                        &#34;vapidKey&#34;: vapidKey
                                    }
                            l.append(d)
                        tokens_dict[key] = l
                elif key==&#39;json_configs&#39;:
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
                            if &#39;&#34;{}&#34;&#39;.format(x) in js_content or &#34;&#39;{}&#39;&#34;.format(x) in js_content or &#34;={}&#34;.format(x) in js_content or &#34;= {}&#34;.format(x) in js_content or &#34;:{}&#34;.format(x) in js_content or &#34;: {}&#34;.format(x) in js_content:
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
    url_pattern = re.compile(r&#39;https?://\S+|/\S+&#39;)

    # Find all matches in the JavaScript code
    matches = re.findall(url_pattern, js_content)

    # Filter out URLs that start with &#39;/&#39;
    extracted_urls = [match if match.startswith(&#39;http&#39;) else base_url + match for match in matches]
    urls=[]
    for x in extracted_urls:
        x=x.split(&#39;&#34;&#39;)[0]
        x=x.split(&#39;;&#39;)[0]
        x=x.split(&#34;&#39;&#34;)[0]
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
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        return requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
    except:
        return &#39;&#39;</code></pre>
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
    file_extension=&#34;png&#34;,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    number=(1, 9),
    auto_fill=10,
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
):
    for x in form[&#34;inputs&#34;]:
        if x[&#34;name&#34;].strip() in dont_change:
            x[&#34;value&#34;] = dont_change[x[&#34;name&#34;]]
        else:
            if x[&#34;name&#34;].strip() in dont_send:
                form[&#34;inputs&#34;].remove(x)
            else:
                if x[&#34;name&#34;].strip() not in leave_empty:
                    if x[&#34;name&#34;].strip() == param:
                        if file_extension==None:
                            file_extension=random.choice(x[&#34;accept&#34;])
                        if x[&#34;type&#34;] == &#34;file&#34;:
                            if not mime_type:
                                x[&#34;value&#34;] = (
                                    payload + &#34;.&#34; + file_extension,
                                    files_upload[file_extension],
                                )
                            else:
                                x[&#34;value&#34;] = (
                                    payload + &#34;.&#34; + file_extension,
                                    files_upload[file_extension],
                                    mime_type,
                                )
                        else:
                            x[&#34;value&#34;] = payload
                    else:
                        if x[&#34;name&#34;].strip() in predefined_inputs:
                            x[&#34;value&#34;] = predefined_inputs[x[&#34;name&#34;]]
                        else:
                            if x[&#34;value&#34;] == &#34;&#34;:
                                if x[&#34;type&#34;] == &#34;file&#34;:
                                    if not mime_type:
                                        x[&#34;value&#34;] = (
                                            &#34;bane_test&#34;
                                            + str(random.randint(100000, 999999))
                                            + &#34;.&#34;
                                            + file_extension,
                                            files_upload[file_extension],
                                        )
                                    else:
                                        x[&#34;value&#34;] = (
                                            &#34;bane_test&#34;
                                            + str(random.randint(100000, 999999))
                                            + &#34;.&#34;
                                            + file_extension,
                                            files_upload[file_extension],
                                            mime_type,
                                        )
                                else:
                                    #if x[&#39;value&#39;]==&#39;&#39;:
                                        if x[&#34;type&#34;] == &#34;number&#34;:
                                            x[&#34;value&#34;] += str(random.randint(int(float(x.get(&#39;min&#39;,0))), int(float(x.get(&#39;max&#39;,9)))))
                                        elif x[&#39;type&#39;] in [&#39;text&#39;,&#39;password&#39;,&#39;search&#39;,&#39;textarea&#39;]:
                                            leng=random.randint(int(float(x.get(&#39;min&#39;,1))), int(float(x.get(&#39;max&#39;,64)))+1)
                                            for i in range(leng):
                                                x[&#34;value&#34;] += random.choice(lis)
                                        elif x[&#39;type&#39;]==&#39;email&#39;:
                                            leng=random.randint(int(float(x.get(&#39;min&#39;,1))), int(float(x.get(&#39;max&#39;,15)))-len(email_extension)+1)
                                            for i in range(leng):
                                                x[&#34;value&#34;] += random.choice(string.ascii_lowercase)
                                            x[&#34;value&#34;]+=email_extension
                                        elif x[&#39;type&#39;]==&#39;tel&#39;:
                                            x[&#34;value&#34;]=generate_random_phone_number(phone_pattern)
                                        elif x[&#39;type&#39;]==&#39;url&#39;:
                                            x[&#34;value&#34;]=generate_random_url()
                                        elif x[&#39;type&#39;]==&#39;date&#39;:
                                            x[&#34;value&#34;]=random_date(x[&#39;min&#39;], x[&#39;max&#39;])
                                        elif x[&#39;type&#39;]==&#39;color&#39;:
                                            x[&#39;value&#39;]=generate_random_html_input_color()      
                            if x[&#34;type&#34;] in [&#34;select&#34;, &#34;radio&#34;, &#34;checkbox&#34;]:
                                if len(x[&#34;value&#34;]) == 0 or x[&#34;value&#34;] == &#34;&#34;:
                                    x[&#34;value&#34;] = &#34;&#34;
                                    for i in range(auto_fill):
                                        x[&#34;value&#34;] += random.choice(lis)
                                else:
                                    x[&#34;value&#34;] = random.choice(x[&#34;value&#34;])
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
    &#34;&#34;&#34;
    same as &#34;inputs&#34; function but it works on forms input fields only
    &#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    l = []
    fom = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        i = soup.find_all(&#34;form&#34;)
        for f in i:
            ac = f.get(&#34;action&#34;)
            if not ac:
                ac = u
            &#34;&#34;&#34;if len(ac)==0:
    ac=u
   if ac[0]==&#34;/&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+ac
   if ac[:4]!=&#34;http&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+&#34;/&#34;+ac&#34;&#34;&#34;
            if &#34;://&#34; not in ac:
                ur = u[: u.rfind(&#34;/&#34;)]
                if ac[0] == &#34;/&#34;:
                    ac = ac[1 : len(ac)]
                ac = ur + &#34;/&#34; + ac
            me = f.get(&#34;method&#34;)
            if not me:
                me = &#34;get&#34;
            if len(me) == 0:
                me = &#34;get&#34;
            me = me.lower()
            p = f.find_all(&#34;textarea&#34;)
            for r in p:
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;)
                    if v == None:
                        v = &#34;&#34;
                if value == True:
                    y = s + &#34;:&#34; + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            p = f.find_all(&#34;input&#34;)
            for r in p:
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;)
                    if v == None:
                        v = &#34;&#34;
                if value == True:
                    y = s + &#34;:&#34; + v
                else:
                    y = s
                if y not in l:
                    l.append(y)
            fom.append({&#34;inputs&#34;: l, &#34;action&#34;: ac, &#34;method&#34;: me})
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
    &#34;&#34;&#34;
    same as &#34;forms&#34; function but it return detailed information about all forms in a given page
    &#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    base_url=u.split(&#39;://&#39;)[0]+domain
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    l = []
    fom = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        i = soup.find_all(&#34;form&#34;)
        for f in i:
            form_id=f.get(&#39;id&#39;,&#39;&#39;)
            try:
                tb_inputs = f.find_all(&#34;table&#34;)[0].find_all(&#34;input&#34;)
            except:
                tb_inputs = []
            try:
                tb_textareas = f.find_all(&#34;table&#34;)[0].find_all(&#34;textarea&#34;)
            except:
                tb_textareas = []
            try:
                tb_selects = f.find_all(&#34;table&#34;)[0].find_all(&#34;select&#34;)
            except:
                tb_selects = []
            ac = urljoin(u, f.get(&#34;action&#34;,&#39;&#39;))
            enc_ty = f.get(&#34;enctype&#34;, &#34;application/x-www-form-urlencoded&#34;)
            if not ac:
                ac = u
            &#34;&#34;&#34;if len(ac)==0:
    ac=u
   if ac[0]==&#34;/&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+ac
   if ac[:4]!=&#34;http&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+&#34;/&#34;+ac&#34;&#34;&#34;
            if &#34;://&#34; not in ac:
                ur = u[: u.rfind(&#34;/&#34;)]
                if ac[0] == &#34;/&#34;:
                    ac = ac[1 : len(ac)]
                ac = ur + &#34;/&#34; + ac
            me = f.get(&#34;method&#34;, &#34;get&#34;)
            if not me:
                me = &#34;get&#34;
            if len(me) == 0:
                me = &#34;get&#34;
            me = me.lower()
            &#34;&#34;&#34;radios={}
            checkxoes={}&#34;&#34;&#34;
            p = f.find_all(&#34;textarea&#34;) + tb_textareas
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.renderContents().decode().split(&#34;&lt;/textarea&gt;&#34;)[0]
                    typ = r.get(&#34;type&#34;, &#34;textarea&#34;).lower()
                    max_size=r.get(&#39;maxlength&#39;,64)
                    if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;max&#39;:max_size,&#39;min&#39;:r.get(&#39;minlength&#39;,1),&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            h_v = {}
            p = f.find_all(&#34;input&#34;) + tb_inputs
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;, &#34;&#34;)
                    typ = r.get(&#34;type&#34;, &#34;text&#34;).lower()
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;required&#39;:required}
                    if y[&#39;type&#39;] in [&#39;text&#39;,&#39;password&#39;,&#39;email&#39;,&#39;url&#39;,&#39;tel&#39;,&#39;search&#39;]:
                        max_size=r.get(&#39;maxlength&#39;,64)
                        if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                        y.update({&#39;max&#39;:int(max_size),&#39;min&#39;:int(r.get(&#39;minlength&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;number&#39;:
                        y.update({&#39;max&#39;:int(r.get(&#39;max&#39;,10)),&#39;min&#39;:int(r.get(&#39;min&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;date&#39;:
                        y.update({&#39;max&#39;:r.get(&#39;max&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;)),&#39;min&#39;:r.get(&#39;min&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;))})
                    elif y[&#39;type&#39;]==&#39;file&#39;:
                        y.update({&#39;accept&#39;:[ x.replace(&#39;.&#39;,&#39;&#39;).strip() for x in y.get(&#39;accept&#39;,&#39;.png&#39;).split(&#39;,&#39;)]})
                    &#34;&#34;&#34;elif y[&#39;type&#39;]==&#39;radio&#39;:
                        if y[&#39;name&#39;] not in radios:
                            radios[y[&#39;name&#39;]]=[]
                        radios[y[&#39;name&#39;]].append(y)
                    elif y[&#39;type&#39;]==&#39;checkbox&#39;:
                        if y[&#39;name&#39;] not in checkxoes:
                            checkxoes[y[&#39;name&#39;]]=[]
                        checkxoes[y[&#39;name&#39;]].append(y)&#34;&#34;&#34;
                    if typ.lower() == &#34;hidden&#34;:
                        h_v.update({s: v})
                    if y not in l :#and y[&#39;name&#39;] not in radios and y[&#39;name&#39;] not in checkxoes:
                        l.append(y)
            p = f.find_all(&#34;select&#34;) + tb_selects
            opts = []
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    for x in r.find_all(&#34;option&#34;):
                        opts.append(x.text)
                    y = {&#34;name&#34;: s, &#34;value&#34;: opts, &#34;type&#34;: &#34;select&#34;,&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            &#34;&#34;&#34;for x in radios:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;radio&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in radios[x]]})
            for x in checkxoes:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;checkbox&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in checkxoes[x]]})&#34;&#34;&#34;
            fom.append(
                {
                    &#39;id&#39;:form_id,
                    &#34;inputs&#34;: sort_inputs(l),
                    &#34;action&#34;: ac.lower(),
                    &#34;enctype&#34;: enc_ty.lower(),
                    &#34;method&#34;: me.lower(),
                    &#34;hidden_values&#34;: h_v,
                    &#34;is_url&#34;:False
                }
            )
            l = []
    except Exception as e:
        pass
    if include_links==True:
        fom+=get_links_from_page_source(soup,u,&#39;&#39;)
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
    &#34;&#34;&#34;
    same as &#34;forms&#34; function but it return detailed information about all forms in a given page
    &#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    l = []
    fom = []
    try:
        c = text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        i = soup.find_all(&#34;form&#34;)
        for f in i:
            form_id=f.get(&#39;id&#39;,&#39;&#39;)
            try:
                tb_inputs = f.find_all(&#34;table&#34;)[0].find_all(&#34;input&#34;)
            except:
                tb_inputs = []
            try:
                tb_textareas = f.find_all(&#34;table&#34;)[0].find_all(&#34;textarea&#34;)
            except:
                tb_textareas = []
            try:
                tb_selects = f.find_all(&#34;table&#34;)[0].find_all(&#34;select&#34;)
            except:
                tb_selects = []
            ac = urljoin(u, f.get(&#34;action&#34;,&#39;&#39;))
            enc_ty = f.get(&#34;enctype&#34;, &#34;application/x-www-form-urlencoded&#34;).lower()
            if not ac:
                ac = u
            &#34;&#34;&#34;if len(ac)==0:
    ac=u
   if ac[0]==&#34;/&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+ac
   if ac[:4]!=&#34;http&#34;:
    url_o=&#34;/&#34;.join(u.split(&#39;/&#39;)[:-1])
    ac=url_o+&#34;/&#34;+ac&#34;&#34;&#34;
            if &#34;://&#34; not in ac:
                ur = u[: u.rfind(&#34;/&#34;)]
                if ac[0] == &#34;/&#34;:
                    ac = ac[1 : len(ac)]
                ac = ur + &#34;/&#34; + ac
            me = f.get(&#34;method&#34;, &#34;get&#34;).lower()
            if not me:
                me = &#34;get&#34;
            if len(me) == 0:
                me = &#34;get&#34;
            me = me.lower()
            &#34;&#34;&#34;radios={}
            checkxoes={}&#34;&#34;&#34;
            p = f.find_all(&#34;textarea&#34;) + tb_textareas
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.renderContents().decode().split(&#34;&lt;/textarea&gt;&#34;)[0]
                    typ = r.get(&#34;type&#34;, &#34;textarea&#34;).lower()
                    max_size=r.get(&#39;maxlength&#39;,64)
                    if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;max&#39;:max_size,&#39;min&#39;:r.get(&#39;minlength&#39;,1),&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            h_v = {}
            p = f.find_all(&#34;input&#34;) + tb_inputs
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    v = r.get(&#34;value&#34;, &#34;&#34;)
                    typ = r.get(&#34;type&#34;, &#34;text&#34;).lower()
                    y = {&#34;name&#34;: s, &#34;value&#34;: v, &#34;type&#34;: typ,&#39;required&#39;:required}
                    if y[&#39;type&#39;] in [&#39;text&#39;,&#39;password&#39;,&#39;email&#39;,&#39;url&#39;,&#39;tel&#39;,&#39;search&#39;]:
                        max_size=r.get(&#39;maxlength&#39;,64)
                        if r.get(&#39;size&#39;,0)!=0:
                            max_size= r.get(&#39;size&#39;,64)
                        y.update({&#39;max&#39;:int(max_size),&#39;min&#39;:int(r.get(&#39;minlength&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;number&#39;:
                        y.update({&#39;max&#39;:int(r.get(&#39;max&#39;,64)),&#39;min&#39;:int(r.get(&#39;min&#39;,1))})
                    elif y[&#39;type&#39;]==&#39;date&#39;:
                        y.update({&#39;max&#39;:r.get(&#39;max&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;)),&#39;min&#39;:r.get(&#39;min&#39;,datetime.datetime.today().strftime(&#34;%Y-%m-%d&#34;))})
                    elif y[&#39;type&#39;]==&#39;file&#39;:
                        y.update({&#39;accept&#39;:[ x.replace(&#39;.&#39;,&#39;&#39;).strip() for x in y.get(&#39;accept&#39;,&#39;.png&#39;).split(&#39;,&#39;)]})
                    &#34;&#34;&#34;elif y[&#39;type&#39;]==&#39;radio&#39;:
                        if y[&#39;name&#39;] not in radios:
                            radios[y[&#39;name&#39;]]=[]
                        radios[y[&#39;name&#39;]].append(y)
                    elif y[&#39;type&#39;]==&#39;checkbox&#39;:
                        if y[&#39;name&#39;] not in checkxoes:
                            checkxoes[y[&#39;name&#39;]]=[]
                        checkxoes[y[&#39;name&#39;]].append(y)&#34;&#34;&#34;
                    if typ.lower() == &#34;hidden&#34;:
                        h_v.update({s: v})
                    if y not in l :#and y[&#39;name&#39;] not in radios and y[&#39;name&#39;] not in checkxoes:
                        l.append(y)
            p = f.find_all(&#34;select&#34;) + tb_selects
            opts = []
            for r in p:
                required=False
                if &#39;required&#39; in r.attrs:
                    required=True
                if r.has_attr(&#34;name&#34;):
                    s = r.get(&#34;name&#34;)
                    for x in r.find_all(&#34;option&#34;):
                        opts.append(x.text)
                    y = {&#34;name&#34;: s, &#34;value&#34;: opts, &#34;type&#34;: &#34;select&#34;,&#39;required&#39;:required}
                    if y not in l:
                        l.append(y)
            &#34;&#34;&#34;for x in radios:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;radio&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in radios[x]]})
            for x in checkxoes:
                l.append({&#39;name&#39;:x,&#39;type&#39;:&#39;checkbox&#39;,&#39;value&#39;:[i[&#39;value&#39;] for i in checkxoes[x]]})&#34;&#34;&#34;
            fom.append(
                {
                    &#39;id&#39;:form_id,
                    &#34;inputs&#34;: sort_inputs(l),
                    &#34;action&#34;: ac,
                    &#34;enctype&#34;: enc_ty,
                    &#34;method&#34;: me,
                    &#34;hidden_values&#34;: h_v,
                    &#34;is_url&#34;:False
                }
            )
            l = []
    except Exception as e:
        pass #raise(e)
    if include_links==True:
        fom+=get_links_from_page_source(soup,u,&#39;&#39;)
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
    if &#34;is_url&#34; not in data:
        raise ValueError(&#34;The &#39;is_url&#39; key is missing in the input data&#34;)

    if data[&#34;is_url&#34;]:
        # If is_url is True, generate a URL
        url = data.get(&#34;action&#34;, &#34;&#34;)
        if not url:
            raise ValueError(&#34;Missing &#39;action&#39; key for URL generation&#34;)
        
        query_parameters = []
        for input_field in data.get(&#34;inputs&#34;, []):
            name = input_field.get(&#34;name&#34;, &#34;&#34;)
            value = input_field.get(&#34;value&#34;, &#34;&#34;)
            query_parameters.append(&#34;{}={}&#34;.format(name,value))
        
        if query_parameters:
            url += &#34;?&#34; + &#34;&amp;&#34;.join(query_parameters)

        return url

    else:
        # If is_url is False, generate an HTML form
        form_id = data.get(&#34;id&#34;, &#34;&#34;)
        form_method = data.get(&#34;method&#34;, &#34;post&#34;)
        form_action = data.get(&#34;action&#34;, &#34;&#34;)
        form_enctype = data.get(&#34;enctype&#34;, &#34;application/x-www-form-urlencoded&#34;)

        inputs = &#34;&#34;
        for input_field in data.get(&#34;inputs&#34;, []):
            name = input_field.get(&#34;name&#34;, &#34;&#34;)
            value = input_field.get(&#34;value&#34;, &#34;&#34;)
            input_type = input_field.get(&#34;type&#34;, &#34;text&#34;)
            required = &#34;required&#34; if input_field.get(&#34;required&#34;, False) else &#34;&#34;
            input_element = &#34;&lt;input type=&#39;{}&#39; name=&#39;{}&#39; value=&#39;{}&#39; {}&gt;&#34;.format(input_type,name,value,required)
            inputs += input_element

        html_form = &#34;&#34;&#34;
        &lt;form id=&#39;{}&#39; method=&#39;{}&#39; action=&#39;{}&#39; enctype=&#39;{}&#39;&gt;
            {}
        &lt;/form&gt;
        &#34;&#34;&#34;.format(form_id,form_method,form_action,form_enctype,inputs)
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
    color_hex = &#34;#{:02X}{:02X}{:02X}&#34;.format(r, g, b)
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
    phone_number = &#34;&#34;
    for char in pattern:
        if char == &#34;X&#34;:
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
    protocols = [&#34;http&#34;, &#34;https&#34;]
    protocol = random.choice(protocols)
    domain = random.choice(domainl)
    return &#34;{}://{}/&#34;.format(protocol,domain)</code></pre>
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
    if url.endswith(&#39;/&#39;)==False:
        url+=&#39;/&#39;
    domain=url.split(&#39;/&#39;)[0] if url.startswith(&#39;http&#39;)==False else url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    l=soup.find_all(&#39;a&#39;)
    links=[{&#39;url&#39;:x[&#39;href&#39;].replace(&#39;&amp;amp;&#39;,&#39;&amp;&#39;),&#39;id&#39;:x.get(&#39;id&#39;,&#39;&#39;)} for x in l if x.has_attr(&#39;href&#39;)]
    media_tags = soup.find_all([&#39;img&#39;, &#39;audio&#39;, &#39;video&#39;, &#39;source&#39;,&#39;embed&#39;])
    links+=[{&#39;url&#39;:x[&#39;src&#39;].replace(&#39;&amp;amp;&#39;,&#39;&amp;&#39;),&#39;id&#39;:x.get(&#39;id&#39;,&#39;&#39;) } for x in media_tags if x.has_attr(&#39;src&#39;)]
    links.append({&#39;url&#39;:url,&#39;id&#39;:url_id})
    #print(links)
    #links_list=[]
    root_links=[]
    forms=[]
    for l in links:
        x=l[&#39;url&#39;]
        l_id=l[&#39;id&#39;]
        if &#39;?&#39; in x and x.split(&#39;?&#39;)[0] not in root_links:
            a=urljoin(url, x)
            #print(a)
            if a.startswith(url.split(domain)[0]+domain)==True:
                forms.append(url_to_get_form(a,l_id))
                root_links.append(x.split(&#39;?&#39;)[0])
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
        for i in x[&#34;inputs&#34;]:
            if i[&#34;type&#34;].lower().strip() == &#34;password&#34;:
                return x
    raise Exception(&#34;No login form&#34;)</code></pre>
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
        for i in x[&#34;inputs&#34;]:
            if i[&#34;type&#34;].lower().strip() == &#34;file&#34;:
                l.append(x)
    if l==[]:
        raise Exception(&#34;No file upload form&#34;)
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
        for i in x[&#34;inputs&#34;]:
            if i[&#34;type&#34;].lower().strip() == &#34;file&#34;:
                l.append(x)
    if l==[]:
        raise Exception(&#34;No file upload form&#34;)
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
    &#34;&#34;&#34;
     this function is to get the names and values of input fields on a given webpage to scan.

     it takes 4 arguments:

     u: the page&#39;s link (http://...)
     value: (set by default to: False) to return the value of the fields set it to:True then the field&#39;s name and value will be string of 2
     values sperated by &#34;:&#34;
     timeout: (set by default to: 10) timeout flag for the request
     bypass: (set by default to: False) to bypass anti-crawlers

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;link=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.inputs(link)
    [&#39;email&#39;,&#39;password&#39;,&#39;rememberme&#39;]
    &gt;&gt;&gt;a=bane.inputs(link,value=True)
    [&#39;email&#39;,&#39;password&#39;,&#39;rememberme:yes&#39;,&#39;rememberme:no&#39;]

    &#34;&#34;&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if bypass == True:
        u += &#34;#&#34;
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    l = []
    try:
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        p = soup.find_all(&#34;textarea&#34;)
        for r in p:
            if r.has_attr(&#34;name&#34;):
                s = r.get(&#34;name&#34;)
                v = r.get(&#34;value&#34;)
                if v == None:
                    v = &#34;&#34;
            if value == True:
                y = s + &#34;:&#34; + v
            else:
                y = s
            if y not in l:
                l.append(y)
        p = soup.find_all(&#34;input&#34;)
        for r in p:
            v = &#34;&#34;
            if r.has_attr(&#34;name&#34;):
                s = str(r)
                s = s.split(&#39;name=&#34;&#39;)[1].split(&#34;,&#34;)[0]
                s = s.split(&#39;&#34;&#39;)[0].split(&#34;,&#34;)[0]
                if r.has_attr(&#34;value&#34;) and (value == True):
                    v = str(r)
                    v = v.split(&#39;value=&#34;&#39;)[1].split(&#34;,&#34;)[0]
                    v = v.split(&#39;&#34;&#39;)[0].split(&#34;,&#34;)[0]
            if value == True:
                y = s + &#34;:&#34; + v
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
<div class="desc"><p>this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram&hellip;).</p>
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
    &#34;&#34;&#34;
    this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram...).

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.media(url)

    &gt;&gt;&gt;bane.media(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    h = {}
    try:
        if bypass == True:
            u += &#34;#&#34;
        hea.update(headers)
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        ul = u.split(&#34;://&#34;)[1].split(&#39;&#34;&#39;)[0]
        ur = ul.replace(&#34;www.&#34;, &#34;&#34;)
        for a in soup.findAll(&#34;a&#34;):
            try:
                if (
                    a.has_attr(&#34;href&#34;)
                    and (u not in a[&#34;href&#34;])
                    and (ur not in a[&#34;href&#34;])
                    and (a[&#34;href&#34;][:4] == &#34;http&#34;)
                ):
                    txt = a.text
                    if a[&#34;href&#34;] not in h:
                        h.update({txt: a[&#34;href&#34;]})
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
    start_date = datetime.datetime.strptime(start_date, &#34;%Y-%m-%d&#34;)
    end_date = datetime.datetime.strptime(end_date, &#34;%Y-%m-%d&#34;)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date.strftime(&#34;%Y-%m-%d&#34;)</code></pre>
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
    return re.sub(r&#34;&lt;!--(.|\s|\n)*?--&gt;&#34;, &#34;&#34;, text, flags=re.DOTALL)</code></pre>
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
        cookie = &#34;&#34;
    if not new_cookies:
        new_cookies = &#34;&#34;
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
    for x in a[&#34;inputs&#34;]:
        if x[&#34;type&#34;].lower().strip() == &#34;password&#34;:
            d.update({x[&#34;name&#34;]: password})
        elif (
            x[&#34;type&#34;].lower().strip() == &#34;text&#34;
            or x[&#34;type&#34;].lower().strip() == &#34;email&#34;
            or x[&#34;type&#34;].lower().strip() == &#34;tel&#34;
        ):
            d.update({x[&#34;name&#34;]: username})
        else:
            d.update({x[&#34;name&#34;]: x[&#34;value&#34;]})
    return [d, a[&#34;action&#34;]]</code></pre>
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
    file_extension=&#34;png&#34;,
    email_extension=&#39;@gmail.com&#39;,
    phone_pattern=&#39;XXX-XXX-XXXX&#39;,
    dont_change={},
    number=(1, 9),
    leave_empty=[],
    dont_send=[],
    mime_type=None,
    predefined_inputs={},
    headers={}
):
    cookies = None
    h = {&#34;User-Agent&#34;: user_agent}
    if cookie:
        h.update({&#34;Cookie&#34;: cookie})
        cookies = cookie
    h.update(headers)
    
    try:
        r = requests.Session().get(url, proxies=proxy, headers=h, verify=False, timeout=timeout)
    except:
        return False
    cook = None
    try:
        cook = r.headers[&#34;Set-cookie&#34;]
    except:
        pass
    cookies = set_correct_cookies(cook, cookie=cookie)
    form = forms_parser_text(url, r.text)[form_index]
    h = {&#34;User-Agent&#34;: user_agent}
    if cookies and len(cookies.strip()) &gt; 0:
        h.update({&#34;Cookie&#34;: cookies})
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
        if x[&#34;type&#34;] not in [u&#34;radio&#34;, u&#34;checkbox&#34;]:
            d.append(x)
        if x[&#34;name&#34;] not in a and (x[&#34;type&#34;] == u&#34;radio&#34; or x[&#34;type&#34;] == u&#34;checkbox&#34;):
            a.append(x[&#34;name&#34;])
    for x in a:
        d.append(
            {
                &#34;type&#34;: [i[&#34;type&#34;] for i in l if i[&#34;name&#34;] == x][0],
                &#34;name&#34;: x,
                &#34;value&#34;: [i[&#34;value&#34;] for i in l if i[&#34;name&#34;] == x],
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
    domain=base_url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
    h={}
    if cookie:
        h.update({&#39;Cookie&#39;:cookie})
    if user_agent:
        h.update({&#39;User-Agent&#39;:user_agent})
    else:
        h.update({&#39;User-Agent&#39;:random.choice(ua)})
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
            soup = BeautifulSoup(response.content, &#39;html.parser&#39;)

            # Extract all links from the page
            for anchor_tag in soup.find_all(&#39;a&#39;, href=True):
                href = anchor_tag[&#39;href&#39;]
                absolute_url = urljoin(url, href)
                try:
                    this_domain=absolute_url.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0]
                except:
                    this_domain=&#39;&#39;

                if absolute_url not in visited_urls and absolute_url.split(&#39;?&#39;)[0].split(&#39;#&#39;)[0] not in root_urls and domain == this_domain:
                    visited_urls.add(absolute_url)
                    urls_to_visit.append(absolute_url)
                    root_urls.append(absolute_url.split(&#39;?&#39;)[0].split(&#39;#&#39;)[0])
            if include_id==True:
                collected_urls.add({&#39;url&#39;:url,&#39;id&#39;:anchor_tag.get(&#39;id&#39;,&#39;&#39;)})
            else:
                collected_urls.add(url)
            #print(len(collected_urls))

        except requests.exceptions.RequestException as e:
            print(&#34;Error fetching URL: {}&#34;.format(e))

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
    &#34;&#34;&#34;
    this function collects the subdomains found on the targeted webpage.

    the function takes those arguments:

    u: the targeted link
    timeout: (set by default to 10) timeout flag for the request
    bypass: (set by default to False) option to bypass anti-crawlers by simply adding &#34;#&#34; to the end of the link :)

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;url=&#39;http://www.example.com&#39;
    &gt;&gt;&gt;bane.subdomains_extract(url)

    &gt;&gt;&gt;bane.subdomains_extract(url,bypass=True)&#34;&#34;&#34;
    if urlparse(u).path == &#34;&#34;:
        u += &#34;/&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    h = {}
    if cookie:
        hea = {&#34;User-Agent&#34;: us, &#34;Cookie&#34;: cookie}
    else:
        hea = {&#34;User-Agent&#34;: us}
    hea.update(headers)
    try:
        if bypass == True:
            u += &#34;#&#34;
        c = requests.Session().get(
            u, headers=hea, proxies=proxy, timeout=timeout, verify=False
        ).text
        if html_comments == False:
            c = remove_html_comments(c)
        ul = u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
        soup = BeautifulSoup(c, &#34;html.parser&#34;)
        for a in soup.findAll(&#34;a&#34;):
            if (
                a.has_attr(&#34;href&#34;)
                and (ul.replace(&#34;www&#34;, &#34;&#34;) in a[&#34;href&#34;])
                and (ul not in a[&#34;href&#34;])
                and (a[&#34;href&#34;][:4] == &#34;http&#34;)
            ):
                txt = a.text
                try:
                    hr = a[&#34;href&#34;].split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
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
    cookie = &#34;&#34;
    for x in c2:
        cookie += x + &#34;=&#34; + c2[x] + &#34;;&#34;
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
    #print(&#39;&amp;&#39;.join(u.split(&#39;?&#39;)[1:]).replace(&#39;?&#39;,&#39;&amp;&#39;).split(&#39;&amp;&#39;))
    #print(u.split(&#39;?&#39;)[1].split(&#39;&amp;&#39;))
    inputs=[]
    for x in &#39;&amp;&#39;.join(u.split(&#39;?&#39;)[1:]).replace(&#39;?&#39;,&#39;&amp;&#39;).split(&#39;&amp;&#39;):
        try:
            inputs.append({&#39;name&#39;:x.split(&#39;=&#39;)[0],&#39;type&#39;:&#39;text&#39;,&#39;value&#39;:x.split(&#39;=&#39;)[1]})
        except:
            inputs.append({&#39;name&#39;:x.split(&#39;=&#39;)[0],&#39;type&#39;:&#39;text&#39;,&#39;value&#39;:&#39;&#39;})
    #inputs=[ {&#39;name&#39;:x.split(&#39;=&#39;)[0],&#39;type&#39;:&#39;text&#39;,&#39;value&#39;:x.split(&#39;=&#39;)[1]} for x in u.split(&#39;?&#39;)[1].split(&#39;&amp;&#39;)]
    return {
                    &#34;inputs&#34;: inputs,
                    &#34;action&#34;: u.split(&#39;?&#39;)[0],
                    &#34;enctype&#34;: &#39;application/x-www-form-urlencoded&#39;,
                    &#34;method&#34;: &#39;get&#39;,
                    &#34;id&#34;:url_id,
                    &#34;hidden_values&#34;: [],
                    &#34;is_url&#34;:True
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
<li><code><a title="bane.utils" href="index.md">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.utils.pager.cookies_to_dict" href="#bane.utils.pager.cookies_to_dict">cookies_to_dict</a></code></li>
<li><code><a title="bane.utils.pager.crawl" href="#bane.utils.pager.crawl">crawl</a></code></li>
<li><code><a title="bane.utils.pager.crawl_text" href="#bane.utils.pager.crawl_text">crawl_text</a></code></li>
<li><code><a title="bane.utils.pager.examine_js_code" href="#bane.utils.pager.examine_js_code">examine_js_code</a></code></li>
<li><code><a title="bane.utils.pager.extract_secrets_from_text" href="#bane.utils.pager.extract_secrets_from_text">extract_secrets_from_text</a></code></li>
<li><code><a title="bane.utils.pager.extract_urls_from_js" href="#bane.utils.pager.extract_urls_from_js">extract_urls_from_js</a></code></li>
<li><code><a title="bane.utils.pager.fetch_url" href="#bane.utils.pager.fetch_url">fetch_url</a></code></li>
<li><code><a title="bane.utils.pager.form_filler" href="#bane.utils.pager.form_filler">form_filler</a></code></li>
<li><code><a title="bane.utils.pager.forms" href="#bane.utils.pager.forms">forms</a></code></li>
<li><code><a title="bane.utils.pager.forms_parser" href="#bane.utils.pager.forms_parser">forms_parser</a></code></li>
<li><code><a title="bane.utils.pager.forms_parser_text" href="#bane.utils.pager.forms_parser_text">forms_parser_text</a></code></li>
<li><code><a title="bane.utils.pager.generate_human_poc" href="#bane.utils.pager.generate_human_poc">generate_human_poc</a></code></li>
<li><code><a title="bane.utils.pager.generate_random_html_input_color" href="#bane.utils.pager.generate_random_html_input_color">generate_random_html_input_color</a></code></li>
<li><code><a title="bane.utils.pager.generate_random_phone_number" href="#bane.utils.pager.generate_random_phone_number">generate_random_phone_number</a></code></li>
<li><code><a title="bane.utils.pager.generate_random_url" href="#bane.utils.pager.generate_random_url">generate_random_url</a></code></li>
<li><code><a title="bane.utils.pager.get_links_from_page_source" href="#bane.utils.pager.get_links_from_page_source">get_links_from_page_source</a></code></li>
<li><code><a title="bane.utils.pager.get_login_form" href="#bane.utils.pager.get_login_form">get_login_form</a></code></li>
<li><code><a title="bane.utils.pager.get_upload_form" href="#bane.utils.pager.get_upload_form">get_upload_form</a></code></li>
<li><code><a title="bane.utils.pager.get_upload_form_text" href="#bane.utils.pager.get_upload_form_text">get_upload_form_text</a></code></li>
<li><code><a title="bane.utils.pager.inputs" href="#bane.utils.pager.inputs">inputs</a></code></li>
<li><code><a title="bane.utils.pager.media" href="#bane.utils.pager.media">media</a></code></li>
<li><code><a title="bane.utils.pager.random_date" href="#bane.utils.pager.random_date">random_date</a></code></li>
<li><code><a title="bane.utils.pager.readable_js_code" href="#bane.utils.pager.readable_js_code">readable_js_code</a></code></li>
<li><code><a title="bane.utils.pager.remove_html_comments" href="#bane.utils.pager.remove_html_comments">remove_html_comments</a></code></li>
<li><code><a title="bane.utils.pager.set_correct_cookies" href="#bane.utils.pager.set_correct_cookies">set_correct_cookies</a></code></li>
<li><code><a title="bane.utils.pager.set_login_form" href="#bane.utils.pager.set_login_form">set_login_form</a></code></li>
<li><code><a title="bane.utils.pager.set_up_injection" href="#bane.utils.pager.set_up_injection">set_up_injection</a></code></li>
<li><code><a title="bane.utils.pager.sort_inputs" href="#bane.utils.pager.sort_inputs">sort_inputs</a></code></li>
<li><code><a title="bane.utils.pager.spider_url" href="#bane.utils.pager.spider_url">spider_url</a></code></li>
<li><code><a title="bane.utils.pager.subdomains_extract" href="#bane.utils.pager.subdomains_extract">subdomains_extract</a></code></li>
<li><code><a title="bane.utils.pager.update_cookies" href="#bane.utils.pager.update_cookies">update_cookies</a></code></li>
<li><code><a title="bane.utils.pager.url_to_get_form" href="#bane.utils.pager.url_to_get_form">url_to_get_form</a></code></li>
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