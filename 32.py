s = "()(())"

stack = []
boundary = -1
max_length = 0

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        if not stack:
            boundary = i
        else:
            stack.pop()
            if stack:
                length = i - stack[-1]
            else:
                length = i - boundary
            max_length = max(max_length, length)

print(max_length)

# ---------------------------------------------------------
# EXPLANATION:
# This code finds the length of the LONGEST VALID PARENTHESES substring.
#
# Key ideas:
# - Use a stack to store indices of '('
# - Use `boundary` to mark the last invalid ')'
#
# Why indices instead of characters?
# - Indices help calculate substring lengths easily.
#
# How it works:
# - When we see '(' → push its index onto the stack
# - When we see ')':
#     - If stack is empty → no matching '('
#       → mark this index as a boundary (invalid start)
#     - Else:
#       → pop one '(' from stack (valid pair formed)
#       → calculate current valid length:
#           - If stack still has elements:
#               length = current_index - last '(' index
#           - Else:
#               length = current_index - boundary
#       → update max_length
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = "()(())"
# index: 0 1 2 3 4 5
# chars: ( ) ( ( ) )
#
# Initial:
# stack = []
# boundary = -1
# max_length = 0
#
# i=0 → '('
# stack = [0]
#
# i=1 → ')'
# stack not empty → pop → stack=[]
# stack empty → length = 1 - (-1) = 2
# max_length = 2
#
# i=2 → '('
# stack = [2]
#
# i=3 → '('
# stack = [2,3]
#
# i=4 → ')'
# pop → stack=[2]
# stack not empty → length = 4 - 2 = 2
# max_length = 2
#
# i=5 → ')'
# pop → stack=[]
# stack empty → length = 5 - (-1) = 6
# max_length = 6
#
# FINAL RESULT:
# max_length = 6
# ---------------------------------------------------------
