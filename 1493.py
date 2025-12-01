# This is a SLIDING WINDOW solution because:
# We want the LONGEST subarray that satisfies a condition:
#     "subarray contains AT MOST 1 zero"
# Whenever window is valid (≤1 zero), expand it by moving j (right pointer).
# Whenever window becomes invalid (>1 zero), shrink it by moving i (left pointer).
# This expand-when-valid, shrink-when-invalid pattern = classic sliding window.

nums = [1,1,0,1]

i = 0                 # left pointer of window
zero_count = 0        # how many zeros are inside the current window
max_len = 0           # longest valid window found

for j in range(len(nums)):     # j = right pointer expanding the window

    # When we include nums[j] into the window:
    if nums[j] == 0:
        zero_count += 1        # we count the zero

    # If the window has more than 1 zero, shrink it from the left (i):
    while zero_count > 1:
        # If the element at i is a zero, removing it reduces zero_count
        if nums[i] == 0:
            zero_count -= 1
        i += 1                 # move left pointer to shrink window

    # Now the window [i, j] has at most 1 zero → valid window
    # Length of this valid window = j - i + 1
    max_len = max(max_len, j - i + 1)


# We MUST delete exactly 1 element → subtract 1.
print(max_len - 1)



"""
===========================
DRY RUN for nums = [1,1,0,1]
===========================

Start:
i = 0
zero_count = 0
max_len = 0

--------------------------------------------
Step j = 0 → nums[j] = 1
--------------------------------------------
nums = [1]
zero_count = 0
window = [0,0] → valid (≤1 zero)
max_len = max(0, 0-0+1) = 1

--------------------------------------------
Step j = 1 → nums[j] = 1
--------------------------------------------
nums = [1,1]
zero_count = 0
window = [0,1] → valid
max_len = max(1, 1-0+1) = 2

--------------------------------------------
Step j = 2 → nums[j] = 0
--------------------------------------------
nums = [1,1,0]
zero_count = 1
window = [0,2] → valid
max_len = max(2, 2-0+1) = 3

--------------------------------------------
Step j = 3 → nums[j] = 1
--------------------------------------------
nums = [1,1,0,1]
zero_count = 1
window = [0,3] → valid
max_len = max(3, 3-0+1) = 4

--------------------------------------------
Final max_len = 4
But we MUST delete 1 element → return 4 - 1 = 3
--------------------------------------------

Answer = 3
"""
