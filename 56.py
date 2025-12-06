class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 📌 PROBLEM TYPE:
        # "Merge Intervals" — Given a list of possibly overlapping intervals,
        # merge all intervals that overlap and return only non-overlapping intervals.
        #
        # Example:
        # Input  → [[1,3], [2,6], [8,10], [15,18]]
        # Output → [[1,6], [8,10], [15,18]]
        #
        # Goal: Combine all intervals that have overlap.

        # 🧠 INTUITION:
        # If intervals are sorted by start time, then overlapping intervals will be next to each other.
        # So:
        #   1) Sort intervals by start
        #   2) Compare current interval with last merged interval
        #   3) If overlapping → merge by extending the end bound
        #   4) If not overlapping → push new interval into output

        intervals.sort(key=lambda i: i[0])  # Sort by start time
        output = [intervals[0]]             # First interval automatically included

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]         # End of most recently added interval

            # Case 1 — Overlap:
            # If current interval starts before or at lastEnd → overlapping
            if start <= lastEnd:
                # Extend/merge interval by updating the end to the maximum
                output[-1][1] = max(lastEnd, end)
            else:
                # Case 2 — No overlap:
                # Simply append interval to output list
                output.append([start, end])

        return output


"""
-------------------------- 🔎 DRY RUN EXAMPLE --------------------------

Input:
intervals = [[1,3], [2,6], [8,10], [15,18]]

Step 1: Sort (already sorted)
Step 2: output = [[1,3]]

Iterating:
(start=2, end=6)
   lastEnd = 3
   2 <= 3 → overlap → merge
   update [1,3] → [1,6]
   output = [[1,6]]

(start=8, end=10)
   lastEnd = 6
   8 > 6 → no overlap → append
   output = [[1,6], [8,10]]

(start=15, end=18)
   lastEnd = 10
   15 > 10 → no overlap → append
   output = [[1,6], [8,10], [15,18]]

Final answer:
[[1,6], [8,10], [15,18]]

------------------------------------------------------------

Another quick example:
intervals = [[1,4], [2,3]]

Sorted → [[1,4], [2,3]]
output = [[1,4]]

Check second interval:
start=2, end=3
lastEnd=4
2 <= 4 → overlap → merge → output stays [[1,4]]

Final output: [[1,4]]

------------------------------------------------------------
⏱ Complexity:
Time  → O(n log n) for sorting, then O(n) scan
Space → O(n) for result storage

"""
