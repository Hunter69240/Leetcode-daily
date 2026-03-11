class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1: maximum money robbed up to 2 houses before current house
        # rob2: maximum money robbed up to 1 house before current house
        rob1, rob2 = 0, 0

        # Pattern: [rob1, rob2, n, n+1, ...]
        # At each house, we decide: rob current house + rob1, or skip it and keep rob2
        for n in nums:
            # Calculate max money if we include current house (n + rob1) 
            # vs if we skip it (rob2)
            temp = max(n + rob1, rob2)
            
            # Shift the window forward:
            # rob1 becomes what rob2 was (move 2 houses back → 1 house back)
            rob1 = rob2
            
            # rob2 becomes the new maximum (move 1 house back → current position)
            rob2 = temp
        
        # rob2 contains the maximum money that can be robbed from all houses
        return rob2
