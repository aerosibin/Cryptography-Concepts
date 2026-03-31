import numpy as np

def hash(text):
    hash_value = 0x811C9DC5  # Initial seed
    prime = 0x01000193       # Prime multipler
    
    for char in text:
        hash_value ^= ord(char)
        hash_value = (hash_value * prime) & 0xFFFFFFFF
        hash_value = ((hash_value << 5) | (hash_value >> 27)) & 0xFFFFFFFF
        
    return hex(hash_value)

def encrypt_hill(plaintext, key_matrix):
    plaintext = plaintext.upper().replace(" ", "")
    while len(plaintext) % 3 != 0:
        plaintext += 'X'
    nums = [ord(c) - ord('A') for c in plaintext]
    nums_matrix = np.array(nums).reshape(-1, 3).T 
    cipher_nums = np.dot(key_matrix, nums_matrix) % 26
    return "".join(chr(int(n) + ord('A')) for n in cipher_nums.flatten('F'))


def modInverse(a, m):
    for x in range(1, m):
        if (((a % m) * (x % m)) % m == 1):
            return x
    return None

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = modInverse(det % modulus, modulus)
    
    if det_inv is None:
        raise ValueError("Matrix is not invertible modulo 26. Choose a different key.")
    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_inv % modulus

def decrypt_hill(ciphertext, key_matrix):
    key_inv = matrix_mod_inverse(key_matrix, 26)
    nums = [ord(c) - ord('A') for c in ciphertext]
    cipher_matrix = np.array(nums).reshape(-1, 3).T
    plain_nums = np.dot(key_inv, cipher_matrix) % 26
    return "".join(chr(int(n) + ord('A')) for n in plain_nums.flatten('F'))

key = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
message = "CAT"

#Hill Encryption
ciphertext = encrypt_hill(message, key)
decrypt = decrypt_hill(ciphertext, key)
hash_text = hash(ciphertext)

print(f"Plain text:      {message}")
print(f"Ciphertext:   {ciphertext}")
print(f"Decrypted text: {decrypt}")
print(f"Custom Hash:  {hash_text}")
