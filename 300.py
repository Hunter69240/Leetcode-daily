class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i] will store the length of the longest increasing subsequence
        # starting at index i
        LIS = [1] * len(nums)

        # Traverse from right to left
        for i in range(len(nums) - 1, -1, -1):
            # Check all elements to the right of i
            for j in range(i + 1, len(nums)):
                # If nums[j] can extend the increasing subsequence from nums[i]
                if nums[i] < nums[j]:
                    # Update LIS[i] with the best possible extension
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # The answer is the longest among all LIS[i] values
        return max(LIS)
