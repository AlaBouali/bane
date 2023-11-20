from ..cms.utils import *

class MySQL_MySQL_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('mysql','mysql',version=version,**kwargs)