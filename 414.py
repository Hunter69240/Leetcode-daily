# nums = [-1, 2, 3]  # Input list of numbers

# # Step 1: Remove duplicates by converting list to a set, then back to a list
# # Using set(nums) removes all duplicate values since sets only store unique elements
# nums = list(set(nums))

# # Step 2: Sort the list in ascending order
# nums.sort()
# print(nums)  # Optional: print the sorted unique list

# # Step 3: Check if the list has fewer than 3 unique elements
# if len(nums) < 3:
#     print(max(nums))  # If less than 3 unique numbers, return the largest one
# else:
#     print(nums[-3])   # Else return the 3rd largest number (3rd from end in sorted list)

#ORRRRRRRR

# # Initialize three variables to track the top 3 unique maximum values
# # Start with the lowest possible value (negative infinity)
# first = second = third = float('-inf')

# # Loop through each number in the input list
# for num in nums:
#     # Skip this number if it's already one of the top 3 (to ensure uniqueness)
#     if num in (first, second, third):
#         continue

#     # If the number is greater than current first (maximum)
#     if num > first:
#         # Push down previous values to make room for the new first
#         third = second
#         second = first
#         first = num

#     # If the number is less than first but greater than second
#     elif num > second:
#         # Push down second to third, and update second
#         third = second
#         second = num

#     # If the number is less than second but greater than third
#     elif num > third:
#         third = num  # Just update third

# # After processing all numbers:
# # If we have found a valid third maximum, return it
# # Else (there were fewer than 3 unique numbers), return the maximum (first)
# print(third if third != float('-inf') else first)
