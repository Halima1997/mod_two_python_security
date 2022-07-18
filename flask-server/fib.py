import string


def caesar(msg, key):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    cipher = str.maketrans(alphabet, shifted_alphabet)
    return msg.translate(cipher)

print(caesar('hello world',3))