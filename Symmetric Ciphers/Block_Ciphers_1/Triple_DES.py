import requests

def encrypt(key, plaintext):
    url = "https://aes.cryptohack.org/triple_des/encrypt/"
    response = requests.get(f"{url}{key}/{plaintext}/")
    data = response.json()
    if "error" in data:
        raise ValueError(data["error"])
    return data["ciphertext"]

def encrypt_flag(key):
    url = "https://aes.cryptohack.org/triple_des/encrypt_flag/"
    response = requests.get(f"{url}{key}/")
    data = response.json()
    if "error" in data:
        raise ValueError(data["error"])
    return data["ciphertext"]

# The key insight from the hint is using a specific key pattern:
# 8 bytes of zeros followed by 8 bytes of ones
key = "00" * 8 + "FF" * 8 + "00" * 8  # 24 bytes for Triple DES (K1|K2|K3)

# First, get the encrypted flag using our special key
encrypted_flag = encrypt_flag(key)
print(f"Encrypted flag: {encrypted_flag}")

# Then, encrypt the encrypted flag again with the same key
# Due to the meet-in-the-middle property of Triple DES with this specific key,
# this will effectively decrypt the flag
decrypted_flag = encrypt(key, encrypted_flag)
print(f"Decrypted flag: {decrypted_flag}")

# Convert the hex to ASCII
flag = bytes.fromhex(decrypted_flag).decode('ascii')
print(f"Flag: {flag}")