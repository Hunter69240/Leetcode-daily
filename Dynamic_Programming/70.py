#METHOD -1

# Problem: Climbing Stairs
# Goal: count number of distinct ways to reach step n

n = 2

# DP array
# res[i] represents number of ways to reach step i
res = [0 for i in range(n + 1)]

# Base cases:
# Step 0 → 1 way (do nothing)
# Step 1 → 1 way (one single step)
res[0], res[1] = 1, 1

# Why this is DP:
# - Problem has overlapping subproblems:
#   ways(i) is reused multiple times in recursion tree
# - Optimal substructure:
#   ways(i) = ways(i-1) + ways(i-2)
# - We store results to avoid recomputation → tabulation (bottom-up DP)

# Build solution from smallest subproblems → larger ones
# Direction matters: we compute i only after i-1 and i-2 are known
for i in range(2, n + 1):

    # Transition:
    # To reach step i:
    # - last move was 1 step → came from i-1
    # - last move was 2 steps → came from i-2
    # total ways = sum of both possibilities
    res[i] = res[i - 1] + res[i - 2]

# Final DP table
print(res)


# ---------------- DRY RUN (n = 2) ----------------

# Initial:
# res = [0, 0, 0]

# After base case:
# res = [1, 1, 0]

# Loop starts from i = 2

# i = 2:
# res[2] = res[1] + res[0]
#        = 1 + 1
#        = 2
# res = [1, 1, 2]

# Loop ends

# Final result:
# res = [1, 1, 2]
# Answer = res[n] = res[2] = 2
#
# Interpretation:
# Ways to reach step 2:
# - 1 + 1
# - 2
#
# Total = 2

# #DP because questions asks number of ways asked
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # Initialize base cases: one way to reach the first two steps (step 0 and step 1)
#         one, two = 1, 1

#         # Iterate n-1 times to update the number of ways to reach each step
#         for i in range(n-1):
#             temp = one           # Store the previous value of 'one'
#             one = one + two      # Update 'one' as sum of the previous two steps
#             two = temp           # Update 'two' to the old value of 'one'
        
#         # Final answer is the number of ways to reach nth step
#         return one


