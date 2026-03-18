# ============================================================
# PROBLEM: Combinations (LC 77)
# Given n=4, k=2 → find all combinations of k numbers from [1..n]
# APPROACH: Backtracking — build combination slot by slot,
#           undo choices to explore all valid paths
# ============================================================

res = []   # stores all valid combinations found
k = 2      # how many numbers each combination must have
n = 4      # pick numbers from range [1..n]


def backtracking(current, start, k, n):
    # ----------------------------------------------------------
    # WHAT:  the recursive backtracking function
    # WHY:   builds one combination incrementally, slot by slot
    # PARAMS:
    #   current → the combination being built right now  e.g. [1, 3]
    #   start   → the smallest number we're allowed to pick next
    #             (always > last picked, so we never go backwards)
    #             WHY: prevents [1,2] and [2,1] both appearing
    #   k       → target length of each combination
    #   n       → upper bound of the number range
    # ----------------------------------------------------------

    # ── BASE CASE ─────────────────────────────────────────────
    # WHAT:  check if current combination is complete
    # WHY:   when we've picked exactly k numbers, we have one
    #        valid combination — save it and stop going deeper
    # NOTE:  current[:] is a COPY — if we append current directly,
    #        it will change later when we pop (same object in memory)
    #
    # DRY RUN:
    #   call: backtracking([1,2], 3, 2, 4)
    #   len([1,2]) == 2 == k  → save [1,2] to res, return
    if len(current) == k:
        res.append(current[:])
        return

    # ── CHOICE LOOP ───────────────────────────────────────────
    # WHAT:  loop over every number we're still allowed to pick
    # WHY:   at each slot, we try each candidate and recurse
    # NOTE:  starts at `start`, not 1 — ensures we only pick
    #        numbers greater than the last one picked
    #        e.g. if we picked 2, next loop starts at 3
    #
    # DRY RUN (first call):
    #   backtracking([], 1, 2, 4)
    #   loop: i = 1, 2, 3, 4
    for i in range(start, n + 1):

        # ── PRUNING ───────────────────────────────────────────
        # WHAT:  early exit when it's impossible to complete
        #        the combination from this point forward
        # WHY:   saves time by not exploring dead-end branches
        #
        # CONDITION EXPLAINED:
        #   numbers still available = n - i + 1
        #     (from i to n inclusive, how many numbers are left)
        #   slots still needed      = k - len(current)
        #     (how many more numbers we must still pick)
        #   if available < needed → impossible → stop the loop
        #
        # WHY break and not continue?
        #   if i=4 doesn't have enough numbers, i=5,6... won't either
        #   so we break the whole loop, not just skip this i
        #
        # DRY RUN:
        #   current=[1], i=4, n=4, k=2
        #   available = 4 - 4 + 1 = 1
        #   needed    = 2 - 1     = 1
        #   1 < 1 → FALSE → don't prune, continue normally
        #
        #   current=[], i=4, n=4, k=2
        #   available = 4 - 4 + 1 = 1
        #   needed    = 2 - 0     = 2
        #   1 < 2 → TRUE → break, no point trying 4 as first pick
        if n - i + 1 < k - len(current):
            break

        # ── MAKE CHOICE ───────────────────────────────────────
        # WHAT:  add number i to the current combination
        # WHY:   we're committing to this choice and going deeper
        #
        # DRY RUN:
        #   current=[], i=1 → current becomes [1]
        current.append(i)

        # ── RECURSE ───────────────────────────────────────────
        # WHAT:  go deeper to fill the next slot
        # WHY:   we've picked i, now pick the next number
        # NOTE:  pass i+1 as start — next number must be > i
        #        (ensures strictly increasing order → no duplicates)
        #
        # DRY RUN:
        #   current=[1] → backtracking([1], 2, 2, 4)
        #     inside that call, loop i=2,3,4:
        #       i=2 → append 2 → backtracking([1,2], 3, 2, 4) → SAVE [1,2]
        #       i=3 → append 3 → backtracking([1,3], 4, 2, 4) → SAVE [1,3]
        #       i=4 → append 4 → backtracking([1,4], 5, 2, 4) → SAVE [1,4]
        backtracking(current, i + 1, k, n)

        # ── UNDO (BACKTRACK) ──────────────────────────────────
        # WHAT:  remove the last added number from current
        # WHY:   THIS is the actual backtracking step
        #        after exploring all paths that start with i,
        #        we remove i so we can try i+1 in the next iteration
        #        restores current to exactly what it was before append
        #
        # DRY RUN:
        #   after exploring everything starting with [1] →
        #   pop 1 → current=[] again → loop continues with i=2
        #   after exploring everything starting with [2] →
        #   pop 2 → current=[] again → loop continues with i=3
        current.pop()


# ── INITIAL CALL ──────────────────────────────────────────────
# WHAT:  kick off the recursion
# WHY:   start with empty combination, first pick can be 1
backtracking([], 1, k, n)

# ── OUTPUT ────────────────────────────────────────────────────
# WHAT:  print final result
# EXPECTED for n=4, k=2:
#   [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
print(res)