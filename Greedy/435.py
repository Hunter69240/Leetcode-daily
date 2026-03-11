class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 📌 PROBLEM TYPE:
        # "Non-overlapping Intervals" — We must remove the MINIMUM number of intervals
        # so that the remaining intervals do not overlap.
        #
        # Example:
        # Input  → [[1,2],[2,3],[3,4],[1,3]]
        # Output → 1  (remove [1,3] to make all others non-overlapping)
        #
        # Goal: Count how many intervals must be removed.

        # 🧠 INTUITION / GREEDY STRATEGY:
        # Sort by start time so intervals appear in timeline order.
        #
        # To minimize removals, when two intervals overlap, we should keep the interval
        # that ends earlier — because it leaves more room for future intervals.
        #
        # Logic:
        #   - If current interval does NOT overlap → update prevEnd
        #   - If it DOES overlap → remove ONE interval
        #       but keep the interval with the smaller end value (tighter interval)
        #       because it increases chance of fitting the next intervals.

        intervals.sort()
        res = 0  # count of removed intervals
        prevEnd = intervals[0][1]  # end time of last kept interval

        for start, end in intervals[1:]:
            if start >= prevEnd:
                # No overlap → keep current interval
                prevEnd = end
            else:
                # Overlap detected → must remove 1 interval
                res += 1
                # Keep the interval with smaller end value (better for future)
                prevEnd = min(prevEnd, end)

        return res


"""
-------------------------- 🔎 DRY RUN EXAMPLE --------------------------

Input:
intervals = [[1,2], [2,3], [3,4], [1,3]]
After sort:
[[1,2], [1,3], [2,3], [3,4]]

Initialize:
res = 0
prevEnd = 2   (end of first interval)

Go through remaining:

1) [1,3]
   start = 1 < prevEnd = 2 → OVERLAP
   res = 1
   prevEnd = min(2, 3) = 2   (keep the smaller ending interval)

2) [2,3]
   start = 2 >= prevEnd = 2 → NO OVERLAP
   prevEnd = 3

3) [3,4]
   start = 3 >= prevEnd = 3 → NO OVERLAP
   prevEnd = 4

End → res = 1 → remove only one interval

---------------------------------------------------------------

Another example:
intervals = [[1,100], [2,3], [3,4], [4,5]]

Sorted:
[[1,100], [2,3], [3,4], [4,5]]

Start:
prevEnd = 100

[2,3] → overlaps with 100 → res=1, keep smaller end → prevEnd=3
[3,4] → no overlap → prevEnd=4
[4,5] → no overlap → prevEnd=5

Final → res = 1

---------------------------------------------------------------
⏱ Complexity:
Time  → O(n log n) due to sorting
Space → O(1) extra space

"""
