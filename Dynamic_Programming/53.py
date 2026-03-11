class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Intuition:
        # We use Kadane's Algorithm. The idea is:
        # - As we move through the array, we keep a running sum (curSum).
        # - If curSum ever becomes negative, it can't help in forming a maximum subarray,
        #   so we reset it to 0.
        # - At each step, we update maxSub with the best (maximum) sum seen so far.
        #
        # Example:
        # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        # curSum starts at 0
        # -2 → curSum = -2 → negative, reset to 0
        # 1  → curSum = 1 → maxSub = 1
        # -3 → curSum = -2 → reset to 0
        # 4  → curSum = 4 → maxSub = 4
        # -1 → curSum = 3
        # 2  → curSum = 5 → maxSub = 5
        # 1  → curSum = 6 → maxSub = 6
        # -5 → curSum = 1
        # 4  → curSum = 5
        # Final answer = 6 (subarray [4, -1, 2, 1])

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub
