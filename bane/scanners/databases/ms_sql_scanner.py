from ..cms.utils import *

class Microsoft_SQL_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('microsoft','sql_server',version=version,**kwargs)