from bane.cryptographers.utils import *

def sha384_string(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return sha384 encrypted string
  """
        return hashlib.sha384(w).hexdigest()

def sha384_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return sha384_string(w)


def dsha384(w, z):
    if w and z:
        w = hashlib.sha384(w).hexdigest()
        if w == z:
            return True
        return False
