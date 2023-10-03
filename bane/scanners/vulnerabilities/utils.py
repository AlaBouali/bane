import subprocess, os, xtelnet, sys, cgi, re, json,platform
from colorama import Fore, Back, Style

if platform.system()=='Java':
        Fore.WHITE = ""
        Fore.GREEN = ""
        Fore.RED = ""
        Fore.YELLOW = ""
        Fore.BLUE = ""
        Fore.MAGENTA = ""
        Style.RESET_ALL = ""

if sys.version_info < (3, 0):
    if (sys.platform.lower() == "win32") or (sys.platform.lower() == "win64"):
        Fore.WHITE = ""
        Fore.GREEN = ""
        Fore.RED = ""
        Fore.YELLOW = ""
        Fore.BLUE = ""
        Fore.MAGENTA = ""
        Style.RESET_ALL = ""
    import urllib, HTMLParser
    from urlparse import urlparse
    from urllib import unquote as url_decode
else:
    from urllib.parse import urlparse
    from urllib.parse import unquote as url_decode
    import urllib.parse as urllib
    import html.parser as HTMLParser

unicode = str
import requests, socket, random, time, ssl
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import bs4,socks
from bs4 import BeautifulSoup
from bane.common.payloads import *
from bane.utils.pager import *
from bane.utils.js_fuck import js_fuck
from bane.utils.handle_files import write_file, delete_file
from bane.gather_info.info_s import extract_root_domain


def random_string(size):
    s = ""
    for x in range(size):
        s += random.choice(lis)
    return s


def setup_to_submit(form):
    d = {}
    f = {}
    for x in form["inputs"]:
        if x["type"] == "file":
            f.update({x["name"]: x["value"]})
        else:
            d.update({x["name"]: x["value"]})
    return d, f


def setup_proxy(pr, prs):
    if pr:
        return pr
    if prs:
        return random.choice(prs)
    return None


def setup_ua(usra):
    if usra:
        return usra
    return random.choice(ua)


def valid_parameter(parm):
    try:
        float(parm)
        return False
    except:
        return True

