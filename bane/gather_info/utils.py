import requests, urllib, socket, random, time, re, threading, sys, json, os, xtelnet
import bs4
from bs4 import BeautifulSoup
from ..common.payloads import *
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

from ..utils.extrafun import *
if os.path.isdir("/data/data/com.termux/") == False:
    import dns.resolver






