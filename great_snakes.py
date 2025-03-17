import requests
import binascii

# Collect multiple ciphertexts
ciphertexts = []
for _ in range(100):
    response = requests.get("https://aes.cryptohack.org/stream_consciousness/encrypt/")
    data = response.json()
    ciphertext = binascii.unhexlify(data['ciphertext'])
    ciphertexts.append(ciphertext)

# Find the longest ciphertext, assumed to be the flag
longest_ct = max(ciphertexts, key=len)

# Compute the first 7 bytes of the keystream using 'crypto{' prefix
keystream = bytearray()
for c, p in zip(longest_ct[:7], b'crypto{'):
    keystream.append(c ^ p)

# Decrypt the rest of the ciphertext by guessing remaining keystream bytes
flag = bytearray()
for i in range(len(longest_ct)):
    if i < len(keystream):
        flag.append(longest_ct[i] ^ keystream[i])
    else:
        # Guess keystream byte using other ciphertexts
        for ct in ciphertexts:
            if len(ct) > i:
                # Try common characters like space, underscore, letters
                for guess in [32, 95] + list(range(97, 123)):
                    k = ct[i] ^ guess
                    valid = True
                    for other_ct in ciphertexts:
                        if len(other_ct) > i and (other_ct[i] ^ k) not in range(32, 127):
                            valid = False
                            break
                    if valid:
                        keystream.append(k)
                        flag.append(longest_ct[i] ^ k)
                        break
                else:
                    continue
                break
        else:
            # Fallback: assume the flag character and compute keystream
            flag_byte = longest_ct[i] ^ 0  # Adjust based on observed patterns
            flag.append(flag_byte)
            keystream.append(longest_ct[i] ^ flag_byte)

# Convert to string and check for flag format
flag_str = flag.decode(errors='ignore')
if 'crypto{' in flag_str and flag_str.endswith('}'):
    print("Flag found:", flag_str)
else:
    print("Flag not found. Try collecting more ciphertexts.")