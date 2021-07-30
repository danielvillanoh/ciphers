# author: Daniel Villano-Herrera
# date: 7/30/2021

# difficulty: medium

# Wikipedia: https://en.wikipedia.org/wiki/Caesar_cipher
#   Read this for a better understanding of the cipher.

# Introduction
#
# Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.
#
# The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using
#   an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular
#   arithmetic. The letter is shifted for as many values as the value of the key.
#
# The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13.
#
# A ROT13 on the Latin alphabet would be as follows:
#
# Plain:  abcdefghijklmnopqrstuvwxyz
# Cipher: nopqrstuvwxyzabcdefghijklm
#
# It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.
#
# Ciphertext is written out in the same formatting as the input including spaces and punctuation.
# Examples
#
#     ROT5 omg gives trl
#     ROT0 c gives c
#     ROT26 Cool gives Cool
#     ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#     ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.
#
# Instructions
#   1 - The program should accept input in the form of a string, which will be the plain text. This is the text
#           to be encrypted.
#   2 - The program should also accept a key from the user, which will be the shift for the rotational cipher.
#   2 - Convert the plain text into cipher text using the rotational cipher, shifting by the amount specified
#           by the user.
#   3 - Print the result to the user.
#
# WRITE CODE BELOW #

