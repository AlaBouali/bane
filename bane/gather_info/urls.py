from bane.gather_info.utils import *


class URL_Info:

    @staticmethod
    def security_check(url,timeout=25,proxy=None,user_agent=None,cookie=None,headers={}):
        h={}
        pr=url.split('://')[0]
        dm=url.split('://')[1]
        report_url='https://sitecheck.sucuri.net/results/{}/{}'.format(pr,dm)
        if headers not in [{},None]:
            h.update({'Referer': report_url})
            h.update({'Accept': 'application/json'})
            h.update({'Sec-Fetch-Dest': 'empty'})
            h.update({'Sec-Fetch-Mode': 'cors'})
            h.update({'Sec-Fetch-Site': 'same-origin'})
            h.update({'Te': 'trailers'})
        if user_agent:
            h.update({"User-Agent": user_agent})
        else:
            h.update({"User-Agent": random.choice(Common_Variables.user_agents_list)})
        if cookie:
            h.update({"Cookie": cookie})
        h.update(headers)
        try:
            d= requests.Session().get('https://sitecheck.sucuri.net/api/v3/',params={'scan':url},headers=h,proxies=proxy,timeout=timeout).json()
            d.update({'report_url':report_url})
            return d
        except:
            return {}


    @staticmethod
    def deep_inspect(url,timeout=25,proxy=None,user_agent=None,cookie=None,headers={}):
        h={}
        if user_agent:
            h.update({"User-Agent": user_agent})
        else:
            h.update({"User-Agent": random.choice(Common_Variables.user_agents_list)})
        if cookie:
            h.update({"Cookie": cookie})
        h.update(headers)
        try:
            d= requests.Session().post('https://radar.cloudflare.com/scan?index=&_data=routes%2Fscan%2Findex',data={'url':url},headers=h,proxies=proxy,timeout=timeout).json()
            url_id=d['data']['result']['uuid']
            report_url='https://radar.cloudflare.com/scan/'+url_id
            while True:
                time.sleep(5)
                h={}
                if user_agent:
                    h.update({"User-Agent": user_agent})
                else:
                    h.update({"User-Agent": random.choice(Common_Variables.user_agents_list)})
                if cookie:
                    h.update({"Cookie": cookie})
                h.update(headers)
                d=requests.Session().get('https://radar.cloudflare.com/scan?index=&_data=routes%2Fscan%2Findex',data={'url':url},headers=h,proxies=proxy,timeout=timeout).json()
                if '"message":"OK"' in str(d):
                    break
            d.update({'report_url':report_url})
            return d
        except Exception as ex:
            return {}


    @staticmethod
    def http_options(
        u,
        timeout=10,
        user_agent=None,
        cookie=None,
        headers=None,
        proxy=None,
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        if headers:
            heads.update(headers)
        try:
            s = requests.session()
            a = dict(s.options(u, headers=heads, proxies=proxy, timeout=timeout).headers)
        except Exception as ex:
            return {}
        b = {}
        for x in a:
            if 'access-control-' in x.lower():
                b.update({x:a[x]})
        return b


    @staticmethod
    def headers(
        u,
        timeout=10,
        user_agent=None,
        cookie=None,
        headers=None,
        proxy=None,
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        if headers:
            heads.update(headers)
        try:
            #"safe": sec,
            s = requests.session()
            a = s.get(u, headers=heads, proxies=proxy, timeout=timeout).headers
        except Exception as ex:
            return None
        return a