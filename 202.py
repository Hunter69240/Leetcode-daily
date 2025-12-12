class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        # -------------------------------------------------------
        # EXPLANATION:
        # A number is "happy" if repeatedly replacing it with the
        # sum of the squares of its digits eventually reaches 1.
        #
        # If we ever see the SAME number again, we are in a cycle
        # → it will never reach 1 → return False.
        #
        # The set 'visit' keeps track of previously seen numbers.
        # -------------------------------------------------------

        # -------------------------------------------------------
        # DRY RUN EXAMPLE: n = 19
        #
        # visit = {}
        #
        # LOOP 1:
        #   n = 19 not in visit → add it
        #   sumOfSquares(19):
        #       9^2 = 81
        #       1^2 = 1
        #       total = 82
        #   n = 82
        #
        # LOOP 2:
        #   n = 82 not in visit → add it
        #   sumOfSquares(82):
        #       2^2 = 4
        #       8^2 = 64
        #       total = 68
        #   n = 68
        #
        # LOOP 3:
        #   n = 68 not in visit → add it
        #   sumOfSquares(68):
        #       8^2 = 64
        #       6^2 = 36
        #       total = 100
        #   n = 100
        #
        # LOOP 4:
        #   n = 100 not in visit → add it
        #   sumOfSquares(100):
        #       0^2 = 0
        #       0^2 = 0
        #       1^2 = 1
        #       total = 1
        #   n == 1 → return True
        #
        # RESULT → True (19 is a happy number)
        # -------------------------------------------------------

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False  # cycle detected → not a happy number


    def sumOfSquares(self, n: int) -> int:
        output = 0

        # -------------------------------------------------------
        # EXPLANATION OF THIS FUNCTION:
        # Takes a number and returns sum of squares of its digits.
        #
        # Example: n = 82 → 8² + 2² = 64 + 4 = 68
        #
        # DRY RUN: n = 68
        #   digit = 8 → 8² = 64 → output = 64
        #   digit = 6 → 6² = 36 → output = 100
        # -------------------------------------------------------

        while n:
            digit = n % 10       # get last digit
            digit *= digit       # square it
            output += digit      # add to total
            n //= 10             # remove last digit

        return output
