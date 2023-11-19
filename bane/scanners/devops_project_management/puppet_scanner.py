from ..cms.utils import *

class Puppet_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('puppet',version=version,**kwargs)