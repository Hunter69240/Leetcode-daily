def a():
    n = 10

    low = 0
    high = n

    while low <= high:
        mid = (low + high) // 2

        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            low = mid + 1
        else:
            high = mid - 1


s = a()
print(s)


# ---------------------------------------------------------
# EXPLANATION:
# This code solves the "Guess Number Higher or Lower" problem.
#
# There is a hidden number between 1 and n.
# The API guess(num) returns:
#   0  → correct guess
#   1  → guessed number is LOWER than the picked number
#  -1  → guessed number is HIGHER than the picked number
#
# Goal:
# Find the hidden number using the minimum number of guesses.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY BINARY SEARCH:
#
# The guess API gives directional feedback.
# This allows us to discard half of the search space each time.
#
# Time complexity improves from O(n) to O(log n).
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW THE SEARCH WORKS:
#
# low = 0
# high = n
#
# mid = current guess
#
# Case 1: guess(mid) == 0
#   → correct number found
#
# Case 2: guess(mid) == 1
#   → mid is LOWER than target
#   → search RIGHT half
#
# Case 3: guess(mid) == -1
#   → mid is HIGHER than target
#   → search LEFT half
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN (EXAMPLE):
#
# Suppose hidden number = 6
#
# low=0, high=10 → mid=5
# guess(5)=1 → target is higher → low=6
#
# low=6, high=10 → mid=8
# guess(8)=-1 → target is lower → high=7
#
# low=6, high=7 → mid=6
# guess(6)=0 → FOUND
#
# RESULT:
# 6
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
