from bane.bruteforce.utils import *


class decrypt:
    __slots__ = ["stop", "finish", "result", "logs"]

    def __init__(
        self,
        u,
        word_list=[],
        threads_daemon=True,
        md5_hash=False,
        sha1_hash=False,
        sha256_hash=False,
        sha224_hash=False,
        sha384_hash=False,
        sha512_hash=False,
        base64_string=False,
        caesar_hash=False,
        logs=False,
    ):
        self.logs = logs
        self.stop = False
        self.finish = False
        self.result = {}
        t = threading.Thread(
            target=self.crack,
            args=(
                u,
                word_list,
                md5_hash,
                sha1_hash,
                sha256_hash,
                sha224_hash,
                sha384_hash,
                sha512_hash,
                base64_string,
                caesar_hash,
                logs,
            ),
        )
        t.daemon = threads_daemon
        t.start()

    def crack(
        self,
        u,
        word_list,
        md5_hash,
        sha1_hash,
        sha256_hash,
        sha224_hash,
        sha384_hash,
        sha512_hash,
        base64_string,
        caesar_hash,
        logs,
    ):
        if self.logs == True:
            print("[!]hash: " + u + "\nbruteforcing has started!!!\n")
        for x in word_list:
            if self.stop == True:
                break
            if md5_hash == True:
                if dmd5(x, u) == True:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: md5")
                    self.result = {u: ["md5:" + x]}
                    break
            if sha1_hash == True:
                if dsha1(x, u) == True:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: sha1")
                    self.result = {u: ["sha1:" + x]}
                    break
            if sha256_hash == True:
                if dsha256(x, u) == True:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: sha256")
                    self.result = {u: ["sha256:" + x]}
                    break
            if sha224_hash == True:
                if dsha224(x, u) == True:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: sha224")
                    self.result = {u: ["sha224:" + x]}
                    break
            if sha384_hash == True:
                if dsha384(x, u) == True:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: sha384")
                    self.result = {u: ["sha384:" + x]}
                    break
            if sha512_hash == True:
                if dsha512(x, u) == True:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: sha512")
                    self.result = {u: ["sha512:" + x]}
                    break
            if base64_string == True:
                if base64_decode(x) == u:
                    if self.logs == True:
                        print("[+]Hash match found: " + x + " | Type: base64")
                    self.result = {u: ["base64:" + x]}
                    break
            if caesar_hash == True:
                for i in range(1, 27):
                    if dcaesar(x, i) == True:
                        if self.logs == True:
                            print(
                                "[+]Hash match found: "
                                + x
                                + " | Type: caesar | Key: "
                                + str(i)
                            )
                        self.result = {u: ["caesar" + str(i) + ":" + x]}
                        break
        if self.result == {}:
            if self.logs == True:
                print("[-]No match found")
        self.finish = True

    def done(self):
        return self.finish