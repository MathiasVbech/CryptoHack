def extended_gcd(a, m):
    # Extended Euclidean algorithm to find multiplicative inverse
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = egcd(b % a, a)
            return gcd, y - (b // a) * x, x

    # Find multiplicative inverse
    gcd, x, _ = egcd(a, m)
    
    # Ensure the inverse is positive and within the modulus
    if x < 0:
        x += m
    
    return x

# Find the multiplicative inverse of 3 mod 13
p = 13
a = 3

# Calculate the multiplicative inverse
inverse = extended_gcd(a, p)

print(f"Multiplicative inverse of {a} mod {p} is: {inverse}")

# Verify the result
verification = (a * inverse) % p
print(f"Verification: {a} * {inverse} ≡ {verification} mod {p}")