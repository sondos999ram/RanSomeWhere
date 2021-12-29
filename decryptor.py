import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto import Random
import base64
key = "aGFja2xhYg=="
public_key="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyKphUCe18Eel8L/v0zxm
km3rwSJ+MD5+MmjyPA8RB5ihw7xap78fMS5B7mrp7Eog4m4Ra7RH1sjXOz6t7wQb
VsOFPIfYr7PjoFghdjzKRCmOdwKtY9/1l5rWs2Mli9bGs5IssNtmbFDKJyXUeMZz
LsqokGYZpJMDWPBQuZiIlw/uUj79YpOwEhaT9Iyrg03eqbWvNbIdPXmKzrGpP6Ai
BKcKJ7ufpqi5nYLsVOj4f1MdC17q1uYU18LH0JfzRS/79knqqmKAvIoE/LbVXdKz
4v5ayCaV5WG2qEDJpSdLUGdC9DdIT2VpPBypz6nRhUvl7sonVSkTeUZBKZqpx7fK
XwIDAQAB
-----END PUBLIC KEY-----"""
private_key='''-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,3C8148DE8B94FC07

SPptaj0CBN5DkolADW7xV69AuqSWF57lR3DdNB0RJPG/bZDiVuYOmmXgU4eqGnPs
z9YZmf9jWGsh/eCIFAsPNB/mGlOAPhCgXRZWf9lZpIg+j+OQ+vf2lQW9NzzBQgjL
BZcNbM/Q5zowVIDdnLHKpidzzOfBPu7do7KUBGLsFfRDuCrzxHlWnYyRg0G8qRjc
LqdVnmivZsBhIIMobVCSuQgiJol3wg/egC0VlWk4SGaW9AP9lDiWy/sft6fZJzMR
4J8EHh4jNyClxcdoGqY8VjaCYcPUtAd33teWNL/Mcqe8tyzA7qmCPYIgsf1XlfTU
iU+jU5UeLEpcyvBhLYiA3DfQTbBfAnLz9mIqt8aWPz+FuUzPQhszMavs4Rd5J1Jg
BmZXJ2UTi4rzIbGbdNmjgpAjLXroLHQZt/XAwXKTjJW13OZNVuBBRJ4B7JTJBkxW
2fzG+Xy7lYX8JuNWxoUaZiewQRX0yV1+k55tRhDsgJ+KAdQ0IPed7ADZbR4LHPh6
hqU4Gyeb46qaQ9Wvfw/J+BFJ/WXqCRpncx8E9SgIHQcbPZ4QJBfB/XjM5AqS6R/O
+IXbZvVPvVEHLqJ3Uvvho2/8U1qH3z2PBXPGzT/Ew8Kgcv4JZC94GSwdr+FPiZJQ
0UcGNCSAGQpYmeX+rix0Dkgcs/OVw4tan8o7ytpzJsIisATTjkxWpN/vQKh/cQWB
2L7Tw42ENQXB6yIM6anTlHZPWdEs5nuVQ5FmcY6pxjv5Y8B34GkUGJrjSlMFNv/W
Uwffn250+eZp5nKo/K0yoBcuLf2Lt65Hjjv0jDI7uOqLF8ay/yBiyZsYiPpb0PiQ
b25Tae2Kfj1nF0rH20452XfCyXFytVeBAesNrPZg18FV5AMKX9tyC1jxb1Qe8mUg
3CnHjx3tozfwzi+Y10kHCPzfnpXqm74wrU11G39Azhw4O/xyO3Yz2kyBJMbkPiL7
GhWhk8SWeZwUj8LIEPoNGvFfQko7NojJmcXo1O1a1IN3pfuUmm9vC0bGXnFTBJsr
AoAovBYrXmfTRfomGrAW1Z5wGMb8++3u/auqB2YiAEj58H8pdlU8U04zxkQoEpeJ
tlMyTeM3TodYhu9rVrzw94lZvJITlxBAUBrUYAdkds0C5BxHZ4dUoFG+uCBPMyhd
UwIuIwb6M0E+yTpzazfwHTnvab2zdd8uIkoXGlGWaImeCpcLuwnmiS5krUtchLsF
Upwoy1Q88yQWvzKP4Ofb3x9kLlN3VmSgaUvVriTJjgeHymhVBWe6PDhz9bb8KGSw
Zi2rmFFCQstJ4Q4EWpRNjhpUppTQOw+zYYoUztDlD2NGXhrEkIVjGUAf04ZFhDot
pT8l5k59LJSlNAhZ002CGF2BCzMgbbEji6zK8xl6U8HPx0IR4uQq8nHd+uZ0W/py
YGq5Rq1FI++0m/205Zy4/MurTel+5gjP94WUavM5pBVhsGjDP2saj481DVejQvZz
9ytr5ogywcF/XyYfPYsSw+khQpgz4bVe+jk6zQ6Vlp6zYdzrkmBbV6f1sHpAD8H0
wRRkbFbNxUDTMLGC4AZyHa5n216e5VBgkmFhkTAU5g4GBekta/wc8fvIZ1EMdkkE
-----END RSA PRIVATE KEY-----'''

def getkey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

hashed=getkey(base64.b64decode(key))
IV = Random.new().read(16)
encryptor = AES.new(hashed, AES.MODE_CBC, IV)
print(hashed)
recipient_key = RSA.import_key(public_key)
encryptorRSA = PKCS1_OAEP.new(recipient_key)
enckey=encryptorRSA.encrypt(hashed)
print(enckey)
print(len(enckey))
#f=open('/home/kali/RanSomeWhere/plain','wb')
#f.write(enckey)
#f.close()
#x=open('/home/kali/RanSomeWhere/plain','rb')
#enckey=x.read()
#print(enckey)

server_key = RSA.import_key(open('private.pem').read(), passphrase="123456")
decryptorRSA = PKCS1_OAEP.new(server_key)
deckey=decryptorRSA.decrypt(enckey)
print(deckey)
#f=open('/home/kali/RanSomeWhere/key','wb')
#f.write(deckey)
