nums = [4, 6, 7, 7]
res = []

# ------------------------------------------------------------
# 🔹 WHAT IS THE SUM / PROBLEM ABOUT?
# ------------------------------------------------------------
# We are finding all increasing subsequences of length ≥ 2.
#
# A subsequence:
# - Does NOT need to be contiguous
# - Must maintain original order
#
# Condition:
# - Sequence must be NON-DECREASING (nums[i] >= previous element)
#
# So this is NOT a numerical sum problem,
# but a problem where we COLLECT all valid subsequences.


# ------------------------------------------------------------
# 🔹 WHAT TYPE OF PROBLEM IS THIS?
# ------------------------------------------------------------
# This is a BACKTRACKING problem.
#
# Let’s verify using the 3 key questions:
#
# 1. Does it ask for ALL solutions?
#    ✅ Yes → we need ALL increasing subsequences
#
# 2. Do you build the answer piece by piece?
#    ✅ Yes → we keep adding elements to current sequence (cur)
#
# 3. Can a partial solution become invalid mid-way?
#    ✅ Yes → if next number < last element → invalid → skip
#
# 👉 Hence: BACKTRACKING


# ------------------------------------------------------------
# 🔹 BACKTRACKING FUNCTION
# ------------------------------------------------------------

def backtracking(cur, index):
    
    # --------------------------------------------------------
    # 🔹 BASE CASE (COLLECT ANSWER)
    # --------------------------------------------------------
    if len(cur) >= 2:
        # If current subsequence has length ≥ 2
        # → it's a valid answer
        
        res.append(cur[:])  
        # IMPORTANT: use copy (cur[:]) to avoid reference issues
    
    
    # --------------------------------------------------------
    # 🔹 LOCAL SET FOR DUPLICATE HANDLING
    # --------------------------------------------------------
    s = set()
    # Used to avoid duplicates at SAME recursion level
    # (important because nums has duplicate 7)


    # --------------------------------------------------------
    # 🔹 TRY ALL CHOICES FROM CURRENT INDEX
    # --------------------------------------------------------
    for i in range(index, len(nums)):
        
        # ----------------------------------------------------
        # 🔹 SKIP DUPLICATES (same level)
        # ----------------------------------------------------
        if nums[i] in s:
            # If already used in this level → skip
            continue
        
        
        # ----------------------------------------------------
        # 🔹 VALIDATION CHECK (increasing condition)
        # ----------------------------------------------------
        elif cur and nums[i] < cur[-1]:
            # If current number is smaller than last picked
            # → breaks non-decreasing condition → skip
            continue
        
        
        # ----------------------------------------------------
        # 🔹 CHOOSE
        # ----------------------------------------------------
        else:
            s.add(nums[i])
            # Mark as used in this level
            
            cur.append(nums[i])
            # Add element to current subsequence
            
            
            # ------------------------------------------------
            # 🔹 EXPLORE
            # ------------------------------------------------
            backtracking(cur, i + 1)
            # Move forward (subsequence → no reuse of same index)
            
            
            # ------------------------------------------------
            # 🔹 UNDO (BACKTRACK)
            # ------------------------------------------------
            cur.pop()
            # Remove last element to try next possibility


# Start recursion
backtracking([], 0)

print(res)



# ------------------------------------------------------------
# 🔹 DRY RUN (nums = [4,6,7,7])
# ------------------------------------------------------------

# Initial:
# cur = []
# index = 0
# res = []

# CALL backtracking([], 0)

# i = 0 → nums[0] = 4
# cur = [] → valid
# s = {4}
# cur = [4]

# CALL backtracking([4], 1)

# i = 1 → nums[1] = 6
# 6 >= 4 ✔
# cur = [4,6]
# res = [[4,6]]

# CALL backtracking([4,6], 2)

# i = 2 → nums[2] = 7
# 7 >= 6 ✔
# cur = [4,6,7]
# res = [[4,6], [4,6,7]]

# CALL backtracking([4,6,7], 3)

# i = 3 → nums[3] = 7
# 7 >= 7 ✔
# cur = [4,6,7,7]
# res = [[4,6], [4,6,7], [4,6,7,7]]

# BACKTRACK → cur = [4,6,7]

# BACKTRACK → cur = [4,6]

# i = 3 → nums[3] = 7
# allowed (new level set)
# cur = [4,6,7]
# res = [..., [4,6,7]] (duplicate avoided by set)

# BACKTRACK → cur = [4]

# i = 2 → nums[2] = 7
# cur = [4,7]
# res = [..., [4,7]]

# i = 3 → nums[3] = 7
# skipped due to set (duplicate at same level)

# BACKTRACK → cur = []

# i = 1 → nums[1] = 6
# cur = [6]
# continue similar...

# ------------------------------------------------------------
# ✅ FINAL OUTPUT:
# [
#   [4,6], [4,6,7], [4,6,7,7],
#   [4,7], [4,7,7],
#   [6,7], [6,7,7],
#   [7,7]
# ]
# ------------------------------------------------------------