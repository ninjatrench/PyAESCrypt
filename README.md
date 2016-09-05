![alt text](https://img.shields.io/badge/build-passing-green.svg "Python 3")
![alt text](https://img.shields.io/badge/with%20love%20from-india-ff69b4.svg "Harsh Daftary")


# PyAESCrypt
Simple API to perform AES encryption on Python. This is counterpart of AESCrypt library Android, Ruby and Obj-C (https://github.com/scottyab/AESCrypt-Android and https://github.com/Gurpartap/aescrypt)


For compatiblity with AESCrypt-android Ruby and Obj-c, pyAESCrypt has the same defaults namely: 

 * 256-bit AES key (generated using sha-256)
 * CBC mode
 * PKCS7Padding
 * Blank/Empty IV **(default)**

**By default it uses base64 encoding and decoding of final ciphertext, you can skip it by passing encoding=False in object constructor** 

##Dependency
 * Python Crypto Module, hashlib and base64
 * Currently works on Python 3.x (needs some string conversion changes to work on python 2, pull requests are welcome)

# Usage

## Encrypt
 - Without base64 Encoding
```
  a = PyAesCrypt(encoding=False)
  c = a.encrypt("password","hello world")
  print(c)
  >>> b'\xd8\x1d\xb6q-\xd4\x0b\x9b7\xe5`b\x84\xb0h\xf3'
```
 - With base64 Encoding
```
  a = PyAesCrypt()
  c = a.encrypt("password","hello world")
  print(c)
  >>> b'2B22cS3UC5s35WBihLBo8w=='
```
## Decrypt
 - Without base64 Encoding
```
  a = PyAesCrypt(encoding=False)
  d = a.decrypt("password",b'\xd8\x1d\xb6q-\xd4\x0b\x9b7\xe5`b\x84\xb0h\xf3')
  print(d)
  >>> b'hello world'
```
 - With base64 Encoding
```
  a = PyAesCrypt()
  d = a.decrypt("password",b'2B22cS3UC5s35WBihLBo8w==')
  print(d)
  >>> b'hello world'
```

#Contributing
 - I created this library because I wanted similar implementation on Android Client and Python Server so it might be buggy.
 - I welcome pull requests, issues and feedback also improved documentation.
