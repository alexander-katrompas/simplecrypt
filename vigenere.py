"""
Caesar encrption and decryption

Author: Alex Katrompas
"""

import caesar
from collections import Counter
import constants as cs
import re

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

def ic(text, lettersonly=False):
    # calculates the frequency distribution of letters
    # and how closely it approximated a normal distribution
    total = 0.0
    numerator = 0.0
    ic = 0.0

    text = text.lower()
    if lettersonly:
        regex = re.compile('[^a-z]')
        text = regex.sub('', text)
    
    f = Counter(text) # frequencies of each character
    for cc in f: # iterate through character counts (cc)
        # calculate the numerator in the formula and total character count
        numerator += f[cc] * (f[cc] - 1)
        total += f[cc]
    if total: ic = numerator / (total * (total - 1))
    return ic

def partition(text, num):
    # divides up text into "columns"
    # example key length 2: 'abcdef' ==> 'ace'
    #                                    'bdf'
    cols = [""] * num
    for i, c in enumerate(text):
        # i % num will be 0 to max key length
        cols[i % num] += c
    return cols # example, ['ace','bdf']
    # the reason for partitioning by key length is that each partition
    # will have been partioned into what was encrypted by the same key
    # therefore the IC should be close to the English IC and not random

def find_keylen_ics(ctext):
    low = 2 # smallest key length
    high = int(len(ctext) / 2) # highest key length
    if high >= 10:
        high = 10 #bound key length to something reasonable
    
    results = {}
    for length in range(low, high + 1):
        cols = partition(ctext, length) # all 'columns' for ctext
        ics = []
        for col in cols:  # get the ic for each 'column' in this partition
            ics.append((ic(col)))
        results[length] = sum(ics) / len(ics) # get average ic per key length

    return sorted(results.items(), key=lambda kv: -kv[1])

def crack(message):
    message = message.lower()
    message = "VIAYISBEQOWPKMQYRQAYCVEPKMQYRLOGMXRYSXNYMLDSLVIQORRORKSPJOGFYWCC"
    print("   =========================")
    best = find_keylen_ics(message)
    for k, v in best:
        print("%14s%3d%5s%6.3f" % ("key length:", k,"ic:", v))
    print("   =========================\n")
    
    
    
    
    
    return

