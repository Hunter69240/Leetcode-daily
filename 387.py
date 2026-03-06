# Problem:
# Find the index of the FIRST non-repeating character in a string.
#
# Example:
# s = "leetcode"
#
# Characters:
# l e e t c o d e
# 0 1 2 3 4 5 6 7
#
# 'l' appears once → answer = 0
#
# Approach:
# We use a dictionary to store:
#
#     character → (count_of_character , first_index_where_it_appeared)
#
# Example dictionary entry:
#     'e' : (3,1)
#
# Meaning:
#     'e' appears 3 times
#     first seen at index 1
#
# Algorithm Steps:
#
# 1. Traverse the string once
#    → build the dictionary with character counts
#
# 2. Traverse the string again
#    → the first character with count = 1 is the answer
#
# If no such character exists → return -1


s="leetcode"

# dictionary to store:
# key   → character
# value → tuple (count , first_index)
d = {}


# FIRST PASS
# Purpose:
# Count how many times each character appears
# while remembering the first index it appeared

for i in range(len(s)):

    # If character seen for the first time
    if s[i] not in d:

        # store:
        # count = 1
        # first index = i
        d[s[i]] = (1, i)

    else:
        # character already seen
        # increase its count

        # get previous count
        count = d[s[i]][0] + 1

        # update tuple
        # keep the original first index
        d[s[i]] = (count, d[s[i]][1])


# Dry Run of FIRST LOOP
#
# s = "leetcode"
#
# Step 1
# i = 0
# s[i] = 'l'
#
# d = {'l':(1,0)}
#
#
# Step 2
# i = 1
# s[i] = 'e'
#
# d = {
#      'l':(1,0),
#      'e':(1,1)
#     }
#
#
# Step 3
# i = 2
# s[i] = 'e'
#
# previous count = 1
# new count = 2
#
# d = {
#      'l':(1,0),
#      'e':(2,1)
#     }
#
#
# Step 4
# i = 3
# s[i] = 't'
#
# d = {
#      'l':(1,0),
#      'e':(2,1),
#      't':(1,3)
#     }
#
#
# Step 5
# i = 4
# s[i] = 'c'
#
# d = {
#      'l':(1,0),
#      'e':(2,1),
#      't':(1,3),
#      'c':(1,4)
#     }
#
#
# Step 6
# i = 5
# s[i] = 'o'
#
# d = {
#      'l':(1,0),
#      'e':(2,1),
#      't':(1,3),
#      'c':(1,4),
#      'o':(1,5)
#     }
#
#
# Step 7
# i = 6
# s[i] = 'd'
#
# d = {
#      'l':(1,0),
#      'e':(2,1),
#      't':(1,3),
#      'c':(1,4),
#      'o':(1,5),
#      'd':(1,6)
#     }
#
#
# Step 8
# i = 7
# s[i] = 'e'
#
# previous count = 2
# new count = 3
#
# FINAL DICTIONARY:
#
# d = {
#      'l':(1,0),
#      'e':(3,1),
#      't':(1,3),
#      'c':(1,4),
#      'o':(1,5),
#      'd':(1,6)
#     }


# SECOND PASS
# Purpose:
# Find the FIRST character whose count == 1

for i in range(len(s)):

    # check count stored in dictionary
    if d[s[i]][0] == 1:

        # first unique character found
        print(i)

        # stop searching
        break


# If loop never breaks
# → no unique character exists
else:
    print(-1)


# Dry Run of SECOND LOOP
#
# i = 0
# s[i] = 'l'
#
# d['l'] = (1,0)
#
# count == 1 → TRUE
#
# print(0)
#
# loop stops


# Final Output
#
# 0


# Time Complexity
# O(n)
#
# first loop → O(n)
# second loop → O(n)


# Space Complexity
# O(k)
#
# k = number of unique characters stored in dictionary