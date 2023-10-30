#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
try:
    if sys.version_info < (3, 0):
        from scapy.all import *
    else:
        from kamene.all import *
except:
    pass
import random
import socket
import requests
