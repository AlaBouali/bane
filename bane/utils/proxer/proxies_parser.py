from .utils import *
from .proxies_checker import *

class Proxies_Parser:

    @staticmethod
    def parse_proxy_string(s,proxy_type):
        s=s.strip()
        s=s.split(':')
        try:
            socket.gethostbyname(s[0])
        except:
            return
        try:
            int(s[1])
        except:
            return
        if len(s)==2:
            return {'proxy_host':s[0],'proxy_port':int(s[1]),'proxy_username':None,'proxy_password':None,'proxy_type':proxy_type}
        if len(s)==3:
            return {'proxy_host':s[0],'proxy_port':int(s[1]),'proxy_username':s[2],'proxy_password':'','proxy_type':proxy_type}
        if len(s)==4:
            return {'proxy_host':s[0],'proxy_port':int(s[1]),'proxy_username':s[2],'proxy_password':s[3],'proxy_type':proxy_type}

    @staticmethod
    def parse_proxies_list(l,proxy_type):
        if type(l)==str:
            if len(l.split('\n'))>1:
                l=l.split('\n')
        if type(l)==list or type(l)==tuple:
            l= [Proxies_Parser.parse_proxy_string(x,proxy_type) for x in l]
            return [x for x in l if x!=None]
        else:
            return [Proxies_Parser.parse_proxy_string(l,proxy_type)]


    @staticmethod
    def load_and_parse_proxies(source,proxies_type):
        if source==None:
            return []
        elif type(source)==dict:
            if list(source.keys())==['proxy_host', 'proxy_port', 'proxy_username', 'proxy_password', 'proxy_type']:
                return [source]
            else:
                return []
        data=[]
        if type(source)==str:
            if ':' in source:
                return [Proxies_Parser.parse_proxy_string(source,proxies_type)]
            if source.endswith('.json'):
                with open(source) as f:
                    return Proxies_Parser.load_and_parse_proxies(json.load(f),proxies_type)
            f=open(source,'r')
            data=f.readlines()
            f.close()
        elif type(source)==list or type(source)==tuple:
            if len(source)==0:
                return []
            if type(source[0])==dict:
                if list(source[0].keys())==['proxy_host', 'proxy_port', 'proxy_username', 'proxy_password', 'proxy_type']:
                    return source
            for x in source:
                if type(x)==str:
                    data.append(x)
        return Proxies_Parser.parse_proxies_list(data,proxies_type)


