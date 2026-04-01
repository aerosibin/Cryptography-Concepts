# Hill Cipher Encryption & Custom Hashing Implementation

This repository contains a Python implementation of a **3x3 Hill Cipher** and a **custom bitwise hash function**. It demonstrates the application of linear algebra in cryptography and the mechanics of data integrity through hashing.

---

## Theory & Concepts

### Hill Cipher
The Hill Cipher is a polyalphabetic substitution cipher based on linear algebra. 
* **Encryption**: Plaintext is divided into blocks of size $n$ ($n=3$). Each block is treated as a vector $P$ and multiplied by an $n \times n$ key matrix $K$ modulo 26:  
    $$C = (K \cdot P) \pmod{26}$$
* **Decryption**: To retrieve the message, the ciphertext vector $C$ is multiplied by the modular inverse of the key matrix:  
    $$P = (K^{-1} \cdot C) \pmod{26}$$
    *Note: A key matrix is only valid if its determinant is non-zero and coprime to 26.*

### Custom Hash
The hashing algorithm is inspired by the **FNV (Fowler–Noll–Vo)** hash. It ensures data integrity by:
1.  **XORing** each character code into a 32-bit initial seed.
2.  Multiplying by a specific **Prime Multiplier** (`0x01000193`).
3.  Applying a **Circular Bit Rotation** (`<< 5 | >> 27`) to distribute bits across the digest, ensuring a high "avalanche effect" where small input changes yield vastly different outputs.

---

## 🚀 Instructions to Run

### 1. Prerequisites
Ensure you have **Python 3.x** installed. You will also need the **NumPy** library for matrix operations.
```bash
pip install numpy
```

## 2. Execution

Save the provided Python code as `hill_cipher.py`.

Run the script via your terminal or IDE:

```bash
python hill_cipher.py
```

## Worked Examples

Below are two test cases demonstrating the transformation of plaintext through the encryption and hashing process.

### Example 1: Standard 3-Letter Word
* **Plaintext**: `CAT`
* **Key Matrix**: 
 [6 24  1] [13 16 10] [20 17 15] 
* **Ciphertext Output**: `FIN`
* **Hash Output**: `0xe2148930`

### Example 2: Padded Message (Length not multiple of 3)
* **Plaintext**: `SIBIN`
* **Key Matrix**: 
    [6 24  1] [13 16 10] [20 17 15] 
* **Processing**: The system pads `SIBIN` with `X` to fulfill the 3x3 matrix requirements, resulting in the block `SIBINX`.
* **Ciphertext Output**: `PIRTWY`
* **Hash Output**: `0x412958c6`

---

## Function Reference

| Function | Description |
| :--- | :--- |
| **`encrypt_hill`** | Handles text normalization (uppercase/padding) and performs matrix-vector multiplication modulo 26. |
| **`decrypt_hill`** | Reverses encryption by applying the modular inverse of the key matrix to the ciphertext. |
| **`matrix_mod_inverse`** | Computes the inverse matrix specifically for $mod \ 26$ using the determinant and adjugate matrix. |
| **`hash`** | A custom implementation using XOR folding, prime multipliers, and bitwise rotation to create a 32-bit hex digest. |
