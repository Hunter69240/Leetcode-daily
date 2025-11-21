# # The following code snippet provides two different approaches to find all the numbers missing
# # from a list `nums` which contains numbers in the range 1 to n (where n = length of nums).
# # Some numbers may be duplicated, and some may be missing.

# # First Approach: Using a Set for Membership Checking

# # nums = [1, 1]  # Example input list

# # nums_set = set(nums)  # Convert list to set to enable O(1) average membership lookup

# # missing = []  # Initialize list to hold missing numbers

# # Loop over all numbers from 1 to n (inclusive)
# # For each number i, check if it is NOT in nums_set
# # If it is missing from nums, add it to the missing list
# # This method has O(n) time complexity and O(n) space complexity due to the set

# # for i in range(1, len(nums) + 1):
# #     if i not in nums_set:
# #         missing.append(i)

# # print(missing)  # Output the list of missing numbers



# # Second Approach: In-Place Swapping Method to Achieve O(1) Extra Space

# # The class Solution contains the method findDisappearedNumbers:
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         n = len(nums)  # Store length of input array

#         # The key idea:
#         # Each number x in nums should ideally be placed at index x - 1.
#         # For example, number 3 should be placed at index 2.
#         # By placing numbers in their correct positions, we can identify which numbers are missing:
#         # if index i does not contain the number i+1, then i+1 is missing from the original array.

#         for i in range(n):
#             # While the current number is not at its correct place, and the target position does not already have the correct number,
#             # swap the current number with the number at its target position.
#             while nums[i] != nums[nums[i] - 1]:
#                 # Swap numbers to put nums[i] in its correct position at nums[i] - 1
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

#         # After this rearrangement, numbers that are not at their correct indices indicate missing values.
#         # Collect all indices where nums[i] != i + 1 and add i + 1 to the missing list.
#         return [i + 1 for i in range(n) if nums[i] != i + 1]


# # Example usage:
# # sol = Solution()
# # nums = [4,3,2,7,8,2,3,1]
# # print(sol.findDisappearedNumbers(nums))  # Output: [5,6]


# # Summary of the ideology:
# # - The set approach uses extra space but is conceptually simple and efficient for smaller inputs.
# # - The in-place swapping approach cleverly uses the array indices as a hash to position numbers correctly,
# #   which reduces extra space to O(1) and keeps time complexity at O(n).
# # - By rearranging the list such that each number x is at index x-1, any mismatch between index and value
# #   reveals missing numbers.
# # - This method avoids extra data structures and works by leveraging the properties of the input constraints
# #   (numbers in the range [1, n]) to do the detection in-place.
