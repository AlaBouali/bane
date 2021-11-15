import socket
def valid_target(adr):
  try:
   a=socket.gethosbyname(adr.split(':')[0]).split('.')
  except:
   return False
  f=[10,169,172,198,127]
  o1=int(a[0])
  o2=int(a[1])
  if (o1 not in d):
   if o1==127 or o1==10:
    return False
   if o1 in f:
    if ((o1==192)and(o2==168)):
     return False
    if ((o2==172)and((o2>=16)and(o2<=32))):
     return False
    if((o1==100)and(o2==64)):
     return False
    if((o1==169)and (o2==254)):
     return False
    if((o1==198)and(o2==18)):
     return False
   else:
    return True