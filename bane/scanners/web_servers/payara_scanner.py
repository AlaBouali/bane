from ..cms.utils import *

class Payara_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('payara','payara',version=version,**kwargs)