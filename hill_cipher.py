import numpy as np
from hash_func import hash

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

def decrypt_hill(ciphertext, key_matrix, hash1):
    if hash1==hash(ciphertext):
        key_inv = matrix_mod_inverse(key_matrix, 26)
        nums = [ord(c) - ord('A') for c in ciphertext]
        cipher_matrix = np.array(nums).reshape(-1, 3).T
        plain_nums = np.dot(key_inv, cipher_matrix) % 26
        return "".join(chr(int(n) + ord('A')) for n in plain_nums.flatten('F'))
    else:
        print("Decryption failed")


