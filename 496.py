nums1 = [4, 1, 2]
nums2 = [   1, 3, 4, 2]

stack = []
nextGreater = {}

for i in nums2:
    while stack and i > stack[-1]:
        nextGreater[stack.pop()] = i
    stack.append(i)

res = []
for i in nums1:
    res.append(nextGreater.get(i, -1))

print(res)


# ---------------------------------------------------------
# EXPLANATION:
# This code solves the "Next Greater Element I" problem.
#
# Goal:
# For each element in nums1, find the NEXT GREATER element
# to its right in nums2.
# If no greater element exists, return -1.
#
# Approach:
# - Use a MONOTONIC DECREASING STACK while scanning nums2
# - Build a hashmap (nextGreater) that stores:
#       element -> its next greater element
# - Then answer queries for nums1 using the hashmap
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY A MONOTONIC STACK?
#
# The stack keeps elements in DECREASING order.
#
# When a larger number appears:
# - It becomes the "next greater element" for all smaller
#   elements popped from the stack.
#
# Each element is pushed and popped at most once → O(n)
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN (BUILDING nextGreater):
#
# nums2 = [1, 3, 4, 2]
#
# stack = []
# nextGreater = {}
#
# -------------------------
# i = 1
# stack empty → push 1
# stack = [1]
#
# -------------------------
# i = 3
# 3 > 1 → pop 1
# nextGreater[1] = 3
# stack = []
# push 3
# stack = [3]
#
# -------------------------
# i = 4
# 4 > 3 → pop 3
# nextGreater[3] = 4
# stack = []
# push 4
# stack = [4]
#
# -------------------------
# i = 2
# 2 < 4 → no pop
# push 2
# stack = [4, 2]
#
# End of loop
#
# Elements left in stack (4, 2) have NO next greater element
#
# nextGreater = {1: 3, 3: 4}
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN (ANSWERING nums1):
#
# nums1 = [4, 1, 2]
#
# 4 → not in nextGreater → -1
# 1 → nextGreater[1] = 3
# 2 → not in nextGreater → -1
#
# res = [-1, 3, -1]
# ---------------------------------------------------------

# ---------------------------------------------------------
# FINAL OUTPUT:
# [-1, 3, -1]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n + m)
#   n = len(nums2)
#   m = len(nums1)
#
# SPACE COMPLEXITY:
# O(n) for stack and hashmap
# ---------------------------------------------------------
