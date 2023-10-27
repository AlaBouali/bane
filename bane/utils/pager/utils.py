import requests, random, re, time, furl, sys, datetime , string,json,ast

try:
    import jsbeautifier
except:
    pass
if sys.version_info < (3, 0):
    from urlparse import urlparse,urljoin
    from urllib import unquote as url_decode
else:
    from urllib.parse import urlparse,urljoin
    from urllib.parse import unquote as url_decode



import urllib3



#from bane.cryptographers.hasher import base64_decode
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import bs4
from bs4 import BeautifulSoup
from bane.common.payloads import *
from bane.gather_info.info_s import extract_root_domain

def remove_html_comments(text):
    return re.sub(r"<!--(.|\s|\n)*?-->", "", text, flags=re.DOTALL)


def cookies_to_dict(cookies):
    d = {}
    a = cookies.split(";")
    for x in a:
        if "=" in x:
            d.update({x.split("=")[0].strip(): x.split("=")[1].strip()})
    return d


def update_cookies(cookies, cook):
    c1 = {}
    c2 = {}
    if cookies:
        c1 = cookies_to_dict(cookies)
    if cook:
        c2 = cookies_to_dict(cook)
    c2.update(c1)
    cookie = ""
    for x in c2:
        cookie += x + "=" + c2[x] + ";"
    return cookie


def set_correct_cookies(new_cookies, cookie=None):
    if not cookie:
        cookie = ""
    if not new_cookies:
        new_cookies = ""
    if cookie and len(cookie) > 0:
        if new_cookies and len(new_cookies) > 0:
            cookies = update_cookies(new_cookies, cookie)
        else:
            cookies = cookie
    else:
        cookies = new_cookies
    return cookies

