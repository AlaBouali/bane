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


def get_public_dns(timeout=10):
    try:
        return requests.get('https://public-dns.info/nameservers.txt',
                            timeout=timeout).text.split('\n')
    except:
        return []

