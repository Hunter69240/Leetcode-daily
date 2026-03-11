class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Create a DP array of size (amount + 1)
        # dp[i] represents the number of ways to make up amount 'i'
        dp = [0] * (amount + 1)

        # Base case: there's exactly 1 way to make amount 0 (use no coins)
        dp[0] = 1

        # Iterate through each coin one by one
        # This ensures combinations are counted, not permutations
        for coin in coins:

            # For each coin, update the ways to make every amount
            # starting from 'coin' up to the target 'amount'
            for i in range(coin, amount + 1):

                # Add ways to make (i - coin) to dp[i]
                # Because if we can make (i - coin), then adding this coin
                # will let us make 'i' as well
                dp[i] = dp[i] + dp[i - coin]

        # The final answer: number of ways to make up the target 'amount'
        return dp[amount]
