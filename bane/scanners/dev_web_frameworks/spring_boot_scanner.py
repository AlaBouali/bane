from ..cms.utils import *

class Spring_Boot_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('spring_boot',version=version,**kwargs)