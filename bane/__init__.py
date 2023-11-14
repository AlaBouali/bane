#coding: utf-8


__version__='5.0.0'

__author__="Ala Bouali"

__author_nicknames__=["Merlin", "Chaotic Mind", "Ala", "Mr. Ego","Smirky"]

__author_email__="ala.bouali.1997@gmail.com"

__author_github__="https://github.com/AlaBouali"

__author_linkedin__="https://tn.linkedin.com/in/ala-bouali"


from bane.bruteforce import *
from bane.common import *
from bane.cryptographers import *
from bane.ddos import *
from bane.gather_info import *
from bane.scanners import *
from bane.utils import *

while True:
    a=RANDOM_GENERATOR.get_random_user_agent()
    if a not in Common_Variables.user_agents_list:
        Common_Variables.user_agents_list.append(a)
    if len(Common_Variables.user_agents_list)==20000:
        break