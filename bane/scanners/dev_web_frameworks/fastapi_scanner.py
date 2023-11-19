from ..cms.utils import *

class FastAPI_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('fastapi',version=version,**kwargs)