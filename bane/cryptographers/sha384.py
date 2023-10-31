from bane.cryptographers.utils import *

class SHA348:

    @staticmethod
    def hash(w, encode=None):
        if type(w)==str:
            if encode:
                w=w.encode(encode)
            else:
                w=w.encode()
            """
    function to return sha384 encrypted string
    """
        return hashlib.sha384(w).hexdigest()

    @staticmethod
    def hash_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return SHA348.hash(w)


    @staticmethod
    def compare_hash(word, hash):
        if word and hash:
            word = SHA348.hash(word)
            if word == hash:
                return True
            return False
