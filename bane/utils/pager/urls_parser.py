from .utils import *

class URLS_Parser:

    @staticmethod
    def url_to_get_form(u,url_id):
        #print('&'.join(u.split('?')[1:]).replace('?','&').split('&'))
        #print(u.split('?')[1].split('&'))
        inputs=[]
        for x in '&'.join(u.split('?')[1:]).replace('?','&').split('&'):
            try:
                inputs.append({'name':x.split('=')[0],'type':'text','value':x.split('=')[1]})
            except:
                inputs.append({'name':x.split('=')[0],'type':'text','value':''})
        #inputs=[ {'name':x.split('=')[0],'type':'text','value':x.split('=')[1]} for x in u.split('?')[1].split('&')]
        return {
                        "inputs": inputs,
                        "action": u.split('?')[0],
                        "enctype": 'application/x-www-form-urlencoded',
                        "method": 'get',
                        "id":url_id,
                        "hidden_values": [],
                        "is_url":True
                    }


    @staticmethod
    def get_links_from_page_source(soup,url,url_id):
        if url.endswith('/')==False:
            url+='/'
        domain=url.split('/')[0] if url.startswith('http')==False else url.split('://')[1].split('/')[0]
        l=soup.find_all('a')
        links=[{'url':x['href'].replace('&amp;','&'),'id':x.get('id',''),'is_url':True} for x in l if x.has_attr('href')]
        media_tags = soup.find_all(['img', 'audio', 'video', 'source','embed'])
        links+=[{'url':x['src'].replace('&amp;','&'),'id':x.get('id',''),'is_url':None } for x in media_tags if x.has_attr('src')]
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
                    forms.append(URLS_Parser.url_to_get_form(a,l_id))
                    root_links.append(x.split('?')[0])
        return forms



