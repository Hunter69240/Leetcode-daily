# Given a list of words, the goal is to group **anagrams** together.
# An anagram is a word formed by rearranging the letters of another word.
# Example: "eat", "tea", "ate" are all anagrams.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}  
# 'groups' will map:
#   sorted letters of a word  --->  list of words that match those letters
# Example final form:
#   { "aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"] }

for word in strs:
    # Sort the letters of the word to form a key.
    # All anagrams have the same sorted form.
    # Example: "eat" -> "aet", "tea" -> "aet"
    key = "".join(sorted(word))

    # Insert the word into the dictionary under its sorted key.
    # setdefault(key, []) means:
    # - If key doesn't exist, create key with empty list.
    # - Then append the current word.
    groups.setdefault(key, []).append(word)

    # --- DRY RUN ---
    # Iteration 1: word = "eat"
    #   key = "aet"
    #   groups = {"aet": ["eat"]}
    #
    # Iteration 2: word = "tea"
    #   key = "aet"
    #   groups = {"aet": ["eat", "tea"]}
    #
    # Iteration 3: word = "tan"
    #   key = "ant"
    #   groups = {"aet": ["eat", "tea"], "ant": ["tan"]}
    #
    # Iteration 4: word = "ate"
    #   key = "aet"
    #   groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan"]}
    #
    # Iteration 5: word = "nat"
    #   key = "ant"
    #   groups = {"aet": ["eat", "tea", "ate"], "ant": ["tan", "nat"]}
    #
    # Iteration 6: word = "bat"
    #   key = "abt"
    #   groups = {"aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]}

# Convert only the grouped lists (dictionary values) into the final output format.
result = list(groups.values())

# result will be:
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]
print(result)
