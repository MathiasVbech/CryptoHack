import base64

# Hex string to decode
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Decode hex to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Step 2: Encode bytes to Base64
base64_encoded = base64.b64encode(decoded_bytes)

# Convert Base64 bytes to string for printing
base64_string = base64_encoded.decode('ascii')

print("Original Hex String:", hex_string)
print("Decoded Bytes:", decoded_bytes)
print("Base64 Encoded:", base64_string)