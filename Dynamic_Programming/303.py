# # class NumArray(object):

# #     def __init__(self, nums):
# #         """
# #         Initialize the NumArray object with the integer list nums.
# #         :type nums: List[int]
# #         """
# #         self.nums = nums  # Store the input list for future queries

# #     def sumRange(self, left, right):
# #         """
# #         Calculate and return the sum of the elements between indices left and right inclusive.
# #         :type left: int
# #         :type right: int
# #         :rtype: int
# #         """
# #         sum = 0  # Initialize sum to zero
# #         # Iterate through the elements from index 'left' to 'right' inclusive
# #         for i in range(left, right + 1):
# #             sum += self.nums[i]  # Add the element at index i to sum
# #         return sum  # Return the computed sum

# # # Usage:
# # # obj = NumArray(nums)
# # # param_1 = obj.sumRange(left, right)

# # # Note:
# # # - This implementation correctly sums the subarray elements.
# # # - However, sumRange takes O(n) time for each query (where n is right-left+1).
# # # - If you need to process multiple queries efficiently, consider using a prefix sum array in __init__
# # #   to answer sumRange queries in O(1) time.



# class NumArray(object):

#     def __init__(self, nums):
#         """
#         Initialize the NumArray object and precompute prefix sums.
#         :type nums: List[int]
#         """
#         self.prefix_sum = [0] * (len(nums) + 1)
#         for i in range(1, len(nums) + 1):
#             # prefix_sum[i] stores sum of nums[0] to nums[i-1]
#             self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

#     def sumRange(self, left, right):
#         """
#         Return the sum of elements between indices left and right inclusive.
#         :type left: int
#         :type right: int
#         :rtype: int
#         """
#         # Use the difference of prefix sums to get the sum in O(1) time
#         return self.prefix_sum[right + 1] - self.prefix_sum[left]
