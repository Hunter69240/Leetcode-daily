class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # ---------------------------------------------------------
        # EXPLANATION:
        # We reverse the bits of a 32-bit unsigned integer.
        #
        # For each bit position i from 0 to 31:
        #   1) Extract the i-th bit from n using:
        #        (n >> i) & 1
        #   2) Place this bit at position (31 - i) in res.
        #
        # This effectively mirrors the bits from left to right.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        #
        # n = 00000000000000000000000000001010 (binary for 10)
        #
        # i = 0:
        #   bit = (n >> 0) & 1 = 0
        #   res |= 0 << 31 → res unchanged
        #
        # i = 1:
        #   bit = (n >> 1) & 1 = 1
        #   res |= 1 << 30
        #
        # i = 2:
        #   bit = (n >> 2) & 1 = 0
        #
        # i = 3:
        #   bit = (n >> 3) & 1 = 1
        #   res |= 1 << 28
        #
        # ...
        #
        # After all 32 iterations:
        # res = 01010000000000000000000000000000
        #
        # Which is the bit-reversed version of n.
        # ---------------------------------------------------------

        for i in range(32):
            bit = (n >> i) & 1          # extract i-th bit
            res = res | (bit << (31 - i))  # place it at reversed position

        return res
