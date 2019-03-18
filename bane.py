#coding: utf-8
'''

email:

      trap.leader.123@gmail.com

facebook:

      https://www.facebook.com/ala.chamtouri.73

linkedin:

      https://www.linkedin.com/in/ala-bouali-bb17ab132/
'''
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
from payloads import *
from proxin import *
from scrappin import *
from infoin import *
from formin import *
from hashin import *
from Dosin import *
from filin import *
from scannin import *
from iot import *
from extrafun import *
from bruteforcin import *
