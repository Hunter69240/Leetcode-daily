class Solution:
    def rob(self, nums: List[int]) -> int:
        # Handle the circular constraint by considering 3 scenarios:
        # 1. Rob only the first house (nums[0])
        # 2. Rob houses excluding the first (nums[1:])
        # 3. Rob houses excluding the last (nums[:-1])
        # Return maximum of all three options
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        # Solves the standard (linear) house robber problem
        # using dynamic programming with space optimization
        
        # rob1: max money robbed up to 2 houses ago
        # rob2: max money robbed up to the previous house
        rob1, rob2 = 0, 0

        # Iterate through each house
        for n in nums:
            # Decide: rob current house (rob1 + n) OR skip it (rob2)
            newRob = max(rob1 + n, rob2)
            
            # Shift the variables for the next iteration
            rob1 = rob2  # Previous "rob2" becomes new "rob1"
            rob2 = newRob  # Current max becomes new "rob2"
        
        # Return the maximum money that can be robbed
        return rob2
