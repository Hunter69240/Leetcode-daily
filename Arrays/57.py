class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 📌 PROBLEM TYPE:
        # "Insert Interval" — We are given a list of non-overlapping intervals sorted by start time.
        # We need to insert `newInterval` into the list and merge any intervals that overlap.
        #
        # Example:
        # intervals = [[1,3], [6,9]], newInterval = [2,5]
        # Output     = [[1,5], [6,9]]

        res = []

        # 🧠 INTUITION:
        # Iterate through the intervals and compare each with newInterval:
        #
        # Case 1 ➤ Completely before newInterval: [--- interval ---]   [--- newInterval ---]
        #         → no overlap → add interval to result
        #
        # Case 2 ➤ Completely after newInterval:  [--- newInterval ---]   [--- interval ---]
        #         → newInterval comes first → add it and return the rest
        #
        # Case 3 ➤ Overlapping regions:
        #         → merge by expanding newInterval boundaries:
        #           new.start = min(new.start, interval.start)
        #           new.end   = max(new.end, interval.end)

        for i in range(len(intervals)):
            # Case 2: newInterval lies completely before current interval → insert it now
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]  # rest can be copied directly (already sorted & non-overlapping)

            # Case 1: newInterval lies completely after current interval → keep interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Case 3: Overlap detected → merge the intervals by updating newInterval boundaries
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # After loop → either newInterval belongs at the end or is the merged version
        res.append(newInterval)
        return res


"""
-------------------------- 🔎 DRY RUN EXAMPLE --------------------------

Example input:
intervals = [[1,3], [6,9]]
newInterval = [2,5]

Start:
res = []

i = 0 → intervals[0] = [1,3]
Check overlap:
    newInterval = [2,5]
    intervals[0] start = 1 ≤ newInterval end 5
    intervals[0] end   = 3 ≥ newInterval start 2
→ Overlap -> merge
    newInterval = [min(2,1), max(5,3)] = [1,5]

i = 1 → intervals[1] = [6,9]
Check:
    newInterval end = 5 < intervals[1] start = 6
→ newInterval fully before [6,9]
Append and return:
    res = [[1,5]] + [[6,9]]

Final output: [[1,5], [6,9]]

-----------------------------------------------------------------------

Another example:
intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
newInterval = [4,8]

Walkthrough:
i = 0 → [1,2] before newInterval → res = [[1,2]]
i = 1 → [3,5] overlaps → merge → newInterval = [3,8]
i = 2 → [6,7] overlaps → merge → newInterval = [3,8]
i = 3 → [8,10] overlaps → merge → newInterval = [3,10]
i = 4 → [12,16] is after → append merged interval and return

Final answer: [[1,2], [3,10], [12,16]]

-----------------------------------------------------------------------

⏱ Complexity:
Time  → O(n) — single pass
Space → O(n) — result storage

"""
