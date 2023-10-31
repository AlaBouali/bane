from bane.cryptographers.utils import *

class BASE64:

    @staticmethod
    def encode(w, encode=None):
        if w:
            if encode:
                w.encode(encode)
            else:
                w.encode()
            """
    function to return base64 encoded string
    """
            return base64.b64encode(w)


    @staticmethod
    def decode(w, encode=None):
        if w:
            if encode:
                w.encode(encode)
            else:
                w.encode()
            """
    function to return base64 decoded string
    """
            return base64.b64decode(w)



    @staticmethod
    def encode_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return BASE64.encode(w)


    @staticmethod
    def decode_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return BASE64.decode(w)
