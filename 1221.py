s = "LLLLRRRR"

res = 0
lcount = 0

# ---------------------------------------------------------------
# EXPLANATION:
# lcount tracks balance:
#   L → +1
#   R → -1
#
# When lcount becomes 0, we found a balanced substring.
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# DRY RUN for s = "LLLLRRRR"
#
# Start: res=0, lcount=0
#
# i='L' → lcount=1
# i='L' → lcount=2
# i='L' → lcount=3
# i='L' → lcount=4       (still not zero)
#
# i='R' → lcount=3
# i='R' → lcount=2
# i='R' → lcount=1
# i='R' → lcount=0  → balanced substring found
#                    res = 1
#
# END OF LOOP
# FINAL RESULT: res = 1
# ---------------------------------------------------------------

for i in s:
    if i == "R":
        lcount -= 1
    else:
        lcount += 1

    if lcount == 0:
        res += 1
        lcount = 0

print(res)
