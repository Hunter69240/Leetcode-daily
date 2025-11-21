import heapq

class MedianFinder(object):

    def __init__(self):
        # Max-heap (simulated with negative values) for the smaller half of numbers
        self.small = []
        # Min-heap for the larger half of numbers
        self.large = []

    def addNum(self, num):
        """
        Add a number into the data structure.
        :type num: int
        :rtype: None
        """

        # If num belongs to the larger half (greater than the smallest in large heap)
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # Otherwise, push into small heap (as negative for max-heap simulation)
            heapq.heappush(self.small, -1 * num)

        # Balance the heaps so that their sizes differ at most by 1
        if len(self.small) > len(self.large) + 1:
            # Move the largest from small to large
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # Move the smallest from large to small
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self):
        """
        Find the median of all added numbers.
        :rtype: float
        """
        # If small has more elements → median is top of small (converted back to positive)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        # If large has more elements → median is top of large
        elif len(self.large) > len(self.small):
            return self.large[0]
        # If equal size → median is average of two tops
        return (-1 * self.small[0] + self.large[0]) / 2.0


# Example usage:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())  # → 1.5
# obj.addNum(3)
# print(obj.findMedian())  # → 2
