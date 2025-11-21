class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Result list to store all possible combinations
        res = []

        # Mapping of digits to corresponding characters on a phone keypad
        digitToChar = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # Recursive backtracking function
        def backtrack(i, curStr):
            # Base case: if the current string length equals the digits length,
            # we found a valid combination → add it to result
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            # Recursive case: try all possible characters for the current digit
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)  # move to next digit and append character

        # Only call backtrack if digits is not empty (edge case: input = "")
        if digits:
            backtrack(0, "")

        # Return all possible combinations
        return res
