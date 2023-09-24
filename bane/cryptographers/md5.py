from bane.cryptographers.utils import *

def md5_string(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return md5 encrypted string
  """
        return hashlib.md5(w).hexdigest()


def md5_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return md5_string(w)


def dmd5(w, z):
    if w and z:
        w = hashlib.md5(w).hexdigest()
        if w == z:
            return True
        return False
