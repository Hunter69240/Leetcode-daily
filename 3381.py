class Solution(object):
    def maxSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # prefix[i] will store the MINIMUM prefix sum seen so far
        # for indices where (index % k == i)
        prefix = [float("inf")] * k
        prefix[0] = 0  # For subarrays starting at index 0

        res = float("-inf")  # Store max subarray sum
        total = 0  # Running total (prefix sum)

        for i, n in enumerate(nums):
            total += n               # Update total prefix sum
            length = i + 1           # 1-based length of prefix
            prefix_len = length % k  # Mod bucket for the current index

            # Candidate best sum: total - minimum prefix seen with same mod length
            res = max(res, total - prefix[prefix_len])

            # Update minimum prefix sum for this mod bucket
            prefix[prefix_len] = min(prefix[prefix_len], total)

        return res


'''
nums = [4, -2, 3, 7, -5, 2]
k = 3


| i | num | total | length | length % k | prefix[length % k] | Candidate = total - prefix | res  | Updated prefix |
| - | --- | ----- | ------ | ---------- | ------------------ | -------------------------- | ---- | -------------- |
| 0 | 4   | 4     | 1      | 1          | inf                | -inf                       | -inf | prefix[1] = 4  |
| 1 | -2  | 2     | 2      | 2          | inf                | -inf                       | -inf | prefix[2] = 2  |
| 2 | 3   | 5     | 3      | 0          | 0                  | 5 - 0 = 5                  | 5    | prefix stays   |
| 3 | 7   | 12    | 4      | 1          | 4                  | 12 - 4 = 8                 | 8    | prefix stays   |
| 4 | -5  | 7     | 5      | 2          | 2                  | 7 - 2 = 5                  | 8    | prefix stays   |
| 5 | 2   | 9     | 6      | 0          | 0                  | 9 - 0 = 9                  | 9    | prefix stays   |



res = 9


'''