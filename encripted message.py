import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f'chars: {chars}')
# print(f'key: {key}')

#Encription Start

original_text = input('Enter your message to encript: ')
encripted_text = ""

for letter in original_text:
    index = chars.index(letter)
    encripted_text += key[index]

print(f"Original Message: {original_text}")
print(f"Encrypted Message: {encripted_text}")


#Decription Start

encripted_text = input('Enter your encript message to Decript: ')
original_text = ""

for letter in encripted_text:
    index = key.index(letter)
    original_text += chars[index]

print(f"Encrypted Message: {encripted_text}")
print(f"Original Message: {original_text}")