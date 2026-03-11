import heapq   # Import heapq module for heap operations

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heapq.nlargest(k, nums) returns a list of the k largest elements from nums,
        # sorted in descending order (largest to smallest).
        # Example: nums = [3,2,1,5,6,4], k=2 → [6,5]
        
        # The k-th largest element will be the last element of this list (index -1),
        # because the list is sorted from largest to smallest.
        return heapq.nlargest(k, nums)[-1]
