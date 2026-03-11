nums = [1, 2, 3, 1]  # List of numbers to check for duplicates
numsset = set()      # Initialize an empty set to store unique numbers

# Loop through each number in the list
for i in nums:
    # If the number is already in the set, it's a duplicate
    if i in numsset:
        print(True)  # Duplicate found
        break        # Exit the loop early
    numsset.add(i)   # Add the number to the set if not already present
else:
    # This else block belongs to the for-loop, not the if-statement
    # It runs only if the loop completes without encountering a break
    print(False)     # No duplicates found
