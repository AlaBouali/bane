from ..cms.utils import *

class ReactJS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('facebook','react',version=version,**kwargs)