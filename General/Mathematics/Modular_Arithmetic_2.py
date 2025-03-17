# First, let's calculate the modular exponentiation for p = 17

# 3^17 mod 17
print("3^17 mod 17:", pow(3, 17, 17))

# 5^17 mod 17
print("5^17 mod 17:", pow(5, 17, 17))

# 7^16 mod 17
print("7^16 mod 17:", pow(7, 16, 17))

# Now for the final calculation with p = 65537
p = 65537
base = 27324678765465536

# Calculate base^(p-1) mod p using Python's built-in pow function
result = pow(base, p-1, p)
print(f"{base}^({p-1}) mod {p}:", result)