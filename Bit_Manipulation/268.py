#2 Solutions

#Solution 1
# ---------------------------------------------------------
# EXPLANATION:
# The array contains numbers from 0 to n with one missing.
#
# Formula for sum of numbers from 0 to n:
#   n * (n + 1) / 2
#
# The missing number = expected sum - actual sum
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [3,0,1]
#
# n = len(nums) = 3
#
# Expected numbers: 0,1,2,3
#
# req_sum = (3 * 4) / 2 = 6
#
# total_sum = 3 + 0 + 1 = 4
#
# Missing number = 6 - 4 = 2
# ---------------------------------------------------------
nums = [3, 0, 1]

n = len(nums)
total_sum = sum(nums)
req_sum = (n * (n + 1)) / 2
print(req_sum - total_sum)


#Solution 2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        # ---------------------------------------------------------
        # EXPLANATION:
        # We use the fact that:
        #   missing = (0 + 1 + 2 + ... + n) - sum(nums)
        #
        # Instead of calculating sums separately, we do it in one loop:
        #   res starts with n
        #   for each index i, add i and subtract nums[i]
        #
        # All existing numbers cancel out,
        # leaving only the missing number.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        # nums = [3,0,1]
        #
        # Initial:
        # res = len(nums) = 3
        #
        # i = 0:
        #   res += (0 - 3) → res = 0
        #
        # i = 1:
        #   res += (1 - 0) → res = 1
        #
        # i = 2:
        #   res += (2 - 1) → res = 2
        #
        # FINAL RESULT: 2
        # ---------------------------------------------------------

        for i in range(len(nums)):
            res += (i - nums[i])

        return res
