n = 3
res = 0
shift_length = 0
mod = 10**9 + 7

for i in range(1, n + 1):

    # If i is power of 2, increase bit length
    # (i & (i-1)) removes lowest set bit
    # If result becomes 0 → only one set bit → power of 2
    if i & (i - 1) == 0:
        shift_length += 1

    # Left shift previous result to make space
    # Then add current number
    res = ((res << shift_length) + i) % mod

print(res)