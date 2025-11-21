import heapq  # Import heapq for heap operations

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        # Python's heapq is a MIN-heap by default.
        # To simulate a MAX-heap (because we need the largest stones),
        # we negate all stone weights.
        stones = [-s for s in stones]

        # Turn the list into a valid heap
        heapq.heapify(stones)

        # Keep smashing until we have <= 1 stone left
        while len(stones) > 1:
            # Pop the two heaviest stones (remember: values are negative)
            first = heapq.heappop(stones)   # largest stone (most negative)
            second = heapq.heappop(stones)  # second largest

            # If they are not equal, the new stone = difference
            # Since values are negative, subtracting keeps it correct
            if second > first:  
                # Push back the difference into the heap
                # (still negated to keep max-heap behavior)
                heapq.heappush(stones, first - second)

        # If no stones left, return 0
        # Otherwise, return the absolute value of the last stone
        stones.append(0)  # ensures at least one element to return
        return abs(stones[0])
