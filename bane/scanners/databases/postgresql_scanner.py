from ..cms.utils import *

class PostgreSQL_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('postgresql','postgresql',version=version,**kwargs)