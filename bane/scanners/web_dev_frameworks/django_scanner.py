from ..cms.utils import *

class Django_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('django',version=version,**kwargs)