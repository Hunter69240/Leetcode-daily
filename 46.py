class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base case: if nums is empty, return a list with an empty list
        # This acts as the starting point for building permutations
        if len(nums) == 0:
            return [[]]
        
        # Recursively get all permutations of the remaining elements (excluding the first one)
        perms = self.permute(nums[1:])
        res = []

        # For each smaller permutation, insert nums[0] into every possible position
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()  # copy to avoid modifying the original list
                p_copy.insert(i, nums[0])  # insert the first element at position i
                res.append(p_copy)  # add this new permutation to the result list

        # Return all built permutations
        return res
