# author: Daniel Villano-Herrera
# date: 7/29/2021

# difficulty: easy

# Wikipedia: https://en.wikipedia.org/wiki/Atbash
#   Read this for a better understanding of the cipher.

# Introduction
#
# Create an implementation of the atbash cipher, an ancient encryption system created in the Middle East.
#
# The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such
#   that the resulting alphabet is backwards. The first letter is replaced with the last letter,
#   the second with the second-last, and so on.
#
# An Atbash cipher for the Latin alphabet would be as follows:
#
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: zyxwvutsrqponmlkjihgfedcba
#
# It is a very weak cipher because it only has one possible key, and it is a simple monoalphabetic substitution
#   cipher. However, this may not have been an issue in the cipher's time.
#
# Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, and
#   punctuation is excluded. This is to make it harder to guess things based on word boundaries.
#
# Examples
#
#     Encoding test gives gvhg
#     Decoding gvhg gives test
#     Decoding gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt gives thequickbrownfoxjumpsoverthelazydog
#
#
# Program Requirements:
#   1 - The program should accept input in the form of a string, which will be the plain text. This is the text
#           to be encrypted.
#   2 - Convert the plain text into cipher text using the atbash cipher.
#   3 - Print the result to the user.
#
# HINTS:
#   1 - It may be helpful to tell the program what the plain alphabet is, as well as the cipher.
#   2 - Remember that lists can be built up, meaning it may be useful to start with an empty list.
#
# WRITE DOWN THE STEPS BEFORE ATTEMPTING THE PROGRAM

# Step 1: Write out the normal alphabet and the cipher alphabet.
lower_normal_alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower_cipher_alphabet = lower_normal_alphabet[::-1]
upper_normal_alphabet = lower_normal_alphabet.upper()
upper_cipher_alphabet = lower_cipher_alphabet.upper()

# Step 2: Get the word we're going to encrypt
plain_text = input('Enter text: ')
cipher_text = ''

# Step 5
for i in range(len(plain_text)):
    # Step 3(a)
    current_letter = plain_text[i]
    # If the current letter is a space, then concatenate the cipher text with the space.
    if current_letter == ' ':
        cipher_text += ' '

    # Else if the current letter is uppercase, then we do the steps 3 and 4 but only on uppercase.
    elif current_letter.isupper():
        position = upper_normal_alphabet.find(current_letter)

        # Step 3(c)
        cipher_letter = upper_cipher_alphabet[position]

        # Step 4
        cipher_text += cipher_letter
    else:
        # Step 3(b)
        position = lower_normal_alphabet.find(current_letter)

        # Step 3(c)
        cipher_letter = lower_cipher_alphabet[position]

        # Step 4
        cipher_text += cipher_letter

print(cipher_text)
