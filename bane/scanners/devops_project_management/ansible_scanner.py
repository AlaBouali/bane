from ..cms.utils import *

class Ansible_Scanner:

    @staticmethod
    def scan(version,**kwargs):
        return Vulners_Search_Scanner.scan('ansible',version=version,**kwargs)