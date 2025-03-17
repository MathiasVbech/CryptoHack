from datetime import datetime, timedelta
import requests

def bit_flip_attack():
    # Request an initial cookie
    def request_cookie():
        r = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie/")
        return r.json()["cookie"]

    def request_check_admin(cookie, iv):
        r = requests.get(f"http://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/")
        return r.json()

    # Generate the original plaintext with the current timestamp
    expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
    plain = f"admin=False;expiry={expires_at}".encode()

    # Get the initial cookie
    cookie = request_cookie()

    # Perform the bit-flipping attack
    def flip(cookie, plain):
        # Find the start of 'admin=False'
        start = plain.find(b'admin=False')
        
        # Convert cookie to bytes
        cookie_bytes = bytes.fromhex(cookie)
        
        # Prepare fake IV and cipher
        iv = [0xff]*16
        cipher_fake = list(cookie_bytes)
        
        # Target plaintext to insert
        fake = b';admin=True;'
        
        # Carefully modify bytes to flip bits
        for i in range(len(fake)):
            # XOR to modify the specific block
            cipher_fake[16+i] = plain[16+i] ^ cookie_bytes[16+i] ^ fake[i]
            iv[start+i] = plain[start+i] ^ cookie_bytes[start+i] ^ fake[i]
        
        # Convert back to hex
        cipher_fake = bytes(cipher_fake).hex()
        iv = bytes(iv).hex()
        
        return cipher_fake, iv

    # Execute the bit-flip
    modified_cookie, modified_iv = flip(cookie, plain)

    # Check if we successfully became admin
    result = request_check_admin(modified_cookie, modified_iv)
    print(result)

# Run the attack
bit_flip_attack()