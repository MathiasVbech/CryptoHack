# First congruence: 11 ≡ x mod 6
# This means we want to find the remainder when 11 is divided by 6
x = 11 % 6
print(f"x (11 mod 6) = {x}")

# Second congruence: 8146798528947 ≡ y mod 17
# This means we want to find the remainder when 8146798528947 is divided by 17
y = 8146798528947 % 17
print(f"y (8146798528947 mod 17) = {y}")

# Find the smaller of x and y
result = min(x, y)
print(f"Smaller of x and y: {result}")