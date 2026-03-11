class TrieNode:
    def __init__(self):
        # Each node stores its children in a dictionary (char -> TrieNode)
        self.children = {}
        # Flag to mark the end of a complete word
        self.endOfWord = False


class Trie:

    def __init__(self):
        # Root node of the Trie (empty initially)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.
        """
        cur = self.root

        # Traverse each character in the word
        for c in word:
            # If the character is not present, create a new TrieNode
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # Move to the next node
            cur = cur.children[c]

        # Mark the last node as the end of a word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        """
        Return True if the word exists in the Trie, otherwise False.
        """
        cur = self.root

        # Traverse each character
        for c in word:
            if c not in cur.children:
                return False  # Character not found → word doesn’t exist
            cur = cur.children[c]

        # Return True only if the last node marks the end of a word
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Return True if there exists any word in the Trie 
        that starts with the given prefix.
        """
        cur = self.root

        # Traverse each character of the prefix
        for c in prefix:
            if c not in cur.children:
                return False  # Prefix not found
            cur = cur.children[c]

        # If traversal succeeds, prefix exists
        return True


# Example usage:
# obj = Trie()
# obj.insert("apple")
# print(obj.search("apple"))    # True
# print(obj.search("app"))      # False
# print(obj.startsWith("app"))  # True
