import requests
import hashlib
import json
from Crypto.Cipher import AES


#download wordlist wget https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words -O words.txt
# Get the encrypted flag
def get_encrypted_flag():
    url = "https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["ciphertext"]

# Decrypt locally
def decrypt_flag_with_key(ciphertext_hex, key):
    try:
        ciphertext = bytes.fromhex(ciphertext_hex)
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)
        return decrypted
    except Exception as e:
        print(f"Error with key: {e}")
        return None

# Main function to brute force words
def main():
    ciphertext = get_encrypted_flag()
    print(f"Encrypted flag: {ciphertext}")
    
    # Download the word list if you don't have it
    # Use the same word list as specified in the source
    try:
        with open("words.txt", "r") as f:
            words = [w.strip() for w in f.readlines()]
    except:
        print("Could not open words.txt - please download the word list first")
        return
    
    print(f"Loaded {len(words)} words from dictionary")
    
    # Try each word
    for i, word in enumerate(words):
        if i % 1000 == 0:
            print(f"Tried {i} words...")
        
        # Hash the word using MD5 as specified in the source
        key = hashlib.md5(word.encode()).digest()
        
        # Try to decrypt
        plaintext = decrypt_flag_with_key(ciphertext, key)
        
        if plaintext:
            # Check if it looks like a flag
            try:
                decoded = plaintext.decode('utf-8', errors='ignore')
                if "crypto{" in decoded:
                    print(f"Found the flag with password '{word}'!")
                    print(f"Flag: {decoded}")
                    return
            except:
                # If decoding fails, probably not the right key
                pass
    
    print("Password not found in the word list")

if __name__ == "__main__":
    main()