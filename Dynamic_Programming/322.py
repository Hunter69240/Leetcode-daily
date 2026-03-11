class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with amount+1 (impossible value) for all positions
        # dp[i] represents minimum coins needed to make amount i
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0

        # Iterate through all amounts from 1 to target amount
        for a in range(1, amount + 1):
            # Try using each coin denomination
            for c in coins:
                # Check if current coin can be used (amount - coin >= 0)
                if a - c >= 0:
                    # Update dp[a] with minimum of:
                    # 1. Current value (dp[a])
                    # 2. 1 + coins needed for remaining amount (dp[a-c])
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        # Return result: if dp[amount] is still amount+1, no solution exists (return -1)
        # Otherwise return the minimum number of coins needed
        return dp[amount] if dp[amount] != (amount + 1) else -1
