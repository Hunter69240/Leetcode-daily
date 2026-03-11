class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at both ends
        nums = [1] + nums + [1]
        
        # Memo: (l, r) -> max coins from bursting balloons in nums[l:r]
        dp = {}

        def dfs(l, r):
            # No balloons left in interval
            if l > r:
                return 0

            # Return cached result
            if (l, r) in dp:
                return dp[(l, r)]
            
            best = 0
            
            # Choose each balloon i as the last one to burst in this interval
            for i in range(l, r + 1):
                # Coins gained from bursting i last
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                
                # Add optimal coins from left and right sub-intervals
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                
                best = max(best, coins)
            
            dp[(l, r)] = best
            return best
        
        # Solve for the full interval (excluding the artificial boundaries)
        return dfs(1, len(nums) - 2)
