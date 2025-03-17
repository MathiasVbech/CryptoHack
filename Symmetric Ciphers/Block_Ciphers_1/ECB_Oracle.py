#!/usr/bin/env python3
import requests
import time
import string

def encrypt(plaintext_hex):
    url = f"https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext_hex}/"
    try:
        r = requests.get(url)
        return r.json()["ciphertext"]
    except:
        time.sleep(2)  # Wait if error
        return None

def bruteforce():
    flag = ''
    block_size = 32  # 16 bytes in hex representation
    
    # Characters to try
    chars = '{' + '_' + '}' + string.digits + string.ascii_lowercase + string.ascii_uppercase
    
    while True:
        padding_len = 31 - len(flag)  # Ensure alignment with block boundary
        padding = '1' * padding_len
        
        # Get reference ciphertext
        ref = encrypt(padding.encode().hex())
        if not ref:
            continue
        
        # Try each possible next character
        found = False
        for c in chars:
            test_input = padding + flag + c
            result = encrypt(test_input.encode().hex())
            if not result:
                continue
            
            # Compare the second block
            if result[block_size:block_size*2] == ref[block_size:block_size*2]:
                flag += c
                print(f"Found: {flag}")
                found = True
                
                # If we find closing brace, we're done
                if c == '}':
                    return flag
                break
            
            time.sleep(1)  # Avoid rate limiting
        
        if not found:
            print("Could not find next character")
            break
    
    return flag

if __name__ == "__main__":
    result = bruteforce()
    print(f"Flag: {result}")