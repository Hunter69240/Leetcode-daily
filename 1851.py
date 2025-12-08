class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # ------------------------ INTUITION ------------------------
        # For each query point q, we need the length of the smallest interval [l, r]
        # such that l <= q <= r.
        #
        # Instead of checking every interval for every query (which is too slow),
        # we use a min-heap to always keep track of the smallest valid interval that covers q.
        #
        # Main idea:
        # 1. Sort intervals by start time
        # 2. Sort queries in increasing order
        # 3. For each query q:
        #       - Add to heap all intervals that *start* before or at q
        #       - Remove from heap intervals that *ended* before q
        #       - The heap now contains only intervals that cover q
        #       - The smallest interval is on top of the min-heap
        #
        # Heap stores (interval_length, interval_end)
        # so the smallest interval length is always at the top.

        intervals.sort()  # sort intervals by starting point
        minHeap = []      # stores ONLY intervals that include current query
        res = {}          # map query -> result
        i = 0             # pointer for intervals to push into heap

        # ------------------- DRY RUN EXAMPLE IN COMMENTS -------------------
        # intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
        # queries   = [2, 3, 4, 5]
        #
        # intervals sorted stays: [[1,4], [2,4], [3,6], [4,4]]
        # sorted queries: [2, 3, 4, 5]
        #
        # q = 2:
        #   add intervals starting <= 2: [1,4] len=4, [2,4] len=3 --> heap [(3,4),(4,4)]
        #   remove intervals ending < 2 --> none
        #   smallest len = 3 --> answer for 2
        #
        # q = 3:
        #   add intervals starting <=3: [3,6] len=4 --> heap [(3,4),(4,4),(4,6)]
        #   remove intervals ending <3 --> none
        #   smallest len = 3 --> answer for 3
        #
        # q = 4:
        #   add intervals starting <=4: [4,4] len=1 --> heap [(1,4),(3,4),(4,6),(4,4)]
        #   remove intervals ending <4 --> none
        #   smallest len = 1 --> answer for 4
        #
        # q = 5:
        #   add? none (all added already)
        #   remove intervals ending <5 --> pop (1,4), (3,4), (4,4)
        #   top of heap = (4,6) --> answer for 5

        # ------------------------ PROCESS EACH QUERY ------------------------
        for q in sorted(queries):

            # add all intervals whose start <= q (meaning they *might* cover q)
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))  # store (interval length, right end)
                i += 1

            # remove intervals that ended before q (no longer cover q)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # the top of heap is smallest interval that covers q
            res[q] = minHeap[0][0] if minHeap else -1

        # return answers in original query order
        return [res[q] for q in queries]
