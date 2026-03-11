# Check if any permutation of s1 is a substring of s2

s1 = "abc"
s2 = "acb"

# Initialize frequency dictionaries for s1 and window in s2
s1d = {}
s2d = {}
hasp = False  # This flag will be set to True if a valid permutation is found

# Count character frequencies in s1
for i in s1:
    if i in s1d:
        s1d[i] += 1
    else:
        s1d[i] = 1

# Set up a sliding window of size len(s1)
i = 0
j = i + len(s1)

# Slide the window over s2 while keeping window size fixed
while j <= len(s2):
    s2d.clear()  # Clear the previous window's frequency map

    # Count character frequencies in current window s2[i:j]
    for k in s2[i:j]:
        if k in s2d:
            s2d[k] += 1
        else:
            s2d[k] = 1

    # If current window has same character frequency as s1, it's a valid permutation
    if s1d == s2d:
        hasp = True
        break  # No need to check further, one match is enough

    # Slide the window by one position
    i += 1
    j += 1

# Print result: True if permutation found, else False
print(hasp)
