def a():
    # Problem:
    # Determine if the array can be split into two subsets with equal sum.
    # Equivalent reduction:
    # → Check if there exists a subset with sum = total_sum // 2

    nums = [1,5,11,5]

    # res_set will store all reachable subset sums
    # Initially only 0 is possible (pick nothing)
    res_set = set()
    res_set.add(0)

    # Target sum each subset must achieve
    target = sum(nums) // 2

    # If total sum is odd → cannot split equally
    if sum(nums) % 2 != 0:
        return False

    # Iterate through each number
    for i in nums:

        # new_set will store sums formed by INCLUDING current number i
        new_set = set()

        # For every previously reachable sum j
        for j in res_set:
            # If we include current number i,
            # new sum becomes j + i
            new_set.add(i + j)

        # Merge:
        # - old sums → excluding i
        # - new sums → including i
        # This preserves all subset possibilities
        res_set = res_set.union(new_set)

        # Early check:
        # If target sum becomes reachable, we can stop
        if target in res_set:
            return True

        # ---- DRY RUN ----
        # nums = [1,5,11,5], target = 11
        #
        # Start: {0}
        #
        # i = 1:
        #   new_set = {1}
        #   res_set = {0,1}
        #
        # i = 5:
        #   new_set = {5,6}
        #   res_set = {0,1,5,6}
        #
        # i = 11:
        #   new_set = {11,12,16,17}
        #   res_set = {0,1,5,6,11,...}
        #   target (11) found → return True

    # If target never reached
    return False


print(a())

# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#         # If total sum is odd, it cannot be split into two equal subsets
#         if sum(nums) % 2:
#             return False
        
#         dp = set()
#         dp.add(0)  # 0 sum is always possible (choose no elements)
#         target = sum(nums) // 2  # We only need to check for half the sum

#         # Iterate from the last element to the first
#         for i in range(len(nums) - 1, -1, -1):
#             nextDP = set()
#             # For every sum we have seen so far, try including nums[i]
#             for t in dp:
#                 # If we exactly reach the target, we can stop early
#                 if t + nums[i] == target:
#                     return True
#                 # Add the new sum formed by including nums[i]
#                 nextDP.add(t + nums[i])
#                 # Also keep the sum formed by NOT including nums[i]
#                 nextDP.add(t)
#             # Move to the next dp set
#             dp = nextDP
            
        
#         # Final check: whether target sum is achievable
#         return True if target in dp else False
