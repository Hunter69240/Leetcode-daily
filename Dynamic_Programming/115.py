# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         # Memoization cache to store results of subproblems
#         cache = {}

#         def dfs(i, j):
#             # If we've matched all characters of t, we found a valid subsequence
#             if j == len(t):
#                 return 1

#             # If we've exhausted s but not t, no subsequence can be formed
#             if i == len(s):
#                 return 0

#             # Return cached result if available
#             if (i, j) in cache:
#                 return cache[(i, j)]

#             # Case 1: Characters match — we can either use s[i] or skip it
#             if s[i] == t[j]:
#                 cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
#             else:
#                 # Case 2: Characters don't match — only option is to skip s[i]
#                 cache[(i, j)] = dfs(i + 1, j)

#             return cache[(i, j)]

#         # Start DFS from the beginning of both strings
#         return dfs(0, 0)

s = "rabbbit"
t = "rabbit"

dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(len(s)+1):
    dp[i][0]=1

for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1]==t[j-1]:
            dp[i][j]=dp[i-1][j-1] + dp[i-1][j]
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])