from ..cms.utils import *

class NodeJS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('node.js',version=version,**kwargs)