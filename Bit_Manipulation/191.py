## 2 METHODS ##

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        # ---------------------------------------------------------
        # EXPLANATION:
        # We count how many 1-bits are present in the binary
        # representation of the number.
        #
        # n % 2 gives the last bit (0 or 1).
        # Right shift (n >> 1) removes the last bit.
        #
        # We keep doing this until n becomes 0.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        # n = 11
        # Binary of 11 = 1011
        #
        # Iteration 1:
        #   n = 11 → n % 2 = 1 → res = 1
        #   n >> 1 → n = 5  (101)
        #
        # Iteration 2:
        #   n = 5 → n % 2 = 1 → res = 2
        #   n >> 1 → n = 2  (10)
        #
        # Iteration 3:
        #   n = 2 → n % 2 = 0 → res = 2
        #   n >> 1 → n = 1  (1)
        #
        # Iteration 4:
        #   n = 1 → n % 2 = 1 → res = 3
        #   n >> 1 → n = 0
        #
        # Loop ends.
        # FINAL RESULT: 3
        # ---------------------------------------------------------

        while n:
            res += n % 2   # add last bit
            n = n >> 1    # shift right to process next bit

        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        # ---------------------------------------------------------
        # EXPLANATION:
        # This uses Brian Kernighan’s Algorithm.
        #
        # Key idea:
        #   n & (n - 1) removes the RIGHTMOST 1-bit from n.
        #
        # So each loop iteration:
        #   - removes one set bit
        #   - increments the count
        #
        # Number of iterations = number of 1-bits.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        # n = 11
        # Binary: 1011
        #
        # Iteration 1:
        #   n = 1011
        #   n-1 = 1010
        #   n & (n-1) = 1010
        #   res = 1
        #
        # Iteration 2:
        #   n = 1010
        #   n-1 = 1001
        #   n & (n-1) = 1000
        #   res = 2
        #
        # Iteration 3:
        #   n = 1000
        #   n-1 = 0111
        #   n & (n-1) = 0000
        #   res = 3
        #
        # Loop ends.
        # FINAL RESULT: 3
        # ---------------------------------------------------------

        while n:
            n = n & (n - 1)  # remove rightmost 1-bit
            res += 1

        return res
