import requests

def get_encrypted_image():
    """Fetch encrypted image from the server"""
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    response = requests.get(url)
    return bytes.fromhex(response.json()['encrypted'])

def decrypt_image():
    # Known PNG header
    png_hdr = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 
                     0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52])
    
    # Get encrypted image
    encrypted = get_encrypted_image()
    
    # Extract keystream by XORing known header with encrypted header
    keystream = []
    for i in range(len(png_hdr)):
        keystream.append(png_hdr[i] ^ encrypted[i])
    
    # Decrypt the entire image by repeating the keystream
    decrypted = []
    for i in range(len(encrypted)):
        decrypted.append(encrypted[i] ^ keystream[i % len(keystream)])
    
    # Write decrypted image
    with open('decrypted_bean_counter.png', 'wb') as fd:
        fd.write(bytes(decrypted))
    
    print(f"Image decrypted. File size: {len(decrypted)} bytes")

# Run the decryption
decrypt_image()