"""
driver file for testing Caesar and Vigenere crypt, decrypt, and cracking

Author: Alex Katrompas
"""

import caesar
import constants as cs
import vigenere

print("=================================")
print("===========CAESAR CYPER==========")
print("=================================")
print()

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

print("\n")
print("=================================")
print("=========VIGENERE CYPER==========")
print("=================================")
print()

M = "theentiremessageforthevigenerecypher"
K = 'key'

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

# note this version of cracking does not allow for non alpha characters
print("Cracking '", C, "' by finding repeated blocks of text...\n", sep="")
vigenere.crack(C)
