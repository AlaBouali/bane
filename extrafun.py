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
