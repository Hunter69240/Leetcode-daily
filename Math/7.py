class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31
        MAX = 2147483647   #  2^31 - 1

        res = 0

        # ---------------------------------------------------------
        # EXPLANATION:
        # We reverse the digits of an integer.
        #
        # Steps in each loop:
        #   1) Extract the last digit using fmod(x, 10)
        #   2) Remove the last digit from x using x / 10
        #   3) Append the digit to res (res = res * 10 + digit)
        #
        # Before appending, we check for overflow:
        #   If res goes outside 32-bit signed integer range,
        #   we immediately return 0.
        # ---------------------------------------------------------

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE: x = 123
        #
        # Initial:
        # x = 123, res = 0
        #
        # Iteration 1:
        #   digit = 123 % 10 = 3
        #   x = 123 // 10 = 12
        #   res = 0 * 10 + 3 = 3
        #
        # Iteration 2:
        #   digit = 12 % 10 = 2
        #   x = 12 // 10 = 1
        #   res = 3 * 10 + 2 = 32
        #
        # Iteration 3:
        #   digit = 1 % 10 = 1
        #   x = 1 // 10 = 0
        #   res = 32 * 10 + 1 = 321
        #
        # Loop ends (x == 0)
        # FINAL RESULT: 321
        # ---------------------------------------------------------
        #
        # DRY RUN (NEGATIVE): x = -123
        #
        # Iteration 1:
        #   digit = -123 % 10 = -3
        #   x = -123 // 10 = -12
        #   res = -3
        #
        # Iteration 2:
        #   digit = -12 % 10 = -2
        #   x = -1
        #   res = -32
        #
        # Iteration 3:
        #   digit = -1 % 10 = -1
        #   x = 0
        #   res = -321
        #
        # FINAL RESULT: -321
        # ---------------------------------------------------------

        while x:
            digit = int(math.fmod(x, 10))  # get last digit (works for negatives)
            x = int(x / 10)               # remove last digit

            # Overflow check (positive side)
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            # Overflow check (negative side)
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            # Append digit
            res = (res * 10) + digit

        return res
