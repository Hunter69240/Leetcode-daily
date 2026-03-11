nums = [1,1,0,1,1,1]

count = 0  # This will hold the maximum number of consecutive 1s found so far
c = 0      # This counts the current streak of consecutive 1s

for i in nums:
    if i == 1:
        c += 1  # Increment current streak if the element is 1
    else:
        count = max(c, count)  # Update max count if current streak ended
        c = 0                  # Reset current streak count when 0 is encountered

count = max(c, count)  # After loop ends, check if the last streak is the longest
print(count)           # Print the maximum count of consecutive 1s found
