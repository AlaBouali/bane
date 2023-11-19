from ..cms.utils import *

class Docker_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('docker',version=version,**kwargs)