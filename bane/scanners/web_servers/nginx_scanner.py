from ..cms.utils import *

class Nginx_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('f5','nginx',version=version,**kwargs)