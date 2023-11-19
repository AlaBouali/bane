from ..cms.utils import *

class IOS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('apple','iphone_os',version=version,**kwargs)