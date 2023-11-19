from ..cms.utils import *

class Symfony_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('symfony',version=version,**kwargs)