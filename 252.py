"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 📌 PROBLEM TYPE:
        # "Meeting Rooms" — Given meeting time intervals, return True if a person
        # can attend ALL meetings without any time conflicts.
        #
        # A meeting is represented as:
        #    Interval(start, end)
        #
        # If any two meetings overlap, the person cannot attend both → return False.

        # 🧠 INTUITION:
        # To detect overlap, sort meetings by start time.
        # After sorting, overlapping meetings will be NEXT to each other.
        #
        # So:
        #   - Sort by start time
        #   - Compare every meeting with the previous one
        #   - If the previous meeting ends AFTER the next meeting starts → overlap → False

        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]  # previous meeting
            i2 = intervals[i]      # current meeting

            # ❗ If the previous meeting ends after the current meeting starts,
            #    the person would already be in another meeting → scheduling conflict.
            if i1.end > i2.start:
                return False

        # ✔ No overlaps detected → all meetings can be attended
        return True


"""
-------------------------- 🔎 DRY RUN EXAMPLE --------------------------

Input:
intervals = [[0,30], [5,10], [15,20]]

After sorting by start:
[[0,30], [5,10], [15,20]]

Compare:
i1 = [0,30],  i2 = [5,10]
30 > 5 → conflict → return False

Result: False

-------------------------------------------------------------
Another example:
intervals = [[7,10], [2,4]]

Sort:
[[2,4], [7,10]]

Compare:
i1 = [2,4],  i2 = [7,10]
4 > 7 ? No → no conflict

Loop ends → return True

-------------------------------------------------------------
⏱ Complexity:
Time  → O(n log n) for sorting
Space → O(1) extra space

"""
