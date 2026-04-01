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

##  Instructions to Run

### 1. Prerequisites
Ensure you have **Python 3.x** installed. You will also need the **NumPy** library for matrix operations.

```bash
pip install numpy
```

## 2. Execution

Download all the three codes `hill_cipher.py`, `hash_func.py`, `test_script.py`

Run the script via your terminal or IDE:

```bash
python test_script.py
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

## Hash Function Justification

The implemented hashing algorithm is a custom non-cryptographic hash inspired by the FNV-1a (Fowler–Noll–Vo) architecture, modified with a bitwise circular shift to enhance diffusion.

---

### Design Choice & Logic

**1. Initial Entropy (The Offset Basis)**  
The hash starts with a 32-bit constant `0x811C9DC5`. This ensures that even empty or very short strings begin with a non-zero state, preventing simple collisions.

**2. XOR Folding**  
Each character of the ciphertext is XORed into the internal state. This ensures that every single bit of the input message affects the final output, a property known as the *Avalanche Effect*.

**3. Prime Multiplication**  
We use the FNV prime `0x01000193`. Multiplying by a prime number helps "scatter" the internal state across the 32-bit integer space, making the hash less predictable and reducing the likelihood of collisions for similar strings (e.g., `"CAT"` vs `"CAR"`).

**4. Bitwise Circular Rotation**  
hash_value = (hash_value << 5) | (hash_value >> 27)
This operation performs a **left rotation**. Unlike a standard shift (where bits are lost), rotation preserves all bit information by moving them to the other end. This ensures that the influence of a character at the beginning of the message is still felt at the end of the calculation.

**5. 32-Bit Masking**  
The `& 0xFFFFFFFF` operation ensures the hash behaves consistently as a 32-bit unsigned integer, providing a uniform output length in hexadecimal format.

---

### Why This is Unique?

While standard **FNV-1a** only uses XOR and multiplication, this implementation adds a circular bitwise shift (`5` bits left, `27` bits right). This modification alters the mathematical trajectory of the hash, ensuring the output is distinct from standard library implementations and other student projects using basic polynomial hashes.

---

### Role in the System

The hash acts as an **Integrity Checksum**.

Before the Hill Cipher attempts decryption, the system verifies that the hash of the received ciphertext matches the original hash. If even a single bit of the ciphertext is altered during transmission, the XOR-rotation logic will cause the hashes to mismatch, and the system will trigger a **"Decryption failed"** alert.

## Function Reference

| Function | Description |
| :--- | :--- |
| **`encrypt_hill`** | Handles text normalization (uppercase/padding) and performs matrix-vector multiplication modulo 26. |
| **`decrypt_hill`** | Reverses encryption by applying the modular inverse of the key matrix to the ciphertext. |
| **`matrix_mod_inverse`** | Computes the inverse matrix specifically for $mod \ 26$ using the determinant and adjugate matrix. |
| **`hash`** | A custom implementation using XOR folding, prime multipliers, and bitwise rotation to create a 32-bit hex digest. |
