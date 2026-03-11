def a():
    # Total maximum score allowed
    n = 10

    # Minimum score at which drawing stops
    k = 1

    # Maximum points that can be drawn in one move
    maxPts = 10

    # If Alice never draws (k == 0) OR
    # even the maximum possible score is within n,
    # probability of winning is 1
    if k == 0 or n >= k + maxPts - 1:
        return 1.0

    # dp[i] = probability of getting exactly score i
    dp = [0.0] * (n + 1)

    # Base case: probability of score 0 is 1
    dp[0] = 1.0

    # Sliding window sum of last maxPts dp values
    window_sum = 1.0

    # Accumulates probabilities of valid final scores
    result = 0.0

    # Compute probabilities for scores from 1 to n
    for score in range(1, n + 1):

        # Probability of reaching current score
        dp[score] = window_sum / maxPts

        # If score is less than k, game continues
        # so include this probability in window_sum
        if score < k:
            window_sum += dp[score]
        else:
            # If score >= k, game stops
            # add probability to result
            result += dp[score]

        # Remove probability that falls out of the window
        if score - maxPts >= 0:
            window_sum -= dp[score - maxPts]

    # Return final winning probability
    return result


# Call the function
s = a()

# Print the result
print(s)
