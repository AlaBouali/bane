from ..cms.utils import *

class MySQL_Oracle_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('oracle','mysql',version=version,**kwargs)