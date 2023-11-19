from ..cms.utils import *

class Busybox_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('busybox','busybox',version=version,**kwargs)