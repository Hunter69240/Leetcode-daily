class Solution:
    def countSubstrings(self, s: str) -> int:
        # Variable to store the total count of palindromic substrings
        res = 0

        # Iterate through each character as a potential center
        for i in range(len(s)):
            # Case 1: Count ODD length palindromes (single character center)
            # Examples: "a", "aba", "racecar"
            l = r = i  # Start with left and right pointers at the same position
            
            # Expand outward while characters match and indices are valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1  # Found a valid palindrome, increment counter
                l -= 1    # Move left pointer outward
                r += 1    # Move right pointer outward
            
            # Case 2: Count EVEN length palindromes (center between two characters)
            # Examples: "aa", "abba", "aabbaa"
            l = i       # Left pointer starts at current position
            r = i + 1   # Right pointer starts at next position
            
            # Expand outward while characters match and indices are valid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1  # Found a valid palindrome, increment counter
                l -= 1    # Move left pointer outward
                r += 1    # Move right pointer outward
        
        # Return total count of palindromic substrings
        return res


#OR

class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res