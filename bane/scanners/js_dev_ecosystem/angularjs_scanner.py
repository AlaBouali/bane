from ..cms.utils import *

class AngularJS_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan_cpe('angularjs','angular.js',version=version,**kwargs)