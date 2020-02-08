"""
Caesar encrption and decryption

Author: Alex Katrompas
"""

import caesar
from collections import Counter
import constants as cs
import operator
import re

def freq_score(text):
    freqs = {
        'a': 8167,
        'b': 1492,
        'c': 2782,
        'd': 4253,
        'e': 12702,
        'f': 2228,
        'g': 2015,
        'h': 6094,
        'i': 6966,
        'j': 153,
        'k': 772,
        'l': 4025,
        'm': 2406,
        'n': 6749,
        'o': 7507,
        'p': 1929,
        'q': 95,
        'r': 5987,
        's': 6327,
        't': 9056,
        'u': 2758,
        'v': 978,
        'w': 2360,
        'x': 150,
        'y': 1974,
        'z': 74
    }

    score = 0
    for c in text:
        if c == ' ':
            score += 10000
        elif c.lower() in freqs:
            score += freqs[c.lower()]
        elif ord(c) >= 128:
            score -= 5000
        else:
            score -= 1000

    return score

def generateKeyString(key, length):
    keyString = ""
    keyLength = len(key)
    for i in range(length):
        keyString += key[i % keyLength]
    return keyString

def encrypt(message, key, xor=False):
    
    encrypted = ""
    keyString = generateKeyString(key, len(message))

    i = 0
    for ch in message:
        if xor:
            num = format(ord(ch) ^ ord(keyString[i]), "x")
            if len(num) % 2: num = "0" + num
            encrypted += num
        else:
            encrypted += caesar.encrypt(ch, cs.offset(keyString[i]))
        i += 1

    return encrypted

def decrypt(message, key, xor=False):
    decrypted = ""
    keyString = generateKeyString(key, len(message))
    
    if xor:
        i = j = 0
        length = len(message)
        while i < length:
            ch = message[i:i+2]
            ch = int(ch, 16)
            #print(ch)
            ch = format(ch ^ ord(keyString[j]), "x")
            ch = chr(int(ch, 16))
            decrypted += ch
            i+=2
            j+=1
    else:
        for i, ch in enumerate(message):
            decrypted += caesar.decrypt(ch, cs.offset(keyString[i]))

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
    # the reason for partitioning by *possible* key length is that each
    # partition will have been partioned into what was encrypted by the same
    # key therefore the IC should be close to the English IC and not random

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

def find_key(ctext, keylen):
    # this assumes key is alpha only
    ctext = ctext.lower()
    key = ""

    # break up text so that each partition is what is encrpted by same key position
    parted = partition(ctext, keylen)

    # for each block that could be dectrypted by the key length given
    for col in parted: 
        # print(col)
        scores = {}
        for i, letter in enumerate(cs.ALPHALOWER): # enumerating 1:A, 2:B, etc
            # transposed will be each group of characters encrypted with the
            # same letter. if key len is 4, there will be 4 groups of 26 where
            # each group represents all possible characters as that group's key
            transposed = [cs.ALPHALOWER[(cs.ALPHALOWER.index(c) - i) %
                len(cs.ALPHALOWER)] for c in col]
            # scores is ranks each of letter a-z, for each group
            scores[letter] = freq_score(transposed)
        key += max(scores.items(), key=operator.itemgetter(1))[0]

    return key

def crack(message):
    # note this version of cracking does not allow for non alpha characters
   
    message = message.lower()
    print("   ================================")
    best = find_keylen_ics(message)
    for k, v in best:
        key = find_key(message, k)
        print("%21s%3d%5s%6.3f" % ("trying key length:", k, "ic:", v), end="")
        print(" with key:", key)
        print("    ", decrypt(message, key))
        print()
    print("   ================================\n")

    return
