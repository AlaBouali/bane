from ..cms.utils import *

class Debian_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('debian','debian_linux',version=version,**kwargs)