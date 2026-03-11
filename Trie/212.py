class TrieNode:
    def __init__(self):
        # Each node has children (dict of char -> TrieNode)
        self.children = {}
        # Flag to indicate if a complete word ends here
        self.isWord = False
    
    def addWord(self, word):
        """
        Insert a word into the Trie.
        """
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True  # mark end of word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1️⃣ Build Trie from given words
        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()  # res = found words, visit = track visited cells

        # 2️⃣ DFS backtracking function
        def dfs(r, c, node, word):
            # Base conditions: out of bounds, already visited, or char not in trie
            if (
                r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r, c) in visit or 
                board[r][c] not in node.children
            ):
                return
            
            # Mark cell as visited
            visit.add((r, c))

            # Move to the next trie node
            node = node.children[board[r][c]]
            word += board[r][c]

            # If this node marks the end of a word → add to result
            if node.isWord:
                res.add(word)

            # Explore neighbors (up, down, left, right)
            dfs(r - 1, c, node, word)  # up
            dfs(r + 1, c, node, word)  # down
            dfs(r, c - 1, node, word)  # left
            dfs(r, c + 1, node, word)  # right

            # Backtrack → unmark cell
            visit.remove((r, c))
        
        # 3️⃣ Run DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # Convert result set to list
        return list(res)
