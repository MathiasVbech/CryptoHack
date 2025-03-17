# XOR Challenge Solver

def xor_with_key(string, key):
    """
    XOR each character of the string with the given key
    
    Args:
    string (str): Input string to XOR
    key (int): Integer to XOR with each character
    
    Returns:
    str: XORed string
    """
    # Convert each character to its Unicode integer and XOR with the key
    xored_chars = [chr(ord(char) ^ key) for char in string]
    
    # Join the XORed characters back into a string
    return ''.join(xored_chars)

# Test the function
input_string = "label"
key = 13

# Perform XOR
result = xor_with_key(input_string, key)

# Prepare the flag format
flag = f"crypto{{{result}}}"

print("Original String:", input_string)
print("XOR Key:", key)
print("XORed Result:", result)
print("Flag:", flag)