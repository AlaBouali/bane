from bane.gather_info.utils import *
from.domains import Domain_Info

class IP_Info:

    @staticmethod
    def parse_IP(ip):
        if '://' in ip:
            ip=ip.split('://')[1].split('/')[0]
        if ':' in ip:
            ip=ip.split(':')[0]
        return ip

    @staticmethod
    def my_ip(proxy=None, timeout=15):
        """
        this function is for getting your ip using: ipinfo.io
        usage:
        >>>import bane
        >>>bane.myip()
        xxx.xx.xxx.xxx"""
        try:
            return requests.Session().get(
                "https://api.ipify.org",
                headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                proxies=proxy,
                timeout=timeout,
            ).text.strip()
        except:
            pass
        return ""


    @staticmethod
    def get_host_name(ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except:
            return 

    @staticmethod
    def geo_ip(u, timeout=15, proxy=None):
        """
        this function is for getting: geoip informations
        """
        ip=IP_Info.parse_IP(ip)
        try:
            return requests.Session().get(
                "https://api.db-ip.com/v2/free/" + u,
                headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                proxies=proxy,
                timeout=timeout,
            ).json()
        except Exception as ex:
            pass
        return {}


    @staticmethod
    def reverse_ip_lookup(u, timeout=10, proxy=None):
        """
        this function is for: reverse ip look up
        if you've used it 100 times in 24 hours, your IP will be banned by "api.hackertarget.com" so i highly recommand you to use the "proxy" option by adding a http(s) proxy:


        """
        ip=IP_Info.parse_IP(ip)
        try:
            r = requests.Session().get(
                "https://api.hackertarget.com/reverseiplookup/?q=" + u,
                headers={"User-Agent": random.choice(Common_Variables.user_agents_list)},
                proxies=proxy,
                timeout=timeout,
            ).text
            return r.split("\n")
        except Exception as ex:
            pass
        return []


    @staticmethod
    def check_ip_via_shodan(ip,proxy=None,timeout=15,logs=False):
        inp=ip
        if type(ip)==dict:
            l=[]
            ips=[]
            for x in list(ip.keys()):
                a=socket.gethostbyname(x.split(':')[0])
                if a not in ips:
                    data=IP_Info.check_ip_via_shodan(a,proxy=proxy,timeout=timeout,logs=logs)
                    if type(data)==list:
                            for v in data:
                                if v not in l and v!={}:
                                    l+=data
                    else:
                            if data not in l and data!={}:
                                l.append(data)
                    ips.append(a)
            return l
        if type(ip) in [tuple,list]:
            l=[]
            ips=[]
            for x in ip:
                a=socket.gethostbyname(x.split(':')[0])
                if a not in ips:
                    data=IP_Info.check_ip_via_shodan(a,proxy=proxy,timeout=timeout,logs=logs)
                    if type(data)==list:
                            for v in data:
                                if v not in l and v!={}:
                                    l+=data
                    else:
                            if data not in l and data!={}:
                                l.append(data)
                    ips.append(a)
            return l
        ip=IP_Info.parse_IP(ip)
        try:
            resolved=socket.gethostbyname(ip.split(':')[0])
        except:
            return {}
        if resolved!=ip:
            try:
                ip=Domain_Info.resolve(ip)
            except:
                pass
        if type(ip) in [tuple,list]:
            l=[]
            for x in ip:
                data=IP_Info.check_ip_via_shodan(x,proxy=proxy,timeout=timeout,logs=logs)
                if type(data)==list:
                            for v in data:
                                if v not in l and v!={}:
                                    l+=data
                else:
                            if data not in l and data!={}:
                                l.append(data)
            return l
        ip=socket.gethostbyname(ip)
        if logs==True:
            print('[i] IP scan via Shodan  ( in some cases they are outdated, so please verify them manually before submitting them ) :')
            print('[+] Target: '+ip)
        try:
            d= requests.Session().get('https://internetdb.shodan.io/{}'.format(ip),headers={'User-Agent':random.choice(Common_Variables.user_agents_list)},proxies=proxy,timeout=timeout).json()
            v={}
            for x in d['vulns']:
                v.update({x:['https://www.cve.org/CVERecord?id='+x,'https://nvd.nist.gov/vuln/detail/'+x,'https://cve.mitre.org/cgi-bin/cvename.cgi?name='+x]})
            del d['vulns']
            d['exploits']=v
            d['input']=inp
            if logs==True:
                print()
                print('[+] CPEs:')
                print()
                for x in d['cpes']:
                    print(x)
                print() 
                print('[+] Hostnames:')
                print()
                for x in d['hostnames']:
                    print(x)
                print() 
                print('[+] Open ports:')
                print()
                for x in d['ports']:
                    print(x)
                print() 
                print('[+] Shodan tags:')
                print()
                for x in d['tags']:
                    print(x)
                print() 
                print('[+] Exploits URLs :')
                print()
                for x in d['exploits']:
                    for i in d['exploits'][x]:
                        print(i)
                print() 
            return d
        except:
            return {}


    @staticmethod
    def get_IP_info(ip,timeout=15,proxy=None):
        d={}
        ip=IP_Info.parse_IP(ip)
        d.update({'host_name':IP_Info.get_host_name(ip)})
        d.update({'geo_ip_location':IP_Info.geo_ip(ip,timeout=timeout,proxy=proxy)})
        d.update({'reverse_ip_lookup':IP_Info.reverse_ip_lookup(ip,timeout=timeout,proxy=proxy)})
        d.update({'shodan_report':IP_Info.check_ip_via_shodan(ip,timeout=timeout,proxy=proxy)})
        return d
