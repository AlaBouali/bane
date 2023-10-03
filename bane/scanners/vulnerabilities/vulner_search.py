from bane.scanners.vulnerabilities.utils import *

def vulners_search(
    software,
    url="https://vulners.com/api/v3/burp/software/",
    file_name="",
    save_to_file=False,
    max_vulnerabilities=100,
    version="",
    software_type="software",
    user_agent=None,
    cookie=None,
    api_key='',
    proxy=None,
    timeout=20,
):
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
        us = random.choice(ua)
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
        ty = "software"
        if software_type:
            ty = software_type
        if ty not in ["software", "cpe"]:
            raise Exception('type must be: "software" or "cpe"')
        d = {
            "maxVulnerabilities": max_vuln,
            "version": ver,
            "type": ty,
            "software": software,
            'apikey':api_key
        }
        r = requests.get(
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
                l.append(
                     x[
                            "_source"
                        ]
                )
                i += 1
            return l
        else:
            return {'error':"couldn't find vulnerabilities for this version"}
    except:
        pass
    return []
