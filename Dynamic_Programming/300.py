def a():
    # Problem:
    # Find the length of the longest strictly increasing subsequence (not necessarily contiguous)

    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]

    # Why DP:
    # Each position can act as an ending point of a subsequence
    # To know the best subsequence ending here, we must look at all valid previous endings
    # Overlapping subproblems → DP stores results

    # State:
    # dp[i] = length of the longest increasing subsequence that ends exactly at index i
    dp = [1 for _ in range(len(nums))]

    # Transition:
    # For each i, check all j < i
    # If nums[j] < nums[i], we can extend subsequence ending at j
    for i in range(len(dp)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Final answer:
    # LIS can end anywhere → take max over all dp[i]
    return max(dp)


# --- STATE MEANING + DRY RUN ---

# nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]

# dp[0] = 1
# Meaning: LIS ending at index 0 → [1]

# dp[1] = 2
# From 1 → 3
# Meaning: [1, 3]

# dp[2] = 3
# From 3 → 6
# Meaning: [1, 3, 6]

# dp[3] = 4
# From 6 → 7
# Meaning: [1, 3, 6, 7]

# dp[4] = 5
# From 7 → 9
# Meaning: [1, 3, 6, 7, 9]

# dp[5] = 3
# 4 cannot extend from 9,7,6
# Can extend from 3 → 4
# Meaning: [1, 3, 4]

# dp[6] = 6
# 10 extends from 9
# Meaning: [1, 3, 6, 7, 9, 10]

# dp[7] = 4
# 5 extends from 4
# Meaning: [1, 3, 4, 5]

# dp[8] = 5
# 6 extends from 5
# Meaning: [1, 3, 4, 5, 6]

# Final dp:
# [1, 2, 3, 4, 5, 3, 6, 4, 5]

# Answer = max(dp) = 6

print(a())


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         # LIS[i] will store the length of the longest increasing subsequence
#         # starting at index i
#         LIS = [1] * len(nums)

#         # Traverse from right to left
#         for i in range(len(nums) - 1, -1, -1):
#             # Check all elements to the right of i
#             for j in range(i + 1, len(nums)):
#                 # If nums[j] can extend the increasing subsequence from nums[i]
#                 if nums[i] < nums[j]:
#                     # Update LIS[i] with the best possible extension
#                     LIS[i] = max(LIS[i], 1 + LIS[j])

#         # The answer is the longest among all LIS[i] values
#         return max(LIS)
