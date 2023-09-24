from bane.scanners.vulnerabilities.utils import *

def exposed_telnet(u, p=23, timeout=5):
    try:
        t = xtelnet.session()
        t.connect(u, p=p, timeout=timeout)
        t.destroy()
        return True
    except:
        pass
    return False

