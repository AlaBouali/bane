from ..cms.utils import *

class Apache_HTTP_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('apache','http_server',version=version,**kwargs)