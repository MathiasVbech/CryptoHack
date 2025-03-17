from pwn import * # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import long_to_bytes

HOST = 'socket.cryptohack.org'
PORT = 13377

r = remote(HOST, PORT, level='debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def decode_data(encoded_type, encoded_value):
    """
    Decode the data based on the encoding type
    """
    if encoded_type == "base64":
        return base64.b64decode(encoded_value).decode()
    elif encoded_type == "hex":
        return bytes.fromhex(encoded_value).decode()
    elif encoded_type == "rot13":
        return codecs.decode(encoded_value, 'rot_13')
    elif encoded_type == "bigint":
        # Remove '0x' prefix if present
        if encoded_value.startswith('0x'):
            encoded_value = encoded_value[2:]
        return long_to_bytes(int(encoded_value, 16)).decode()
    elif encoded_type == "utf-8":
        return ''.join(chr(x) for x in encoded_value)
    else:
        raise ValueError(f"Unknown encoding type: {encoded_type}")

# Main solving loop
try:
    while True:
        # Receive the challenge
        received = json_recv()
        
        # Check if we've reached the end
        if 'flag' in received:
            print("Flag:", received['flag'])
            break
        
        # Decode the encoded value
        decoded_value = decode_data(received['type'], received['encoded'])
        
        # Send the decoded value back
        to_send = {
            "decoded": decoded_value
        }
        json_send(to_send)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    r.close()