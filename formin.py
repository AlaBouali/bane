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
