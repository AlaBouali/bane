from ..cms.utils import *

class Kubernetes_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('kubernetes',version=version,**kwargs)