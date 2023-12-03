import flask,os
import socket,os,sys
try:
    import pwinput
except:
    pwinput=input
from ...utils.socket_connection import *
from ...cryptographers.xor import XOR
import os, sys, socket, random, time, threading, xtelnet
from ...common.payloads import *
from ...scanners.vulnerabilities.adb_exploit import *

from ...bruteforce.hydra import *
from ...utils.pager.rand_generator import *
from ...utils.handle_files import *

import socket,sys,os,time
import threading
from ...cryptographers.xor import XOR

if sys.version_info < (3, 0):
    user_input=raw_input
else:
    user_input=input
