from ..cms.utils import *

class Git_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('git',version=version,**kwargs)