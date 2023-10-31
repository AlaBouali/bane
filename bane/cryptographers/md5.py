from bane.cryptographers.utils import *

class MD5:
    
    @staticmethod
    def hash(w, encode=None):
        if type(w)==str:
            if encode:
                w=w.encode(encode)
            else:
                w=w.encode()
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
            word = MD5.hash(word)
            if word == hash:
                return True
            return False
