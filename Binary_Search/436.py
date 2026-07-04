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

intervals = [[3,4],[2,3],[1,2]]

orig_index = {tuple(intervals[i]): i for i in range(len(intervals))}
sorted_intervals = sorted(intervals)

dict_res = {}
res = []

for i in range(len(sorted_intervals)):
    end = sorted_intervals[i][1]

    j = 0
    k = len(sorted_intervals)

    while j < k:
        m = (j + k) // 2

        if sorted_intervals[m][0] >= end:
            k = m
        else:
            j = m + 1

    if j == len(sorted_intervals):
        dict_res[tuple(sorted_intervals[i])] = -1
    else:
        dict_res[tuple(sorted_intervals[i])] = orig_index[tuple(sorted_intervals[j])]

for interval in intervals:
    res.append(dict_res[tuple(interval)])

print(res)

# ---------------------------------------------------------
# EXPLANATION:
#
# 1. Store the original index of every interval because the
#    intervals will be sorted.
#
# 2. Sort the intervals by start time.
#
# 3. For each interval:
#      - Take its end value.
#      - Binary search to find the first interval whose
#        start >= end.
#      - If found, store that interval's original index.
#      - Otherwise store -1.
#
# 4. The answers are currently stored by interval, so build
#    the final result back in the original input order.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# intervals = [[3,4],[2,3],[1,2]]
#
# Original indices:
# (3,4) -> 0
# (2,3) -> 1
# (1,2) -> 2
#
# Sorted:
# [[1,2],[2,3],[3,4]]
#
# [1,2]
# end = 2
# first start >=2 -> [2,3]
# answer = 1
#
# [2,3]
# end = 3
# first start >=3 -> [3,4]
# answer = 0
#
# [3,4]
# end = 4
# no valid interval
# answer = -1
#
# Original order:
#
# [3,4] -> -1
# [2,3] -> 0
# [1,2] -> 1
#
# Result:
# [-1,0,1]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n log n)
#
# SPACE COMPLEXITY:
# O(n)
# ---------------------------------------------------------