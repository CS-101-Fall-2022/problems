# Author: Waqar Saleem
# Date: Fall 2022 semester
# Course: CS 101 Programming Fundamentals
# Purpose: demonstrating a solution to the Caesar cipher.
# Reference: https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution
# Functions:
#   - encrypt: given a plaintext and a shift amount, apply a rotation substitution
#     cipher to obtain the ciphertext
#   - decrypt: given a ciphertext and a shift amount, apply a rotation substitution
#     cipher to obtain the plaintext
# Concepts: the implementation below uses
#   - functions
#   - computation
#   - modular arithmetic
#   - string data type
#   - some string methods
#   - string concatenation
#   - addition assignment operator
#   - iteration
#   - ASCII encoding
# Variations:
#   - Conditional can be used instead of modular arithmetic
#   - The arithmetic can be different
#   - Substitution can be through str.replace() instead of arithmetic
#   - Substitution can be through a dictionary instead of arithmetic
#   - Cipher text can be in blocks of 5 letters separated by space
#   - Non-letters can be handled


def test_encrypt():
    # edge case
    assert encrypt("", 13) == ""
    # ignore non-alphabets
    assert encrypt(" habib ", 13) == encrypt("h , 13  abib ", 13) == encrypt("habib!", 13) == encrypt("habib", 13)
    # ignore case
    assert encrypt("habib", 13) == encrypt("HABIB", 13) == encrypt("HaBiB", 13)
    # tests
    assert encrypt("habib", 0) == "HABIB"
    assert encrypt("hello", 13) == "BYFFI"
    assert encrypt("hello", 10) == "ROVVY"

def test_decrypt():
    # edge case
    assert decrypt("", 13) == ""
    # tests
    assert decrypt("RKLSLEXSFOBCSDI", 10) == 'HABIBUNIVERSITY'
    assert decrypt("UNOVOHAVIREFVGL", 13) == 'HABIBUNIVERSITY'

def encrypt(plaintext, shift):
    plaintext = plaintext.upper()
    ciphertext = ''
    for c in plaintext:
        if c.isalpha():
            d = ord(c) - ord('A')
            d = (d + shift) % 26
            d = chr(ord('A') + d)
            ciphertext += d
    return ciphertext
    
def decrypt(ciphertext, shift):
    plaintext = ''
    for c in ciphertext:
        d = ord(c) - ord('A')
        d = (d - shift) % 26
        d = chr(ord('A') + d)
        plaintext += d
    return plaintext
    
