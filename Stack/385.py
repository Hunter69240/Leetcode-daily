class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = 0
        isnum = False
        sign = 1

        for ch in s:
            if ch == '[':
                stack.append(NestedInteger())

            elif ch == ']':
                if isnum:
                    num *= sign
                    stack[-1].add(NestedInteger(num))
                    num = 0
                    isnum = False
                    sign = 1

                ni = stack.pop()
                if stack:
                    stack[-1].add(ni)
                else:
                    return ni

            elif ch == ',':
                if isnum:
                    num *= sign
                    stack[-1].add(NestedInteger(num))
                    num = 0
                    isnum = False
                    sign = 1

            else:
                if ch.isdigit():
                    isnum = True
                    num = num * 10 + int(ch)
                else:
                    if ch == '-':
                        sign = -1


# ---------------------------------------------------------
# EXPLANATION:
# This code DESERIALIZES a string representation of a nested list
# into a NestedInteger structure.
#
# Examples:
# "324"        → NestedInteger(324)
# "[123,[456,[789]]]" → NestedInteger containing nested lists
#
# Core idea:
# - Use a STACK to manage nested structures
# - Build numbers digit by digit
# - When ']' is found, complete the current NestedInteger
# ---------------------------------------------------------

# ---------------------------------------------------------
# VARIABLES:
#
# stack → holds NestedInteger objects for each nesting level
# num   → builds multi-digit numbers
# isnum → tells whether we are currently building a number
# sign  → handles negative numbers
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW EACH CHARACTER IS HANDLED:
#
# '[' :
#   - Start a new NestedInteger
#   - Push it onto the stack
#
# digit:
#   - Build number (supports multi-digit numbers)
#
# '-' :
#   - Mark the number as negative
#
# ',' :
#   - End of a number → add it to current NestedInteger
#
# ']' :
#   - Finish last number if any
#   - Pop NestedInteger from stack
#   - Attach it to previous NestedInteger
#   - If stack becomes empty → this is the final result
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = "[123,[456,[789]]]"
#
# '[' → push new NI → stack=[[]]
#
# '1','2','3' → num=123
# ',' → add 123 → stack=[[123]]
#
# '[' → push new NI → stack=[[123], []]
#
# '4','5','6' → num=456
# ',' → add 456 → stack=[[123], [456]]
#
# '[' → push new NI → stack=[[123], [456], []]
#
# '7','8','9' → num=789
# ']' → add 789 → pop → attach → stack=[[123], [456,[789]]]
#
# ']' → pop → attach → stack=[[123,[456,[789]]]]
#
# ']' → pop → stack empty → RETURN result
#
# FINAL STRUCTURE:
# [123,[456,[789]]]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) — each character processed once
#
# SPACE COMPLEXITY:
# O(n) — stack for nested structures
# ---------------------------------------------------------
