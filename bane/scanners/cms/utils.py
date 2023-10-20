import requests, random, json, sys,socket
import urllib3,time
from bane.scanners.vulnerabilities.vulns import vulners_search,sniffable_links,page_clickjacking,setup_proxy
from bane.gather_info.info_s import get_subdomains,extract_root_domain

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bane.common.payloads import ua

if sys.version_info < (3, 0):
    from urlparse import urlparse
else:
    from urllib.parse import urlparse

from bs4 import BeautifulSoup
from bane.utils.proxer import get_requests_proxies_from_parameters