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

    for i in range(length):
        # get character one at a time
        char = message[i]

        if char in cs.ALPHAUPPER:
            # encrypt uppercase characters in plain text
            result += cs.ALPHAUPPER[(cs.offset(char) + key) % 26]
        elif char in cs.ALPHALOWER:
            # encrypt lowercase characters in plain text
            result += cs.ALPHALOWER[(cs.offset(char) + key) % 26]
        elif char in cs.NONALPHA:
            # encrypt numbers and punctuation
            result += cs.NONALPHA[(cs.offset(char) + key) % naLength]
        else:
            result += char
    
    return result

def decrypt(message, key):
    return encrypt(message, -key)

def bruteForceCrack(message):
    print("  Trying all non-alphabetic keys...")
    print("  ---------------------------------")
    for ch in cs.NONALPHA:
        print(" ", ch, decrypt(message, cs.offset(ch)))
    print()
    
    print("  Trying all lowercase keys...")
    print("  ----------------------------")
    for ch in cs.ALPHALOWER:
        print(" ", ch, decrypt(message, cs.offset(ch)))
    print()
    print("  Trying all uppercase keys...")
    print("  ----------------------------")
    for ch in cs.ALPHAUPPER:
        print(" ", ch, decrypt(message, cs.offset(ch)))
    print()

def probabilisticCrack(message):
    # only works if key is 0-25 (i.e. a-z or A-Z)

    results = {} # make and empty dictionary
    for key in message: 
        # get highest frequency letter
        results[key] = results.get(key, 0) + 1

    mostUsedLetter = max(results, key=results.get)
    c = cs.offset(mostUsedLetter)
    print("  Highest Frequency Letter:", mostUsedLetter, "with a value of", c, "\n")

    for ch in cs.FREQUENCY:
        diff = ((c - cs.offset(ch)) % 26);
        #print("difference between trial key", ch, cs.ALPHALOWER[c], "is", cs.offset(ch), "-", c, "=", diff)
        print("  Odds are", mostUsedLetter, "is",ch, "so the key must be",cs.ALPHALOWER[diff], "...")
        print("    Message:", decrypt(message, diff))
