import os,sys,time
try:
 import stem
 from stem import Signal
 from stem.control import Controller
except:
 pass
def tor_switch_no_password(interval=30,logs=True):
 '''
    this function is for auto ip switching of tor's nodes, it doesnt work on windows because it use the command on linux to restart tor' service in a chosen interval.

   it takes the following parameters:

   new: (set by default to: 30) the interval in seconds between switching tor's nodes
   logs: (set by default to: True) showing the screen prints

   example:

   >>>import bane
   >>>bane.torswitch1(new=15)
 
'''
 i=True
 if (sys.platform == "win32") or( sys.platform == "win64"):
  print("[-]This option is not for windows")
  i=False
 if i==True:
  while True:
   try:
    os.system('systemctl reload tor')
    if logs==True:
     print("IP changed, sleeping for {} seconds...".format(interval))
    time.sleep(interval)
   except KeyboardInterrupt:
    break
def tor_switch_with_password(interval=30,password=None,p=9051,logs=True):
 '''
   this one does work on any OS, you just need to activate tor's control port 9051 and set the password.

   it takes the next parameters:

   new: (set by default to: 30) the interval in seconds between switching tor's nodes
   password: your password
   p: (set by default to: 9051) tor's control port
   logs: (set by default to: True) showing the screen prints
'''
 if password==None:
  print("[-]you need to put your control port's password for authentication!!!")
 else:
  while True:
   try:
    with Controller.from_port(port = p) as controller:
     controller.authenticate(password =password )
     controller.signal(Signal.NEWNYM)
     controller.close()
    if logs==True:
     print("IP changed, sleeping for {} seconds...".format(interval))
    time.sleep(interval)
   except KeyboardInterrupt:
    break
