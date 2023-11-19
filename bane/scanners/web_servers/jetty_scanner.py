from ..cms.utils import *

class Jetty_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('eclipse','jetty',version=version,**kwargs)