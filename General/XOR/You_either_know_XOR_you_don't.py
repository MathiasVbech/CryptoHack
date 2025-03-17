from itertools import cycle

ciphertext_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ciphertext = bytes.fromhex(ciphertext_hex)
known_plaintext = b'crypto{'

# Derive the partial key from the known plaintext
partial_key = bytes([c ^ p for c, p in zip(ciphertext[:len(known_plaintext)], known_plaintext)])

# The next ciphertext byte after the known plaintext
next_cipher = ciphertext[len(known_plaintext)]
# Assume the next plaintext character is '1' (as in 'crypto{1...')
assumed_char = ord('1')
next_key_byte = next_cipher ^ assumed_char

# Complete the key
key = partial_key + bytes([next_key_byte])

# Decrypt the entire ciphertext with the derived key
decrypted = bytes([c ^ k for c, k in zip(ciphertext, cycle(key))])

print(decrypted.decode())