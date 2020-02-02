"""
Caesar encrption and decryption

Author: Alex Katrompas

"""

ALPHAUPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHALOWER = "abcdefghijklmnopqrstuvwxyz"
NONALPHA = " !\"#$%&'()*+,-./0123456789:;<=>?@"
FREQUENCY = "etaoinshrdlcumwfgypbvkjxqz"

UPPERA = ord('A')
LOWERA = ord('a')
NONALPHA0 = ord(NONALPHA[0])

def offset(key):
    off = 0
    if key in ALPHALOWER:
        off = ord(key) - LOWERA
    elif key in ALPHAUPPER:
        off = ord(key) - UPPERA
    elif key in NONALPHA:
        off = ord(key) - NONALPHA0
    
    return off
