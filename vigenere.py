"""
Caesar encrption and decryption

Author: Alex Katrompas
"""

import caesar
import constants as cs

def generateKeyString(key, length):
    keyString = ""
    keyLength = len(key)
    for i in range(length):
        keyString += key[i % keyLength]
    return keyString

def encrypt(message, key):
    encrypted = ""
    keyString = generateKeyString(key, len(message))

    i = 0
    for ch in message:
        encrypted += caesar.encrypt(ch, cs.offset(keyString[i]))
        i += 1

    return encrypted

def decrypt(message, key):
    decrypted = ""
    keyString = generateKeyString(key, len(message))
    
    i = 0
    for ch in message:
        decrypted += caesar.decrypt(ch, cs.offset(keyString[i]))
        i += 1

    return decrypted

