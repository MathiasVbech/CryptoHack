import requests

class CompressionOracleAttack:
    def __init__(self, base_url='https://aes.cryptohack.org/ctrime/encrypt/'):
        self.base_url = base_url
        # Exact alphabet order from the hint
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}0123456789abcdefghijklmnopqrstuvwxyz"

    def encrypt(self, plaintext):
        """Encrypt plaintext via server endpoint"""
        try:
            url = self.base_url + plaintext.hex() + '/'
            response = requests.get(url)
            return response.json()['ciphertext']
        except Exception as e:
            print(f"Encryption error: {e}")
            return None

    def crack_flag(self):
        # Start with known prefix
        flag = b"crypto{"
        
        # Continue until flag is complete
        last_chr = b""
        while last_chr != b"}":
            # Baseline: encrypt flag + wildcard repeated twice
            baseline_payload = (flag + b"*") * 2
            baseline_out = self.encrypt(baseline_payload)
            baseline_len = len(baseline_out)
            
            # Try each character in the alphabet
            for c in self.alphabet:
                # Create test payload
                test_payload = (flag + c.encode()) * 2
                test_out = self.encrypt(test_payload)
                
                # Print current attempt
                print(f"Trying char: {c}")
                print(f"Baseline length: {baseline_len}, Test length: {len(test_out)}")
                
                # If test payload is shorter, we found a match
                if len(test_out) < baseline_len:
                    flag += c.encode()
                    last_chr = c.encode()
                    print(f"Matched character: {c}")
                    print(f"Current flag: {flag}")
                    break
        
        return flag

    def run_attack(self):
        flag = self.crack_flag()
        print("\nCracked Flag:", flag.decode())

# Run the attack
if __name__ == "__main__":
    attacker = CompressionOracleAttack()
    attacker.run_attack()