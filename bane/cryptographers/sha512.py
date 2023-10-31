from bane.cryptographers.utils import *

class SHA512:

    @staticmethod
    def hash(w, encode=None):
        if type(w)==str:
            if encode:
                w=w.encode(encode)
            else:
                w=w.encode()
            """
    function to return sha512 encrypted string
    """
        return hashlib.sha512(w).hexdigest()


    @staticmethod
    def hash_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return SHA512.hash(w)


    @staticmethod
    def compare_hash(word, hash):
        if word and hash:
            word = SHA512.hash(word)
            if word == hash:
                return True
            return False
