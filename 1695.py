nums = [5, 2, 1, 2, 5, 2, 1, 2, 5]

seen = set()        # Stores the unique elements in the current window
i = 0               # Left pointer of the sliding window
current_sum = 0     # Sum of elements in the current window
max_sum = 0         # Track the maximum sum found so far

for j in range(len(nums)):  # j is the right pointer
    # If the current element is already in the window (duplicate), shrink the window from the left
    while nums[j] in seen:
        seen.remove(nums[i])       # Remove leftmost element
        current_sum -= nums[i]     # Subtract it from current sum
        i += 1                     # Move the left pointer right

    seen.add(nums[j])              # Add the new element to the set
    current_sum += nums[j]         # Add its value to the current sum
    max_sum = max(max_sum, current_sum)  # Update max sum if needed

print(max_sum)  # Final output
