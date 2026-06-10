def a():
    # Define the list of coins and the target amount
    nums = [1, 2, 3]
    target = 4
    
    # Initialize a DP array with size (target + 1) filled with zeros
    # dp[i] will store the number of ways to make up the amount i using the given coins
    dp = [0] * (target + 1)
    
    # There is one way to make the amount 0, which is to use no coins
    dp[0] = 1
    
    # Iterate through each amount from 1 to target
    for i in range(1, target + 1):
        # For each coin in the list of coins
        for num in nums:
            # Calculate the difference between the current amount and the coin value
            diff = i - num
            
            # If the difference is non-negative, it means we can use this coin to make up the current amount
            if diff >= 0:
                # Add the number of ways to make up the amount `diff` to the current number of ways to make up amount `i`
                dp[i] += dp[diff]
    
    # Return the number of ways to make up the target amount using the given coins
    return dp[target]


print(a())
