nums = [1, 1, 1, 2, 2, 3]

j = 0
count = 0
prev = None

# ---------------------------------------------------------
# EXPLANATION:
# This code removes duplicates from a SORTED array
# such that each number appears AT MOST TWICE.
#
# Two-pointer approach:
# - i → scans every element
# - j → position to place valid elements
#
# Variables:
# - prev  → previous number seen
# - count → how many times current number has been used
#
# Rule:
# - When a new number appears, reset count to 0
# - Allow copying only if count < 2
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [1,1,1,2,2,3]
#
# Initial:
# j=0, prev=None, count=0
#
# i=0 → nums[0]=1
#   1 != prev → prev=1, count=0
#   count < 2 → nums[0]=1
#   j=1, count=1
#
# i=1 → nums[1]=1
#   same as prev
#   count < 2 → nums[1]=1
#   j=2, count=2
#
# i=2 → nums[2]=1
#   same as prev
#   count == 2 → SKIP
#
# i=3 → nums[3]=2
#   2 != prev → prev=2, count=0
#   count < 2 → nums[2]=2
#   j=3, count=1
#
# i=4 → nums[4]=2
#   same as prev
#   count < 2 → nums[3]=2
#   j=4, count=2
#
# i=5 → nums[5]=3
#   3 != prev → prev=3, count=0
#   count < 2 → nums[4]=3
#   j=5, count=1
#
# Modified nums (first j elements):
# [1,1,2,2,3]
#
# FINAL j = 5
# ---------------------------------------------------------

for i in range(len(nums)):
    if nums[i] != prev:
        prev = nums[i]
        count = 0

    if count < 2:
        nums[j] = nums[i]
        j += 1
        count += 1

print(j)
