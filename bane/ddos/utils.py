import requests, socks, os, sys, urllib, socket, random, time, threading, ssl
import urllib3,json
from collections import OrderedDict
from ..utils.socket_connection import *
try:
    if sys.version_info < (3, 0):
        from scapy.all import UDP,IP,DNS,DNSQR,Raw
    else:
        from kamene.all import UDP,IP,DNS,DNSQR,Raw
except:
    pass
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import the dependencies for each python version
if sys.version_info < (3, 0):
    # Python 2.x
    import httplib
    import urllib2
    try:
        from scapy.config import conf

        conf.ipv6_enabled = False
        from scapy.all import UDP,IP,DNS,DNSQR,Raw
    except:
        pass
else:
    # Python 3.x
    import http.client

    httplib = http.client
    import urllib.request

    urllib2 = urllib.request
    try:
        from kamene.config import conf

        conf.ipv6_enabled = False
        from kamene.all import UDP,IP,DNS,DNSQR,Raw
    except:
        pass
from struct import *
from ..utils.pager.rand_generator import *
from ..common.payloads import *
from ..utils.handle_files import *
from ..utils.proxer import *
from ..utils.pager import *
termux=False
adr=False

if os.path.isdir("/data/data") == True:
    adr = True  # the device is an android
if os.path.isdir("/data/data/com.termux/") == True:
    termux = True  # the application which runs the module is Termux
if (termux == False) or (adr == False):
    from bane.utils.swtch import *



class DDoS_Class:

    def done(self):
        if "stop" in dir(self):
            return False
        return True

    def reset(self):
        l = []
        for x in self.__dict__:
            self.__dict__[x] = None
            l.append(x)
        for x in l:
            delattr(self, x)

    def kill(self):
        self.stop = True
        a = self.__dict__["counter"]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
        return a

