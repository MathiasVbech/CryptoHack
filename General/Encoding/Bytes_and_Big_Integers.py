from Crypto.Util.number import long_to_bytes

# The large integer to convert
large_num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer back to bytes
message_bytes = long_to_bytes(large_num)

# Decode the bytes to a string
message = message_bytes.decode('ascii')

print("Original Number:", large_num)
print("Decoded Message:", message)

# Optional: Print out the byte representation and hex representation
print("\nBytes:", message_bytes)
print("Hex Representation:", message_bytes.hex())