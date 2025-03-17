# Hex Decoder
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Convert hex string to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Convert bytes to string for printing
decoded_flag = decoded_bytes.decode('ascii')

print("Decoded Flag:", decoded_flag)

# This shows the reversibility of the process
print("\nConverting back to hex:")
print(decoded_flag.encode('ascii').hex())