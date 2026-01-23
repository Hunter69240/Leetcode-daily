def a():
    num = 17

    low = 0
    high = num

    while low <= high:
        mid = (low + high) // 2
        prod = mid * mid

        if prod == num:
            return True
        elif prod > num:
            high = mid - 1
        else:
            low = mid + 1

    return False


s = a()
print(s)


# ---------------------------------------------------------
# EXPLANATION:
# This code checks whether a number is a PERFECT SQUARE
# without using sqrt().
#
# A perfect square is:
#   x = k * k for some integer k
#
# The solution uses BINARY SEARCH.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY BINARY SEARCH WORKS:
#
# - Squares increase monotonically as k increases
# - If mid² is too large, all larger values are invalid
# - If mid² is too small, all smaller values are invalid
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW THE SEARCH WORKS:
#
# low = 0
# high = num
#
# mid = candidate number
# prod = mid * mid
#
# Case 1: prod == num
#   → num is a perfect square
#
# Case 2: prod > num
#   → mid is too large → search left
#
# Case 3: prod < num
#   → mid is too small → search right
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# num = 17
#
# low=0, high=17 → mid=8 → 8²=64 > 17 → high=7
# low=0, high=7  → mid=3 → 3²=9 < 17  → low=4
# low=4, high=7  → mid=5 → 5²=25 > 17 → high=4
# low=4, high=4  → mid=4 → 4²=16 < 17 → low=5
#
# low > high → exit loop
#
# RESULT:
# False
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
