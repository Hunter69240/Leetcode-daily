nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]

n = len(nums)
res = [-1] * n
stack = []

for i in range(2 * n):
    curr = nums[i % n]

    while stack and nums[stack[-1]] < curr:
        idx = stack.pop()
        res[idx] = curr

    if i < n:
        stack.append(i)

print(res)


# ---------------------------------------------------------
# EXPLANATION:
# This code solves the "Next Greater Element II" problem.
#
# Goal:
# For each element in a CIRCULAR array,
# find the NEXT GREATER element.
#
# If no greater element exists, keep -1.
#
# Circular means:
# - After the last element, we continue from the start.
#
# ---------------------------------------------------------
# KEY IDEA:
# - Use a MONOTONIC DECREASING STACK of indices
# - Traverse the array TWICE (2 * n) to simulate circularity
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY STACK STORES INDICES (NOT VALUES):
# - We need to update res at the correct position
# - Values alone are not enough
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW THE LOOP WORKS:
#
# for i in range(2 * n):
#   i % n gives circular indexing
#
# - First pass (i < n):
#   Push indices into the stack
#
# - Second pass (i >= n):
#   Only try to resolve pending elements
#   (do NOT push indices again)
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN (SIMPLIFIED):
#
# nums = [100,1,11,1,120,111,123,1,-1,-100]
#
# stack = []
# res = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
#
# -------------------------
# i=0 → curr=100
# push 0
# stack=[0]
#
# i=1 → curr=1
# push 1
# stack=[0,1]
#
# i=2 → curr=11
# pop 1 → res[1]=11
# push 2
# stack=[0,2]
#
# i=3 → curr=1
# push 3
# stack=[0,2,3]
#
# i=4 → curr=120
# pop 3 → res[3]=120
# pop 2 → res[2]=120
# pop 0 → res[0]=120
# push 4
# stack=[4]
#
# ...
#
# i=6 → curr=123
# pop 5 → res[5]=123
# pop 4 → res[4]=123
# push 6
# stack=[6]
#
# -------------------------
# Second pass resolves remaining indices
#
# FINAL RESULT:
# [120, 11, 120, 120, 123, 123, -1, 100, 100, 100]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) → each index pushed & popped once
#
# SPACE COMPLEXITY:
# O(n) → stack and result array
# ---------------------------------------------------------
