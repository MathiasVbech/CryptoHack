import requests
import binascii

def encrypt(plain, iv):
    """Encrypt plaintext via the server's endpoint"""
    url = f"https://aes.cryptohack.org/symmetry/encrypt/{plain}/{iv}"
    r = requests.get(url).json()
    return bytes.fromhex(r["ciphertext"])

def encrypt_flag():
    """Get encrypted flag from server"""
    url = "https://aes.cryptohack.org/symmetry/encrypt_flag"
    r = requests.get(url).json()
    return bytes.fromhex(r["ciphertext"])

def xor_bytes(a, b):
    """XOR two byte strings of equal length"""
    return bytes(x ^ y for x, y in zip(a, b))

def crack_flag():
    # Get encrypted flag
    iv_ciphertext = encrypt_flag()
    
    # Split IV and ciphertext
    iv = iv_ciphertext[:16].hex()
    flag_ciphertext = iv_ciphertext[16:]
    
    # Encrypt chosen plaintext (all zeros)
    chosen_ciphertext = encrypt("00"*33, iv)
    
    # XOR flag ciphertext with chosen ciphertext to reveal flag
    flag = xor_bytes(flag_ciphertext, chosen_ciphertext)
    
    return flag.decode()

# Crack and print the flag
print(crack_flag())