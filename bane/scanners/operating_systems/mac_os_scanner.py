from ..cms.utils import *

class Mac_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('apple','macos',version=version,**kwargs)