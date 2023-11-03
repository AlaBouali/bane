import flask,os
import socket,os,sys,pwinput
from bane.utils.socket_connection import *
from bane.cryptographers.xor import XOR
import os, sys, socket, random, time, threading, xtelnet
from bane.common.payloads import *
from bane.scanners.vulnerabilities.adb_exploit import *

from bane.bruteforce.hydra import *
from bane.utils.pager.rand_generator import *
from bane.utils.handle_files import *

import socket,sys,os,time
import threading
from bane.cryptographers.xor import XOR

if sys.version_info < (3, 0):
    user_input=raw_input
else:
    user_input=input
