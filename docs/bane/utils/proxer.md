<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.utils.proxer API documentation</title>
<meta content="" name="description"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" rel="preload stylesheet"/>
<link as="style" crossorigin="" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" rel="stylesheet preload"/>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script crossorigin="" defer="" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</meta></head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.utils.proxer</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import requests, socks, socket, random, re,os,sys
import bs4
from bs4 import BeautifulSoup
from bane.common.payloads import *
from bane.utils.pager import crawl


def proxyscrape(protocol="http", timeout=10, country="all", ssl="all", anonymity="all",proxy=None):
    if protocol.lower() not in ("http", "socks4", "socks5", "all"):
        raise Exception(
            'protocol value must be: "http" or "socks4" or "socks5" or "all"'
        )
    if ssl.lower() not in ("no", "yes", "all"):
        raise Exception('protocol value must be: "no" or "yes" or "all"')
    if anonymity.lower() not in ("elite", "anonymous", "transparent", "all"):
        raise Exception(
            'protocol value must be: "elite" or "anonymous" or "transparent" or "all"'
        )
    return requests.Session().get(
        "https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol="
        + protocol
        + "&amp;timeout="
        + str(timeout * 1000)
        + "&amp;country="
        + country
        + "&amp;ssl="
        + ssl
        + "&amp;anonymity="
        + anonymity,
        headers={"User-Agent": random.choice(ua)},
        proxies=proxy
    ).text.split("\r\n")


def proxy_check(ip, p, proto="http",username=None,password=None, timeout=5):
    """
    this function is to check if the proxy is dead or not.

    it takes the following arguments:

    proto: (set by default to: http) the proxy type: http/https/socks4/socks5
    ip: proxy's ip
    p: proxy's port
    timeout: (set by default to: 5) the connection's timeout
    """
    i = False
    if proto == "http":
        if username==None and password==None:
            proxy={"http": "http://{}:{}".format(ip,p)}
        else:
            proxy={"http": "http://{}:{}@{}:{}".format(username,password,ip,p)}
        try:
            requests.Session().get(
                "http://ipinfo.io/ip",
                proxies=proxy,
                headers={"User-Agent": random.choice(ua)},
                timeout=timeout,
            )
            i = True
        except:
            pass
    elif proto == "socks4":
        try:
            s = socks.socksocket()
            s.setproxy( 
                    proxy_type=socks.SOCKS4,
                    addr=ip,
                    port=p,
                    username=username,
                    password=password,
            )
            s.settimeout(timeout)
            s.connect(("www.google.com", 80))
            s.close()
            i = True
        except:
            pass
    elif proto == "socks5":
        try:
            s = socks.socksocket()
            s.setproxy( 
                    proxy_type=socks.SOCKS5,
                    addr=ip,
                    port=p,
                    username=username,
                    password=password,
            )
            s.settimeout(timeout)
            s.connect(("www.google.com", 80))
            s.close()
            i = True
        except:
            pass
    return i


def get_tor_socks5_proxy_windows(host=tor_proxy_host,port=tor_proxy_socks5_port_windows):
    proxy=tor_socks5_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy


def get_tor_socks5_proxy_linux(host=tor_proxy_host,port=tor_proxy_socks5_port_linux):
    proxy=tor_socks5_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy


def get_tor_socks5_proxy():
    if (sys.platform.lower() == "win32") or (sys.platform.lower() == "win64"):
        return get_tor_socks5_proxy_windows()
    return get_tor_socks5_proxy_linux()


def get_tor_http_proxy(host=tor_proxy_host,port=tor_proxy_http_port):
    proxy=tor_http_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy


def get_burpsuit_proxy(host=burpsuit_proxy_host,port=burpsuit_proxy_port):
    proxy=burpsuit_http_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy


def get_socks5_proxy_socket(host,port,proxy_host,proxy_port,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        s.setproxy( 
                    proxy_type=socks.SOCKS5,
                    addr=proxy_host,
                    port=proxy_port,
                    username=username,
                    password=password,
            )
        s.connect((host,port))
        return s
    except:
        return


def get_socks4_proxy_socket(host,port,proxy_host,proxy_port,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        s.setproxy( 
                    proxy_type=socks.SOCKS4,
                    addr=proxy_host,
                    port=proxy_port,
                    username=username,
                    password=password,
            )
        s.connect((host,port))
        return s
    except:
        return


def get_socks_proxy_socket(host,port,proxy_host,proxy_port,proxy_type,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        if proxy_type==4:
            s.setproxy( 
                        proxy_type=socks.SOCKS4,
                        addr=proxy_host,
                        port=proxy_port,
                        username=username,
                        password=password,
                )
        elif proxy_type==5:
            s.setproxy( 
                        proxy_type=socks.SOCKS5,
                        addr=proxy_host,
                        port=proxy_port,
                        username=username,
                        password=password,
                )
        s.connect((host,port))
        return s
    except:
        return


def get_http_proxy_socket(host,port,proxy_host,proxy_port,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        s.setproxy( 
                    proxy_type=socks.HTTP,
                    addr=proxy_host,
                    port=proxy_port,
                    username=username,
                    password=password,
            )
        s.connect((host,port))
        return s
    except:
        return


def get_socks5_proxy(proxy_host,proxy_port,username=None,password=None):
    if username==None and password==None:
        return {'http': 'socks5h://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks5h://{}:{}'.format(proxy_host,proxy_port)}
    return {'http': 'socks5h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port), 'https': 'socks5h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port)}


def get_socks4_proxy(proxy_host,proxy_port,username=None,password=None):
    if username==None and password==None:
        return {'http': 'socks4h://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks4h://{}:{}'.format(proxy_host,proxy_port)}
    return {'http': 'socks4h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port), 'https': 'socks4h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port)}


def get_http_proxy(proxy_host,proxy_port,username=None,password=None):
    if username==None and password==None:
        return {'http': 'http://{}:{}'.format(proxy_host,proxy_port), 'https': 'http://{}:{}'.format(proxy_host,proxy_port)}
    return {'http': 'http://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port), 'https': 'http://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port)}



'''def masshttp(count=None, timeout=15):
    """
    this function gather up thousands of HTTP / HTTPS proxies from www.proxyserverlist24.top and proxy-daily.com
    those proxies are not recommended to be used as reliable ones all the time, i use them here just to distribute my attacks
    on next functions...
    if you are willing to use them please check them first!!!
    the function takes an argument (*args) which is the number of proxies to return, in case of no argument given it will
    return the whole list.
    usage:
    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.masshttp()
    &gt;&gt;&gt;bane.masshttp(1500)
    """
    if count != None:
        m = count
    else:
        m = 999999
    u = "http://www.proxyserverlist24.top/#"
    t = []
    l = []
    h = []
    try:
        h3tags1 = crawl(u, timeout=timeout)
        h3tags = []
        for x in h3tags1.keys():
            h3tags.append(h3tags1[x][1])
        for a in h3tags:
            try:
                if ("proxy-server" in str(a)) and ("#" not in (str(a))):
                    try:
                        if a not in l:
                            l.append(a)
                    except Exception as xx:
                        pass
            except Exception as ex:
                pass
                continue
    except Exception as e:
        pass
    for u in l:
        try:
            a = requests.Session().get(
                u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
            )
            ips = re.findall(
                "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                a.text,
            )
            t += ips
        except Exception as e:
            pass
    l = []
    u = "https://www.dailyfreeproxy.com/#"
    try:
        h3tags1 = crawl(u, timeout=timeout)
        h3tags = []
        for x in h3tags1.keys():
            h3tags.append(h3tags1[x][1])
        for a in h3tags:
            try:
                if ("-http" in str(a)) and ("#" not in (str(a))):
                    try:
                        a = str(a)
                        if a not in l:
                            l.append(a)
                    except Exception as xx:
                        pass
            except Exception as ex:
                continue
    except Exception as e:
        pass
    for u in l:
        try:
            a = requests.Session().get(
                u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
            )
            ips = re.findall(
                "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                a.text,
            )
            t += ips
        except Exception as e:
            pass
        u = "http://proxy-daily.com/#"
        try:
            r = requests.Session().get(
                u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
            ).text
            soup = BeautifulSoup(r, "html.parser")
            l = soup.findAll("div")
        except:
            pass
        p = []
        ips = []
        for x in l:
            try:
                ips = re.findall(
                    "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                    str(x),
                )
                if (ips) and (ips not in p):
                    p.append(ips)
            except:
                pass
    try:
        t += p[0]
    except:
        pass
    if count != None:
        while True:
            o = random.choice(t)
            h.append(o)
            if (len(h) == m) or (len(h) == len(t)):
                break
    else:
        h = t
    return h


def massocks4(count=None, timeout=15):
    """
    this function gather up thousands of SOCKS4 proxies from www.proxyserverlist24.top and proxy-daily.com
    those proxies are not recommended to be used as reliable ones all the time, i use them here just to distribute my attacks
    on next functions...
    if you are willing to use them please check them first!!!
    the function takes an argument (*args) which is the number of proxies to return, in case of no argument given it will
    return the whole list.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.massocks4()

    &gt;&gt;&gt;bane.massocks4(100)
    """
    if count != None:
        m = count
    else:
        m = 999999
    s4 = []
    t = []
    l = []
    u = "https://www.dailyfreeproxy.com/#"
    try:
        h3tags1 = crawl(u, timeout=timeout)
        h3tags = []
        for x in h3tags1.keys():
            h3tags.append(h3tags1[x][1])
        for a in h3tags:
            try:
                if ("-socks4" in str(a)) and ("#" not in (str(a))):
                    try:
                        a = str(a)
                        if a not in l:
                            l.append(a)
                    except Exception as xx:
                        pass
            except Exception as ex:
                continue
    except Exception as e:
        pass
    for u in l:
        try:
            a = requests.Session().get(
                u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
            )
            ips = re.findall(
                "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                a.text,
            )
            t += ips
        except Exception as e:
            pass
    l = []
    u = "http://proxy-daily.com/#"
    try:
        r = requests.Session().get(
            u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
        ).text
        soup = BeautifulSoup(r, "html.parser")
        l = soup.findAll("div")
    except Exception as e:
        pass
    p = []
    for x in l:
        try:
            ips = re.findall(
                "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                str(x),
            )
            if (ips) and (ips not in p):
                p.append(ips)
        except Exception as x:
            pass
    try:
        t += p[2]
    except:
        pass
    if count != None:
        while True:
            o = random.choice(t)
            s4.append(o)
            if (len(s4) == m) or (len(s4) == len(t)):
                break
    else:
        s4 = t
    return s4


def massocks5(count=None, timeout=15):
    """
    this function gather up thousands of SOCKS5 proxies from www.proxyserverlist24.top and proxy-daily.com
    those proxies are not recommended to be used as reliable ones all the time, i use them here just to distribute my attacks
    on next functions...
    if you are willing to use them please check them first!!!
    the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
    return the whole list.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.massocks5()

    &gt;&gt;&gt;bane.massocks5(500)
    """
    if count != None:
        m = count
    else:
        m = 999999
    l = []
    t = []
    u = "https://www.dailyfreeproxy.com/#"
    try:
        h3tags1 = crawl(u, timeout=timeout)
        h3tags = []
        for x in h3tags1.keys():
            h3tags.append(h3tags1[x][1])
        for a in h3tags:
            try:
                if ("-socks5" in str(a)) and ("#" not in (str(a))):
                    try:
                        a = str(a)
                        if a not in l:
                            l.append(a)
                    except Exception as xx:
                        pass
            except Exception as ex:
                continue
    except Exception as e:
        pass
    for u in l:
        try:
            a = requests.Session().get(
                u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
            )
            ips = re.findall(
                "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                a.text,
            )
            t += ips
        except Exception as e:
            pass
    u = "http://www.live-socks.net/#"
    l = []
    s5 = []
    try:
        r = requests.Session().get(
            u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
        ).text
        soup = BeautifulSoup(r, "html.parser")
        h3 = soup.find_all("h3", class_="post-title entry-title")
        for ha in h3:
            h3tags = ha.find_all("a")
            for a in h3tags:
                try:
                    a = str(a)
                    if "socks-5" in a:
                        a = a.split('href="')[1]
                        a = a.split('"')[0]
                        if a not in l:
                            l.append(a)
                except Exception as ex:
                    continue
    except Exception as e:
        pass
    for u in l:
        try:
            a = requests.Session().get(
                u, headers={"User-Agent": random.choice(ua)}, timeout=timeout
            )
            ips = re.findall(
                "(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",
                a.text,
            )
            for x in ips:
                if x not in t:
                    t.append(x)
        except Exception as e:
            pass
    if count != None:
        while True:
            o = random.choice(t)
            s5.append(o)
            if (len(s5) == m) or (len(s5) == len(t)):
                break
    else:
        s5 = t
    return s5


def http(logs=True, count=300, timeout=15):
    """
    this function gather up hundreds of HTTP proxies from many sources.
    those proxies are recommended to be used as reliable ones all the time.
    the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
    return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn
    off the the typing if you set it to: False.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.http()

    &gt;&gt;&gt;bane.http(300)"""
    hsl = []
    u = "https://free-proxy-list.net/"
    try:
        if logs == True:
            print("[+]Checking: {}".format(u))
        c = requests.Session().get(u, timeout=timeout).text
        a = 0
        soup = BeautifulSoup(c, "html.parser")
        y = soup.find_all("tr")
        for x in y:
            try:
                a += 1
                x = str(x)
                ip = x.split("&lt;tr&gt;&lt;td&gt;")[1].split("=")[0]
                ip = ip.split("&lt;/td&gt;")[0].split("=")[0]
                p = x.split("&lt;/td&gt;&lt;td&gt;")[1].split("=")[0]
                p = p.split("&lt;/td&gt;")[0].split("=")[0]
                pr = ip + ":" + p
                if pr not in hsl:
                    hsl.append(pr)
                    if (a &gt; 300) or (len(hsl) == count):
                        break
            except Exception as e:
                pass
    except Exception as e:
        pass
    """
 for i in range(1,7):
  if len(hsl)==count:
    break
  try:
   u='https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-'+str(i)
   if logs==True:
    print("[+]Checking: {}".format(u))
   c=requests.Session().get(u,timeout=timeout).text
   soup = BeautifulSoup(c,"html.parser")
   y= soup.find_all("tr")
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
       pass 
     else:
      ip= str(z[1]).split('&lt;td&gt;')[1].split('=')[0]
      ip=ip.split('&lt;/td&gt;')[0].split('=')[0]
      p= str(z[2]).split('&lt;td&gt;')[1].split('=')[0]
      p=p.split('&lt;/td&gt;')[0].split('=')[0]
      pr=ip+':'+p
      if pr not in hsl:
       hsl.append(pr)
       if len(hsl)==count:
         break
    except Exception as e:
     pass
  except Exception as e:
   pass
 """
    ur = [
        "http://www.gatherproxy.com/proxylist/anonymity/?t=Elite",
        "http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous",
    ]
    for u in ur:
        if len(hsl) == count:
            break
        try:
            if logs == True:
                print("[+]Checking: {}".format(u))
            y = []
            c = requests.Session().get(u, timeout=timeout).text
            soup = BeautifulSoup(c, "html.parser")
            for r in soup.find_all("script"):
                h = "".join(map(str, r.contents))
                if "gp.insertPrx" in h:
                    s = h.split(":")
                    ip = s[3].split(",")[0].replace('"', "")
                    p = str(int(s[5].split(",")[0].replace('"', ""), 16))
                    pr = ip + ":" + p
                    if pr not in hsl:
                        hsl.append(pr)
                        if len(hsl) == count:
                            break
        except Exception as e:
            pass
    return hsl


def https(logs=True, count=200, timeout=15):
    """
    this function gather up hundreds of HTTPS proxies from many sources.
    those proxies are recommended to be used as reliable ones all the time.
    the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
    return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn
    off the the typing if you set it to: False.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.https()

    &gt;&gt;&gt;bane.https(200)
    """
    dn = "abcdefghijklmnopqrstuvwxyz"
    hl = []
    u = "https://www.sslproxies.org/"
    try:
        if logs == True:
            print("[+]Checking: {}".format(u))
        c = requests.Session().get(u, timeout=timeout).text
        soup = BeautifulSoup(c, "html.parser")
        y = soup.find_all("tr")
        a = 0
        for x in y:
            try:
                x = str(x)
                ip = x.split("&lt;/td&gt;")[0].split("=")[0]
                ip = ip.split("&lt;tr&gt;&lt;td&gt;")[1].split("=")[0]
                p = x.split("&lt;/td&gt;&lt;td&gt;")[1].split("=")[0]
                p = p.split("&lt;/td&gt;")[0].split("=")[0]
                d = False
                for o in dn:
                    if (o in ip.lower()) or (o in p.lower()):
                        d = True
                if d == False:
                    pr = ip + ":" + p
                    a += 1
                    if pr not in hl:
                        hl.append(pr)
                        if (a == 200) or (len(hl) == count):
                            a = 0
                            break
            except:
                pass
    except:
        pass
    hl = hl[0 : len(hl) - 4]
    """
 ur=['https://list.proxylistplus.com/ssl-List-1', 'https://list.proxylistplus.com/ssl-List-2']
 for u in ur:
  if len(hl)==count:
    break
  try:
   if logs==True:
    print("[+]Checking: {}".format(u))
   c=requests.Session().get(u,timeout=timeout).text
   soup = BeautifulSoup(c,"html.parser")
   y= soup.find_all("tr")
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
      pass 
     else:
       ip= str(z[1]).split('&lt;td&gt;')[1].split('=')[0]
       ip=ip.split('&lt;/td&gt;')[0].split('=')[0]
       p= str(z[2]).split('&lt;td&gt;')[1].split('=')[0]
       p=p.split('&lt;/td&gt;')[0].split('=')[0]
       d=False
       for o in dn:
        if ((o in ip.lower()) or (o in p.lower())):
         d=True
       if d==False:
        pr=ip+':'+p
        a+=1
        if pr not in hl:
         hl.append(pr)
         if (len(hl)==count):
          break
    except Exception as e:
     pass
  except Exception as e:
   pass
 """
    return hl


def socks5(logs=True, count=100, timeout=15):
    """
    this function gather up hundreds of SOCKS5 proxies from many sources.
    those proxies are recommended to be used as reliable ones all the time.
    the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
    return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn
    off the the typing if you set it to: False.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.socks5()

    &gt;&gt;&gt;bane.socks5(50)"""
    s5l = []
    u = "https://www.socks-proxy.net/"
    try:
        if logs == True:
            print("[+]Checking: {}".format(u))
        c = requests.Session().get(u, timeout=timeout).text
        soup = BeautifulSoup(c, "html.parser")
        y = soup.find_all("tr")
        for x in y:
            if "Socks5" in str(x):
                try:
                    x = str(x)
                    ip = x.split("&lt;/td&gt;")[0].split("=")[0]
                    ip = ip.split("&lt;tr&gt;&lt;td&gt;")[1].split("=")[0]
                    p = x.split("&lt;/td&gt;&lt;td&gt;")[1].split("=")[0]
                    p = p.split("&lt;/td&gt;")[0].split("=")[0]
                    pr = ip + ":" + p
                    if pr not in s5l:
                        s5l.append(pr)
                        if len(s5l) == count:
                            break
                except:
                    pass
    except:
        pass
    """
 ur=["https://list.proxylistplus.com/Socks-List-1"," https://list.proxylistplus.com/Socks-List-2"]
 for u in ur:
  if len(s5l)==count:
   break
  try:
   if logs==True:
    print("[+]Checking: {}".format(u))
   c=requests.Session().get(u,timeout=timeout).text
   s = BeautifulSoup(c,"html.parser")
   y=s.find_all('tr')
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
      pass 
     else:
      if "Socks5" in str(x):
       ip= str(z[1]).split('&lt;td&gt;')[1].split('=')[0]
       ip=ip.split('&lt;/td&gt;')[0].split('=')[0]
       p= str(z[2]).split('&lt;td&gt;')[1].split('=')[0]
       p=p.split('&lt;/td&gt;')[0].split('=')[0]
       pr=ip+':'+p
       if pr not in s5l:
        s5l.append(pr)
        if len(s5l)==count:
          break
    except Exception as e:
     pass
  except Exception as e:
   pass
 """
    return s5l


def socks4(logs=True, count=30, timeout=15):
    """
    this function gather up hundreds of SOCKS4 proxies from many sources.
    those proxies are recommended to be used as reliable ones all the time.
    the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
    return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn
    off the the typing if you set it to: False.

    usage:

    &gt;&gt;&gt;import bane
    &gt;&gt;&gt;bane.socks4()

    &gt;&gt;&gt;bane.socks4(50)"""
    s4l = []
    u = "https://www.socks-proxy.net/"
    try:
        if logs == True:
            print("[+]Checking: {}".format(u))
        c = requests.Session().get(u, timeout=timeout).text
        soup = BeautifulSoup(c, "html.parser")
        y = soup.find_all("tr")
        for x in y:
            if "Socks4" in str(x):
                try:
                    x = str(x)
                    ip = x.split("&lt;/td&gt;")[0].split("=")[0]
                    ip = ip.split("&lt;tr&gt;&lt;td&gt;")[1].split("=")[0]
                    p = x.split("&lt;/td&gt;&lt;td&gt;")[1].split("=")[0]
                    p = p.split("&lt;/td&gt;")[0].split("=")[0]
                    pr = ip + ":" + p
                    if pr not in s4l:
                        s4l.append(pr)
                        if len(s4l) == count:
                            break
                except Exception as e:
                    pass
    except Exception as e:
        pass
    """ur=["https://list.proxylistplus.com/Socks-List-1"," https://list.proxylistplus.com/Socks-List-2"]
 for u in ur:
  if len(s4l)==count:
   break
  try:
   if logs==True:
    print("[+]Checking: {}".format(u))
   c=requests.Session().get(u,timeout=timeout).text
   s = BeautifulSoup(c,"html.parser")
   y=s.find_all('tr')
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
      pass 
     else:
      if "Socks4" in str(x):
       ip= str(z[1]).split('&lt;td&gt;')[1].split('=')[0]
       ip=ip.split('&lt;/td&gt;')[0].split('=')[0]
       p= str(z[2]).split('&lt;td&gt;')[1].split('=')[0]
       p=p.split('&lt;/td&gt;')[0].split('=')[0]
       pr=ip+':'+p
       if pr not in s4l:
        s4l.append(pr)
        if len(s4l)==count:
          break
    except Exception as e:
     pass
  except Exception as e:
   pass
 """
    return s4l

'''</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.utils.proxer.get_burpsuit_proxy"><code class="name flex">
<span>def <span class="ident">get_burpsuit_proxy</span></span>(<span>host='127.0.0.1', port=8080)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_burpsuit_proxy(host=burpsuit_proxy_host,port=burpsuit_proxy_port):
    proxy=burpsuit_http_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_http_proxy"><code class="name flex">
<span>def <span class="ident">get_http_proxy</span></span>(<span>proxy_host, proxy_port, username=None, password=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_http_proxy(proxy_host,proxy_port,username=None,password=None):
    if username==None and password==None:
        return {'http': 'http://{}:{}'.format(proxy_host,proxy_port), 'https': 'http://{}:{}'.format(proxy_host,proxy_port)}
    return {'http': 'http://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port), 'https': 'http://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port)}</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_http_proxy_socket"><code class="name flex">
<span>def <span class="ident">get_http_proxy_socket</span></span>(<span>host, port, proxy_host, proxy_port, username=None, password=None, timeout=5)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_http_proxy_socket(host,port,proxy_host,proxy_port,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        s.setproxy( 
                    proxy_type=socks.HTTP,
                    addr=proxy_host,
                    port=proxy_port,
                    username=username,
                    password=password,
            )
        s.connect((host,port))
        return s
    except:
        return</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_socks4_proxy"><code class="name flex">
<span>def <span class="ident">get_socks4_proxy</span></span>(<span>proxy_host, proxy_port, username=None, password=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_socks4_proxy(proxy_host,proxy_port,username=None,password=None):
    if username==None and password==None:
        return {'http': 'socks4h://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks4h://{}:{}'.format(proxy_host,proxy_port)}
    return {'http': 'socks4h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port), 'https': 'socks4h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port)}</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_socks4_proxy_socket"><code class="name flex">
<span>def <span class="ident">get_socks4_proxy_socket</span></span>(<span>host, port, proxy_host, proxy_port, username=None, password=None, timeout=5)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_socks4_proxy_socket(host,port,proxy_host,proxy_port,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        s.setproxy( 
                    proxy_type=socks.SOCKS4,
                    addr=proxy_host,
                    port=proxy_port,
                    username=username,
                    password=password,
            )
        s.connect((host,port))
        return s
    except:
        return</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_socks5_proxy"><code class="name flex">
<span>def <span class="ident">get_socks5_proxy</span></span>(<span>proxy_host, proxy_port, username=None, password=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_socks5_proxy(proxy_host,proxy_port,username=None,password=None):
    if username==None and password==None:
        return {'http': 'socks5h://{}:{}'.format(proxy_host,proxy_port), 'https': 'socks5h://{}:{}'.format(proxy_host,proxy_port)}
    return {'http': 'socks5h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port), 'https': 'socks5h://{}:{}@{}:{}'.format(username,password,proxy_host,proxy_port)}</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_socks5_proxy_socket"><code class="name flex">
<span>def <span class="ident">get_socks5_proxy_socket</span></span>(<span>host, port, proxy_host, proxy_port, username=None, password=None, timeout=5)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_socks5_proxy_socket(host,port,proxy_host,proxy_port,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        s.setproxy( 
                    proxy_type=socks.SOCKS5,
                    addr=proxy_host,
                    port=proxy_port,
                    username=username,
                    password=password,
            )
        s.connect((host,port))
        return s
    except:
        return</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_socks_proxy_socket"><code class="name flex">
<span>def <span class="ident">get_socks_proxy_socket</span></span>(<span>host, port, proxy_host, proxy_port, proxy_type, username=None, password=None, timeout=5)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_socks_proxy_socket(host,port,proxy_host,proxy_port,proxy_type,username=None,password=None,timeout=5):
    try:
        s = socks.socksocket()
        s.settimeout(timeout)
        if proxy_type==4:
            s.setproxy( 
                        proxy_type=socks.SOCKS4,
                        addr=proxy_host,
                        port=proxy_port,
                        username=username,
                        password=password,
                )
        elif proxy_type==5:
            s.setproxy( 
                        proxy_type=socks.SOCKS5,
                        addr=proxy_host,
                        port=proxy_port,
                        username=username,
                        password=password,
                )
        s.connect((host,port))
        return s
    except:
        return</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_tor_http_proxy"><code class="name flex">
<span>def <span class="ident">get_tor_http_proxy</span></span>(<span>host='127.0.0.1', port=8118)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_tor_http_proxy(host=tor_proxy_host,port=tor_proxy_http_port):
    proxy=tor_http_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_tor_socks5_proxy"><code class="name flex">
<span>def <span class="ident">get_tor_socks5_proxy</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_tor_socks5_proxy():
    if (sys.platform.lower() == "win32") or (sys.platform.lower() == "win64"):
        return get_tor_socks5_proxy_windows()
    return get_tor_socks5_proxy_linux()</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_tor_socks5_proxy_linux"><code class="name flex">
<span>def <span class="ident">get_tor_socks5_proxy_linux</span></span>(<span>host='127.0.0.1', port=9050)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_tor_socks5_proxy_linux(host=tor_proxy_host,port=tor_proxy_socks5_port_linux):
    proxy=tor_socks5_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.get_tor_socks5_proxy_windows"><code class="name flex">
<span>def <span class="ident">get_tor_socks5_proxy_windows</span></span>(<span>host='127.0.0.1', port=9150)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_tor_socks5_proxy_windows(host=tor_proxy_host,port=tor_proxy_socks5_port_windows):
    proxy=tor_socks5_proxy.copy()
    for x in proxy:
        proxy[x]=proxy[x].format(host,port)
    return proxy</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.proxy_check"><code class="name flex">
<span>def <span class="ident">proxy_check</span></span>(<span>ip, p, proto='http', username=None, password=None, timeout=5)</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to check if the proxy is dead or not.</p>
<p>it takes the following arguments:</p>
<p>proto: (set by default to: http) the proxy type: http/https/socks4/socks5
ip: proxy's ip
p: proxy's port
timeout: (set by default to: 5) the connection's timeout</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def proxy_check(ip, p, proto="http",username=None,password=None, timeout=5):
    """
    this function is to check if the proxy is dead or not.

    it takes the following arguments:

    proto: (set by default to: http) the proxy type: http/https/socks4/socks5
    ip: proxy's ip
    p: proxy's port
    timeout: (set by default to: 5) the connection's timeout
    """
    i = False
    if proto == "http":
        if username==None and password==None:
            proxy={"http": "http://{}:{}".format(ip,p)}
        else:
            proxy={"http": "http://{}:{}@{}:{}".format(username,password,ip,p)}
        try:
            requests.Session().get(
                "http://ipinfo.io/ip",
                proxies=proxy,
                headers={"User-Agent": random.choice(ua)},
                timeout=timeout,
            )
            i = True
        except:
            pass
    elif proto == "socks4":
        try:
            s = socks.socksocket()
            s.setproxy( 
                    proxy_type=socks.SOCKS4,
                    addr=ip,
                    port=p,
                    username=username,
                    password=password,
            )
            s.settimeout(timeout)
            s.connect(("www.google.com", 80))
            s.close()
            i = True
        except:
            pass
    elif proto == "socks5":
        try:
            s = socks.socksocket()
            s.setproxy( 
                    proxy_type=socks.SOCKS5,
                    addr=ip,
                    port=p,
                    username=username,
                    password=password,
            )
            s.settimeout(timeout)
            s.connect(("www.google.com", 80))
            s.close()
            i = True
        except:
            pass
    return i</code></pre>
</details>
</dd>
<dt id="bane.utils.proxer.proxyscrape"><code class="name flex">
<span>def <span class="ident">proxyscrape</span></span>(<span>protocol='http', timeout=10, country='all', ssl='all', anonymity='all', proxy=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def proxyscrape(protocol="http", timeout=10, country="all", ssl="all", anonymity="all",proxy=None):
    if protocol.lower() not in ("http", "socks4", "socks5", "all"):
        raise Exception(
            'protocol value must be: "http" or "socks4" or "socks5" or "all"'
        )
    if ssl.lower() not in ("no", "yes", "all"):
        raise Exception('protocol value must be: "no" or "yes" or "all"')
    if anonymity.lower() not in ("elite", "anonymous", "transparent", "all"):
        raise Exception(
            'protocol value must be: "elite" or "anonymous" or "transparent" or "all"'
        )
    return requests.Session().get(
        "https://api.proxyscrape.com/v2/?request=getproxies&amp;protocol="
        + protocol
        + "&amp;timeout="
        + str(timeout * 1000)
        + "&amp;country="
        + country
        + "&amp;ssl="
        + ssl
        + "&amp;anonymity="
        + anonymity,
        headers={"User-Agent": random.choice(ua)},
        proxies=proxy
    ).text.split("\r\n")</code></pre>
</details>
</dd>
</dl>
</section>
<section>
</section>
</article>
<nav id="sidebar">
<h1>Index</h1>
<div class="toc">
<ul></ul>
</div>
<ul id="index">
<li><h3>Super-module</h3>
<ul>
<li><code><a href="index.md" title="bane.utils">bane.utils</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.utils.proxer.get_burpsuit_proxy" title="bane.utils.proxer.get_burpsuit_proxy">get_burpsuit_proxy</a></code></li>
<li><code><a href="#bane.utils.proxer.get_http_proxy" title="bane.utils.proxer.get_http_proxy">get_http_proxy</a></code></li>
<li><code><a href="#bane.utils.proxer.get_http_proxy_socket" title="bane.utils.proxer.get_http_proxy_socket">get_http_proxy_socket</a></code></li>
<li><code><a href="#bane.utils.proxer.get_socks4_proxy" title="bane.utils.proxer.get_socks4_proxy">get_socks4_proxy</a></code></li>
<li><code><a href="#bane.utils.proxer.get_socks4_proxy_socket" title="bane.utils.proxer.get_socks4_proxy_socket">get_socks4_proxy_socket</a></code></li>
<li><code><a href="#bane.utils.proxer.get_socks5_proxy" title="bane.utils.proxer.get_socks5_proxy">get_socks5_proxy</a></code></li>
<li><code><a href="#bane.utils.proxer.get_socks5_proxy_socket" title="bane.utils.proxer.get_socks5_proxy_socket">get_socks5_proxy_socket</a></code></li>
<li><code><a href="#bane.utils.proxer.get_socks_proxy_socket" title="bane.utils.proxer.get_socks_proxy_socket">get_socks_proxy_socket</a></code></li>
<li><code><a href="#bane.utils.proxer.get_tor_http_proxy" title="bane.utils.proxer.get_tor_http_proxy">get_tor_http_proxy</a></code></li>
<li><code><a href="#bane.utils.proxer.get_tor_socks5_proxy" title="bane.utils.proxer.get_tor_socks5_proxy">get_tor_socks5_proxy</a></code></li>
<li><code><a href="#bane.utils.proxer.get_tor_socks5_proxy_linux" title="bane.utils.proxer.get_tor_socks5_proxy_linux">get_tor_socks5_proxy_linux</a></code></li>
<li><code><a href="#bane.utils.proxer.get_tor_socks5_proxy_windows" title="bane.utils.proxer.get_tor_socks5_proxy_windows">get_tor_socks5_proxy_windows</a></code></li>
<li><code><a href="#bane.utils.proxer.proxy_check" title="bane.utils.proxer.proxy_check">proxy_check</a></code></li>
<li><code><a href="#bane.utils.proxer.proxyscrape" title="bane.utils.proxer.proxyscrape">proxyscrape</a></code></li>
</ul>
</li>
</ul>
</nav>
</main>
<footer id="footer">
<p>Generated by <a href="https://pdoc3.github.io/pdoc" title="pdoc: Python API documentation generator"><cite>pdoc</cite> 0.10.0</a>.</p>
</footer>
</body>
</html>