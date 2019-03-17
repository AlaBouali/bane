def masshttp(*args):
 '''
   this function gather up thousands of HTTP / HTTPS proxies from www.proxyserverlist24.top and proxy-daily.com
   those proxies are not recommended to be used as reliable ones all the time, i use them here just to distribute my attacks
   on next functions...
   if you are willing to use them please check them first!!!
   the function takes an argument (*args) which is the number of proxies to return, in case of no argument given it will
   return the whole list.

   usage:

   >>>import bane
   >>>bane.masshttp()

   >>>bane.masshttp(1500)
 '''
 if args:
  m=args[0]
 else:
  m=999999
 u="http://www.proxyserverlist24.top/"
 t=[]
 l=[]
 h=[]
 try:
  r=requests.get(u).text
  soup= BeautifulSoup ( r, 'html.parser')
  h3tags = soup.findAll('a')
  for a in h3tags:
    try:
     if (a.has_attr('href') and (u in str(a)) and ("proxy-server" in str(a)) and("#" not in (str(a)))) :
      try:
       a=str(a)
       a=a.split('href="')[1]
       a=a.split('"')[0]
       if (a not in l):
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
   a=requests.get(u,timeout=5)
   ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",a.text)
   t+=ips
  except Exception as e:
   pass
  u="http://proxy-daily.com/"
  try:
   r=requests.get(u).text
   soup= BeautifulSoup ( r, 'html.parser')
   l = soup.findAll('div')
  except:
   pass
  p=[]
  ips=[]
  for x in l:
   try:
    ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",str(x))
    if (ips) and (ips not in p):
     p.append(ips)
   except:
    pass
 try:
  t+=p[0]
 except:
  pass
 if args:
  while True:
   o=random.choice(t)
   h.append(o)
   if (len(h)==m) or (len(h)==len(t)):
    break
 else:
  h=t
 return h
def massocks4(*args):
 '''
   this function gather up thousands of SOCKS4 proxies from www.proxyserverlist24.top and proxy-daily.com
   those proxies are not recommended to be used as reliable ones all the time, i use them here just to distribute my attacks
   on next functions...
   if you are willing to use them please check them first!!!
   the function takes an argument (*args) which is the number of proxies to return, in case of no argument given it will
   return the whole list.

   usage:

   >>>import bane
   >>>bane.massocks4()

   >>>bane.massocks4(100)
 '''
 if args:
  m=args[0]
 else:
  m=999999
 s4=[]
 l=[]
 u="http://proxy-daily.com/"
 try:
   r=requests.get(u).text
   soup= BeautifulSoup ( r, 'html.parser')
   l = soup.findAll('div')
 except Exception as e:
   pass
 p=[]
 for x in l:
   try:
    ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",str(x))
    if (ips) and (ips not in p):
     p.append(ips)
   except Exception as x:
    pass
 t=p[2]
 if args:
  while True:
   o=random.choice(t)
   s4.append(o)
   if (len(s4)==m) or (len(s4)==len(t)):
    break
 else:
  s4=t
 return s4
def massocks5(*args):
 '''
   this function gather up thousands of SOCKS5 proxies from www.proxyserverlist24.top and proxy-daily.com
   those proxies are not recommended to be used as reliable ones all the time, i use them here just to distribute my attacks
   on next functions...
   if you are willing to use them please check them first!!!
   the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
   return the whole list.

   usage:

   >>>import bane
   >>>bane.massocks5()

   >>>bane.massocks5(500)
 '''
 if args:
  m=args[0]
 else:
  m=999999
 u="http://www.live-socks.net/"
 t=[]
 l=[]
 s5=[]
 try:
  r=requests.get(u).text
  soup= BeautifulSoup ( r, 'html.parser')
  h3 = soup.find_all( 'h3',class_='post-title entry-title' )
  for ha in h3:
   h3tags = ha.find_all('a')
   for a in h3tags:
    try:
     a=str(a)
     if("socks-5-servers" in a):
       a=a.split('href="')[1]
       a=a.split('"')[0]
       if (a not in l):
          l.append(a)
    except Exception as ex:
     continue
 except Exception as e:
  pass
 for u in l:
  try:
   a=requests.get(u,timeout=5)
   ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",a.text)
   for x in ips:
    if (x not in t):
     t.append(x)
  except Exception as e:
   pass
 if args:
  while True:
   o=random.choice(t)
   s5.append(o)
   if (len(s5)==m) or (len(s5)==len(t)):
    break
 else:
  s5=t
 return s5
def http(logs=True,count=300):
 '''
   this function gather up hundreds of HTTP proxies from many sources.
   those proxies are recommended to be used as reliable ones all the time.
   the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
   return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn 
   off the the typing if you set it to: False.

   usage:

   >>>import bane
   >>>bane.http()

   >>>bane.http(300)
'''
 hsl=[]
 u="https://free-proxy-list.net/"
 try:
  if logs==True:
   print"[+]Checking:",u
  c=requests.get(u).text
  a=0
  soup = BeautifulSoup(c,"html.parser")
  y=soup.find_all('tr')
  for x in y:
   try:
    a+=1
    x=str(x)
    ip=x.split('<tr><td>')[1].split('=')[0]
    ip=ip.split('</td>')[0].split('=')[0]
    p=x.split('</td><td>')[1].split('=')[0]
    p=p.split('</td>')[0].split('=')[0]
    pr=ip+':'+p
    if pr not in hsl:
     hsl.append(pr)
     if (a>300) or (len(hsl)==count):
      break
   except Exception as e:
    pass
 except Exception as e:
  pass
 for i in range(1,7):
  if len(hsl)==count:
    break
  try:
   u='https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-'+str(i)
   if logs==True:
    print"[+]Checking:",u
   c=requests.get(u).text
   soup = BeautifulSoup(c,"html.parser")
   y= soup.find_all("tr")
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
       pass 
     else:
      ip= str(z[1]).split('<td>')[1].split('=')[0]
      ip=ip.split('</td>')[0].split('=')[0]
      p= str(z[2]).split('<td>')[1].split('=')[0]
      p=p.split('</td>')[0].split('=')[0]
      pr=ip+':'+p
      if pr not in hsl:
       hsl.append(pr)
       if len(hsl)==count:
         break
    except Exception as e:
     pass
  except Exception as e:
   pass
 ur=["http://www.gatherproxy.com/proxylist/anonymity/?t=Elite","http://www.gatherproxy.com/proxylist/anonymity/?t=Anonymous"]
 for u in ur:
  if len(hsl)==count:
    break
  try:
   if logs==True:
    print "[+]Checking:",u
   y=[]
   c=requests.get(u).text
   soup = BeautifulSoup(c,"html.parser")
   for r in soup.find_all("script"):
    h= ''.join(map(str, r.contents))
    if 'gp.insertPrx' in h:
     s = h.split(":")
     ip= s[3].split(",")[0].replace('\"','')
     p = str(int(s[5].split(",")[0].replace('\"',''), 16))
     pr=ip+':'+p
     if pr not in hsl:
       hsl.append(pr)
       if len(hsl)==count:
        break
  except Exception as e:
   pass
 return hsl
def https(logs=True,count=200):
 '''
   this function gather up hundreds of HTTPS proxies from many sources.
   those proxies are recommended to be used as reliable ones all the time.
   the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
   return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn 
   off the the typing if you set it to: False.

   usage:

   >>>import bane
   >>>bane.https()

   >>>bane.https(200)   

'''
 hl=[]
 u='https://www.sslproxies.org/'
 try:
  if logs==True:
   print"[+]Checking:",u
  c=requests.get(u).text
  soup = BeautifulSoup(c,"html.parser")
  y= soup.find_all("tr")
  a=0
  for x in y:
   try:
    x=str(x)
    ip=x.split('</td>')[0].split('=')[0]
    ip=ip.split('<tr><td>')[1].split('=')[0]
    p=x.split('</td><td>')[1].split('=')[0]
    p=p.split('</td>')[0].split('=')[0]
    pr=ip+':'+p
    a+=1
    if pr not in hl:
     hl.append(pr)
     if (a==100) or (len(hl)==count):
      a=0
      break
   except:
    pass
 except:
  pass
 ur=['https://list.proxylistplus.com/ssl-List-1', 'https://list.proxylistplus.com/ssl-List-2']
 for u in ur:
  if len(hl)==count:
    break
  try:
   if logs==True:
    print"[+]Checking:",u
   c=requests.get(u).text
   soup = BeautifulSoup(c,"html.parser")
   y= soup.find_all("tr")
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
      pass 
     else:
       ip= str(z[1]).split('<td>')[1].split('=')[0]
       ip=ip.split('</td>')[0].split('=')[0]
       p= str(z[2]).split('<td>')[1].split('=')[0]
       p=p.split('</td>')[0].split('=')[0]
       pr=ip+':'+p
       if pr not in hl:
        hl.append(pr)
        if len(hl)==count:
          break
    except Exception as e:
     pass
  except Exception as e:
   pass
 return hl
def socks5(logs=True,count=100):
 '''
   this function gather up hundreds of SOCKS5 proxies from many sources.
   those proxies are recommended to be used as reliable ones all the time.
   the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
   return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn 
   off the the typing if you set it to: False.

   usage:

   >>>import bane
   >>>bane.socks5()

   >>>bane.socks5(50)
'''
 s5l=[]
 u='https://www.socks-proxy.net/'
 try:
  if logs==True:
   print"[+]Checking:",u
  c=requests.get(u).text
  soup = BeautifulSoup(c,"html.parser")
  y= soup.find_all("tr")
  for x in y:
   if "Socks5" in str(x):
    try:
     x=str(x)
     ip=x.split('</td>')[0].split('=')[0]
     ip=ip.split('<tr><td>')[1].split('=')[0]
     p=x.split('</td><td>')[1].split('=')[0]
     p=p.split('</td>')[0].split('=')[0]
     pr=ip+':'+p
     if pr not in s5l:
      s5l.append(pr)
      if len(s5l)==count:
        break
    except:
     pass
 except:
   pass
 ur=["https://list.proxylistplus.com/Socks-List-1"," https://list.proxylistplus.com/Socks-List-2"]
 for u in ur:
  if len(s5l)==count:
   break
  try:
   if logs==True:
    print"[+]Checking:",u
   c=requests.get(u).text
   s = BeautifulSoup(c,"html.parser")
   y=s.find_all('tr')
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
      pass 
     else:
      if "Socks5" in str(x):
       ip= str(z[1]).split('<td>')[1].split('=')[0]
       ip=ip.split('</td>')[0].split('=')[0]
       p= str(z[2]).split('<td>')[1].split('=')[0]
       p=p.split('</td>')[0].split('=')[0]
       pr=ip+':'+p
       if pr not in s5l:
        s5l.append(pr)
        if len(s5l)==count:
          break
    except Exception as e:
     pass
  except Exception as e:
   pass
 return s5l
def socks4(logs=True,count=30):
 '''
   this function gather up hundreds of SOCKS4 proxies from many sources.
   those proxies are recommended to be used as reliable ones all the time.
   the function takes an argument which is the number of proxies to return (*args) , in case of no argument given it will
   return the whole list,and another argument (logs) which is set by default to True so you can see the process of the function, you can turn 
   off the the typing if you set it to: False.

   usage:

   >>>import bane
   >>>bane.socks4()

   >>>bane.socks4(50)
'''
 s4l=[]
 u='https://www.socks-proxy.net/'
 try:
  if logs==True:
   print"[+]Checking:",u
  c=requests.get(u).text
  soup = BeautifulSoup(c,"html.parser")
  y= soup.find_all("tr")
  for x in y:
   if "Socks4" in str(x):
    try:
     x=str(x)
     ip=x.split('</td>')[0].split('=')[0]
     ip=ip.split('<tr><td>')[1].split('=')[0]
     p=x.split('</td><td>')[1].split('=')[0]
     p=p.split('</td>')[0].split('=')[0]
     pr=ip+':'+p
     if pr not in s4l:
      s4l.append(pr)
      if len(s4l)==count:
       break
    except Exception as e:
     pass
 except Exception as e:
  pass
 ur=["https://list.proxylistplus.com/Socks-List-1"," https://list.proxylistplus.com/Socks-List-2"]
 for u in ur:
  if len(s4l)==count:
   break
  try:
   if logs==True:
    print"[+]Checking:",u
   c=requests.get(u).text
   s = BeautifulSoup(c,"html.parser")
   y=s.find_all('tr')
   for x in y:
    try:
     z = x.find_all('td')
     if "strong" in str(z):
      pass 
     else:
      if "Socks4" in str(x):
       ip= str(z[1]).split('<td>')[1].split('=')[0]
       ip=ip.split('</td>')[0].split('=')[0]
       p= str(z[2]).split('<td>')[1].split('=')[0]
       p=p.split('</td>')[0].split('=')[0]
       pr=ip+':'+p
       if pr not in s4l:
        s4l.append(pr)
        if len(s4l)==count:
          break
    except Exception as e:
     pass
  except Exception as e:
   pass
 return s4l
def proxy_check(ip,p,proto='http',timeout=5):
 '''
    this function is to check if the proxy is dead or not.

    it takes the following arguments:
    
    proto: (set by default to: http) the proxy type: http/https/socks4/socks5
    ip: proxy's ip
    p: proxy's port
    timeout: (set by default to: 5) the connection's timeout

'''
 i=0
 if (proto=='http') or (proto=='https'):
  try:
   requests.get("http://www.google.com",proxies={proto:'http://'+ip+':'+p},timeout=timeout)
   i+=1
  except:
   pass
 elif proto=='socks4':
  try:
   s =socks.socksocket()
   s.setproxy(socks.PROXY_TYPE_SOCKS4, ip, p, True)
   s.settimeout(timeout)
   s.connect(('www.google.com',80))
   i+=1
  except:
   pass
 elif proto=='socks5':
  try:
   s =socks.socksocket()
   s.setproxy(socks.PROXY_TYPE_SOCKS5, ip, p, True)
   s.settimeout(timeout)
   s.connect(('www.google.com',80))
   i+=1
  except:
   pass
 return i
