from ..cms.utils import *

class Microsoft_IIS_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('microsoft','iis',version=version,**kwargs)