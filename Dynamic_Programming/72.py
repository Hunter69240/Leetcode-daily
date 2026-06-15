# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         # DP cache with dimensions (len(word1)+1) x (len(word2)+1)
#         # Initialize everything to infinity
#         cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

#         # Base case: word1 is empty, so we need to insert remaining chars of word2
#         for j in range(len(word2) + 1):
#             cache[len(word1)][j] = len(word2) - j

#         # Base case: word2 is empty, so we need to delete remaining chars of word1
#         for i in range(len(word1) + 1):
#             cache[i][len(word2)] = len(word1) - i

#         # Fill DP table bottom-up
#         for i in range(len(word1) - 1, -1, -1):
#             for j in range(len(word2) - 1, -1, -1):
#                 # If characters match, no edit needed
#                 if word1[i] == word2[j]:
#                     cache[i][j] = cache[i + 1][j + 1]

#                 else:
#                     # Otherwise, take best of: delete, insert, replace
#                     cache[i][j] = 1 + min(
#                         cache[i + 1][j],  # delete char from word1
#                         cache[i][j + 1],  # insert char into word1
#                         cache[i + 1][j + 1],  # replace char
#                     )

#         return cache[0][0]

#This is a pattern 2b problem as i am given 2 words and told to compare and my current box depends on 3 other boxes , that is y it is 2b pattern
def a():
    word1 = "horse"
    word2 = "ros"
    dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
    for i in range(len(dp[0])):
        dp[0][i]=i
    for i in range(len(dp)):
        dp[i][0]=i
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i]==word2[j]:
                dp[i+1][j+1]=dp[i][j]
            else:
                dp[i+1][j+1]=min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
                
    return (dp[-1][-1])
print(a())

