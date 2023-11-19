from ..cms.utils import *

class NPMJS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('npmjs','npm',version=version,**kwargs)