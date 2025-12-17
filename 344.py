#2 SOLUTIONS

s = ["h", "e", "l", "l", "o"]

i = 0
j = len(s) - 1

# ---------------------------------------------------------
# EXPLANATION:
# We reverse the list in-place using two pointers.
#
# i starts from the beginning of the list.
# j starts from the end of the list.
#
# In each step:
#   - swap s[i] and s[j]
#   - move i forward
#   - move j backward
#
# Loop stops when i >= j.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# Initial:
# s = ["h", "e", "l", "l", "o"]
# i = 0, j = 4
#
# Step 1:
#   swap s[0] and s[4] → "h" ↔ "o"
#   s = ["o", "e", "l", "l", "h"]
#   i = 1, j = 3
#
# Step 2:
#   swap s[1] and s[3] → "e" ↔ "l"
#   s = ["o", "l", "l", "e", "h"]
#   i = 2, j = 2
#
# Loop ends (i == j).
#
# FINAL RESULT:
# s = ["o", "l", "l", "e", "h"]
# ---------------------------------------------------------

while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1

print(s)


r=[]
while s:
    r.append(s.pop())
print(r)
s = r
print(s)