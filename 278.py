'''
Docstring for 278

if isBadVersion(int) returns false it means version isnt bad which means it is good
If it returns true it means version is bad
'''

n = 5

low = 1
high = n

while low <= high:
    mid = (low + high) // 2

    if isBadVersion(mid) == False:
        low = mid + 1
    else:
        high = mid - 1

print(low)


# ---------------------------------------------------------
# EXPLANATION:
# This code solves the "First Bad Version" problem.
#
# Problem statement:
# - Versions are numbered from 1 to n
# - Once a version is bad, all versions after it are also bad
# - isBadVersion(version) tells whether a version is bad
#
# Goal:
# Find the FIRST bad version with the MINIMUM number of API calls.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY BINARY SEARCH:
#
# The versions have a monotonic property:
#   good → good → good → bad → bad → bad
#
# Binary search reduces the number of API calls
# from O(n) to O(log n).
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW THE SEARCH WORKS:
#
# low = 1
# high = n
#
# mid = middle version
#
# Case 1: isBadVersion(mid) == False
#   → mid is GOOD
#   → first bad version must be AFTER mid
#   → low = mid + 1
#
# Case 2: isBadVersion(mid) == True
#   → mid is BAD
#   → first bad version is mid or BEFORE
#   → high = mid - 1
# ---------------------------------------------------------

# ---------------------------------------------------------
# LOOP INVARIANT:
#
# The first bad version is always in the range [low, high]
#
# When the loop ends:
# - low points to the FIRST bad version
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# Suppose versions are:
# [1, 2, 3, 4, 5]
#            ↑
#        first bad = 4
#
# n = 5
#
# low=1, high=5 → mid=3
# isBadVersion(3)=False → low=4
#
# low=4, high=5 → mid=4
# isBadVersion(4)=True → high=3
#
# Loop ends (low=4, high=3)
#
# OUTPUT:
# 4
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(log n)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
