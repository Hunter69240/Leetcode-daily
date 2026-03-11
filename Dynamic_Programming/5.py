class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Variables to store the result palindrome and its length
        res = ""
        resLen = 0

        # Iterate through each character as a potential center
        for i in range(len(s)):
            # Case 1: Check for ODD length palindromes (center is a single character)
            # Example: "aba" has center at 'b'
            l, r = i, i
            # Expand outward while characters match and indices are valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If current palindrome is longer than previous best
                if (r - l + 1) > resLen:
                    res = s[l:r+1]  # Update result substring
                    resLen = r - l + 1  # Update result length
                l -= 1  # Move left pointer outward
                r += 1  # Move right pointer outward
            
            # Case 2: Check for EVEN length palindromes (center is between two characters)
            # Example: "abba" has center between the two 'b's
            l, r = i, i + 1
            # Expand outward while characters match and indices are valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # If current palindrome is longer than previous best
                if (r - l + 1) > resLen:
                    res = s[l:r+1]  # Update result substring
                    resLen = r - l + 1  # Update result length
                l -= 1  # Move left pointer outward
                r += 1  # Move right pointer outward
        
        # Return the longest palindrome found
        return res
