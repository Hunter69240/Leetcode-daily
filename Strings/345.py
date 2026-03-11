s = "leetcode"

s = list(s)

vowels = set('aeiouAEIOU')
i = 0
j = len(s) - 1

# ---------------------------------------------------------
# EXPLANATION:
# This code reverses ONLY the vowels in the string.
#
# Two-pointer approach:
# - i moves from left to right
# - j moves from right to left
#
# Rules:
# - Move i forward until a vowel is found
# - Move j backward until a vowel is found
# - If i < j, swap the vowels
# - Continue until pointers cross
#
# If there are NO vowels, the string remains unchanged.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = ".,"
# s = ['.', ',']
#
# vowels = {a,e,i,o,u,A,E,I,O,U}
#
# Initial:
# i = 0 → s[i] = '.' → not a vowel → i++
# i = 1 → i < len(s)-1 is FALSE → stop
#
# j = 1 → s[j] = ',' → not a vowel → j--
# j = 0 → s[j] = '.' → not a vowel → j--
# j = -1 → stop
#
# Now:
# i = 1, j = -1
#
# i < j → FALSE
# break loop
#
# No swaps happened because there are no vowels.
#
# FINAL STRING:
# ".,"
# ---------------------------------------------------------

while i <= j:
    while i < len(s) - 1 and s[i] not in vowels:
        i += 1

    while j > -1 and s[j] not in vowels:
        j -= 1

    if i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    else:
        break

print("".join(s))
