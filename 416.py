class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If total sum is odd, it cannot be split into two equal subsets
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)  # 0 sum is always possible (choose no elements)
        target = sum(nums) // 2  # We only need to check for half the sum

        # Iterate from the last element to the first
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            # For every sum we have seen so far, try including nums[i]
            for t in dp:
                # If we exactly reach the target, we can stop early
                if t + nums[i] == target:
                    return True
                # Add the new sum formed by including nums[i]
                nextDP.add(t + nums[i])
                # Also keep the sum formed by NOT including nums[i]
                nextDP.add(t)
            # Move to the next dp set
            dp = nextDP
        
        # Final check: whether target sum is achievable
        return True if target in dp else False
