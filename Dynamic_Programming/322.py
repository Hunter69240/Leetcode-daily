def a():
    # INPUT:
    # coins = available denominations
    # amount = target value
    coins = [1, 2, 5]
    amount = 11

    # DP ARRAY:
    # dp[x] = minimum coins needed to form amount x
    # Initialize all to 0 (will be overwritten except dp[0])
    dp = [0 for i in range(amount + 1)]

    # BASE CASE:
    # dp[0] = 0 → 0 coins needed to make amount 0

    # BUILD FROM SMALL → LARGE
    for i in range(1, amount + 1):

        # Assume current amount cannot be formed
        min_coin = float('inf')

        # TRY ALL CHOICES (coins)
        for j in coins:

            # If we take coin j, remaining amount:
            req = i - j

            # INVALID STATE
            if req < 0:
                continue

            # TRANSITION:
            # 1 (current coin) + dp[remaining]
            min_coin = min(min_coin, 1 + dp[req])

            # DRY RUN (coins=[1,2,5], building progressively):

            # i = 1:
            # j = 1 → req = 0 → 1 + dp[0] = 1
            # j = 2,5 → invalid
            # dp[1] = 1

            # i = 2:
            # j = 1 → 1 + dp[1] = 2
            # j = 2 → 1 + dp[0] = 1
            # dp[2] = 1

            # i = 3:
            # j = 1 → 1 + dp[2] = 2
            # j = 2 → 1 + dp[1] = 2
            # dp[3] = 2

            # i = 4:
            # j = 1 → 1 + dp[3] = 3
            # j = 2 → 1 + dp[2] = 2
            # dp[4] = 2

            # i = 5:
            # j = 1 → 1 + dp[4] = 3
            # j = 2 → 1 + dp[3] = 3
            # j = 5 → 1 + dp[0] = 1
            # dp[5] = 1

            # i = 6:
            # j = 1 → 1 + dp[5] = 2
            # j = 2 → 1 + dp[4] = 3
            # j = 5 → 1 + dp[1] = 2
            # dp[6] = 2

            # i = 7:
            # j = 1 → 1 + dp[6] = 3
            # j = 2 → 1 + dp[5] = 2
            # j = 5 → 1 + dp[2] = 2
            # dp[7] = 2

            # i = 8:
            # j = 1 → 1 + dp[7] = 3
            # j = 2 → 1 + dp[6] = 3
            # j = 5 → 1 + dp[3] = 3
            # dp[8] = 3

            # i = 9:
            # j = 1 → 1 + dp[8] = 4
            # j = 2 → 1 + dp[7] = 3
            # j = 5 → 1 + dp[4] = 3
            # dp[9] = 3

            # i = 10:
            # j = 1 → 1 + dp[9] = 4
            # j = 2 → 1 + dp[8] = 4
            # j = 5 → 1 + dp[5] = 2
            # dp[10] = 2

            # i = 11:
            # j = 1 → 1 + dp[10] = 3
            # j = 2 → 1 + dp[9] = 4
            # j = 5 → 1 + dp[6] = 3
            # dp[11] = 3

        # STORE RESULT
        dp[i] = min_coin

    # FINAL ANSWER:
    # If still infinity → not possible
    return dp[-1] if dp[-1] != float('inf') else -1


print(a())


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # Initialize DP array with amount+1 (impossible value) for all positions
#         # dp[i] represents minimum coins needed to make amount i
#         dp = [amount + 1] * (amount + 1)
        
#         # Base case: 0 coins needed to make amount 0
#         dp[0] = 0

#         # Iterate through all amounts from 1 to target amount
#         for a in range(1, amount + 1):
#             # Try using each coin denomination
#             for c in coins:
#                 # Check if current coin can be used (amount - coin >= 0)
#                 if a - c >= 0:
#                     # Update dp[a] with minimum of:
#                     # 1. Current value (dp[a])
#                     # 2. 1 + coins needed for remaining amount (dp[a-c])
#                     dp[a] = min(dp[a], 1 + dp[a - c])
        
#         # Return result: if dp[amount] is still amount+1, no solution exists (return -1)
#         # Otherwise return the minimum number of coins needed
#         return dp[amount] if dp[amount] != (amount + 1) else -1
