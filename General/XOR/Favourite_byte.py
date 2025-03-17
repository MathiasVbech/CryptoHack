# Single-Byte XOR Decryption

def single_byte_xor(hex_string, key):
    """
    XOR a hex-encoded string with a single byte
    
    Args:
    hex_string (str): Hex-encoded input string
    key (int): Single byte key to XOR with
    
    Returns:
    str: Decrypted string
    """
    # Convert hex to bytes
    bytes_data = bytes.fromhex(hex_string)
    
    # XOR each byte with the key
    decrypted_bytes = bytes(b ^ key for b in bytes_data)
    
    try:
        # Try to decode as ASCII
        return decrypted_bytes.decode('ascii')
    except UnicodeDecodeError:
        return None

# Hex-encoded input
hex_input = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Try all possible single-byte keys (0-255)
for key in range(256):
    result = single_byte_xor(hex_input, key)
    
    # Check if decryption produces a readable string
    if result and all(32 <= ord(c) <= 126 for c in result):
        print(f"Key: {key}")
        print(f"Decrypted: {result}")
        print("Flag (if applicable):", f"crypto{{{result}}}")