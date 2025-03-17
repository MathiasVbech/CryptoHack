import base64
import struct

def decode_ssh_public_key(ssh_key):
    # Remove the ssh-rsa prefix and any comments
    key_parts = ssh_key.split()
    base64_key = key_parts[1]
    
    # Decode the base64 key
    decoded_key = base64.b64decode(base64_key)
    
    # Parse the key structure
    # The key format is:
    # 4 bytes length of "ssh-rsa"
    # "ssh-rsa"
    # 4 bytes length of exponent
    # exponent
    # 4 bytes length of modulus
    # modulus
    
    # Skip the "ssh-rsa" part
    offset = 4 + len("ssh-rsa")
    
    # Read exponent length and exponent
    exp_len = struct.unpack('>I', decoded_key[offset:offset+4])[0]
    offset += 4
    exponent = int.from_bytes(decoded_key[offset:offset+exp_len], 'big')
    offset += exp_len
    
    # Read modulus length and modulus
    mod_len = struct.unpack('>I', decoded_key[offset:offset+4])[0]
    offset += 4
    modulus = int.from_bytes(decoded_key[offset:offset+mod_len], 'big')
    
    return modulus

# Bruce's SSH public key
ssh_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCtPLqba+GFvDHdFVs1Vvdk56cKqqw5cdomlu034666UsoFIqkig8H5kNsNefSpaR/iU7G0ZKCiWRRuAbTsuHN+Cz526XhQvzgKTBkTGYXdF/WdG/6/umou3Z0+wJvTZgvEmeEclvitBrPZkzhAK1M5ypgNR4p8scJplTgSSb84Ckqul/Dj/Sh+fwo6sU3S3j92qc27BVGChpQiGwjjut4CkHauzQA/gKCBIiLyzoFcLEHhjOBOEErnvrRPWCIAJhALkwV2rUbD4g1IWa7QI2q3nB0nlnjPnjjwaR7TpH4gy2NSIYNDdC1PZ8reBaFnGTXgzhQ2t0ROBNb+ZDgH8Fy+KTG+gEakpu20bRqB86NN6frDLOkZ9x3w32tJtqqrJTALy4Oi3MW0XPO61UBT133VNqAbNYGE2gx+mXBVOezbsY46C/V2fmxBJJKY/SFNs8wOVOHKwqRH0GI5VsG1YZClX3fqk8GDJYREaoyoL3HKQt1Ue/ZW7TlPRYzAoIB62C0= bschneier@facts"

# Extract and print the modulus
modulus = decode_ssh_public_key(ssh_public_key)
print("Modulus (decimal):", modulus)