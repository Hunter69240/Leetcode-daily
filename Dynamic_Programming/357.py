# Problem: Count all numbers with unique digits in range [0, 10^n)
# Approach: Combinatorics (not backtracking)
# For a k-digit number:
#   - 1st digit: 9 choices (1-9, no leading zero)
#   - 2nd digit: 9 choices (0-9 except 1st digit)
#   - 3rd digit: 8 choices, 4th: 7 choices, ...
# Formula per length k: 9 * 9 * 8 * 7 * ... * (11-k)
# Final answer = 1 (for 0) + 10 (k=1) + sum of above for k=2..n

# DRY RUN for n=3:
# --------------------------------------------------
# n=3, so we count numbers in [0, 1000)
#
# res=10         → covers k=0 (just "0") and k=1 (1-9), total 10 numbers
# uniq_digits=9  → will hold "9 * product so far" for current k
# available=9    → digits still choosable for next position
#
# i=2:
#   uniq_digits = 9 * 9 = 81   → 2-digit unique numbers (10..99)
#   res         = 10 + 81 = 91
#   available   = 9 - 1 = 8
#
# i=3:
#   uniq_digits = 81 * 8 = 648  → 3-digit unique numbers (100..999)
#   res         = 91 + 648 = 739
#   available   = 8 - 1 = 7
#
# loop ends (range(2,4) exhausted)
# return 739  ✓
# --------------------------------------------------

def a():
    n = 3

    if n == 0:
        return 1            # only "0" exists in [0, 10^0) = [0, 1)

    res = 10                # k=1: digits 0-9 are all unique → 10 numbers
    uniq_digits = 9         # 1st digit of any multi-digit number: 9 choices (1-9)
    available = 9           # after fixing 1st digit, 9 digits remain for 2nd slot

    for i in range(2, n + 1):
        uniq_digits *= available   # multiply in choices for this new position
        res += uniq_digits         # add count of k-digit unique numbers to total
        available -= 1             # one more digit is now "used up" for next position

    return res

print(a())   # 739