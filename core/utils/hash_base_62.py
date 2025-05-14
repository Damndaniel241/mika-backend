
# import hashlib

# def base62_encode(num, alphabet='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
#     """Encodes a number in base 62."""
#     if num == 0:
#         return alphabet[0]
#     arr = []
#     base = len(alphabet)
#     while num:
#         num, rem = divmod(num, base)
#         arr.append(alphabet[rem])
#     arr.reverse()
#     return ''.join(arr)

# def generate_base62_hash(text):
#     """Generates a base 62 hash from a string."""
#     hash_hex = hashlib.sha256(text.encode('utf-8')).hexdigest()
#     hash_int = int(hash_hex, 16)
#     return base62_encode(hash_int)

# # Example usage
# text = "example string"
# base62_hash = generate_base62_hash(text)
# print(f"The base 62 hash of '{text}' is: {base62_hash}")

import random

def base62_encode(num, alphabet='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

def generate_random_base62_hash(length=7, alphabet='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    base = len(alphabet)
    max_num = base ** length - 1
    random_num = random.randint(0, max_num)
    return base62_encode(random_num, alphabet).rjust(length, alphabet[0])

# Example usage
random_base62_hash = generate_random_base62_hash()
print(f"Random 7-character base62 hash: {random_base62_hash}")
