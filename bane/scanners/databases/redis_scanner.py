from ..cms.utils import *

class Redis_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('redislabs','redis',version=version,**kwargs)