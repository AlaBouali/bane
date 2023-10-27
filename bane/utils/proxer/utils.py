import requests, socks, socket, random, re,os,sys,threading,ssl
import bs4,bane,json
from bs4 import BeautifulSoup
from bane.common.payloads import *
#from bane.utils.pager import crawl


def wrap_socket_with_ssl(sock,target_host):
    if sock==None:
        return
    if hasattr(ssl, 'PROTOCOL_TLS_CLIENT'):
        # Since Python 3.6
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    elif hasattr(ssl, 'PROTOCOL_TLS'):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    else:
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)#ssl.PROTOCOL_TLS)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context.wrap_socket(sock, server_hostname=target_host)


