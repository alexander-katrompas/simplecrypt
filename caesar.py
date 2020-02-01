"""
Caesar encrption and decryption

Author: Alex Katrompas
"""

import constants as cs

def encrypt(message, key):
    # initialize result
    result = ""
    length = len(message)
    naLength = len(cs.NONALPHA)

    # make offsets for ascii
    A = ord('A')
    a = ord('a')
    NA = ord(cs.NONALPHA[0])

    for i in range(length):
        # get character one at a time
        char = message[i]

        if char in cs.ALPHAUPPER:
            # encrypt uppercase characters in plain text
            result += cs.ALPHAUPPER[((ord(char) - A) + key) % 26]
        elif char in cs.ALPHALOWER:
            # encrypt lowercase characters in plain text
            result += cs.ALPHALOWER[((ord(char) - a) + key) % 26]
        elif char in cs.NONALPHA:
            # encrypt numbers and punctuation
            result += cs.NONALPHA[((ord(char) - NA) + key) % naLength]
        else:
            result += char
    
    return result

def decrypt(message, key):
    return encrypt(message, -key)
