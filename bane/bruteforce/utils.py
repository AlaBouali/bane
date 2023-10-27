import requests, random, smtplib, telnetlib, sys, os, hashlib, base64, subprocess, time, xtelnet, os, threading  # ,requests_ntlm
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from ftplib import FTP
from ..common.payloads import *
from ..utils.proxer import get_socks_proxy_socket

if os.path.isdir("/data/data") == True:
    adr = True
if os.path.isdir("/data/data/com.termux/") == True:
    termux = True
import pymysql
from ..utils.pager import *
from ..scanners.cms.wp import WORDPRESS,setup_proxy
from ..cryptographers.hasher import *
from ..utils.pager import *
from bane.utils import get_requests_proxies_from_parameters,get_socket_proxies_from_parameters,read_file



def process_threaded(a, check_interval=0.1):
    while True:
        try:
            if a.done() == True:
                try:
                    return a.result
                except:
                    pass
                try:
                    return a.counter
                except:
                    return
            time.sleep(check_interval)
        except KeyboardInterrupt:
            a.stop = True
            try:
                return a.result
            except:
                pass
            try:
                return a.counter
            except:
                pass

def load_word_list(l):
    if type(l)==list:
        return l
    return read_file(l)