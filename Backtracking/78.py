class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []   # stores all subsets (final answer)
        subset = []  # current subset being built
        
        # dfs(i) will explore all subsets starting from index i
        def dfs(i):
            # base case: if we've considered all elements
            if i >= len(nums):
                res.append(subset.copy())  # add a copy of current subset
                return 
            
            # decision 1: include nums[i] in the subset
            subset.append(nums[i])
            dfs(i + 1)   # move to next index

            # backtrack: remove nums[i] to try without it
            subset.pop()

            # decision 2: do not include nums[i]
            dfs(i + 1)
        
        # start recursion at index 0
        dfs(0)
        return res
