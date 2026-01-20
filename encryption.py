import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
# these would be used
chars = list(chars)

key = chars.copy()

random.shuffle(key)

# print(f"chars : {chars}")
# print(f"key : {key}")

#encryption
plain_text = input("Enter a message to encrypt : ")
encrypt_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypt_text +=key[index]

print(f"Original message : {plain_text}")
print(f"Encrypted message: {encrypt_text}")


#decryption
plain_text = ""
encrypt_text = input("Enter a message to decrypt : ")

for letter in encrypt_text:
    index = key.index(letter)
    plain_text +=chars[index]

print(f"Encrypted message: {encrypt_text}")
print(f"Original message : {plain_text}")
