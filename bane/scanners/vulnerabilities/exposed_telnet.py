from bane.scanners.vulnerabilities.utils import *

class Exposed_Telent_Scanner:

    @staticmethod
    def scan(u, p=23, timeout=5,**kwargs):
        try:
            t = xtelnet.session()
            t.connect(u, p=p, timeout=timeout,**kwargs)
            t.destroy()
            return True
        except:
            pass
        return False

