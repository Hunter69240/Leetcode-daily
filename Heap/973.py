import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]   # List of 2D points [x, y]
        :type k: int                     # Number of closest points to origin we want
        :rtype: List[List[int]]          # List of k closest points
        """

        minHeap = []   # Will store elements in form [distance, x, y]

        # Step 1: Calculate squared distance from origin for each point
        for x, y in points:
            # Distance formula: sqrt(x^2 + y^2), 
            # but we skip sqrt because squared distance preserves ordering
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        # Step 2: Convert the list into a heap (min-heap by distance)
        heapq.heapify(minHeap)

        res = []   # To store result points

        # Step 3: Extract k closest points
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)  # Pop the smallest distance
            res.append([x, y])                   # Store the point (x, y)
            k -= 1

        # Step 4: Return result
        return res
