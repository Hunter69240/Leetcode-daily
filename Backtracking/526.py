
class Solution:
    def countArrangement(self, n: int) -> int:
        
        # ------------------------------------------------------------
        # 🔹 WHAT IS THE SUM / PROBLEM ABOUT?
        # ------------------------------------------------------------
        # We are counting the number of "beautiful arrangements".
        #
        # A beautiful arrangement is a permutation of numbers from 1 to n
        # such that for every position `index` (1-based):
        #
        #    number % index == 0  OR  index % number == 0
        #
        # So instead of summing numbers, we are "counting valid permutations".
        #
        # 👉 This is a COUNTING problem over permutations with constraints.
        
        
        # ------------------------------------------------------------
        # 🔹 WHAT TYPE OF PROBLEM IS THIS?
        # ------------------------------------------------------------
        # This is a BACKTRACKING problem.
        #
        # Let’s verify using the 3 key questions:
        #
        # 1. Does it ask for ALL solutions?
        #    ✅ Yes → we must count ALL valid permutations
        #
        # 2. Do we build the answer piece by piece?
        #    ✅ Yes → we fill positions one by one (index = 1 → n)
        #
        # 3. Can a partial solution become invalid mid-way?
        #    ✅ Yes → if condition fails, we abandon and backtrack
        #
        # 👉 Hence: BACKTRACKING
        
        
        # ------------------------------------------------------------
        # 🔹 VARIABLES INITIALIZATION
        # ------------------------------------------------------------
        
        visited = set()
        # Keeps track of numbers already used in the permutation
        # Ensures each number is used only once
        
        count = 0
        # Stores total number of valid arrangements found
        
        
        # ------------------------------------------------------------
        # 🔹 BACKTRACKING FUNCTION
        # ------------------------------------------------------------
        
        def backtracking(index):
            nonlocal count
            # Allows us to modify 'count' defined in outer function
            
            
            # --------------------------------------------------------
            # 🔹 BASE CASE
            # --------------------------------------------------------
            if index > n:
                # If we placed numbers in all positions successfully
                # → we found a valid arrangement
                
                count += 1
                return
            
            
            # --------------------------------------------------------
            # 🔹 TRY ALL POSSIBLE CHOICES
            # --------------------------------------------------------
            for i in range(1, n + 1):
                # Try placing number i at position 'index'
                
                
                # ----------------------------------------------------
                # 🔹 VALIDATION CHECK
                # ----------------------------------------------------
                if i in visited:
                    # Skip if number already used
                    continue
                
                if not (i % index == 0 or index % i == 0):
                    # Skip if it doesn't satisfy beautiful condition
                    continue
                
                
                # ----------------------------------------------------
                # 🔹 CHOOSE
                # ----------------------------------------------------
                visited.add(i)
                # Mark number i as used
                
                
                # ----------------------------------------------------
                # 🔹 EXPLORE
                # ----------------------------------------------------
                backtracking(index + 1)
                # Move to next position
                
                
                # ----------------------------------------------------
                # 🔹 UNDO (BACKTRACK)
                # ----------------------------------------------------
                visited.remove(i)
                # Remove i so we can try other possibilities
            
        
        # Start filling from position 1
        backtracking(1)
        
        return count



# ------------------------------------------------------------
# 🔹 DRY RUN (n = 2)
# ------------------------------------------------------------

# Initial:
# n = 2
# visited = {}
# count = 0

# CALL: backtracking(1)

# index = 1
# Try i = 1:
#   visited = {}
#   1 not in visited ✔
#   condition: 1%1==0 ✔
#   → choose 1
#   visited = {1}
#
#   CALL: backtracking(2)
#
#   index = 2
#   Try i = 1:
#       already in visited ❌ skip
#
#   Try i = 2:
#       2 not in visited ✔
#       condition: 2%2==0 ✔
#       → choose 2
#       visited = {1,2}
#
#       CALL: backtracking(3)
#
#       index = 3 > n
#       → valid arrangement found
#       count = 1
#
#       BACKTRACK:
#       visited = {1}
#
#   END LOOP
#
#   BACKTRACK:
#   visited = {}

# Try i = 2:
#   visited = {}
#   2 not in visited ✔
#   condition: 2%1==0 ✔
#   → choose 2
#   visited = {2}
#
#   CALL: backtracking(2)
#
#   index = 2
#   Try i = 1:
#       1 not in visited ✔
#       condition: 2%1==0 ✔
#       → choose 1
#       visited = {2,1}
#
#       CALL: backtracking(3)
#
#       index = 3 > n
#       → valid arrangement found
#       count = 2
#
#       BACKTRACK:
#       visited = {2}
#
#   Try i = 2:
#       already used ❌
#
#   BACKTRACK:
#   visited = {}

# FINAL:
# count = 2

# ------------------------------------------------------------
# ✅ FINAL ANSWER = 2
# ------------------------------------------------------------

