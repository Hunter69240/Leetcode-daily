nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

j = 0   # pointer to place the next valid (non-val) element

# ---------------------------------------------------------
# EXPLANATION:
# This is the "Remove Element" problem (LeetCode style).
#
# Goal:
# - Remove all occurrences of `val` from nums IN-PLACE
# - Return the number of remaining elements
#
# TWO POINTER APPROACH:
# - i → scans each element of nums
# - j → points to the position where the next valid element should go
#
# Logic:
# - If nums[i] != val:
#     copy nums[i] to nums[j]
#     increment j
#
# After the loop:
# - The first `j` elements of nums are the valid ones
# - Elements beyond index j don't matter
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [0,1,2,2,3,0,4,2]
# val = 2
#
# Initial:
# j = 0
#
# i = 0 → nums[0] = 0 ≠ 2
#   nums[0] = 0
#   j = 1
#
# i = 1 → nums[1] = 1 ≠ 2
#   nums[1] = 1
#   j = 2
#
# i = 2 → nums[2] = 2 == val → SKIP
#
# i = 3 → nums[3] = 2 == val → SKIP
#
# i = 4 → nums[4] = 3 ≠ 2
#   nums[2] = 3
#   j = 3
#
# i = 5 → nums[5] = 0 ≠ 2
#   nums[3] = 0
#   j = 4
#
# i = 6 → nums[6] = 4 ≠ 2
#   nums[4] = 4
#   j = 5
#
# i = 7 → nums[7] = 2 == val → SKIP
#
# Final nums (first j elements are valid):
# [0, 1, 3, 0, 4]
#
# j = 5  → number of elements not equal to val
# ---------------------------------------------------------

for i in range(len(nums)):
    if nums[i] != val:
        nums[j] = nums[i]
        j += 1

print(j)
