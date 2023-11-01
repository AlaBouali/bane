class Cookies_Manager:

    @staticmethod
    def cookies_to_dict(cookies):
        if cookies==None or cookies.strip()=='':
            return {}
        d = {}
        a = cookies.split(";")
        for x in a:
            if "=" in x:
                d.update({x.split("=")[0].strip(): x.split("=")[1].strip()})
        return d


    @staticmethod
    def update_cookies(cookies, cook):
        c1 = {}
        c2 = {}
        if cookies:
            c1 = Cookies_Manager.cookies_to_dict(cookies)
        if cook:
            c2 = Cookies_Manager.cookies_to_dict(cook)
        c2.update(c1)
        cookie = ""
        for x in c2:
            cookie += x + "=" + c2[x] + ";"
        return cookie


    @staticmethod
    def set_correct_cookies(new_cookies, cookie=None):
        if not cookie:
            cookie = ""
        if not new_cookies:
            new_cookies = ""
        if cookie and len(cookie) > 0:
            if new_cookies and len(new_cookies) > 0:
                cookies = Cookies_Manager.update_cookies(new_cookies, cookie)
            else:
                cookies = cookie
        else:
            cookies = new_cookies
        return cookies

