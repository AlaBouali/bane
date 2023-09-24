from bane.cryptographers.utils import *

def sha256_string(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return sha256 encrypted string
  """
        return hashlib.sha256(w).hexdigest()

def sha256_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return sha256_string(w)


def dsha256(w, z):
    if w and z:
        w = hashlib.sha256(w).hexdigest()
        if w == z:
            return True
        return False
