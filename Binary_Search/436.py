intervals = [[3,4],[2,3],[1,2]]

# ---------------------------------------------------------
# PROBLEM:
# Given a list of intervals, for each interval i,
# find the interval j such that:
#
#   intervals[j][0] >= intervals[i][1]
#
# and among all such intervals, j has the smallest start.
#
# If no such interval exists, return -1 for that interval.
#
# The result should be in the ORIGINAL order of intervals.
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP 0: STORE ORIGINAL INDICES
#
# We need original indices because we will sort intervals.
# ---------------------------------------------------------
orig_index = {tuple(intervals[i]): i for i in range(len(intervals))}

# ---------------------------------------------------------
# STEP 1: SORT INTERVALS BY START TIME
#
# Sorting helps us apply binary search efficiently.
# ---------------------------------------------------------
sorted_intervals = sorted(intervals)

# ---------------------------------------------------------
# dict_res → maps interval → answer index
# res      → final output array
# ---------------------------------------------------------
dict_res = {}
res = []

# ---------------------------------------------------------
# STEP 2: FOR EACH INTERVAL, FIND THE "RIGHT INTERVAL"
# ---------------------------------------------------------
for i in range(len(sorted_intervals)):
    # End of current interval
    end = sorted_intervals[i][1]

    # -----------------------------------------------------
    # BINARY SEARCH:
    # Find the smallest start >= end
    # -----------------------------------------------------
    j = 0
    k = len(sorted_intervals)

    while j < k:
        m = (j + k) // 2

        # If start at mid is valid, move left
        if sorted_intervals[m][0] >= end:
            k = m
        else:
            j = m + 1

    # -----------------------------------------------------
    # AFTER BINARY SEARCH:
    #
    # j is the first index where:
    # sorted_intervals[j][0] >= end
    # -----------------------------------------------------
    if j == len(sorted_intervals):
        # No valid right interval found
        dict_res[tuple(sorted_intervals[i])] = -1
    else:
        # Store original index of the right interval
        dict_res[tuple(sorted_intervals[i])] = orig_index[tuple(sorted_intervals[j])]

# ---------------------------------------------------------
# STEP 3: BUILD RESULT IN ORIGINAL ORDER
# ---------------------------------------------------------
for i in intervals:
    res.append(dict_res[tuple(i)])

# ---------------------------------------------------------
# OUTPUT
# ---------------------------------------------------------
print(res)

# ---------------------------------------------------------
# DRY RUN:
#
# intervals = [[3,4],[2,3],[1,2]]
#
# Original indices:
# (3,4) → 0
# (2,3) → 1
# (1,2) → 2
#
# Sorted intervals:
# [[1,2],[2,3],[3,4]]
#
# Interval [1,2]:
#   end = 2 → next start >= 2 is [2,3] → index 1
#
# Interval [2,3]:
#   end = 3 → next start >= 3 is [3,4] → index 0
#
# Interval [3,4]:
#   end = 4 → no start >= 4 → -1
#
# Final result (original order):
# [ -1, 0, 1 ]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# Sorting → O(n log n)
# Binary search per interval → O(log n)
# Total → O(n log n)
#
# SPACE COMPLEXITY:
# O(n)
# ---------------------------------------------------------
