#!/usr/bin/env python3

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)

def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

# Print initial welcome messages
print(r.readline().decode())
print(r.readline().decode())
print(r.readline().decode())
print(r.readline().decode())

# Send request to buy flag
request = {
    "buy": "flag"
}
json_send(request)

# Receive and print the response
response = json_recv()
print(response)

# Close the connection
r.close()