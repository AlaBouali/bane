import subprocess, os, xtelnet, sys, cgi, re, json,platform
from colorama import Fore, Back, Style
from bane.utils.proxer import load_and_parse_proxies_all,get_requests_proxies_from_parameters
from bane.utils.handle_files import read_file,write_file,delete_file,clear_file,create_file

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
from bane.gather_info.ips import check_ip_via_shodan


def random_string(size):
    s = ""
    for x in range(size):
        s += random.choice(Common_Variables.source_string)
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


def setup_proxy(proxies):
    return random.choice(proxies)



def setup_ua(usra):
    if usra:
        return usra
    return random.choice(Common_Variables.user_agents_list)


def valid_parameter(parm):
    try:
        float(parm)
        return False
    except:
        return True

