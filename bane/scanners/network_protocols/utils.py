#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
try:
    if sys.version_info < (3, 0):
        from scapy.config import conf
        conf.ipv6_enabled = False
        from scapy.all import UDP,IP,DNS,DNSQR,Raw
    else:
        from kamene.config import conf
        conf.ipv6_enabled = False
        from kamene.all import UDP,IP,DNS,DNSQR,Raw
except:
    pass
import random
import socket
import requests
