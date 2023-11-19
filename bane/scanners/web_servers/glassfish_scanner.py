from ..cms.utils import *

class GlasshFish_Server_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('oracle','glassfish_server',version=version,**kwargs)