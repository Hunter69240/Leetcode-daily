nums = [1, 4, 4, 2, 4]  # The list of numbers in which we want to find a duplicate

seen = set()  # Initialize an empty set to keep track of numbers we have already encountered
duplicate = None  # Variable to store the duplicate number once found, None means no duplicate found yet

# Iterate through each number in the list
for num in nums:
    # Check if the current number is already in the 'seen' set
    if num in seen:
        # If yes, we've found a duplicate, so assign it to 'duplicate'
        duplicate = num
        # Since we only want the first duplicate found, break out of the loop
        break
    # If current number is not in 'seen', add it to the set for future checks
    seen.add(num)

# Print the found duplicate number; if none was found, it will print None
print("Duplicate number is:", duplicate)
