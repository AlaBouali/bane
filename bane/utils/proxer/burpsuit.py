from .utils import *

class BurpSuite_Getter:

    @staticmethod
    def get_proxy(host=Common_Variables.burpsuit_proxy_host,port=Common_Variables.burpsuit_proxy_port):
        proxy=Common_Variables.burpsuit_http_proxy.copy()
        for x in proxy:
            proxy[x]=proxy[x].format(host,port)
        return proxy
