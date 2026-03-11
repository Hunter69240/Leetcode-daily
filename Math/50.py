class Solution:
    def myPow(self, x: float, n: int) -> float:

        def helper(x, n):

            # ---------------------------------------------------------
            # EXPLANATION:
            # This uses fast exponentiation (divide & conquer).
            #
            # Key idea:
            #   xⁿ = (x^(n/2))²                      if n is even
            #   xⁿ = x * (x^(n/2))²                  if n is odd
            #
            # This reduces the power by half each time → O(log n).
            # ---------------------------------------------------------

            if x == 0:
                return 0

            if n == 0:
                return 1

            # Recursively compute x^(n//2)
            res = helper(x, n // 2)

            # Square the half result
            res = res * res

            # If n is odd → multiply one extra x
            return x * res if n % 2 else res

        # ---------------------------------------------------------
        # HANDLE NEGATIVE POWERS:
        #   x^(-n) = 1 / x^n
        # ---------------------------------------------------------

        # Compute using absolute exponent
        res = helper(x, abs(n))

        return res if n >= 0 else 1 / res

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        #
        # INPUT: x = 2, n = 10
        #
        # helper(2, 10):
        #   calls helper(2, 5)
        #
        # helper(2, 5):
        #   calls helper(2, 2)
        #
        # helper(2, 2):
        #   calls helper(2, 1)
        #
        # helper(2, 1):
        #   calls helper(2, 0)
        #
        # helper(2, 0) → returns 1
        #
        # Back up:
        # helper(2, 1):
        #   res = 1² = 1
        #   n=1 is odd → return 2 * 1 = 2
        #
        # helper(2, 2):
        #   res = (2)² = 4
        #   n=2 even → return 4
        #
        # helper(2, 5):
        #   res = (4)² = 16
        #   n=5 odd → return 2 * 16 = 32
        #
        # helper(2, 10):
        #   res = (32)² = 1024
        #   n=10 even → return 1024
        #
        # FINAL RESULT: 1024
        # ---------------------------------------------------------
