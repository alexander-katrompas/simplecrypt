"""
driver file for testing Caesar and Vigenere crypt, decrypt, and cracking

Author: Alex Katrompas
"""

import caesar
import constants as cs
import vigenere

CAESAR = False

if CAESAR:

    M = "The entire message for Caesar Cypher."
    K = 'b'

    print("Key:", K)
    print("Message:", M)
    print("Length:", len(M), "\n")

    C = caesar.encrypt(M, cs.offset(K))
    print("Encrypted:", C)

    m = caesar.decrypt(C, cs.offset(K))
    print("Decrypted:", m, end=" ")

    if M == m:
        print("[success]\n")
    else:
        print("[fail]\n")

    print("Cracking '", C, "' with brute force...\n", sep="")
    caesar.bruteForceCrack(C)

    print("Cracking '", C, "' with probabilistic cracking...\n", sep="")
    caesar.probabilisticCrack(C)

else:
    M = "The entire message for Vigenere Cypher."
    K = 'vige'
    
    print("Key:", K)
    print("Message:", M)
    print("Length:", len(M), "\n")
    
    C = vigenere.encrypt(M, K)
    print("Encrypted:", C)

    m = vigenere.decrypt(C, K)
    print("Decrypted:", m, end=" ")

    if M == m:
        print("[success]\n")
    else:
        print("[fail]\n")

