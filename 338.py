class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        # ---------------------------------------------------------
        # EXPLANATION:
        # dp[i] stores the number of 1-bits in the binary
        # representation of i.
        #
        # Key observation:
        # Numbers repeat bit patterns after powers of 2.
        #
        # For any number i:
        #   let offset be the largest power of 2 ≤ i
        #
        # Then:
        #   dp[i] = 1 + dp[i - offset]
        #
        # Because subtracting offset removes the leading 1-bit.
        # ---------------------------------------------------------

        offset = 1  # current power of 2

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE: n = 5
        #
        # dp = [0,0,0,0,0,0]
        #
        # i = 1:
        #   offset*2 == 2 → not equal to 1
        #   dp[1] = 1 + dp[1-1] = 1
        #
        # i = 2:
        #   offset*2 == 2 → YES → offset = 2
        #   dp[2] = 1 + dp[2-2] = 1
        #
        # i = 3:
        #   offset*2 == 4 → no
        #   dp[3] = 1 + dp[3-2] = 2
        #
        # i = 4:
        #   offset*2 == 4 → YES → offset = 4
        #   dp[4] = 1 + dp[4-4] = 1
        #
        # i = 5:
        #   offset*2 == 8 → no
        #   dp[5] = 1 + dp[5-4] = 2
        #
        # FINAL dp = [0,1,1,2,1,2]
        # ---------------------------------------------------------

        for i in range(1, n + 1):
            # Update offset when i reaches next power of 2
            if offset * 2 == i:
                offset = i

            # Count bits using previous results
            dp[i] = 1 + dp[i - offset]

        return dp
