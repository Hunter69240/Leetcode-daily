class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP cache with dimensions (len(word1)+1) x (len(word2)+1)
        # Initialize everything to infinity
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Base case: word1 is empty, so we need to insert remaining chars of word2
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        # Base case: word2 is empty, so we need to delete remaining chars of word1
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        # Fill DP table bottom-up
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                
                # If characters match, no edit needed
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                
                else:
                    # Otherwise, take best of: delete, insert, replace
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],     # delete char from word1
                        cache[i][j + 1],     # insert char into word1
                        cache[i + 1][j + 1]  # replace char
                    )

        return cache[0][0]
