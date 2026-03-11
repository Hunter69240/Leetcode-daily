class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort first so duplicates are adjacent (important for skipping)

        def backtrack(i, subset):
            # Base case: if we've considered all numbers
            if i == len(nums):
                res.append(subset.copy())  # store a copy of the current subset
                return

            # --- Choice 1: include nums[i] ---
            subset.append(nums[i])
            backtrack(i + 1, subset)  # move to next element
            subset.pop()  # undo choice (backtrack)

            # --- Choice 2: skip nums[i] ---
            # Skip all duplicates of nums[i] to avoid duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)  # move past all duplicates

        backtrack(0, [])  # start recursion with empty subset
        return res
