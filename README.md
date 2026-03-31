# Cryptogaphy-Concepts

# Hill Cipher Encryption & Custom Hashing Implementation

The Hill Cipher is a classical cryptography algorithm based on linear algebra. It uses a square matrix as a key to transform blocks of plaintext into ciphertext. This implementation specifically handles:
1.  **Encryption**: Matrix-vector multiplication modulo 26.
2.  **Decryption**: Inverse matrix calculation using the modular multiplicative inverse of the determinant.
3.  **Hashing**: A custom Fowler–Noll–Vo (FNV) inspired hash with bitwise rotations.

### 1. Hill Cipher (Symmetric Encryption)
The core of the encryption relies on the equation:
$$C = (K \cdot P) \pmod{26}$$
Where:
* **$C$**: Ciphertext vector.
* **$K$**: The $3 \times 3$ encryption key matrix.
* **$P$**: Plaintext vector.

#### Decryption Logic
To decrypt, we find the modular inverse of the key matrix ($K^{-1}$):
$$P = (K^{-1} \cdot C) \pmod{26}$$
The implementation includes a robust `matrix_mod_inverse` function that calculates the determinant and its modular inverse to ensure the matrix can be flipped within the bounds of the 26-letter alphabet.

### 2. Custom Hashing Function
The `hash()` function produces a hexadecimal digest of the ciphertext. It uses:
* **XOR Folding**: Incorporates each character into the hash state.
* **Prime Multiplication**: Spreads the entropy using a specific prime constant (`0x01000193`).
* **Bitwise Rotation**: Left-shifting and OR-ing (`<< 5 | >> 27`) to ensure small changes in input (avalanche effect) result in significantly different hashes.


### Logic Flow
1.  **Pre-processing**: The plaintext is converted to uppercase and padded with 'X' to ensure its length is a multiple of 3.
2.  **Numerical Mapping**: Letters A-Z are mapped to integers 0-25.
3.  **Linear Transformation**: NumPy performs high-speed dot product operations between the key matrix and the message vectors.
4.  **Formatting**: The resulting numbers are converted back to characters and the hash is generated from the final ciphertext.
