from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa

def extract_modulus_from_der(der_cert_path):
    # Read the DER-encoded certificate
    with open(der_cert_path, 'rb') as f:
        der_cert_data = f.read()
    
    # Parse the DER-encoded certificate
    cert = x509.load_der_x509_certificate(der_cert_data)
    
    # Get the public key
    public_key = cert.public_key()
    
    # Extract the modulus
    if isinstance(public_key, rsa.RSAPublicKey):
        modulus = public_key.public_numbers().n
        return modulus
    else:
        raise ValueError("Certificate does not contain an RSA public key")

# File path for the DER certificate
der_cert_path = '2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der'

# Extract and print the modulus
try:
    modulus = extract_modulus_from_der(der_cert_path)
    print("Modulus (decimal):", modulus)
except Exception as e:
    print("Error:", e)