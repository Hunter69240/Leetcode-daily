# ============================================================
# PROBLEM: LeetCode 692 - Top K Frequent Words
# ============================================================
# Given a list of words and an integer k, return the k most
# frequent words. If two words have the same frequency, the
# lexicographically smaller word comes first.
# Output must be sorted by frequency (descending), then
# alphabetically (ascending) for ties.
# ============================================================

# APPROACH USED: Frequency Bucket + Trie per Bucket
# ============================================================
# 1. Count frequency of each unique word using a hash map.
# 2. Group words into buckets where bucket[f] = all words
#    that appear exactly f times.
# 3. Process buckets from highest frequency to lowest.
# 4. For each bucket, insert its words into a fresh Trie.
# 5. DFS the Trie visiting children in a-z order (sorted).
#    This gives all words in that bucket in lexicographic order.
# 6. Collect words into result until we have k words.
#
# Why Trie? Trie DFS in sorted child order naturally gives
# lexicographic output without extra sorting per bucket.
# ============================================================

from typing import List
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}   # maps char -> TrieNode child
        self.is_end = False  # True if a word ends at this node

    def addWord(self, word):
        cur = self                          # start from current node (root when called on root)
        for c in word:
            if c not in cur.children:       # if char path doesn't exist, create it
                cur.children[c] = TrieNode()
            cur = cur.children[c]           # move deeper into trie
        cur.is_end = True                   # mark end of word at final char node


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1   # count how many times each word appears

        buckets = defaultdict(list)
        for word, f in freq.items():
            buckets[f].append(word)         # group words by their frequency

        res = []                            # final result list

        def dfs(node, path):
            if len(res) == k:               # global stop: already collected k words
                return
            if node.is_end:
                res.append(path)            # found a complete word, add to result
            for ch in sorted(node.children):            # visit children in a-z order for lexicographic output
                dfs(node.children[ch], path + ch)       # go deeper, building word char by char

        for f in sorted(buckets.keys(), reverse=True):  # process highest frequency bucket first
            root = TrieNode()                            # fresh trie for each frequency bucket

            for word in buckets[f]:
                root.addWord(word)                       # insert all same-frequency words into trie

            dfs(root, "")                                # DFS gives words in lexicographic order
            if len(res) == k:                            # stop if we already have k words
                break

        return res

# ============================================================
# DRY RUN
# words = ["i","love","leetcode","i","love","coding"], k = 2
# ============================================================
# Step 1: freq = { "i":2, "love":2, "leetcode":1, "coding":1 }
#
# Step 2: buckets = { 2: ["i","love"], 1: ["leetcode","coding"] }
#
# Step 3: sorted bucket keys descending = [2, 1]
#
# --- Process bucket f=2: words = ["i", "love"] ---
# Trie after inserting "i" and "love":
#   root -> 'i' (is_end=True)
#        -> 'l' -> 'o' -> 'v' -> 'e' (is_end=True)
#
# DFS(root, ""):
#   sorted(root.children) = ['i', 'l']
#   -> visit 'i': DFS(i_node, "i")
#       i_node.is_end = True -> res.append("i") -> res = ["i"]
#       i_node.children = {} -> backtrack
#   -> visit 'l': DFS(l_node, "l")
#       -> visit 'o' -> 'v' -> 'e'
#       e_node.is_end = True -> res.append("love") -> res = ["i","love"]
#       len(res) == k=2 -> return immediately
#
# Step 4: len(res) == k -> break outer loop
#
# Final result: ["i", "love"]  ✓
# ============================================================