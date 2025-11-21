class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # dp[i] will be a dictionary that maps:
        #    sum -> number of ways to reach that sum using the first i elements
        #
        # We create dp as a list of dictionaries (using defaultdict for convenience),
        # One dictionary for each "stage" i = 0..len(nums)
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        # Base case:
        # With 0 numbers, the only achievable sum is 0, and there is exactly 1 way to achieve it
        dp[0][0] = 1
    
        # Build dp table
        # For each number, we try assigning +num and -num to all previously reachable sums
        for i in range(len(nums)):
            # Iterate over all current possible sums at stage i
            for cur_sum, count in dp[i].items():
                # If we add nums[i], new sum is cur_sum + nums[i]
                # Add the number of ways to reach the old sum
                dp[i + 1][cur_sum + nums[i]] += count

                # If we subtract nums[i], new sum is cur_sum - nums[i]
                dp[i + 1][cur_sum - nums[i]] += count
        
        # At the end, dp[len(nums)] contains all achievable sums after using all numbers
        # We return the number of ways to reach the target sum
        return dp[len(nums)][target]
