from ..cms.utils import *

class MongoDB_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('mongodb','mongodb',version=version,**kwargs)