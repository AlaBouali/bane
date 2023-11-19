from ..cms.utils import *

class React_Native_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('facebook','react-native',version=version,**kwargs)