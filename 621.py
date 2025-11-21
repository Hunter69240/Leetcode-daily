import heapq
from collections import Counter, deque

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int (cooldown period between the same tasks)
        :rtype: int (minimum time to finish all tasks)
        """

        # Count how many times each task appears
        count = Counter(tasks)

        # We use a max heap (Python has only min-heap, so we negate counts)
        # Example: tasks = ["A","A","A","B","B","B"], count = {"A":3,"B":3}
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        # Keeps track of total time taken
        time = 0

        # Queue to store tasks that are cooling down (not ready to run yet)
        # Each entry = [remaining_count, time_when_it_can_run]
        q = deque()

        # Process until both heap (ready tasks) and queue (cooldown tasks) are empty
        while maxHeap or q:
            time += 1   # Each loop = 1 unit of time passes

            if maxHeap:
                # Pop the most frequent task
                cnt = 1 + heapq.heappop(maxHeap)  
                # (adding 1 because values are negative, so -3 -> -2 means one less task left)
                
                if cnt:  
                    # If there are still occurrences left, put it in cooldown queue
                    # It can be run again only after 'n' units of time
                    q.append([cnt, time + n])

            # Check if the front of the cooldown queue is ready to run again
            if q and q[0][1] == time:
                # Push it back to the heap (ready to be scheduled again)
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
