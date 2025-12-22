# s = "the sky is blue"
s = "a good   example"

# Remove leading and trailing spaces
s = s.strip()

a = ""      # temporary string to build a word in reverse
res = ""    # final result string

# ---------------------------------------------------------
# EXPLANATION:
# This code reverses the order of words in a string.
#
# Rules:
# - Extra spaces between words should be ignored
# - Words should appear in reverse order
# - Only one space between words in the result
#
# Approach:
# - Traverse the string from RIGHT to LEFT
# - Build each word character by character in `a`
# - When a space is found:
#     - if `a` is empty → skip (extra spaces)
#     - else → reverse `a` and append to result
# - After loop, append the last word
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = "a good   example"
# after strip → "a good   example"
#
# Start from right:
#
# i points to 'e' → a="e"
# i points to 'l' → a="el"
# i points to 'p' → a="elp"
# i points to 'm' → a="elpm"
# i points to 'a' → a="elpma"
# i points to 'x' → a="elpmax"
# i points to 'e' → a="elpmaxe"
#
# i points to ' ' (space):
#   a != "" → append " example"
#   res = " example"
#   reset a=""
#
# skip extra spaces
#
# next letters:
# i points to 'd' → a="d"
# i points to 'o' → a="do"
# i points to 'o' → a="doo"
# i points to 'g' → a="doog"
#
# space found:
#   append " good"
#   res = " example good"
#   reset a=""
#
# next letter:
# i points to 'a' → a="a"
#
# loop ends
#
# append last word:
# res = " example good a"
#
# strip leading space:
# FINAL RESULT = "example good a"
# ---------------------------------------------------------

for i in range(len(s) - 1, -1, -1):
    if s[i] == " ":
        if a == "":
            continue
        res += " "
        res += a[::-1]
        a = ""
        continue
    a += s[i]

# append the last word
res += " "
res += a[::-1]

# remove leading space
res = res.strip()

print(res)
