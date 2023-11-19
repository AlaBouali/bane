from ..cms.utils import *

class Angular_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('angularjs','angular',version=version,**kwargs)