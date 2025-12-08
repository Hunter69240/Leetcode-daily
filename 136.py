class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ---------------------- INTUITION ----------------------
        # Each number in the array appears twice except one single number.
        # We need to find that number.
        #
        # XOR trick:
        #   a ^ a = 0          (same numbers cancel out)
        #   a ^ 0 = a          (XOR with 0 keeps the number unchanged)
        #   XOR is commutative and associative:
        #     a ^ b ^ a = (a ^ a) ^ b = 0 ^ b = b
        #
        # So if we XOR all numbers together:
        #   all paired numbers become 0
        #   the unpaired number is the only one left

        x = 0  # start with 0 because n ^ 0 = n  (neutral element for XOR)

        # ---------------------- LINE BY LINE ----------------------
        # Loop through every number n in nums
        for n in nums:
            x ^= n   # x = x XOR n
            # After each step, pairs cancel out. Only the single number survives.

        return x     # remaining value is the number that appeared once
