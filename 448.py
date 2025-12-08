class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # ---------------------------- INTUITION ----------------------------
        # Given an array of size n containing numbers from 1 to n,
        # some numbers may appear once, some twice, and some may be missing.
        # We need to find which numbers from 1..n do NOT appear in nums.
        #
        # Trick:
        # Every number `n` has a target index `n - 1`.
        # If we see number `n`, we mark index (n - 1) as "visited".
        #
        # Instead of using extra memory like a hash set,
        # we mark visited numbers by NEGATING the value at target index.
        #
        # At the end:
        # If an index has a POSITIVE value, it means we never visited that number → missing.

        # ---------------------- FIRST PASS: MARK VISITED NUMBERS ----------------------
        for n in nums:
            index = abs(n) - 1      # convert number to index (1 → 0, 2 → 1, ... n → n-1)
            if nums[index] > 0:     # only negate once (avoid negating twice, which makes + again)
                nums[index] = -nums[index]  # mark as visited (negate value)

        # ---------------------- SECOND PASS: COLLECT MISSING NUMBERS ------------------
        result = []
        for i, val in enumerate(nums):
            # if val is still positive, index i was never marked → number (i+1) missing
            if val > 0:
                result.append(i + 1)

        return result

# nums = [4, 3, 2, 7, 8, 2, 3, 1]

# First loop (marking):
# n = 4 → index = 3 → nums[3] becomes -7
# n = 3 → index = 2 → nums[2] becomes -2
# n = 2 → index = 1 → nums[1] becomes -3
# n = 7 → index = 6 → nums[6] becomes -3
# n = 8 → index = 7 → nums[7] becomes -1
# n = 2 → index = 1 → nums[1] already negative → skip
# n = 3 → index = 2 → nums[2] already negative → skip
# n = 1 → index = 0 → nums[0] becomes -4

# Array becomes:
# [-4, -3, -2, -7, 8, 2, -3, -1]

# Second loop (collecting):
# i=0 → -4 < 0 → skip
# i=1 → -3 < 0 → skip
# i=2 → -2 < 0 → skip
# i=3 → -7 < 0 → skip
# i=4 → 8  > 0 → missing number = 5
# i=5 → 2  > 0 → missing number = 6
# i=6 → -3 < 0 → skip
# i=7 → -1 < 0 → skip

# Result = [5, 6]



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
