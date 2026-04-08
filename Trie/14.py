# PROBLEM
# Given an array of strings, return the longest common prefix among all strings.
# Example:
# ["flower","flow","flight"] -> "fl"
#
# WHY TRIE
# - problem is prefix based
# - we compare characters from beginning
# - branching means prefix stops
# - trie naturally stores shared prefix once
# - longest prefix = walk trie until branching


# Trie node represents one character in prefix tree
class TrieNode:
    def __init__(self):
        # dictionary storing next possible characters
        # char -> TrieNode
        self.children = {}

        # marks end of a complete word
        # important because prefix must stop if one word ends
        self.is_end = False


class Trie:
    def __init__(self):
        # root represents empty prefix
        self.root = TrieNode()

    # INSERT WORD INTO TRIE
    def insert(self, word):

        # start from root for every word
        node = self.root

        # process characters one by one
        for ch in word:

            # if character path not present -> create new node
            if ch not in node.children:
                node.children[ch] = TrieNode()

            # move to next node (current character node)
            node = node.children[ch]

        # mark end of word
        # needed so we stop prefix if shorter word exists
        node.is_end = True


    # FIND LONGEST COMMON PREFIX
    def longest_common_prefix(self):

        # store characters of prefix
        prefix = []

        # start traversal from root
        node = self.root

        # continue only when:
        # 1. only one child -> still common path
        # 2. not end of word -> no shorter word stopping prefix
        while len(node.children) == 1 and not node.is_end:

            # get the only child character
            ch = next(iter(node.children))

            # add character to prefix
            prefix.append(ch)

            # move to next node
            node = node.children[ch]

        # convert list of chars to string
        return "".join(prefix)


class Solution:
    def longestCommonPrefix(self, strs):

        # edge case: empty list
        if not strs:
            return ""

        # create trie
        trie = Trie()

        # insert all words into trie
        for word in strs:
            trie.insert(word)

        # traverse trie to find longest prefix
        return trie.longest_common_prefix()



# ---------------- DRY RUN ----------------

# INPUT
# ["flower","flow","flight"]

# STEP 1: insert "flower"
# root -> f -> l -> o -> w -> e -> r

# STEP 2: insert "flow"
# reuse f
# reuse l
# reuse o
# reuse w
# mark w as end

# trie now
# root
#  └─ f
#      └─ l
#          └─ o
#              └─ w (end)
#                  └─ e
#                      └─ r

# STEP 3: insert "flight"
# reuse f
# reuse l
# i not present -> create branch

# final trie
# root
#  └─ f
#      └─ l
#          ├─ o
#          │   └─ w ...
#          └─ i
#              └─ g ...

# STEP 4: find prefix

# node = root
# children = {f} -> one child -> add "f"

# node = f
# children = {l} -> one child -> add "l"

# node = l
# children = {o,i} -> two children -> stop

# prefix = "fl"

# OUTPUT
# "fl"