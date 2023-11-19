from ...scanners.vulnerabilities.utils import *
from ...scanners.vulnerabilities.vulner_search import Vulners_Search_Scanner


class ElasticSearch_Scanner:

    @staticmethod
    def scan(u,ssl_enabled=False, timeout=5, p=9200,proxy_host=None,proxy_port=None,proxy_username=None,proxy_password=None,proxy_type=None,api_key=None):
        if proxy_type!=None:
            
            prox={'proxy_host':proxy_host,'proxy_port':proxy_port,'proxy_username':proxy_username,'proxy_password':proxy_password,'proxy_type':proxy_type}
        else:
            prox=[]
        data={}
        if proxy_type=='socks4' or proxy_type=='s4':
            proxy_type=socks.PROXY_TYPE_SOCKS4
        elif proxy_type=='socks5' or proxy_type=='s5':
            proxy_type=socks.PROXY_TYPE_SOCKS5
        else:
            proxy_type=None
        try:
            s = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            if proxy_type!=None:
                s.setproxy( 
                        proxy_type=proxy_type,
                        addr=proxy_host,
                        port=proxy_port,
                        username=proxy_username,
                        password=proxy_password,
                )
            s.settimeout(timeout)
            s.connect((u, p))
            if ssl_enabled==True:
                s=Socket_Connection.wrap_socket_with_ssl(s,u)
            s.send(
                b"GET / HTTP/1.1\r\n\r\n"
            )
            c = s.recv(10240).decode('utf-8').replace('","   ','", ').strip()
            #cleaned_json = re.sub(r'"(\w+)":\s*"', r'"\1":"', c.decode('utf-8')).replace('","     ','",     ')
            s.close()
            data=json.loads(c)
            version=data["version" ]["number"]
            wp_vulns=[]
            wpvulns=Vulners_Search_Scanner.scan('elasticsearch',version=version,http_proxies=prox,api_key=api_key)
            for x in wpvulns:
                if 'elasticsearch' in x['title'].lower() or 'elasticsearch' in x['description'].lower():
                    wp_vulns.append(x)
            for x in wp_vulns:
                for i in ['cpe', 'cpe23', 'cwe', 'affectedSoftware']:
                    try:
                        del x[i]
                    except:
                        pass
            data.update({'exploits':wp_vulns})
        except Exception as ex:
            raise Exception(ex)
            return {}
        return data

