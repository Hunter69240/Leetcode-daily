nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 1

nums.sort()
res = float('inf')
max_diff = float('inf')

# ---------------------------------------------------------
# EXPLANATION:
# This is the "3Sum Closest" problem.
#
# Goal:
# Find three numbers whose sum is CLOSEST to the target.
#
# APPROACH: SORT + TWO POINTERS (GREEDY)
#
# Steps:
# 1) Sort the array
# 2) Fix one element nums[i]
# 3) Use two pointers:
#    - j = i + 1 (next element)
#    - k = last index
# 4) Compute sum_target = nums[i] + nums[j] + nums[k]
# 5) Track how close this sum is to target
# 6) Move pointers greedily:
#    - If sum_target > target → decrease sum → move k left
#    - Else → increase sum → move j right
#
# Why greedy?
# - Array is sorted
# - Moving pointers always moves sum closer in the needed direction
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [10,20,30,40,50,60,70,80,90]
# target = 1
#
# Initial:
# res = inf
# max_diff = inf
#
# ---------------------------------------------------------
# i = 0 → nums[i] = 10
# j = 1 (20), k = 8 (90)
#
# sum_target = 10 + 20 + 90 = 120
# diff = |1 - 120| = 119
# max_diff > diff → update:
#   res = 120
#   max_diff = 119
#
# sum_target > target → k--
#
# ---------------------------------------------------------
# j = 1, k = 7 (80)
# sum_target = 10 + 20 + 80 = 110
# diff = 109 → update res = 110
#
# k--
#
# Continue shrinking k:
# 100, 90, 80, 70, 60
#
# Best so far becomes:
# sum_target = 10 + 20 + 30 = 60
# diff = |1 - 60| = 59
#
# ---------------------------------------------------------
# i = 1 → nums[i] = 20
# j = 2 (30), k = 8 (90)
# sum_target = 140
# diff = 139 → worse than current best → ignore
#
# Continue similarly for all i
#
# Since all numbers are POSITIVE and target is very SMALL,
# the smallest possible sum is the closest.
#
# FINAL RESULT:
# res = 60
# ---------------------------------------------------------

for i in range(len(nums)):
    j = i + 1
    k = len(nums) - 1

    while j < k:
        sum_target = nums[i] + nums[j] + nums[k]
        diff = abs(target - sum_target)

        # update closest sum if better
        if max_diff > diff:
            res = sum_target
            max_diff = diff

        # greedy pointer movement
        if sum_target > target:
            k -= 1
        else:
            j += 1

print(res)
