class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # If the endWord is not in the dictionary, transformation is impossible
        if endWord not in wordList:
            return 0
        
        # Map pattern -> list of words matching that pattern
        # Example: h*t -> ["hot", "hit"]
        nei = collections.defaultdict(list)

        # Add beginWord into wordList (so patterns include it too)
        wordList.append(beginWord)

        # Build pattern dictionary
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        # BFS setup
        visit = set([beginWord])      # visited words
        q = deque([beginWord])        # queue for BFS
        res = 1                       # initial ladder length (counting beginWord)

        # BFS traversal
        while q:
            for i in range(len(q)):
                word = q.popleft()
                
                # If we reach the target, return the number of steps
                if word == endWord:
                    return res

                # Try all patterns of current word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    
                    # For all words that share the same pattern
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)   # mark as visited
                            q.append(neiWord)   # add to queue
            
            # Finished one BFS level -> increment path length
            res += 1
        
        # If BFS ends without finding endWord, return 0
        return 0
