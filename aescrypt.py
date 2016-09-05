from Crypto.Cipher import AES
import base64
import hashlib


class PyAesCrypt(object):
    def __init__(self,iv=None,encoding=True):
        self.iv = iv
        self.encoding = encoding

    def encrypt(self,key,message):
        cipher = AES.new(key=self._hashkey(key=key))
        cipher_text = cipher.encrypt(self.pkcs7padding(data=message))
        if self.encoding:
            return base64.b64encode(s=cipher_text)
        return cipher_text

    def pkcs7padding(self,data):
        bs = 8
        padding = bs - len(data) % bs
        padding_text = chr(padding) * padding
        return data + padding_text

    def pkcs7decode(self, text):
        if type(text) is bytes:
            pad = ord(text.decode("utf-8")[-1])
            return text[:-pad]
        else:
            raise RuntimeError("bytes required found %s" % type(text))

    def _hashkey(self,key):
        return hashlib.sha256(key.encode()).digest()

    def decrypt(self,key,message):
        cipher = AES.new(key=self._hashkey(key=key))
        if self.encoding:
            resp = cipher.decrypt(ciphertext=base64.b64decode(s=message))
        else:
            resp = cipher.decrypt(ciphertext=message)
        return self.pkcs7decode(text=resp)
