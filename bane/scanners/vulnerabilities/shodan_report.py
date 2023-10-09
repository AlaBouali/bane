from bane.scanners.vulnerabilities.utils import *


def shodan_report(ip, api_key, file_name="shodan_report",save_to_file=False,proxy=None):
    u = "https://api.shodan.io/shodan/host/{}?key={}".format(ip, api_key)
    try:
        r = requests.Session().get(u, headers={"User-Agent": random.choice(ua)},proxies=proxy).text
        if save_to_file==True:
            with open(file_name.split(".")[0] + ".json", "w") as outfile:
                json.dump(json.loads(r), outfile, indent=4)
            outfile.close()
        return json.loads(r)
    except:
        return {}

