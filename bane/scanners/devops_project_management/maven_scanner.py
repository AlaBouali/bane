from ..cms.utils import *

class Maven_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('maven',version=version,**kwargs)