from bane.scanners.vulnerabilities.utils import *

class Vulners_Search_Scanner:

    @staticmethod
    def scan(
        software,
        url="https://vulners.com/api/v3/burp/software/",
        file_name="",
        save_to_file=False,
        max_vulnerabilities=100,
        version="",
        user_agent=None,
        cookie=None,
        api_key='',
        timeout=20,
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None,
        basic_only=True
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)
        if api_key==None:
            api_key=''
        if not file_name:
            if version:
                file_name = software + "_" + version.replace(".", "-")
            else:
                file_name = software
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
        else:
            hea = {"User-Agent": us}
        try:
            ver = ""
            if version:
                ver = version
            max_vuln = 100
            if max_vulnerabilities:
                max_vuln = max_vulnerabilities
            d = {
                "maxVulnerabilities": max_vuln,
                "version": ver,
                "type": 'software',
                "software": software,
                'apikey':api_key
            }
            r = requests.Session().get(
                url,
                params=d,
                headers=hea,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            )
            c = json.loads(r.text)
            if c["result"] == "OK":
                if save_to_file==True:
                    with open(file_name.split(".")[0] + ".json", "w") as outfile:
                        json.dump(c, outfile, indent=4)
                    outfile.close()
                l = []
                m = c["data"]["search"]
                i = 0
                for x in m:
                    #print(x)
                    if software.lower() in str(x).lower():
                        l.append(
                            x[
                                    "_source"
                                ]
                        )
                        i += 1
                if basic_only==False:
                    return l
                else:
                    return [{'title':x.get('title',''),'description':x.get('description',''),'href':x.get('href',''),'sourceHref':x.get('sourceHref',''),'published':x.get('published',''),'cvelist':x.get('cvelist',[''])[0],'score':x.get('cvss',{'score':"N/A"})['score'],'vector':x.get('cvss',{'vector':"N/A"})['vector']} for x in l]
            else:
                return []#{'error':"couldn't find vulnerabilities for this version"}
        except Exception as ex:
            pass
        return []

    def scan_cpe(
        software,
        vendor,
        url="https://vulners.com/api/v3/burp/software/",
        file_name="",
        save_to_file=False,
        max_vulnerabilities=100,
        version="",
        user_agent=None,
        cookie=None,
        api_key='',
        timeout=20,
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None,
        proxy=None,
        basic_only=True
        ):
        proxies=Proxies_Interface.get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        if proxy==None:
                proxy=Vulnerability_Scanner_Utilities.setup_proxy(proxies)
        if api_key==None:
            api_key=''
        if not file_name:
            if version:
                file_name = software + "_" + version.replace(".", "-")
            else:
                file_name = software
        if user_agent:
            us = user_agent
        else:
            us = random.choice(Common_Variables.user_agents_list)
        if cookie:
            hea = {"User-Agent": us, "Cookie": cookie}
        else:
            hea = {"User-Agent": us}
        try:
            ver = ""
            if version:
                ver = version
            max_vuln = 100
            if max_vulnerabilities:
                max_vuln = max_vulnerabilities
            software="cpe:/a:{}:{}".format(vendor,software)
            d = {
                "maxVulnerabilities": max_vuln,
                "version": ver,
                "type": 'cpe',
                "software": software,
                'apikey':api_key
            }
            r = requests.Session().get(
                url,
                params=d,
                headers=hea,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            )
            c = json.loads(r.text)
            if c["result"] == "OK":
                if save_to_file==True:
                    with open(file_name.split(".")[0] + ".json", "w") as outfile:
                        json.dump(c, outfile, indent=4)
                    outfile.close()
                l = []
                m = c["data"]["search"]
                i = 0
                for x in m:
                    #print(x)
                    if software.lower() in str(x).lower():
                        l.append(
                            x[
                                    "_source"
                                ]
                        )
                        i += 1
                if basic_only==False:
                    return l
                else:
                    return [{'title':x.get('title',''),'description':x.get('description',''),'href':x.get('href',''),'sourceHref':x.get('sourceHref',''),'published':x.get('published',''),'cvelist':x.get('cvelist',[''])[0],'score':x.get('cvss',{'score':"N/A"})['score'],'vector':x.get('cvss',{'vector':"N/A"})['vector']} for x in l]
            else:
                return []#{'error':"couldn't find vulnerabilities for this version"}
        except:
            pass
        return []
