class TrieNode:
    def __init__(self):
        # Each node has:
        # - children: dict mapping char -> TrieNode
        # - word: boolean flag, True if a word ends here
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        # Root node (empty, no characters yet)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the Trie.
        """
        cur = self.root
        for c in word:
            # If character doesn't exist at this level, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move down to the child node
            cur = cur.children[c]

        # After inserting all characters, mark this node as a word ending
        cur.word = True

    def search(self, word: str) -> bool:
        """
        Searches a word in the Trie.
        '.' can match any character.
        """

        def dfs(j, node):
            """
            Recursive depth-first search:
            j -> index in the word we're checking
            node -> current TrieNode
            """
            cur = node

            # Traverse the word starting at index j
            for i in range(j, len(word)):
                c = word[i]

                # Case 1: '.' -> match any character
                if c == '.':
                    # Try *all children* recursively
                    for child in cur.children.values():
                        if dfs(i + 1, child):  # If any child path matches
                            return True
                    return False  # No path matched

                # Case 2: normal character
                else:
                    if c not in cur.children:
                        return False  # character not found
                    cur = cur.children[c]

            # After processing all characters, return if this is a word ending
            return cur.word

        # Start DFS from root with index 0
        return dfs(0, self.root)


# Example usage:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")

print(obj.search("pad"))   # False (not in dictionary)
print(obj.search("bad"))   # True
print(obj.search(".ad"))   # True (matches "bad", "dad", "mad")
print(obj.search("b.."))   # True (matches "bad")
