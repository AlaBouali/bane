from ..cms.utils import *

class Windows_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('microsoft','windows',version=version,**kwargs)