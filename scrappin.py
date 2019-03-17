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
