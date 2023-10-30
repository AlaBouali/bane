import socks,socket,ssl,random
from .proxer import Proxies_Getter
from bane.common.payloads import *

class Socket_Connection:

    @staticmethod
    def wrap_socket_with_ssl(sock,target_host):
        if sock==None:
            return
        if hasattr(ssl, 'PROTOCOL_TLS_CLIENT'):
            # Since Python 3.6
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        elif hasattr(ssl, 'PROTOCOL_TLS'):
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        else:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)#ssl.PROTOCOL_TLS)
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context.wrap_socket(sock, server_hostname=target_host)

    def reorder_headers_randomly(s):
        b = s.split("\r\n\r\n")[1]
        a = s.split("\r\n\r\n")[0]
        m = a.split("\r\n")[0]
        c = a.split("\r\n")[1:]
        random.shuffle(c)
        num=random.randint(1,4)
        i=[]
        while len(i)>num:
            q=random.choice(c)
            if 'host:' not in q.lower() or 'user-agent:' not in q.lower() or 'content-length' not in q.lower():
                i.append(q)
        for x in i:
            if x in c:
                c.remove(x)
        return m + "\r\n" + "\r\n".join(c) + "\r\n\r\n" + b


    def random_param():
        a = random.randint(1, 2)
        if a == 1:
            return str(random.randint(1, 1000))
        else:
            return random.choice(Common_Variables.source_string)


    def setup_http_packet(
        target,
        ty,
        paths,
        post_field_min,
        post_field_max,
        post_min,
        post_max,
        cookie,
        user_agents,
    ):
        pa = random.choice(paths)  # bypassing cache engine
        q = ""
        for i in range(random.randint(2, 5)):
            q += Socket_Connection.random_param() + Socket_Connection.random_param()
        p = ""
        for i in range(random.randint(2, 5)):
            p += Socket_Connection.random_param() + Socket_Connection.random_param()
        if "?" in pa:
            jo = "&"
        else:
            jo = "?"
        pa += jo + q + "=" + p
        # setting random headers
        for l in range(random.randint(1, 5)):
            ed = random.choice(Common_Variables.accept_encoding_list)
            oi = random.randint(1, 3)
            if oi == 2:
                gy = 0
                while gy < 1:
                    df = random.choice(Common_Variables.accept_encoding_list)
                    if df != ed:
                        gy += 1
                ed += ", "
                ed += df
        l = random.choice(Common_Variables.accept_language_list)
        for n in range(random.randint(0, 5)):
            l += ";q={},".format(round(random.uniform(0.1, 1), 1)) + random.choice(Common_Variables.accept_language_list)
        kl = random.randint(1, 2)
        ck = ""
        if cookie:
            ck = "Cookie: " + cookie + "\r\n"
        if ty == 1:
            m = "GET {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept: {}\r\nAccept-Language: {}\r\nAccept-Encoding: {}\r\nAccept-Charset: {}\r\nKeep-Alive: {}\r\nConnection: Keep-Alive\r\nCache-Control: {}\r\nReferer: {}\r\nHost: {}\r\n\r\n".format(
                pa,
                ck,
                random.choice(user_agents),
                random.choice(Common_Variables.accept_list),
                l,
                ed,
                random.choice(Common_Variables.accept_charset_list),
                random.randint(100, 1000),
                random.choice(Common_Variables.cache_control_list),
                (
                    random.choice(Common_Variables.referers_list)
                    + random.choice(Common_Variables.source_string)
                    + str(random.randint(0, 100000000))
                    + random.choice(Common_Variables.source_string)
                ),
                target,
            )
        else:
            k = ""
            for _ in range(random.randint(post_field_min, post_field_max)):
                k += random.choice(Common_Variables.source_string)
            j = ""
            for x in range(random.randint(post_min, post_max)):
                j += random.choice(Common_Variables.source_string)
            par = j + "=" + k
            m = "POST {} HTTP/1.1\r\n{}User-Agent: {}\r\nAccept-language: {}\r\nConnection: keep-alive\r\nKeep-Alive: {}\r\nContent-Length: {}\r\nContent-Type: application/x-www-form-urlencoded\r\nReferer: {}\r\nHost: {}\r\n\r\n{}".format(
                pa,
                ck,
                random.choice(user_agents),
                l,
                random.randint(300, 1000),
                len(par),
                (
                    random.choice(Common_Variables.referers_list)
                    + random.choice(Common_Variables.source_string)
                    + str(random.randint(0, 100000000))
                    + random.choice(Common_Variables.source_string)
                ),
                target,
                par,
            )
        return Socket_Connection.reorder_headers_randomly(m)




    def get_socket_connection(host,port,timeout=5,no_delay=False,ssl_wrap=False,**kwargs):
        s=Proxies_Getter.get_proxy_socket(host,port,timeout=timeout,no_delay=no_delay,**kwargs)
        if ssl_wrap==True:
            s=Socket_Connection.wrap_socket_with_ssl(s,host)
        return s


    def get_tor_socket_connection(host,port,new_ip=True,ssl_wrap=False,timeout=5,no_delay=False,**kwargs):
        s=Proxies_Getter.get_tor_socks5_socket(host,port,new_ip=new_ip,timeout=timeout,no_delay=no_delay,**kwargs)
        if ssl_wrap==True:
            s=Socket_Connection.wrap_socket_with_ssl(s,host)
        return s




