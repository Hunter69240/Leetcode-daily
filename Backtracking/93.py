# ============================================================
# PROBLEM: Restore IP Addresses (LC 93)
# Given s="25525511135", return all valid IPs by inserting 3 dots
#
# APPROACH: Backtracking
# WHY backtracking: need ALL valid IPs, build segment by segment,
#                   invalid segments must be abandoned and undone
#
# KEY IDEA: at each step try taking 1, 2, or 3 digits as next segment
#           recurse with remaining string, undo if path is invalid
# ============================================================

s = "25525511135"
res = []          # stores all valid IP addresses found


def backtracking(index, current):
    # ----------------------------------------------------------
    # WHAT:  the recursive backtracking function
    # PARAMS:
    #   index   → current position in string s
    #             tells us how many characters we've consumed so far
    #             e.g. index=3 means first 3 chars already used
    #   current → list of segments built so far
    #             e.g. ["255", "25"] means 2 segments placed
    # ----------------------------------------------------------

    # ── BASE CASE ─────────────────────────────────────────────
    # WHAT:  check if we have a complete valid IP
    # WHY:   two conditions MUST both be true together:
    #
    #   len(current)==4 → we have all 4 segments
    #                     (3 dots placed between them)
    #   index==len(s)   → we've used EVERY character in s
    #                     no leftover digits, no unused digits
    #
    # WHY both together:
    #   4 segments but index < len(s) → digits left over  → invalid
    #   4 segments but index > len(s) → impossible (caught by break)
    #   index==len(s) but < 4 segs   → not enough segments → invalid
    #
    # ".".join(current) converts ["255","255","11","135"]
    #                         to "255.255.11.135"
    #
    # DRY RUN:
    #   current=["255","255","11","135"], index=11, len(s)=11
    #   len=4 AND index==11 → SAVE "255.255.11.135" ✓
    #
    #   current=["255","255","1","1"], index=8, len(s)=11
    #   len=4 BUT index!=11 → digits "135" left over → don't save
    if len(current) == 4 and index == len(s):
        res.append(".".join(current))
        return                        # stop going deeper, path complete

    # ── CHOICE LOOP ───────────────────────────────────────────
    # WHAT:  try taking 1, 2, or 3 digits as the next segment
    # WHY:   valid IP segments are 0-255, max 3 digits
    #        so we never need to try 4+ digits
    #
    # DRY RUN (index=6, s="25525511135"):
    #   length=1 → try s[6:7]  = "1"
    #   length=2 → try s[6:8]  = "11"
    #   length=3 → try s[6:9]  = "111"
    for length in range(1, 4):

        # ── OUT OF BOUNDS CHECK → break ───────────────────────
        # WHAT:  stop if taking `length` chars goes past end of s
        # WHY:   s[index:index+length] would give empty or partial
        #        string — not a valid segment
        #
        # WHY break not continue:
        #   if length=2 already goes out of bounds,
        #   length=3 will DEFINITELY go out of bounds too
        #   no point trying larger lengths → break entire loop
        #
        # DRY RUN:
        #   index=10, len(s)=11
        #   length=1 → 10+1=11 → not > 11 → OK, proceed
        #   length=2 → 10+2=12 → 12 > 11  → BREAK
        if index + length > len(s):
            break

        # ── EXTRACT SEGMENT ───────────────────────────────────
        # WHAT:  slice `length` characters from current position
        # WHY:   this is our candidate for the next IP segment
        #
        # DRY RUN:
        #   index=0, length=3 → segment = s[0:3] = "255"
        #   index=3, length=2 → segment = s[3:5] = "25"
        segment = s[index:index + length]

        # ── INVALID SEGMENT CHECK → continue ──────────────────
        # WHAT:  skip this segment if it violates IP rules
        # WHY:   two things make a segment invalid:
        #
        #   int(segment) > 255
        #     → segment out of valid IP range (0-255)
        #     → e.g. "312" → 312 > 255 → invalid
        #
        #   segment != str(int(segment))
        #     → catches LEADING ZEROS
        #     → "01" → int=1 → str="1" → "01"!="1" → invalid
        #     → "0"  → int=0 → str="0" → "0"=="0"  → valid
        #     → "255"→ int=255→str="255"→ equal     → valid
        #
        # WHY continue not break:
        #   if length=3 gives invalid segment "312",
        #   length=1 "3" or length=2 "31" might still be valid
        #   so skip just THIS length, keep trying others
        #
        # DRY RUN:
        #   segment="01" → int=1 → str="1" → "01"!="1" → SKIP
        #   segment="312"→ 312>255           → SKIP
        #   segment="255"→ 255<=255, "255"=="255" → VALID, proceed
        if segment and (int(segment) > 255 or segment != str(int(segment))):
            continue

        # ── MAKE CHOICE ───────────────────────────────────────
        # WHAT:  commit to this segment by adding it to current
        # WHY:   we've validated it, now explore all paths
        #        that start with this segment
        #
        # DRY RUN:
        #   current=["255"], segment="255" → current=["255","255"]
        current.append(segment)

        # ── RECURSE ───────────────────────────────────────────
        # WHAT:  move to the next position and fill next segment
        # WHY:   index+length advances past the chars we just used
        #        e.g. used "255" (3 chars) at index=0 → next index=3
        #
        # DRY RUN:
        #   current=["255","255"], index=6
        #   backtracking(6+2=8, ["255","255","11"]) for segment="11"
        backtracking(index + length, current)

        # ── UNDO (BACKTRACK) ──────────────────────────────────
        # WHAT:  remove the last segment we added
        # WHY:   THIS is the backtracking step
        #        after exploring ALL paths that use this segment,
        #        remove it so we can try the next length in the loop
        #        restores current to exactly what it was before append
        #
        # DRY RUN:
        #   after exploring everything with ["255","255","11",...] →
        #   pop "11" → current=["255","255"] again
        #   loop continues with length=3 → tries "111" next
        current.pop()


# ── INITIAL CALL ──────────────────────────────────────────────
# WHAT:  kick off recursion from position 0 with empty segments
# WHY:   start fresh — no segments placed, no chars consumed yet
backtracking(0, [])

# ── OUTPUT ────────────────────────────────────────────────────
# EXPECTED: ["255.255.11.135", "255.255.111.35"]
print(res)