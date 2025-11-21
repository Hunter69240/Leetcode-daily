#DP Because q it mentions minimum cost keyword

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Add a 0 at the end to represent the top of the stairs (no cost to stand at the top)
        cost.append(0)

        # Start from the third-to-last step and move backwards to the beginning
        # We iterate backwards because we need to know the minimum cost of future steps
        # to calculate the current step's minimum cost
        for i in range(len(cost)-3, -1, -1):
            # At each step, we have two choices:
            # 1. Climb 1 step: current cost + cost of next step (i+1)
            # 2. Climb 2 steps: current cost + cost of step after next (i+2)
            # We choose the minimum of these two options
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        # We can start from either step 0 or step 1, so return the minimum of both
        return min(cost[0], cost[1])
