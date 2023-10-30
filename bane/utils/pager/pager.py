from .utils import *

from .rand_generator import *
from .form_file_upload import *
from .forms_filler_file import *
from .forms_finder_file import *
from .set_login_form import *
from .urls_parser import *


class Pager_Interface:

    @staticmethod
    def spider_url(base_url, include_links=False, include_id=False,max_pages=5,timeout=15,cookie=None,user_agent=None,proxy=None,headers={},parse_forms=False,only_urls=True):
        domain=base_url.split('://')[1].split('/')[0]
        h={}
        if cookie:
            h.update({'Cookie':cookie})
        if user_agent:
            h.update({'User-Agent':user_agent})
        else:
            h.update({'User-Agent':random.choice(Common_Variables.user_agents_list)})
        h.update(headers)
        visited_urls = set()
        urls_to_visit = [base_url]
        collected_urls = []
        root_urls=[]

        while urls_to_visit and len(collected_urls) < max_pages:
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
                    data={'url':url,'id':anchor_tag.get('id','')}
                if parse_forms==True:
                    data={'url':url,'id':anchor_tag.get('id',''),'forms':FORMS_FINDER.forms_parser_text(url,response.text,include_links=include_links)}
                if only_urls==True:
                    data=url
                if type(data)==str:
                    if data not in collected_urls:
                        collected_urls.append(data)
                else:
                    safe=True
                    for x in collected_urls:
                        if x['url']==data['url']:
                            safe=False
                    if safe==True:
                        collected_urls.append(data)
                #print(collected_urls)
                #print(len(collected_urls))
            except requests.exceptions.RequestException as e:
                print("Error fetching URL: {}".format(e))
                return collected_urls
        return collected_urls







    @staticmethod
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



    @staticmethod
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
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
        else:
            hea = {"User-Agent": us}
        hea.update(headers)
        try:
            return requests.Session().get(u,timeout=timeout,proxies=proxy,verify=False,headers=hea).text
        except:
            return ''



    @staticmethod
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


    @staticmethod
    def readable_js_code(code):
        return jsbeautifier.beautify(code)


    @staticmethod
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
            us = random.choice(Common_Variables.user_agents_list)
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
            secrets.append({'url':u,'secrets':Pager_Interface.extract_secrets_from_text(code)})#,'endpoints':extract_urls_from_js(code,u)})
            for script in script_tags:
                if script.has_attr('src'):
                    url=urljoin(u,script['src'])
                    url_domain=url.split('://')[1].split('/')[0]
                    if Subdomain_Info.extract_root_domain(url_domain)==Subdomain_Info.extract_root_domain(domain):
                        #print(url_domain)
                        code=Pager_Interface.fetch_url(url,user_agent=user_agent,timeout=timeout,proxy=proxy,cookie=cookie,headers=headers)
                        secrets.append({'url':url,'secrets':Pager_Interface.extract_secrets_from_text(code)})#,'endpoints':extract_urls_from_js(code,url)})

        except Exception as ex:
            pass
        return [ x for x in secrets if len(list(x['secrets'].keys()))>0]



    @staticmethod
    def extract_secrets_from_text(js_content):
        tokens_dict = {}
        for key, pattern in Common_Variables.js_exposed_secrets_regexs.items():
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
                                if any(item in str(match).lower() for item in Common_Variables.json_configs_signatures)==True and match not in l:
                                    l.append(match)
                            if len(l)>0:
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
                            if len(l)>0:
                                tokens_dict[key] = l
                except Exception as ex:
                    pass
        return tokens_dict