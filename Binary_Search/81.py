nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2

low = 0
high = len(nums) - 1
is_present = False

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        is_present = True
        break

    if nums[low] == nums[mid] == nums[high]:
        low += 1
        high -= 1

    elif nums[low] <= nums[mid]:
        if nums[low] <= target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    else:
        if nums[mid] < target <= nums[high]:
            low = mid + 1
        else:
            high = mid - 1

print(is_present)


# ---------------------------------------------------------
# EXPLANATION:
# This code searches for a target in a ROTATED SORTED ARRAY
# that MAY CONTAIN DUPLICATES.
#
# This is an extension of binary search.
#
# Standard binary search fails with duplicates, so we add
# extra checks.
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY IDEA:
# At any step, one half of the array must be SORTED.
#
# But duplicates can hide which half is sorted, so:
# - If nums[low] == nums[mid] == nums[high]
#   we shrink the search space.
# ---------------------------------------------------------

# ---------------------------------------------------------
# CASES HANDLED:
#
# 1) nums[mid] == target
#    → found target
#
# 2) nums[low] == nums[mid] == nums[high]
#    → cannot decide sorted half
#    → low++, high--
#
# 3) Left half sorted (nums[low] <= nums[mid])
#    - Check if target lies in left half
#
# 4) Right half sorted
#    - Check if target lies in right half
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [..., 2, ...]  (mostly 1s)
# target = 2
#
# Iterations shrink range until mid lands on 2
#
# Example:
# low=0, high=18 → mid=9 → nums[mid]=1
# nums[low]==nums[mid]==nums[high]
# → low=1, high=17
#
# This continues until mid points to index 13
# where nums[mid] == 2
#
# is_present = True
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# Best / Average: O(log n)
# Worst case (many duplicates): O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
