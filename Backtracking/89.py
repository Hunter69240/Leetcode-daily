# ============================================================
# PROBLEM: Gray Code (LC 89)
# Given n, return any valid n-bit gray code sequence of 2^n integers
# where every adjacent pair differs by exactly 1 bit
#
# APPROACH: Mirror Reflection
#   NOT backtracking — we just need ANY valid sequence, not ALL
#   Key insight: n-bit gray code = n-1 bit sequence
#                                + reversed n-1 bit sequence
#                                  with MSB set to 1
#   Each iteration doubles the list → final length = 2^n
# ============================================================

# ── BASE CASE ─────────────────────────────────────────────────
# WHAT:  start with the n=1 gray code sequence
# WHY:   [0, 1] is the simplest valid gray code —
#        0→1 differs by exactly 1 bit, and 1→0 also differs by 1 bit
#        every larger sequence is built on top of this
#
# DRY RUN (n=3):
#   res starts as [0, 1]
res = [0, 1]

n = 3  # build a 3-bit gray code → need 2^3 = 8 values

# ── MAIN LOOP ─────────────────────────────────────────────────
# WHAT:  iterate once per extra bit we need to add
# WHY:   we start with 1 bit ([0,1]), so we need n-1 more iterations
#        each iteration adds one more bit → doubles the list
# NOTE:  range(1, n) gives i = 1, 2, ..., n-1
#
# DRY RUN (n=3):
#   i=1 → builds the n=2 sequence (4 values)
#   i=2 → builds the n=3 sequence (8 values)
for i in range(1, n):

    # ── REFLECT ───────────────────────────────────────────────
    # WHAT:  create a reversed copy of the current res
    # WHY:   the second half of any gray code is always the
    #        first half in reverse order — this is the mirror
    #        reflection property that guarantees adjacent elements
    #        differ by exactly 1 bit at the boundary too
    # NOTE:  res[::-1] creates a NEW list, doesn't modify res
    #
    # DRY RUN:
    #   i=1: res=[0,1]     → reversed=[1,0]
    #   i=2: res=[0,1,3,2] → reversed=[2,3,1,0]
    reversed = res[::-1]

    # ── SET MSB ───────────────────────────────────────────────
    # WHAT:  add 2^i to every number in the reversed list
    # WHY:   this sets the i-th bit (MSB for this iteration) to 1
    #        for all numbers in the second half
    #        ensures second half numbers are distinct from first half
    #
    # HOW 1<<i works:
    #   i=1 → 1<<1 = 2  = 010 in binary  (sets bit position 1)
    #   i=2 → 1<<2 = 4  = 100 in binary  (sets bit position 2)
    #
    # DRY RUN:
    #   i=1: reversed=[1,0]     → each + 2 → [3,2]
    #        0+2=2(10), 1+2=3(11)  ← in binary, MSB set to 1
    #   i=2: reversed=[2,3,1,0] → each + 4 → [6,7,5,4]
    #        2+4=6(110), 3+4=7(111), 1+4=5(101), 0+4=4(100)
    for j in range(len(reversed)):
        reversed[j] = reversed[j] + (1 << i)

    # ── EXTEND ────────────────────────────────────────────────
    # WHAT:  add all elements of reversed into res one by one
    # WHY:   we want to flatten the new numbers INTO res
    #        extend() adds each element individually
    #        append() would add the whole list as one element → wrong
    #
    # DRY RUN:
    #   i=1: res=[0,1]      extend [3,2]     → res=[0,1,3,2]
    #   i=2: res=[0,1,3,2]  extend [6,7,5,4] → res=[0,1,3,2,6,7,5,4]
    res.extend(reversed)

# ── OUTPUT ────────────────────────────────────────────────────
# WHAT:  print the final gray code sequence
# EXPECTED for n=3:
#   [0, 1, 3, 2, 6, 7, 5, 4]
#
# VERIFY adjacents differ by 1 bit:
#   0(000)↔1(001) ✓   1(001)↔3(011) ✓   3(011)↔2(010) ✓
#   2(010)↔6(110) ✓   6(110)↔7(111) ✓   7(111)↔5(101) ✓
#   5(101)↔4(100) ✓   4(100)↔0(000) ✓  (last↔first also valid)
print(res)