from bane.cryptographers.utils import *

class MD5:
    
    @staticmethod
    def hash(w, encode=None):
        if w:
            if encode:
                w.encode(encode)
            """
    function to return md5 encrypted string
    """
            return hashlib.md5(w).hexdigest()


    @staticmethod
    def hash_file(f):
        if f:
            with open(f, "rb") as f:
                w = f.read()
            f.close()
            return MD5.hash(w)


    @staticmethod
    def compare_hash(word, hash):
        if word and hash:
            word = hashlib.md5(word).hexdigest()
            if word == hash:
                return True
            return False
