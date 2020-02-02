"""
driver file for testing Caesar and Vigenere crypt, decrypt, and cracking

Author: Alex Katrompas
"""

import constants as cs
import caesar
import vigenere


M = "The entire message."
K = 'b'

print("Key:", K)
print("Message:", M)
print("Length:", len(M), "\n")

C = caesar.encrypt(M, cs.offset(K))
print("Encrypted:", C)

m = caesar.decrypt(C, cs.offset(K))
print("Decrypted:", M, end=" ")

if M == m:
    print("[success]\n")
else:
    print("[fail]\n")

print("Cracking '", C, "' with brute force...\n", sep="")
caesar.bruteForceCrack(C)

print("Cracking '", C, "' with probabilistic cracking...\n", sep="")
caesar.probabilisticCrack(C)
