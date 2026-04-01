def hash(text):
    hash_value = 0x811C9DC5  # Initial seed
    prime = 0x01000193       # Prime multipler
    
    for char in text:
        hash_value ^= ord(char)
        hash_value = (hash_value * prime) & 0xFFFFFFFF
        hash_value = ((hash_value << 5) | (hash_value >> 27)) & 0xFFFFFFFF
        
    return hex(hash_value)