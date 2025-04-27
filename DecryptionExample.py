#!/usr/bin/env python3

import os  # Recognizes the OS used
from cryptography.fernet import Fernet  # Used to create the encryption method. Fernet uses 128-bit AES.

# Find the files that will be used for decryption
files = []
for file in os.listdir():  
    if file in ["clown.py", "THEKEY.key", "savior.py"]:  
        continue
    if os.path.isfile(file):  
        files.append(file)

print("Files to be decrypted:", files)

# Read the encryption key
try:
    with open("THEKEY.key", "rb") as THEKEY:
        secretkey = THEKEY.read()
except FileNotFoundError:
    print("Error: THEKEY.key file not found! Unable to decrypt files.")
    exit()

# Secret phrase verification
secretphrase = "me"
user_phrase = input("Who messed up?\n")

if user_phrase == secretphrase:
    for file in files:  
        with open(file, "rb") as THEFILE:
            contents = THEFILE.read()
        try:
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as THEFILE:
                THEFILE.write(contents_decrypted)
            print(f"Decrypted {file} successfully.")
        except Exception as e:
            print(f"Error decrypting {file}: {e}")

    print("Yeah, that's right. Silly you :). Don't fall for this ever again!!! By the way, your files are decrypted.")

else:
    print(" >:( WRONG! >:( ")
