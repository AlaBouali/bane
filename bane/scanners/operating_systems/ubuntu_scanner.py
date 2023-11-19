from ..cms.utils import *

class Ubuntu_OS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('canonical','ubuntu_linux',version=version,**kwargs)