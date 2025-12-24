chars = ["a","a","b","b","c","c","c"]

i, j = 0, 0
count = 0

# ---------------------------------------------------------
# EXPLANATION:
# This is the "String Compression" problem.
#
# Goal:
# Compress the array IN-PLACE such that:
# - Consecutive repeating characters are replaced by:
#     character + count (if count > 1)
# - Return the new length (i)
#
# Two-pointer approach:
# - j → scans the array to count repeating characters
# - i → writes the compressed result back into chars
#
# Steps:
# 1) Use j to find a group of same characters
# 2) Calculate count = length of that group
# 3) Write the character to chars[i]
# 4) If count > 1, write each digit of count
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# chars = ["a","a","b","b","c","c","c"]
#
# Initial:
# i=0, j=0
#
# -------------------------
# GROUP 1: "a","a"
# start = 0
# j moves to 2
# count = 2
#
# chars[i] = 'a' → chars[0] = 'a'
# i = 1
#
# count > 1 → write "2"
# chars[1] = '2'
# i = 2
#
# chars now: ["a","2",...]
#
# -------------------------
# GROUP 2: "b","b"
# start = 2
# j moves to 4
# count = 2
#
# chars[2] = 'b'
# i = 3
#
# write "2"
# chars[3] = '2'
# i = 4
#
# chars now: ["a","2","b","2",...]
#
# -------------------------
# GROUP 3: "c","c","c"
# start = 4
# j moves to 7
# count = 3
#
# chars[4] = 'c'
# i = 5
#
# write "3"
# chars[5] = '3'
# i = 6
#
# chars now: ["a","2","b","2","c","3",...]
#
# j == len(chars) → stop
#
# FINAL:
# chars = ["a","2","b","2","c","3"]
# i = 6 (new length)
# ---------------------------------------------------------

while j < len(chars):
    start = j

    # count how many times the same character repeats
    while j < len(chars) and chars[j] == chars[start]:
        j += 1

    count = j - start

    # write the character
    chars[i] = chars[start]
    i += 1

    # write the count if greater than 1
    if count > 1:
        for digit in str(count):
            chars[i] = digit
            i += 1

print(chars, i)
