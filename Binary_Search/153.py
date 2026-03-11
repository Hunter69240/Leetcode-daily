nums = [3, 4, 5, 0, 1, 2]

i = 0                       # Set the left boundary of the search range
j = len(nums) - 1           # Set the right boundary of the search range

# Binary search loop to find the minimum element
while i < j:
    mid = (i + j) // 2      # Find the middle index

    if nums[j] < nums[mid]: # If mid element is greater than the rightmost,
        i = mid + 1         # The minimum must be to the right of mid
    else:                   # Else, the minimum is at mid or to the left
        j = mid             # Move the right boundary to mid

# After the loop, i == j; that's the index of the minimum element
print(nums[i])              # Output the minimum element
