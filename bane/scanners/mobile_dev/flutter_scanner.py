from ..cms.utils import *

class Flutter_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('flutter','flutter',version=version,**kwargs)