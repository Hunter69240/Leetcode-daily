#Try to find middle first (j)

nums = [3, 1, 4, 2]

stack = []
middle = -float('inf')

for i in range(len(nums) - 1, -1, -1):

    if nums[i] < middle:
        print(True)
        break

    while stack and nums[i] > stack[-1]:
        middle = stack.pop()

    stack.append(nums[i])


# ---------------------------------------------------------
# EXPLANATION:
# This code checks whether a "132 pattern" exists in the array.
#
# A 132 pattern means:
#   There exist indices i < j < k such that:
#       nums[i] < nums[k] < nums[j]
#
# We scan the array from RIGHT to LEFT and use:
# - a STACK to track potential "3" values
# - a variable `middle` to track the best candidate for "2"
#
# ---------------------------------------------------------
# WHY RIGHT TO LEFT?
# - We want nums[j] (the "3") to come BEFORE nums[k] (the "2")
# - Scanning from right allows us to fix j first
#
# ---------------------------------------------------------
# VARIABLES:
# stack  → decreasing stack holding possible "3" values
# middle → the best candidate for "2" (nums[k])
#
# If we ever find nums[i] < middle → 132 pattern found
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [3, 1, 4, 2]
# index:  0  1  2  3
#
# Initial:
# stack = []
# middle = -inf
#
# ---------------------------------------------------------
# i = 3 → nums[i] = 2
# 2 < middle? NO
# stack empty → push 2
# stack = [2]
#
# ---------------------------------------------------------
# i = 2 → nums[i] = 4
# 4 < middle? NO
#
# while stack and 4 > stack[-1]:
#   pop 2 → middle = 2
#
# push 4
# stack = [4]
#
# ---------------------------------------------------------
# i = 1 → nums[i] = 1
# 1 < middle (2)? YES
#
# Pattern found:
#   nums[i] = 1  (1)
#   middle  = 2  (2)
#   nums[j] = 4  (3)
#
# This matches: 1 < 2 < 4
# ---------------------------------------------------------
# OUTPUT:
# True
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY THIS WORKS (INTUITION):
#
# - stack keeps decreasing numbers → candidates for "3"
# - middle stores the largest valid "2" seen so far
# - when nums[i] < middle → we found "1"
#
# Greedy + Monotonic Stack ensures O(n) time.
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) → each element pushed and popped once
#
# SPACE COMPLEXITY:
# O(n) → stack
# ---------------------------------------------------------
