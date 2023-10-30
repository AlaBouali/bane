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
from .cookies_manager import *

def remove_html_comments(text):
    return re.sub(r"<!--(.|\s|\n)*?-->", "", text, flags=re.DOTALL)

