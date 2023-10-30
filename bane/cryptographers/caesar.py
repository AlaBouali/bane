class CAESAR:

    @staticmethod
    def encode(w, k):
        if (type(k) is not int) or (k not in range(1, 27)):
            raise Exception("the key must be an integer between: 1 and 26")
        if (not w) or (len(w) == 0):
            raise Exception("You must provide data")
        a = "abcdefghijklmnopqrstuvwxyz"
        b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c = ""
        for i in w:
            """if (k>26) or (k<1) or (ord(i) not in range(32,127)):
            break"""
            if i in a:
                c += a[(a.index(i) + k) % 26]
            elif i in b:
                c += b[(b.index(i) + k) % 26]
            else:
                c += i
        return c


    @staticmethod
    def decode(w, k):
        if (type(k) is not int) or (k not in range(1, 27)):
            raise Exception("the key must be an integer between: 1 and 26")
        if (not w) or (len(w) == 0):
            raise Exception("You must provide data")
        a = "abcdefghijklmnopqrstuvwxyz"
        b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        c = ""
        for i in w:
            """if (k>26) or (k<1) or (ord(i) not in range(32,128)):
            break"""
            if i in a:
                c += a[(a.index(i) - k) % 26]
            elif i in b:
                c += b[(b.index(i) - k) % 26]
            else:
                c += i
        return c
