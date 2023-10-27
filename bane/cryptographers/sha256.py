from bane.cryptographers.utils import *

class SHA256:

    @staticmethod
    def hash(w, encode=None):
        if w:
            if encode:
                w.encode(encode)
            """
    function to return sha256 encrypted string
    """
            return hashlib.sha256(w).hexdigest()

    @staticmethod
    def hash_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return SHA256.hash(w)


    @staticmethod
    def compare_hash(word, hash):
        if word and hash:
            word = hashlib.sha256(word).hexdigest()
            if word == hash:
                return True
            return False
