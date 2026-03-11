class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        # ---------------------------------------------------------
        # EXPLANATION:
        # We add two integers WITHOUT using '+' or '-'.
        #
        # Bit logic:
        #   a ^ b       → sum without carry
        #   (a & b)<<1  → carry bits
        #
        # Repeat until no carry remains.
        #
        # mask limits numbers to 32 bits to simulate integer overflow.
        # max_int helps convert result back to signed integer.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE: a = 3, b = 5
        #
        # Binary:
        # a = 0011
        # b = 0101
        #
        # Iteration 1:
        #   carry = (a & b) << 1
        #         = (0001) << 1 = 0010
        #
        #   a = a ^ b
        #     = 0011 ^ 0101 = 0110  (6)
        #
        #   b = carry = 0010  (2)
        #
        # Iteration 2:
        #   carry = (a & b) << 1
        #         = (0010) << 1 = 0100
        #
        #   a = 0110 ^ 0010 = 0100  (4)
        #
        #   b = 0100  (4)
        #
        # Iteration 3:
        #   carry = (a & b) << 1
        #         = (0100) << 1 = 1000
        #
        #   a = 0100 ^ 0100 = 0000
        #
        #   b = 1000  (8)
        #
        # Iteration 4:
        #   carry = (a & b) << 1
        #         = (0000) << 1 = 0000
        #
        #   a = 0000 ^ 1000 = 1000  (8)
        #
        #   b = 0000 → loop ends
        #
        # Result = 8
        # ---------------------------------------------------------

        while b != 0:
            carry = (a & b) << 1   # calculate carry
            a = (a ^ b) & mask    # sum without carry
            b = carry & mask      # update carry

        # ---------------------------------------------------------
        # HANDLE NEGATIVE NUMBERS:
        # If a exceeds max positive int,
        # convert it to negative using two's complement.
        # ---------------------------------------------------------

        return a if a <= max_int else ~(a ^ mask)
