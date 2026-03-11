"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # -------------------- INTUITION --------------------
        # We need to find the minimum number of meeting rooms so that
        # no two meetings overlap in the same room.
        #
        # Key idea:
        # - Separate all start times and end times.
        # - Sort both lists.
        # - Then use two pointers to simulate time:
        #       If a meeting starts before the earliest one ends → need new room.
        #       If a meeting ends before the next one starts → free one room.
        # - Track the max rooms needed at any time → that's the answer.

        # -------------------- STEP 1: COLLECT START & END TIMES --------------------
        start = sorted([i.start for i in intervals])  # all start times sorted
        end = sorted([i.end for i in intervals])      # all end times sorted

        # result = maximum rooms ever needed
        # count = current rooms in use
        res, count = 0, 0

        # pointers for start[] and end[] arrays
        s, e = 0, 0

        # -------------------- DRY RUN EXAMPLE IN COMMENTS --------------------
        # Suppose intervals = [(0, 30), (5, 10), (15, 20)]
        # start = [0, 5, 15]
        # end   = [10, 20, 30]
        #
        # s=0, e=0, count=0, res=0
        # 0 < 10 → start → count=1, s=1, res=1
        # 5 < 10 → start → count=2, s=2, res=2
        # 15 ≥ 10 → end   → count=1, e=1
        # 15 < 20 → start → count=2, s=3, res=2
        # s reaches end → stop → result = 2 rooms

        # -------------------- STEP 2: PROCESS STARTS UNTIL ALL DONE --------------------
        while s < len(intervals):

            # If the next meeting starts before the earliest one ends
            if start[s] < end[e]:
                # A new room is needed
                count += 1
                s += 1
            else:
                # A meeting has finished → free a room
                count -= 1
                e += 1

            # Track the maximum rooms ever used
            res = max(res, count)

        return res  # final answer = minimum number of meeting rooms required
