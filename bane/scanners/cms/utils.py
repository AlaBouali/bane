import requests, random, json, sys,socket
import urllib3,time
from bane.scanners.vulnerabilities.vulns import vulners_search,Mixed_Content_Scanner,ClickJacking_Scanner,setup_proxy
from bane.gather_info.info_s import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bane.common.payloads import *

if sys.version_info < (3, 0):
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bane.utils.proxer import *
from bane.gather_info.ips import *