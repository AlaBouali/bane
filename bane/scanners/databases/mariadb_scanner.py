from ..cms.utils import *

class MariaDB_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('mariadb','mariadb',version=version,**kwargs)