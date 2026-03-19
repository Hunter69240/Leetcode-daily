# This program solves the "Combination Sum III" problem
# Goal:
# Find all possible combinations of k numbers (1–9) that add up to n
# Each number can be used only once

res = []  # Global list to store all valid combinations

def backtracking(current, curr_sum, index, k, n):
    """
    current   -> current combination being built
    curr_sum  -> sum of elements in current
    index     -> next number to pick (to avoid reuse)
    k         -> required number of elements
    n         -> target sum
    """

    # ✅ BASE CASE:
    # If we have exactly k numbers AND sum equals target
    if len(current) == k and curr_sum == n:
        res.append(current[:])  # append a COPY of current list
        # Why copy? Because current will change during backtracking

    # 🔁 LOOP: try all numbers from 'index' to 9
    for i in range(index, 10):

        # Add current number to sum
        curr_sum += i

        # ❌ PRUNING:
        # If sum exceeds target, no need to continue further
        # because numbers are increasing (i → 9)
        if curr_sum > n:
            break

        # Choose the number
        current.append(i)

        # Recurse with:
        # - updated sum
        # - next index (i+1 ensures no reuse)
        backtracking(current, curr_sum, i + 1, k, n)

        # 🔙 BACKTRACK:
        # Remove last element and restore sum
        current.pop()
        curr_sum -= i

    return res  # return final result


# Input
k = 3
n = 7

# Call function
print(backtracking([], 0, 1, k, n))


"""
==================== DRY RUN ====================

k = 3, n = 7

Start:
current = [], curr_sum = 0, index = 1

------------------------------------------------
i = 1
current = [1], sum = 1

    i = 2
    current = [1,2], sum = 3

        i = 3
        current = [1,2,3], sum = 6  ❌ len=3 but sum!=7

        i = 4
        current = [1,2,4], sum = 7  ✅ VALID
        res = [[1,2,4]]

        i = 5 → sum = 8 ❌ break

    backtrack → current = [1]

    i = 3
    current = [1,3], sum = 4

        i = 4
        current = [1,3,4], sum = 8 ❌ break

    backtrack

    i = 4
    current = [1,4], sum = 5

        i = 5 → sum = 10 ❌ break

    backtrack

------------------------------------------------
i = 2
current = [2], sum = 2

    i = 3
    current = [2,3], sum = 5

        i = 4
        current = [2,3,4], sum = 9 ❌ break

    backtrack

------------------------------------------------
i = 3
current = [3], sum = 3

    i = 4
    current = [3,4], sum = 7

        i = 5 → sum = 12 ❌ break

    backtrack

------------------------------------------------

FINAL OUTPUT:
[[1,2,4]]

================================================
"""


# ------------------ COMPLEXITY ------------------

# Time Complexity:
# Roughly O(C(9, k)) → combinations of choosing k numbers from 1–9

# Space Complexity:
# O(k) recursion stack + O(result size)