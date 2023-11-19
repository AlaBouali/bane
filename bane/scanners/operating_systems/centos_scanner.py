from ..cms.utils import *

class CentOs_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('centos','centos',version=version,**kwargs)