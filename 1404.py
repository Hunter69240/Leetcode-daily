# -----------------------------------
# Convert Binary String to Integer
# -----------------------------------
s = "10"
s = int(s, 2)     # Convert binary string to decimal

count = 0         # Step counter

# -----------------------------------
# Loop until number becomes 1
# -----------------------------------
while s != 1:
    
    # If number is odd
    if s % 2 == 1:
        s += 1        # Add 1
    else:
        s = s // 2    # Divide by 2
    
    count += 1

print(count)

# -----------------------------------
# Convert Binary String to Integer
# -----------------------------------
s = "10"
s = int(s, 2)

count = 0

# -----------------------------------
# Loop until number becomes 1
# -----------------------------------
while s != 1:
    
    # Check last bit using AND
    if (s & 1) == 1:
        s += 1            # If odd
    else:
        s = s >> 1        # Right shift (divide by 2)
    
    count += 1

print(count)