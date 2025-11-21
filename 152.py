class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize result with the max element (handles all-negative arrays)
        res = max(nums)
        
        # curMax tracks the BEST product ending at current position
        # curMin tracks the WORST (most negative) product ending at current position
        # Why track worst? Because worst × negative = best!
        curMin, curMax = 1, 1

        for n in nums:
            # If we hit 0, all products become 0, so reset and start fresh
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            # Save old curMax because we need it to calculate BOTH new curMax and curMin
            # (If we update curMax first, we lose the old value needed for curMin)
            temp = curMax * n
            
            # Calculate new curMax by considering 3 options:
            # 1. n*curMax: extend the current best streak
            # 2. n*curMin: USE THE WORST! (if n is negative, worst becomes best)
            # 3. n: start fresh from this number (abandon previous products)
            curMax = max(n * curMax, n * curMin, n)
            
            # Calculate new curMin by considering same 3 options:
            # 1. temp (old curMax * n): might create new worst
            # 2. n*curMin: extend the current worst
            # 3. n: start fresh (this number itself might be the worst)
            # We SAVE this worst because it might become best later!
            curMin = min(temp, n * curMin, n)
            
            # Update global result with the best we've seen
            # Note: We compare with curMax (not curMin) because we want maximum
            res = max(res, curMax)
            
        return res
