from bane.cryptographers.utils import *

def xor_string(data, key):
    """
    function to return XOR encrypted string
    """
    i = 0
    c = ""
    l = len(data)
    k = len(key)
    if (not data) or (l == 0):
        raise Exception("You must provide data")
    if (not key) or (k == 0):
        raise Exception("You must provide a key")
    while i < l:
        for x in key:
            if i == l:
                break
            if type(data[i]) == str:
                c += chr(ord(data[i]) ^ ord(x))
            else:
                c += chr(data[i] ^ ord(x))
            i += 1
    i = None
    l = None
    k = None
    data = None
    key = None
    return c


def xor_file(f, key):
    if f and key:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return xor_string(w, key)
