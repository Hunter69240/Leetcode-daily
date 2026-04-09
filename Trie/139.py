# Problem:
# We are given:
# 1. dictionary of ROOT words
# 2. a sentence containing words
#
# We must replace each word in the sentence with the SHORTEST root
# that is a prefix of that word.
#
# Example:
# dictionary = ["cat","bat","rat"]
# "cattle" -> "cat"
# "battery" -> "bat"
#
# Why Trie?
# Because we must check prefixes character-by-character.
# Trie allows:
# - fast prefix lookup
# - early stop when shortest root found
# - shared prefix reuse


# Trie node representing one character
class TrieNode:
    def __init__(self):
        # children = next characters from this node
        # example: {'c': node1, 'b': node2}
        self.children = {}

        # marks end of a valid root word
        self.is_end = False


class Trie:
    def __init__(self):
        # root node of trie (empty start)
        self.root = TrieNode()
    
    # insert root word into trie
    def insert(self, word):

        # start from root
        node = self.root

        # iterate character by character
        for ch in word:

            # if path does not exist create new node
            if ch not in node.children:
                node.children[ch] = TrieNode()

            # move to next node
            node = node.children[ch]

        # mark end of root word
        node.is_end = True


    # How insert stores words (example)
    #
    # insert("cat")
    #
    # root
    #  └── 'c'
    #        └── 'a'
    #              └── 't' (is_end = True)
    #
    # dictionary representation:
    #
    # root.children = {
    #   'c': node1
    # }
    #
    # node1.children = {
    #   'a': node2
    # }
    #
    # node2.children = {
    #   't': node3
    # }
    #
    # node3.is_end = True


    # replace words using trie
    def replace_words(self, sentence, root):

        # store final words
        res = []

        # prefix holder
        prefix = ""

        # start node
        node = root

        # iterate each word in sentence
        for word in sentence.split():

            # reset node for new word
            node = root

            # reset prefix
            prefix = ""

            # traverse characters of word
            for letter in word:

                # if no path in trie stop searching
                if letter not in node.children:
                    break

                # move in trie
                node = node.children[letter]

                # build prefix
                prefix += letter

                # if root found stop (shortest root)
                if node.is_end:
                    break

            # if valid root found replace
            if prefix and node.is_end:
                res.append(prefix)

            # else keep original word
            else:
                res.append(word)

        # join words with space
        return " ".join(res)



# create trie object
trie = Trie()

# dictionary roots
dictionary = ["cat", "bat", "rat"]

# input sentence
sentence = "the cattle was rattled by the battery"

# insert dictionary into trie
for word in dictionary:
    trie.insert(word)

# run replacement
print(trie.replace_words(sentence, trie.root))



# =========================
# DRY RUN
# =========================
#
# Trie built:
#
# root
#  ├ c → a → t*
#  ├ b → a → t*
#  └ r → a → t*
#
#
# sentence:
# "the cattle was rattled by the battery"
#
#
# word = "the"
# t not in root
# append "the"
#
# res = ["the"]
#
#
# word = "cattle"
#
# c -> exists
# a -> exists
# t -> exists + is_end True
#
# prefix = "cat"
#
# res = ["the","cat"]
#
#
# word = "was"
# w not in trie
#
# res = ["the","cat","was"]
#
#
# word = "rattled"
#
# r -> exists
# a -> exists
# t -> exists + is_end True
#
# prefix = "rat"
#
# res = ["the","cat","was","rat"]
#
#
# word = "by"
# b -> exists
# y not in children
#
# no full root
#
# res = ["the","cat","was","rat","by"]
#
#
# word = "the"
# no root
#
# res = ["the","cat","was","rat","by","the"]
#
#
# word = "battery"
#
# b -> exists
# a -> exists
# t -> exists + is_end True
#
# prefix = "bat"
#
# res = ["the","cat","was","rat","by","the","bat"]
#
#
# final:
#
# "the cat was rat by the bat"