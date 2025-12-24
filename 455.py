def s():
    g = [1, 2, 3]
    s = [1, 1]

    g.sort()
    s.sort()

    i = len(g) - 1
    j = len(s) - 1
    res = 0

    while i > -1 and j > -1:
        if s[j] >= g[i]:
            j -= 1
            res += 1
        i -= 1

    return res


a = s()
print(a)

# ---------------------------------------------------------
# EXPLANATION:
# This is the "Assign Cookies" problem.
#
# Each child has a greed factor g[i].
# Each cookie has a size s[j].
#
# A child is satisfied if:
#   cookie size >= greed factor
#
# We want to maximize the number of satisfied children.
#
# GREEDY STRATEGY:
# Always try to satisfy the GREEDIEST child first
# using the LARGEST available cookie.
#
# Why greedy works:
# - The greediest child is the hardest to satisfy.
# - If the largest cookie cannot satisfy this child,
#   no smaller cookie can.
# - If it CAN satisfy them, we should use it immediately
#   instead of wasting it on a less greedy child.
#
# TWO POINTER APPROACH:
# - i points to the child with the largest greed
# - j points to the largest cookie
#
# If the cookie satisfies the child:
#   - assign the cookie
#   - move both pointers
# Otherwise:
#   - skip the child (move i only)
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# Input:
# g = [1,2,3]
# s = [1,1]
#
# After sorting:
# g = [1,2,3]
# s = [1,1]
#
# i=2 (greed=3), j=1 (cookie=1)
# 1 < 3 → cannot satisfy
# → move i
#
# i=1 (greed=2), j=1 (cookie=1)
# 1 < 2 → cannot satisfy
# → move i
#
# i=0 (greed=1), j=1 (cookie=1)
# 1 >= 1 → satisfy
# res = 1
# move i and j
#
# Loop ends
#
# FINAL ANSWER:
# 1
# ---------------------------------------------------------
