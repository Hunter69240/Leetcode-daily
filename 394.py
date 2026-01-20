#Learning : Think of keping value sin stack always of same type to avoid confusion. , Example grouping into tuples when multiple values are to be stored.

s = "3[a]2[bc]"

stack = []
num = 0
curr = ""

for ch in s:
    if ch.isdigit():
        num = num * 10 + int(ch)

    elif ch == "[":
        stack.append((curr, num))
        curr = ""
        num = 0

    elif ch == "]":
        prev_str, count = stack.pop()
        curr = prev_str + count * curr

    else:
        curr += ch

print(curr)

# ---------------------------------------------------------
# EXPLANATION:
# This code DECODEs an encoded string of the form:
#   k[encoded_string]
#
# Rules:
# - k is a positive integer
# - encoded_string inside brackets is repeated k times
# - Encodings can be nested
#
# This is the "Decode String" problem.
#
# Core idea:
# - Use a STACK to remember previous strings and repeat counts
# - Build numbers for multi-digit repetition counts
# - Build current substring character by character
# ---------------------------------------------------------

# ---------------------------------------------------------
# VARIABLES:
#
# stack → stores (previous_string, repeat_count)
# num   → builds the repeat count (handles multi-digit numbers)
# curr  → current decoded string at the current nesting level
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW EACH CHARACTER IS HANDLED:
#
# digit:
#   - build the number (num = num * 10 + digit)
#
# '[' :
#   - push current string and num onto stack
#   - reset curr and num for the new nested level
#
# ']' :
#   - pop (prev_str, count) from stack
#   - repeat curr `count` times
#   - append it to prev_str
#
# letter:
#   - append directly to curr
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = "3[a]2[bc]"
#
# Initial:
# stack = []
# curr = ""
# num = 0
#
# -------------------------
# ch = '3'
# digit → num = 3
#
# ch = '['
# push ("", 3)
# stack = [("", 3)]
# curr = ""
# num = 0
#
# ch = 'a'
# curr = "a"
#
# ch = ']'
# pop ("", 3)
# curr = "" + 3 * "a" = "aaa"
#
# -------------------------
# ch = '2'
# num = 2
#
# ch = '['
# push ("aaa", 2)
# stack = [("aaa", 2)]
# curr = ""
# num = 0
#
# ch = 'b'
# curr = "b"
#
# ch = 'c'
# curr = "bc"
#
# ch = ']'
# pop ("aaa", 2)
# curr = "aaa" + 2 * "bc" = "aaabcbc"
#
# -------------------------
# END OF STRING
#
# FINAL RESULT:
# "aaabcbc"
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) where n is length of the string
#
# SPACE COMPLEXITY:
# O(n) for stack and result string
# ---------------------------------------------------------
