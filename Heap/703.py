import heapq  # Importing heapq to use min-heap operations

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # Store the input list as a heap and keep track of k
        self.minHeap, self.k = nums, k  
        
        # Convert the list into a valid min-heap
        heapq.heapify(self.minHeap)
        
        # If heap size is larger than k, remove the smallest elements
        # This ensures the heap always contains only the k largest elements
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Push the new value into the heap
        heapq.heappush(self.minHeap, val)
        
        # If heap size exceeds k, pop the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The root of the min-heap is the kth largest element
        return self.minHeap[0]


# Example of usage:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
