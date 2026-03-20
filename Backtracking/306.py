# ============================================================
# PROBLEM: Additive Number (LC 306)
# Given a string of digits, return True if it forms an additive sequence
# where every number = sum of the previous two
#
# APPROACH: Backtracking (two phase)
# WHY backtracking: we try ALL possible (first, second) pairs
#                   and for each pair verify the rest is additive
#
# TWO PHASES:
#   Phase 1 → outer loops: try every possible first and second number
#   Phase 2 → check():     verify rest of string is forced by prev1+prev2
#                          NO choices here — next number is always fixed
# ============================================================


def isAdditiveNumber(s):

    # ----------------------------------------------------------
    # WHAT:  verify if s[index:] follows the additive rule
    #        given the last two numbers prev1 and prev2
    # WHY:   once first and second are fixed, every subsequent
    #        number is forced — must equal prev1 + prev2
    #        no loop needed, just check and recurse
    # PARAMS:
    #   index → current position in string s
    #           everything before index is already verified
    #   prev1 → second-to-last number in sequence (integer)
    #   prev2 → last number in sequence (integer)
    # ----------------------------------------------------------
    def check(index, prev1, prev2):

        # ── BASE CASE ─────────────────────────────────────────
        # WHAT:  we've consumed the entire string
        # WHY:   if index reaches end of s, every character has
        #        been matched to a valid additive number → True
        #
        # DRY RUN (s="112358"):
        #   check(6, 5, 8) → index=6 == len(s)=6 → return True
        if index == len(s):
            return True

        # ── COMPUTE EXPECTED NEXT NUMBER ──────────────────────
        # WHAT:  calculate what the next number MUST be
        # WHY:   additive rule says next = prev1 + prev2
        #        convert to string to compare against s[index:]
        #
        # DRY RUN:
        #   prev1=1, prev2=1 → expected=2, expected_str="2"
        #   prev1=1, prev2=2 → expected=3, expected_str="3"
        #   prev1=99,prev2=100→expected=199,expected_str="199"
        expected = prev1 + prev2
        expected_str = str(expected)

        # ── CHECK IF STRING MATCHES EXPECTED ──────────────────
        # WHAT:  verify s[index:] actually starts with expected_str
        # WHY:   if it doesn't, this (first, second) pair is wrong
        #        no point going deeper → return False immediately
        #
        # DRY RUN (s="112358", index=2):
        #   expected_str="2", s[2:]="2358"
        #   "2358".startswith("2") → True → continue
        #
        # DRY RUN (s="112358", index=3, prev1=1, prev2=12):
        #   expected_str="13", s[3:]="358"
        #   "358".startswith("13") → False → return False
        if not s[index:].startswith(expected_str):
            return False

        # ── LEADING ZERO CHECK FOR EXPECTED ───────────────────
        # WHAT:  reject if the expected number has a leading zero
        # WHY:   "013" is not a valid number in an additive sequence
        #        only way expected_str starts with "0" is if sum=0
        #        which only happens as "0" (length 1) — that's fine
        #        "00", "01" etc are invalid
        #
        # NOTE:  this situation is rare but must be handled
        #        e.g. prev1=0, prev2=0 → expected=0 → "0" is ok
        #             but if somehow we got "00" in string → invalid
        #
        # DRY RUN:
        #   expected_str="013" → starts with "0" AND len>1 → False
        #   expected_str="0"   → starts with "0" BUT len=1 → ok
        #   expected_str="123" → doesn't start with "0"    → ok
        if expected_str.startswith("0") and len(expected_str) > 1:
            return False

        # ── RECURSE ───────────────────────────────────────────
        # WHAT:  move forward in string and check next number
        # WHY:   we've confirmed current expected matches → go deeper
        #        new index  = index + len(expected_str)
        #                     (skip past the number we just matched)
        #        new prev1  = prev2
        #                     (slide window: old second becomes new first)
        #        new prev2  = expected
        #                     (the number we just matched becomes new second)
        #
        # WHY NO UNDO (pop):
        #   we're not modifying any list in place
        #   index, prev1, prev2 are just parameters
        #   when this call returns, params automatically revert
        #   nothing to manually undo
        #
        # DRY RUN (s="112358"):
        #   check(2,1,1) → expected=2 → check(3,1,2)
        #   check(3,1,2) → expected=3 → check(4,2,3)
        #   check(4,2,3) → expected=5 → check(5,3,5)
        #   check(5,3,5) → expected=8 → check(6,5,8)
        #   check(6,5,8) → index==len(s) → True
        return check(index + len(expected_str), prev2, expected)

    # ── PHASE 1: TRY ALL (first, second) PAIRS ────────────────
    # WHAT:  two nested loops to pick every possible first and second
    # WHY:   we don't know where first ends and second begins
    #        so we try every possible split point
    #
    # i = end index of first  → first  = s[0:i]
    # j = end index of second → second = s[i:j]
    # rest of string starts at j
    #
    # DRY RUN (s="112358"):
    #   i=1,j=2 → first="1",  second="1"   → check(2, 1, 1)  → True ✓
    #   i=1,j=3 → first="1",  second="12"  → check(3, 1, 12) → False
    #   i=2,j=3 → first="11", second="2"   → check(3,11, 2)  → False
    #   ...
    for i in range(1, len(s)):
        first = s[0:i]

        # ── LEADING ZERO CHECK FOR first ──────────────────────
        # WHAT:  skip if first has a leading zero
        # WHY:   "01", "012" etc are invalid numbers
        # WHY break (not continue):
        #   if first="01" is invalid, first="012","0123" also invalid
        #   making first longer won't fix it → break i loop entirely
        #
        # NOTE:  first="0" (length 1) is valid — only multi-digit
        #        numbers starting with 0 are invalid
        #
        # DRY RUN:
        #   s="10203", i=2 → first="10" → len>1, first[0]="1" → ok
        #   s="01203", i=2 → first="01" → len>1, first[0]="0" → BREAK
        if len(first) > 1 and first[0] == "0":
            break

        for j in range(i + 1, len(s)):
            second = s[i:j]

            # ── LEADING ZERO CHECK FOR second ─────────────────
            # WHAT:  skip if second has a leading zero
            # WHY:   same rule — "05", "023" are invalid
            # WHY break (not continue):
            #   if second="05" invalid, second="052" also invalid
            #   making second longer won't fix it → break j loop
            #   but outer i loop continues — different first might work
            #
            # DRY RUN:
            #   s="10203", i=1, j=3 → second="02" → BREAK j loop
            #   outer loop tries i=2 next
            if len(second) > 1 and second[0] == "0":
                break

            # ── KICK OFF THE CHECK ────────────────────────────
            # WHAT:  verify if rest of string s[j:] is additive
            #        given first and second as starting numbers
            # WHY:   if check returns True, we found a valid sequence
            #        return True immediately — no need to try more pairs
            #
            # int(first), int(second) → convert strings to integers
            #   so check() can do arithmetic (prev1 + prev2)
            #
            # DRY RUN (s="112358"):
            #   i=1,j=2 → check(2, int("1"), int("1"))
            #            = check(2, 1, 1) → True → return True
            if check(j, int(first), int(second)):
                return True

    # ── NO VALID SEQUENCE FOUND ───────────────────────────────
    # WHAT:  all (first, second) pairs tried, none worked
    # WHY:   if we get here, no valid additive split exists
    return False


# ── TEST CASES ────────────────────────────────────────────────
print(isAdditiveNumber("112358"))    # True  — 1,1,2,3,5,8
print(isAdditiveNumber("199100199")) # True  — 1,99,100,199
print(isAdditiveNumber("1023"))      # False — no valid split
print(isAdditiveNumber("000"))       # True  — 0,0,0