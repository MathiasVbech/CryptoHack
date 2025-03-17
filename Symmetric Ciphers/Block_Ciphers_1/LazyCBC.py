import requests

BASE_URL = "https://aes.cryptohack.org/lazy_cbc"

def encrypt(plaintext_hex):
    response = requests.get(f"{BASE_URL}/encrypt/{plaintext_hex}/")
    return response.json()["ciphertext"]

def receive(ciphertext_hex):
    response = requests.get(f"{BASE_URL}/receive/{ciphertext_hex}/")
    return response.json()

def get_flag(key_hex):
    response = requests.get(f"{BASE_URL}/get_flag/{key_hex}/")
    return response.json()

# Encrypt a multi-block plaintext
plaintext = ("61" * 48)  # 3 blocks of "a"
ciphertext = encrypt(plaintext)

# Create modified ciphertext: first_block + zeros + first_block
first_block = ciphertext[:32]
modified_ciphertext = first_block + ("00" * 16) + first_block

# Send to receive endpoint
response = receive(modified_ciphertext)

# If successful, the response will contain the decrypted plaintext
if "error" in response and "Invalid plaintext:" in response["error"]:
    decrypted_hex = response["error"].split(": ")[1]
    decrypted = bytes.fromhex(decrypted_hex)
    
    # Extract the key by XORing the first and third blocks of the decrypted plaintext
    key = bytearray(16)
    for i in range(16):
        key[i] = decrypted[i] ^ decrypted[32+i]
    
    # Get the flag with this key
    flag_response = get_flag(key.hex())
    
    # Convert the hex plaintext to ASCII
    decoded_flag = bytes.fromhex(flag_response["plaintext"]).decode('ascii')
    print(f"Flag: {decoded_flag}")
else:
    print("Unexpected response:", response)