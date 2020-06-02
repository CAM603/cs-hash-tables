# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# Create a list of plaintext frequencies, sorted by frequency.

# Create a list of encrypted text frequencies, sorted by frequency.
from operator import itemgetter
import os
import sys


def letter_frequencies(text):
    frequencies = {}

    for asciicode in range(65, 91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    sorted_letters = sorted(frequencies.items(),
                            key=itemgetter(1), reverse=True)

    return sorted_letters


def readFile(path):
    f = open(path, "r")
    text = f.read()
    f.close()
    return text


def decrypt_dictionary(encrypted_filepath):
    encrypted_text = readFile(encrypted_filepath)

    plaintext_frequencies = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    encrypted_frequencies = letter_frequencies(encrypted_text)

    decryption_dict = {}
    for i in range(0, 26):
        decryption_dict[encrypted_frequencies[i][0]
                        ] = plaintext_frequencies[i][0]

    return decryption_dict


def decrypt_file(encrypted_filepath, decrypted_filepath):
    encrypted_text = readFile(encrypted_filepath)
    decrypted_dict = decrypt_dictionary(encrypted_filepath)

    decrypted_list = []

    for letter in encrypted_text:
        asciicode = ord(letter)
        if asciicode >= 65 and asciicode <= 90:
            decrypted_list.append(decrypted_dict[letter])
        if asciicode == 32:
            decrypted_list.append(" ")

    decrypted_text = "".join(decrypted_list)

    f = open(decrypted_file, "w")
    f.write(decrypted_text)
    f.close()


encrypted_file = os.path.join(sys.path[0], 'ciphertext.txt')
decrypted_file = os.path.join(sys.path[0], 'decipheredtext.txt')

decrypt_file(encrypted_file, decrypted_file)
# Merge these lists to create an estimated mapping between encrypted letters and plaintext letters.
# Use this mapping to create an approximate decryption of the encrypted text.
