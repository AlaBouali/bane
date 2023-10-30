from bane.scanners.vulnerabilities.utils import *

class Shodan_Scanner:

    @staticmethod
    def scan(ip, api_key, file_name="shodan_report",save_to_file=False,proxy=None,http_proxies=None,socks4_proxies=None,socks5_proxies=None):
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        u = "https://api.shodan.io/shodan/host/{}?key={}".format(ip, api_key)
        try:
            r = requests.Session().get(u, headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},proxies=setup_proxy(proxies)).text
            if save_to_file==True:
                with open(file_name.split(".")[0] + ".json", "w") as outfile:
                    json.dump(json.loads(r), outfile, indent=4)
                outfile.close()
            return json.loads(r)
        except:
            return {}

