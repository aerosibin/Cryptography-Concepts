import numpy as np
from hill_cipher import encrypt_hill
from hill_cipher import decrypt_hill
from hash_func import hash

key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

# Example 1
message = "CAT"

#Hill Encryption
ciphertext = encrypt_hill(message, key)
hash_text = hash(ciphertext)
decrypt = decrypt_hill(ciphertext, key, hash_text)


print(f"Plain text:      {message}")
print(f"Ciphertext:   {ciphertext}")
print(f"Custom Hash:  {hash_text}")
print(f"Decrypted text: {decrypt}")
print("------------------")
# Example 2
message = "SIBIN"

#Hill Encryption
ciphertext = encrypt_hill(message, key)
hash_text = hash(ciphertext)
decrypt = decrypt_hill(ciphertext, key, hash_text)


print(f"Plain text:      {message}")
print(f"Ciphertext:   {ciphertext}")
print(f"Custom Hash:  {hash_text}")
print(f"Decrypted text: {decrypt}")

