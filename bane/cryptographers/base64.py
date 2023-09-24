from bane.cryptographers.utils import *

def base64_encode(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return base64 encoded string
  """
        return base64.b64encode(w)


def base64_decode(w, encode=None):
    if w:
        if encode:
            w.encode(encode)
        """
   function to return base64 decoded string
  """
        return base64.b64decode(w)



def base64_encode_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return base64_encode(w)


def base64_decode_file(f):
    if f:
        with open(f, "rb") as f:
            w = f.read()
        f.close()
        return base64_decode(w)
