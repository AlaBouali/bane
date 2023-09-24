from bane.cryptographers.utils import *

def sha512_string(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return sha512 encrypted string
  """
        return hashlib.sha512(w).hexdigest()


def sha512_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return sha512_string(w)


def dsha512(w, z):
    if w and z:
        w = hashlib.sha512(w).hexdigest()
        if w == z:
            return True
        return False
