from ..cms.utils import *

class Apache_Tomcat_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('apache','tomcat',version=version,**kwargs)