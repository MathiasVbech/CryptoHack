def extended_gcd(a, b):
    # Base case
    if a == 0:
        return b, 0, 1
    
    # Recursive case
    gcd, u1, v1 = extended_gcd(b % a, a)
    
    # Update u and v
    u = v1 - (b // a) * u1
    v = u1
    
    return gcd, u, v

# Given primes
p = 26513
q = 32321

# Calculate extended GCD
gcd, u, v = extended_gcd(p, q)

print(f"GCD of {p} and {q}: {gcd}")
print(f"u = {u}")
print(f"v = {v}")
print(f"Verification: {p}*{u} + {q}*{v} = {p*u + q*v}")
print(f"Smaller of u and v: {min(u, v)}")