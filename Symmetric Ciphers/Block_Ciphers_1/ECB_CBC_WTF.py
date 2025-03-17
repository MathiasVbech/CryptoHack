import requests
import json

# Base URL for the API
base_url = "https://aes.cryptohack.org/ecbcbcwtf"

# Step 1: Get the encrypted flag
def get_encrypted_flag():
    url = f"{base_url}/encrypt_flag/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["ciphertext"]

# Step 2: Decrypt the ciphertext using ECB mode
def decrypt_ecb(ciphertext):
    url = f"{base_url}/decrypt/{ciphertext}/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["plaintext"]

# XOR two hex strings
def xor_hex(hex1, hex2):
    # Convert hex strings to bytes
    bytes1 = bytes.fromhex(hex1)
    bytes2 = bytes.fromhex(hex2)
    
    # XOR the bytes
    xored = bytes(b1 ^ b2 for b1, b2 in zip(bytes1, bytes2))
    
    return xored.hex()

# Main function
def main():
    # Get the encrypted flag (IV + ciphertext)
    full_ciphertext = get_encrypted_flag()
    print(f"Full ciphertext: {full_ciphertext}")
    
    # Extract IV (first 16 bytes / 32 hex chars)
    iv = full_ciphertext[:32]
    ciphertext = full_ciphertext[32:]
    print(f"IV: {iv}")
    print(f"Ciphertext: {ciphertext}")
    
    # Split ciphertext into blocks (16 bytes / 32 hex chars each)
    blocks = [ciphertext[i:i+32] for i in range(0, len(ciphertext), 32)]
    
    # Decrypt each block with ECB and recover the plaintext
    flag = ""
    prev_block = iv
    
    for block in blocks:
        # Decrypt the block using ECB
        decrypted_block = decrypt_ecb(block)
        
        # XOR with the previous ciphertext block to get the plaintext
        plaintext_block = xor_hex(decrypted_block, prev_block)
        
        # Convert hex to ASCII
        plaintext_ascii = bytes.fromhex(plaintext_block).decode('utf-8', errors='ignore')
        flag += plaintext_ascii
        
        # Update previous block for next iteration
        prev_block = block
    
    print(f"Flag: {flag}")

if __name__ == "__main__":
    main()