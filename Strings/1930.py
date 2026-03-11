class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Set to store unique palindromic subsequences of form c _ c
        # We store them as tuples (middle_char, outer_char)
        res = set()

        # Characters seen so far (to use as left-side outer char)
        left = set()

        # Count of remaining characters to the right (to use as right-side outer char)
        right = Counter(s)

        # Iterate through each character as the possible middle character
        for m in s:
            # This character is now being used as middle, so remove it from right side
            right[m] -= 1

            # Check all possible outer characters that have appeared before (left side)
            for c in left:
                # We can form c m c if c also appears to the right
                if right[c] > 0:
                    res.add((m, c))

            # Mark this character as seen on the left for future middle positions
            left.add(m)

        # Number of distinct palindromic subsequences of length 3
        return len(res)
