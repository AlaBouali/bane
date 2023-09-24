from bane.cryptographers.utils import *

def sha1_string(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return sha1 encrypted string
  """
        return hashlib.sha1(w).hexdigest()


def sha1_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return sha1_string(w)


def dsha1(w, z):
    if w and z:
        w = hashlib.sha1(w).hexdigest()
        if w == z:
            return True
        return False

