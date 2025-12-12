class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # Reverse the digits to make addition easier (least significant digit first)
        digits = digits[::-1]

        one, i = 1, 0   # 'one' is the carry (initially adding 1), i = index

        # -------------------------------------------------------------------------
        # EXPLANATION:
        # We simulate adding 1 from the end of the number.
        # After reversing, we add from left to right (least significant digit first).
        #
        # Rules:
        # - If digit is 9, it becomes 0 and carry (one) stays 1.
        # - If digit is 0–8, increment it and carry becomes 0 → stop.
        # - If we run out of digits but still have carry, append 1.
        # -------------------------------------------------------------------------

        # -------------------------------------------------------------------------
        # DRY RUN EXAMPLE: digits = [1, 2, 9]
        #
        # After reverse → [9, 2, 1]
        #
        # Start: one = 1, i = 0
        #
        # i=0: digits[0] = 9
        #   → digit becomes 0
        #   → carry stays 1
        # digits = [0, 2, 1]
        #
        # i=1: digits[1] = 2
        #   → digit becomes 3
        #   → carry becomes 0 → STOP LOOP
        # digits = [0, 3, 1]
        #
        # Reverse back → [1, 3, 0]
        # RESULT: [1, 3, 0]
        # -------------------------------------------------------------------------

        while one:  # while carry exists
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0       # 9 becomes 0, carry stays 1
                else:
                    digits[i] += 1      # increase digit, clear carry
                    one = 0
            else:
                # Case: carry is still 1 but no digits left
                # Example: 999 → becomes 1000
                digits.append(1)
                one = 0

            i += 1

        return digits[::-1]  # reverse back to original order
