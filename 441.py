import math

def s():
    # ---------------------------------------------------------
    # PROBLEM:
    # Given n coins, determine how many complete staircase
    # levels can be formed.
    #
    # Level 1 → 1 coin
    # Level 2 → 2 coins
    # Level 3 → 3 coins
    # ...
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # INPUT:
    # n = total number of coins
    # ---------------------------------------------------------
    n = 3

    # ---------------------------------------------------------
    # APPROACH 1: ITERATIVE (SIMULATION)
    #
    # We build the staircase level by level, keeping track
    # of how many coins are used so far.
    # ---------------------------------------------------------

    # level     → current level being formed
    # num_coins → total coins used so far
    level = 1
    num_coins = 1

    # ---------------------------------------------------------
    # STEP 1: KEEP ADDING LEVELS UNTIL COINS ARE INSUFFICIENT
    # ---------------------------------------------------------
    while n > num_coins:
        level += 1
        num_coins += level

    # ---------------------------------------------------------
    # STEP 2: FINAL CHECK
    #
    # If coins used exactly equals n,
    # return the current level.
    #
    # Otherwise, last level was incomplete,
    # so return level - 1.
    # ---------------------------------------------------------
    if num_coins == n:
        return level
    return level - 1


# ---------------------------------------------------------
# FUNCTION CALL
# ---------------------------------------------------------
a = s()
print(a)

# ---------------------------------------------------------
# DRY RUN (n = 3):
#
# Initial:
# n = 3
# level = 1
# num_coins = 1
#
# Loop:
# 3 > 1 → YES
# level = 2
# num_coins = 1 + 2 = 3
#
# Exit loop:
# num_coins == n
#
# Answer = 2
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(k) where k ≈ √n
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------


# =========================================================
# OR (MATHEMATICAL APPROACH)
# =========================================================

def s():
    # ---------------------------------------------------------
    # FORMULA-BASED APPROACH
    #
    # Total coins needed for k levels:
    # 1 + 2 + 3 + ... + k = k(k + 1) / 2
    #
    # We need:
    # k(k + 1) / 2 ≤ n
    #
    # Solve quadratic equation:
    # k² + k - 2n ≤ 0
    #
    # k = ( -1 + sqrt(1 + 8n) ) / 2
    #
    # We take the floor value.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # INPUT:
    # ---------------------------------------------------------
    n = 3

    # ---------------------------------------------------------
    # DIRECT COMPUTATION USING FORMULA
    # ---------------------------------------------------------
    return int((math.sqrt(1 + 8 * n) - 1) // 2)


# ---------------------------------------------------------
# FUNCTION CALL
# ---------------------------------------------------------
print(s())

# ---------------------------------------------------------
# DRY RUN (n = 3):
#
# sqrt(1 + 8*3) = sqrt(25) = 5
# (5 - 1) // 2 = 2
#
# Answer = 2
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ---------------------------------------------------------
