def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test with the example case
print("GCD of 12 and 8:", gcd(12, 8))

# Calculate GCD for the given large numbers
a, b = 66528, 52920
result = gcd(a, b)
print(f"GCD of {a} and {b}:", result)