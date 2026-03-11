nums = [1, 2, 3, 1]  # Input list of numbers
k = 3               # Maximum allowed index difference for duplicate values

d = {}              # Dictionary to store the most recent index of each number

# Loop through each index in the nums list
for i in range(len(nums)):
    # Check if current number has been seen before
    # AND the difference between current and previous index is at most k
    if nums[i] in d and i - d[nums[i]] <= k:
        print(True)  # Found a duplicate within k distance
        break        # Exit loop early since condition is satisfied
    # Update the index of the current number in the dictionary
    d[nums[i]] = i
