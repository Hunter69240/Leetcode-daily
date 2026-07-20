'''
At every (i,j): 
1) First figure out ONE fact -> match = does s[i] align with p[j]?
   (true if same char, or p[j] is '.', and i still in bounds)

2) Then check p[j+1] -> is it '*' ?

   If '*' present -> this is NOT a single choice, it's an OR of 2 attempts:
       - skip "char*" completely -> dfs(i, j+2)
       - if match is true -> consume one char and stay on same j -> dfs(i+1, j)
       (either attempt succeeding is enough)

   If '*' NOT present -> no choice, it's forced:
       - if match true -> advance both -> dfs(i+1, j+1)
       - if match false -> dead end -> False

So match is computed once, then just REUSED differently depending on 
whether a * follows or not. It's a fork (star / no-star), not 3 parallel choices.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Cache to store results of subproblems (i, j)
        # This prevents repeated computation and makes the solution efficient.
        cache = {}

        def dfs(i, j):
            # If we have already computed the result for (i, j), return it
            if (i, j) in cache:
                return cache[(i, j)]

            # If both the string (s) and pattern (p) have been fully matched
            if i >= len(s) and j >= len(p):
                return True

            # If pattern is consumed but string is not, no match
            if j >= len(p):
                return False

            # Check if current characters match:
            # - They match if s is not finished AND the chars are equal OR pattern has '.'
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # Handle "*" wildcard:
            # If next character in pattern is '*', we have two choices:
            # 1. Skip "char*" entirely → dfs(i, j+2)
            # 2. If current char matches, use the '*' to consume one char from s → dfs(i+1, j)
            if j + 1 < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (
                    dfs(i, j + 2) or        # Skip the star
                    (match and dfs(i + 1, j))  # Use the star (repeat the char)
                )
                return cache[(i, j)]

            # If there is no '*', but chars match, just move to next in both
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # If characters do not match and there is no '*', mismatch
            cache[(i, j)] = False
            return False

        # Start DFS at beginning of string and pattern
        return dfs(0, 0)
