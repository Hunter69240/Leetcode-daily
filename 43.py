class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        # ---------------------------------------------------------
        # EXPLANATION:
        # We simulate manual multiplication (like on paper).
        #
        # Example:   123
        #            × 45
        # --------------------------------
        # We multiply each digit of num1 by each digit of num2,
        # and store results in an array `res` where:
        #   res[i1 + i2] holds the ones place
        #   res[i1 + i2 + 1] holds the carry
        #
        # Numbers are reversed so index 0 represents the units place.
        #
        # After all multiplications:
        # - We reverse the result back
        # - Remove leading zeros
        # - Convert to string
        # ---------------------------------------------------------

        if "0" in [num1, num2]:
            return "0"

        # Result size = len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))

        # Reverse both numbers for easier multiplication
        num1, num2 = num1[::-1], num2[::-1]

        # ---------------------------------------------------------
        # DRY RUN EXAMPLE:
        #
        # num1 = "123", num2 = "45"
        # reversed → "321", "54"
        #
        # res size = 5 → [0,0,0,0,0]
        #
        # i1=0 ('3'), i2=0 ('5'):
        #   digit = 3*5 = 15
        #   res[0] += 15 → res = [15,0,0,0,0]
        #   carry: res[1] += 15//10 = 1
        #   ones:  res[0] = 15%10 = 5
        #   res = [5,1,0,0,0]
        #
        # i1=0 ('3'), i2=1 ('4'):
        #   digit = 3*4 = 12
        #   res[1] += 12 → res[1] = 13
        #   carry: res[2] += 13//10 = 1
        #   ones:  res[1] = 13%10 = 3
        #   res = [5,3,1,0,0]
        #
        # i1=1 ('2'), i2=0 ('5'):
        #   digit = 2*5 = 10
        #   res[1] += 10 → res[1] = 13
        #   carry: res[2] += 13//10 = 1 → becomes 2
        #   ones:  res[1] = 3
        #   res = [5,3,2,0,0]
        #
        # i1=1 ('2'), i2=1 ('4'):
        #   digit = 2*4 = 8
        #   res[2] += 8 → res[2] = 10
        #   carry: res[3] += 1
        #   ones:  res[2] = 0
        #   res = [5,3,0,1,0]
        #
        # i1=2 ('1'), i2=0 ('5'):
        #   digit = 1*5 = 5
        #   res[2] += 5 → 5
        #   carry = 0
        #   res = [5,3,5,1,0]
        #
        # i1=2 ('1'), i2=1 ('4'):
        #   digit = 1*4 = 4
        #   res[3] += 4 → 5
        #   carry = 0
        #   res = [5,3,5,5,0]
        #
        # Reverse result → [0,5,5,3,5]
        #
        # Remove leading zeros → final = "5535"
        #
        # Which is correct: 123 × 45 = 5535
        # ---------------------------------------------------------

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])

                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        # Reverse result back
        res, beg = res[::-1], 0

        # Remove leading zeros
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)
