from ..cms.utils import *

class Git_Scanner:

    @staticmethod
    def scan(version):
        return Vulners_Search_Scanner.scan('git',version=version)