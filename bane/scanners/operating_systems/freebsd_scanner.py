from ..cms.utils import *

class FreeBSD_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('freebsd','freebsd',version=version,**kwargs)