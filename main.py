"""
driver file for testing Caesar and Vigenere crypt, decrypt, and cracking

Author: Alex Katrompas
"""

import caesar
import vigenere

M = "Hello World"
K = 'X'

print("Key:", K)
print("Message:", M)
print("Length:", len(M), "\n")

C = caesar.encrypt(M, ord(K))
print("Encrypted:", C)

m = caesar.decrypt(C, ord(K))
print("Decrypted:", M)

if M == m:
    print("success")
else:
    print("fail")