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
