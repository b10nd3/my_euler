"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""
import time
start_time = time.time()

# alphabet = " abcdefghijklmnopqrstuvwxyz"
# alphabet = list(alphabet)
# count = 0
#
#
# with open('d:\coding\Python\Euler\p059_cipher.txt') as f:
#     names = f.readline()
# f.close()
# names = names.split(',')
#
# # print(names)
#
# for x in names:
#     print(x, end = ' ')
# print()

# res = 0
# key = ['a', 'a', 'a']
# for x in key:
#     res += ord(x)
#     print(ord(x))
# print(res)

# for x in names:
#     print(chr(int(x) ^ key), end = ' ')

# for x in names:
#     print(chr(int(x)), end = ' ')

# def xor_cipher(str, key):
#     encript_str = ""
#     for letter in str:
#         encript_str += chr(ord(letter) ^ key)
#     return encript_str
#
#
# strg = "грузите апельсины бочками"
# key = 8
# print("original:\t", strg)
# encr_strg = xor_cipher(strg, key)
# print("encript:\t", encr_strg)
# print("decript:\t", xor_cipher(encr_strg, key))


for i in range(65, 123):
    print(chr(i), i, end=' ')




print()
print("--- %s seconds ---" % (time.time() - start_time))
# input()