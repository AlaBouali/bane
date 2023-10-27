from bane.cryptographers.utils import *

class SHA224:

    @staticmethod
    def hash(w, encode=None):
        if w:
            if encode:
                w.encode(encode)
            """
    function to return sha256 encrypted string
    """
            return hashlib.sha224(w).hexdigest()

    @staticmethod
    def hash_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return SHA224.hash(w)


    @staticmethod
    def compare_hash(word, hash):
        if word and hash:
            word = hashlib.sha224(word).hexdigest()
            if word == hash:
                return True
            return False
