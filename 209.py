target = 11
nums = [1, 2, 3, 4, 5]

min_length = float('inf')
i = 0
j = 0
sum = 0

while j < len(nums):
    sum += nums[j]

    while sum >= target:
        if sum >= target:
            new_length = j - i + 1
            min_length = min(new_length, min_length)

        sum -= nums[i]
        i += 1

    j += 1

print(min_length if min_length != float('inf') else 0)


# ---------------------------------------------------------
# EXPLANATION:
# This code finds the MINIMUM LENGTH of a contiguous subarray
# whose SUM is GREATER THAN OR EQUAL to a given target.
#
# This is the "Minimum Size Subarray Sum" problem.
#
# The solution uses a SLIDING WINDOW technique.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY SLIDING WINDOW WORKS:
# - All numbers are POSITIVE
# - Expanding the window increases the sum
# - Shrinking the window decreases the sum
#
# This allows us to move pointers efficiently.
# ---------------------------------------------------------

# ---------------------------------------------------------
# POINTERS:
#
# i → left pointer (start of window)
# j → right pointer (end of window)
#
# The window is nums[i ... j]
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW THE ALGORITHM WORKS:
#
# 1) Expand the window by moving j forward and adding nums[j]
# 2) When sum >= target:
#    - Update the minimum window length
#    - Shrink the window from the left to find a smaller valid window
# 3) Repeat until j reaches the end
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [1,2,3,4,5]
# target = 11
#
# j=0 → sum=1
# j=1 → sum=3
# j=2 → sum=6
# j=3 → sum=10
# j=4 → sum=15 (>=11)
#
# Now shrink:
# window [0..4] length=5 → min=5
# remove nums[0]=1 → sum=14
# window [1..4] length=4 → min=4
# remove nums[1]=2 → sum=12
# window [2..4] length=3 → min=3
# remove nums[2]=3 → sum=9 (stop shrinking)
#
# Final min_length = 3
# Subarray: [3,4,5]
# ---------------------------------------------------------

# ---------------------------------------------------------
# EDGE CASE:
# If no subarray satisfies the condition → return 0
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) — each element visited at most twice
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
