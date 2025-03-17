# XOR Chain Decryption Challenge

def xor_bytes(a, b):
    """XOR two byte strings"""
    return bytes(x ^ y for x, y in zip(a, b))

# Given hex-encoded keys and flag
KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_XOR_KEY1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_XOR_KEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_XOR_CHAIN = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

# Recover KEY2 by XORing KEY2_XOR_KEY1 with KEY1
KEY2 = xor_bytes(KEY2_XOR_KEY1, KEY1)

# Recover KEY3 by XORing KEY2_XOR_KEY3 with KEY2
KEY3 = xor_bytes(KEY2_XOR_KEY3, KEY2)

# Decrypt FLAG using the XOR chain properties
# FLAG = FLAG ^ KEY1 ^ KEY3 ^ KEY2
flag = xor_bytes(FLAG_XOR_CHAIN, KEY1)
flag = xor_bytes(flag, KEY3)
flag = xor_bytes(flag, KEY2)

# Convert to string and print
flag_str = flag.decode('ascii')
print("Decrypted Flag:", flag_str)

# Demonstrate XOR properties used:
print("\nXOR Properties Demonstration:")
print("Commutative: A ^ B = B ^ A ✓")
print("Associative: (A ^ B) ^ C = A ^ (B ^ C) ✓")
print("Identity: A ^ 0 = A ✓")
print("Self-Inverse: A ^ A = 0 ✓")