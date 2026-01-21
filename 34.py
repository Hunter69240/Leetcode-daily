nums = [5, 7, 7, 8, 8, 10]
target = 8

left = 0
right = len(nums) - 1

left_occurance = -1
right_occurance = -1

# -------- find LEFTMOST occurrence --------
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        left_occurance = mid
        right = mid - 1
    elif nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

# -------- find RIGHTMOST occurrence --------
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        right_occurance = mid
        left = mid + 1
    elif nums[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

print(left_occurance, right_occurance)


# ---------------------------------------------------------
# EXPLANATION:
# This code finds the FIRST and LAST position of a target
# value in a SORTED array.
#
# We use BINARY SEARCH twice:
# 1) First binary search → find LEFTMOST occurrence
# 2) Second binary search → find RIGHTMOST occurrence
#
# Why two searches?
# - Normal binary search stops at any match
# - We must force the search to continue left or right
#   to find boundaries
# ---------------------------------------------------------

# ---------------------------------------------------------
# PART 1: FIND LEFTMOST OCCURRENCE
#
# When nums[mid] == target:
# - Save mid as a potential answer
# - Move RIGHT pointer LEFT (right = mid - 1)
#   to keep searching for earlier occurrence
# ---------------------------------------------------------

# ---------------------------------------------------------
# PART 2: FIND RIGHTMOST OCCURRENCE
#
# When nums[mid] == target:
# - Save mid as a potential answer
# - Move LEFT pointer RIGHT (left = mid + 1)
#   to keep searching for later occurrence
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [5,7,7,8,8,10]
# target = 8
#
# -------- LEFTMOST SEARCH --------
#
# left=0, right=5 → mid=2 → nums[2]=7 < 8 → left=3
# left=3, right=5 → mid=4 → nums[4]=8 == target
#   left_occ = 4
#   right = 3
# left=3, right=3 → mid=3 → nums[3]=8 == target
#   left_occ = 3
#   right = 2
# loop ends
#
# left_occurrence = 3
#
# -------- RIGHTMOST SEARCH --------
#
# left=0, right=5 → mid=2 → nums[2]=7 < 8 → left=3
# left=3, right=5 → mid=4 → nums[4]=8 == target
#   right_occ = 4
#   left = 5
# left=5, right=5 → mid=5 → nums[5]=10 > 8 → right=4
# loop ends
#
# right_occurrence = 4
#
# FINAL ANSWER:
# [3, 4]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n) + O(log n) = O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
