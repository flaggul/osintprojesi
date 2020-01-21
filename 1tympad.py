#!/usr/bin/env python3

import string
import random
import sys

abc = string.ascii_lowercase
oneTimePad = list(abc)

instaKey = '' #insert instagram flag here
twittKey = '' #insert twitter flag here
stackKey = '' #insert stack exchange flag here

onetime = 'itvhnyqfsx'

def encrypt(msg, key):
    ciphertext = ''
    for idx, char in enumerate(msg):
        charIdx = abc.index(char)
        keyIdx = oneTimePad.index(key[idx])

        cipher = (keyIdx + charIdx) % len(oneTimePad)
        ciphertext += abc[cipher]

    return ciphertext

def decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''

    charIdx = abc.index(ciphertext[0])
    keyIdx = oneTimePad.index(key[0])

    cipher = (charIdx - keyIdx) % len(oneTimePad)
    char = abc[cipher]

    return char + decrypt(ciphertext[1:], key[1:])

tmp1 = encrypt(instaKey, twittKey)
tmp2 = encrypt(tmp1, stackKey)
tmp3 = decrypt(tmp2, onetime)

print(tmp3)
