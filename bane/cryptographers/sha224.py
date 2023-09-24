from bane.cryptographers.utils import *

def sha224_string(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return sha256 encrypted string
  """
        return hashlib.sha224(w).hexdigest()

def sha224_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return sha224_string(w)


def dsha224(w, z):
    if w and z:
        w = hashlib.sha224(w).hexdigest()
        if w == z:
            return True
        return False
