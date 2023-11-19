from ..cms.utils import *

class Apache_Coyote_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('apache','coyote_http_connector',version=version,**kwargs)