from ..cms.utils import *

class Windows_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('microsoft','windows_server',version=version,**kwargs)