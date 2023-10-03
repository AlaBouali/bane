import requests, urllib, socket, random, time, re, threading, sys, json, os, xtelnet
import bs4
from bs4 import BeautifulSoup
from bane.common.payloads import *
import tldextract
try:
    if sys.version_info < (3, 0):
        from scapy.config import conf

        conf.ipv6_enabled = False
        from scapy.all import *
    else:
        from kamene.config import conf

        conf.ipv6_enabled = False
        from kamene.all import IP,TCP,sr
except:
    pass
if os.path.isdir("/data/data/com.termux/") == False:
    import dns.resolver


def extract_root_domain(subdomain):
    extracted = tldextract.extract(subdomain)
    if extracted.suffix.count('.') > 1:
        root_domain = "{}.{}".format(extracted.domain,extracted.suffix)
    else:
        root_domain = extracted.registered_domain
    return root_domain




def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile("<.*?>")
    return re.sub(clean, "", text)



def get_banner(u, p=23, timeout=3, payload=None):
    try:
        return xtelnet.get_banner(u, p=p, timeout=timeout, payload=payload)
    except:
        return None




