from ..cms.utils import *

class Flask_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('flask',version=version,**kwargs)