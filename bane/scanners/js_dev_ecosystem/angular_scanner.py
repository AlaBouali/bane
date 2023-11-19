from ..cms.utils import *

class Angular_Scanner:

    @staticmethod
    def scan_core(version,user_agent=None,cookie=None,timeout=20,headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        url='https://security.snyk.io/package/npm/@angular%2Fcore/{}'.format(version)
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update(headers)
        try:
            r=requests.get(url,headers=heads,verify=False,proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies),timeout=timeout)
            soup = BeautifulSoup(r.text, 'html.parser')
            tb=soup.find_all('table')
            t=None
            for x in tb:
                if 'id="sortable-table"' in str(x):
                    t=x
                    break
            if t==None:
                return []
            d=[]
            for x in t.find('tbody').find_all('tr'):
                a=x.find_all('td')[0].find('a')
                d.append({'title':a.get_text().strip(),'url':'https://security.snyk.io/'+a['href']})
            return d
        except Exception as ex:
            return []
        
    @staticmethod
    def scan_package(package,version,user_agent=None,cookie=None,timeout=20,headers={},http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        url='https://security.snyk.io/package/npm/@angular%2F{}/{}'.format(package,version)
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            heads = {"User-Agent": us, "Cookie": cookie}
        else:
            heads = {"User-Agent": us}
        heads.update(headers)
        try:
            r=requests.get(url,headers=heads,verify=False,proxies=Vulnerability_Scanner_Utilities.setup_proxy(proxies),timeout=timeout)
            soup = BeautifulSoup(r.text, 'html.parser')
            tb=soup.find_all('table')
            t=None
            for x in tb:
                if 'id="sortable-table"' in str(x):
                    t=x
                    break
            if t==None:
                return []
            d=[]
            for x in t.find('tbody').find_all('tr'):
                a=x.find_all('td')[0].find('a')
                d.append({'title':a.get_text().strip(),'url':'https://security.snyk.io/'+a['href']})
            return d
        except Exception as ex:
            return []