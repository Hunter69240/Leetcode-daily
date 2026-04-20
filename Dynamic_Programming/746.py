def a():
    # INPUT:
    # cost[i] = cost of stepping on stair i
    cost = [10, 15, 20]

    # WHY DP:
    # Problem asks for minimum cost with choices at each step (1 or 2 jumps)
    # Overlapping subproblems + optimal substructure → Dynamic Programming

    # WHAT dp REPRESENTS:
    # dp[i] = minimum cost required to reach position i
    # NOTE:
    # - "position" is NOT the stair itself
    # - position i means standing just before stepping onto stair i
    # - final goal is position len(cost) → top (beyond last stair)

    # WHY len(cost) + 1:
    # extra slot needed to represent "top of floor"
    dp = [0 for i in range(len(cost) + 1)]

    # BASE CASE:
    # dp[0] = 0 → start before first stair
    # dp[1] = 0 → start before second stair
    # (given you can start from index 0 or 1)

    # BUILD DP:
    # we compute from left → right because:
    # dp[i] depends on dp[i-1] and dp[i-2] (already computed)
    for i in range(2, len(cost) + 1):

        # TRANSITION:
        # to reach position i, you must come from:
        # - position i-1 (stepped on stair i-1 → pay cost[i-1])
        # - position i-2 (stepped on stair i-2 → pay cost[i-2])

        value = min(
            dp[i - 1] + cost[i - 1],  # 1-step jump
            dp[i - 2] + cost[i - 2]   # 2-step jump
        )

        # store best cost for reaching position i
        dp[i] = value

    # ANSWER:
    # dp[last] = minimum cost to reach top
    return dp[-1]


print(a())

'''
DRY RUN 

cost = [10, 15, 20]
n = 3

dp = [0, 0, 0, 0]
       0  1  2  3   (positions)

i = 2:
    dp[2] = min(
        dp[1] + cost[1],  → 0 + 15 = 15
        dp[0] + cost[0]   → 0 + 10 = 10
    )
    dp[2] = 10

dp = [0, 0, 10, 0]

i = 3:
    dp[3] = min(
        dp[2] + cost[2],  → 10 + 20 = 30
        dp[1] + cost[1]   → 0 + 15 = 15
    )
    dp[3] = 15

dp = [0, 0, 10, 15]

RETURN dp[3] = 15
'''


# #DP Because q it mentions minimum cost keyword

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # Add a 0 at the end to represent the top of the stairs (no cost to stand at the top)
#         cost.append(0)

#         # Start from the third-to-last step and move backwards to the beginning
#         # We iterate backwards because we need to know the minimum cost of future steps
#         # to calculate the current step's minimum cost
#         for i in range(len(cost)-3, -1, -1):
#             # At each step, we have two choices:
#             # 1. Climb 1 step: current cost + cost of next step (i+1)
#             # 2. Climb 2 steps: current cost + cost of step after next (i+2)
#             # We choose the minimum of these two options
#             cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

#         # We can start from either step 0 or step 1, so return the minimum of both
#         return min(cost[0], cost[1])
