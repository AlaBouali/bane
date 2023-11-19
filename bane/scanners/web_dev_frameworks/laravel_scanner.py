from ..cms.utils import *

class Laravel_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('laravel',version=version,**kwargs)