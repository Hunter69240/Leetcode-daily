nums = [1, 2, 1, 3, 5, 6, 4]

peak = 0
low = 0
high = len(nums) - 1

while low < high:
    mid = (low + high) // 2

    if nums[mid] > nums[mid + 1]:
        #Could be peak thats y no +1
        high = mid
    else:
        #No chance of peak as mid is less thats y +1
        low = mid + 1

print(low)


# ---------------------------------------------------------
# EXPLANATION:
# This code finds a PEAK ELEMENT in an array.
#
# A peak element is an index i such that:
#   nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
#
# Note:
# - The array may have multiple peaks
# - We can return the index of ANY peak
#
# This solution uses a BINARY SEARCH approach
# and runs in O(log n) time.
# ---------------------------------------------------------

# ---------------------------------------------------------
# KEY IDEA:
# Look at nums[mid] and nums[mid + 1]
#
# - If nums[mid] > nums[mid + 1]:
#     We are on a descending slope
#     → A peak exists on the LEFT (including mid)
#
# - Else:
#     We are on an ascending slope
#     → A peak exists on the RIGHT
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY THIS WORKS:
# - If slope goes down, there must be a peak before or at mid
# - If slope goes up, there must be a peak after mid
#
# This holds even if the peak is at the boundaries.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [1, 2, 1, 3, 5, 6, 4]
#
# low=0, high=6
#
# mid=3 → nums[3]=3, nums[4]=5
# 3 < 5 → ascending → low=4
#
# low=4, high=6
# mid=5 → nums[5]=6, nums[6]=4
# 6 > 4 → descending → high=5
#
# low=4, high=5
# mid=4 → nums[4]=5, nums[5]=6
# 5 < 6 → ascending → low=5
#
# low=5, high=5 → stop
#
# PEAK INDEX = 5
# PEAK VALUE = 6
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
