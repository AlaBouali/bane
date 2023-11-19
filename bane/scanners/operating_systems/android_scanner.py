from ..cms.utils import *

class Android_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('google','android',version=version,**kwargs)