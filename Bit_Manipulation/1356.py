# -----------------------------------
# Sort Integers by Number of 1 Bits
# -----------------------------------

arr = [1024,512,256,128,64,32,16,8,4,2,1]

# -----------------------------------
# Helper Function: Count Set Bits
# -----------------------------------
def countones(n):
    count = 0
    
    # Brian Kernighan’s Algorithm
    # Each iteration removes the lowest set bit
    while n > 0:
        count += 1
        n = n & (n - 1)
        
    return count


# -----------------------------------
# Main Logic
# -----------------------------------

# Dictionary to group numbers by number of set bits
count = {}

for i in arr:
    numberofones = countones(i)
    
    # If this bit-count not seen before, create list
    if numberofones not in count:
        count[numberofones] = []
        
    # Append number into its group
    count[numberofones].append(i)

# Final sorted result
res = []

# Sort by bit count (key)
for i in sorted(count):
    
    # Sort numbers inside same bit-count group
    res.extend(sorted(count[i]))

print(res)