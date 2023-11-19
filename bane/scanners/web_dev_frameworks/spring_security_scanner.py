from ..cms.utils import *

class Spring_Security_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('spring_security',version=version,**kwargs)