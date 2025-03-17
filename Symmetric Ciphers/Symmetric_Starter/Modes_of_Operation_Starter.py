import requests
import json

# Base URL for the API
base_url = "https://aes.cryptohack.org/block_cipher_starter"

# Step 1: Get the encrypted flag
def get_encrypted_flag():
    url = f"{base_url}/encrypt_flag/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["ciphertext"]

# Step 2: Decrypt the ciphertext
def decrypt_ciphertext(ciphertext):
    url = f"{base_url}/decrypt/{ciphertext}/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["plaintext"]

# Step 3: Convert hex to ASCII
def hex_to_ascii(hex_string):
    return bytes.fromhex(hex_string).decode('utf-8', errors='ignore')

# Main function
def main():
    # Get the encrypted flag
    ciphertext = get_encrypted_flag()
    print(f"Encrypted flag: {ciphertext}")
    
    # Decrypt the ciphertext
    plaintext_hex = decrypt_ciphertext(ciphertext)
    print(f"Decrypted flag (hex): {plaintext_hex}")
    
    # Convert to ASCII
    flag = hex_to_ascii(plaintext_hex)
    print(f"Flag: {flag}")

if __name__ == "__main__":
    main()