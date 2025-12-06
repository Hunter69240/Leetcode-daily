class Solution:
    def checkValidString(self, s: str) -> bool:
        # 🧩 PROBLEM TYPE:
        # We need to check whether a string made of '(', ')', and '*' can become a
        # valid parenthesis string. '*' can act as '(' or ')' or be empty.

        # 🧠 IDEA / INTUITION:
        # Instead of trying all replacements for '*', we track the RANGE of possible
        # open parentheses counts as we scan left → right.
        #
        # leftMin = minimum possible number of unmatched '(' so far
        # leftMax = maximum possible number of unmatched '(' so far
        #
        # '(' → must increase both
        # ')' → must decrease both
        # '*' → could be '(' OR ')' OR empty
        #       → decreases leftMin (if '*' becomes ')')
        #       → increases leftMax (if '*' becomes '(')

        leftMin, leftMax = 0, 0

        for c in s:
            if c == '(':
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ')':
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:  # '*'
                leftMin, leftMax = leftMin - 1, leftMax + 1

            # ❗ If leftMax becomes negative → even the maximum scenario has more ')'
            #    than '(' → impossible to ever fix → return False
            if leftMax < 0:
                return False

            # leftMin can NEVER be negative. If it goes below zero, clamp it to zero
            # because minimum possible unmatched '(' can't be less than 0.
            if leftMin < 0:
                leftMin = 0

        # ✔ At the end: if there is ANY interpretation that balances parentheses,
        # the minimum unmatched '(' (leftMin) must be 0.
        return leftMin == 0


"""
-------------------- 🔎 DRY RUN EXAMPLE --------------------

Example: s = "(*))"

Start: leftMin = 0, leftMax = 0

1) '('
   leftMin = 1, leftMax = 1
   range = [1, 1]

2) '*'
   leftMin = 1 - 1 = 0    (if '*' behaves as ')')
   leftMax = 1 + 1 = 2    (if '*' behaves as '(')
   range = [0, 2]

3) ')'
   leftMin = 0 - 1 = -1 → clamp to 0
   leftMax = 2 - 1 = 1
   range = [0, 1]

4) ')'
   leftMin = 0 - 1 = -1 → clamp to 0
   leftMax = 1 - 1 = 0
   range = [0, 0]

END → leftMin == 0 → valid string → return True

------------------------------------------------------------

Another example: s = "(*()"
Dry run:
Start range: [0, 0]

'('  → [1, 1]
'*'  → [0, 2]
'('  → [1, 3]
')'  → [0, 2]

End → leftMin == 0 → valid → return True

------------------------------------------------------------

Failure example: s = ")("
Start range: [0,0]

')' → [-1, -1] → leftMax < 0 → return False immediately

------------------------------------------------------------
"""
