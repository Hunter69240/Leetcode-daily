s = "abcd"

hash = {}
left = set()
res = 0

# ----------------------------------------------------------
# EXPLANATION (in comments):
# hash  = counts of characters to the RIGHT of current index
# left  = set of characters seen so far (on the LEFT)
#
# After moving each character from hash → left:
#   if number of unique chars on left == number of unique chars on right,
#   then we increment res.
#
# This is checking how many "good splits" exist.
# ----------------------------------------------------------

# ----------------------------------------------------------
# FIRST LOOP: BUILD FREQUENCY MAP OF ALL CHARACTERS
#
# s = "abcd"
#
# After loop:
# hash = {
#   'a': 1,
#   'b': 1,
#   'c': 1,
#   'd': 1
# }
# ----------------------------------------------------------

for i in s:
    hash[i] = hash.get(i, 0) + 1

print(hash)

# ----------------------------------------------------------
# SECOND LOOP: MOVE CHARACTERS FROM RIGHT SIDE → LEFT SIDE
# And check if unique count of left == unique count of right.
#
# Initially:
#   left = {}
#   hash = {'a':1,'b':1,'c':1,'d':1}
#   res = 0
# ----------------------------------------------------------

for i in s:
    # Remove one occurrence from right side
    hash[i] -= 1

    # Add to left side
    left.add(i)

    # If this character count on right becomes 0, remove it
    if hash[i] == 0:
        del hash[i]

    # ------------------------------------------------------
    # DRY RUN:
    #
    # i = 'a':
    #   hash['a'] → 0 → remove 'a'
    #   hash becomes {'b':1,'c':1,'d':1}
    #   left = {'a'}
    #   len(left)=1, len(hash)=3 → not equal
    #
    # i = 'b':
    #   hash['b'] → 0 → remove 'b'
    #   hash becomes {'c':1,'d':1}
    #   left = {'a','b'}
    #   len(left)=2, len(hash)=2 → EQUAL → res=1
    #
    # i = 'c':
    #   hash['c'] → 0 → remove 'c'
    #   hash becomes {'d':1}
    #   left = {'a','b','c'}
    #   len(left)=3, len(hash)=1 → not equal
    #
    # i = 'd':
    #   hash['d'] → 0 → remove 'd'
    #   hash becomes {}
    #   left = {'a','b','c','d'}
    #   len(left)=4, len(hash)=0 → not equal
    #
    # FINAL res = 1
    # ------------------------------------------------------

    if len(left) == len(hash):
        res += 1

print(res)
