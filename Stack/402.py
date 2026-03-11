#If order matters and smallest number req , think of monotonic stack

num = "1432219"
k = 3
stack = []
i = 0

while i < len(num):
    curr = num[i]

    while stack and k > 0 and stack[-1] > curr:
        stack.pop()
        k -= 1

    stack.append(curr)
    i += 1

while k > 0:
    stack.pop()
    k -= 1

res = "".join(stack).lstrip("0")
print(res if res else "0")


# ---------------------------------------------------------
# EXPLANATION:
# This code solves the "Remove K Digits" problem.
#
# Goal:
# Remove exactly k digits from the number string `num`
# so that the resulting number is the SMALLEST possible.
#
# Core idea:
# - Use a MONOTONIC INCREASING STACK
# - Remove digits that make the number larger when a smaller
#   digit appears to the right
#
# This is a GREEDY approach:
# - Always remove the leftmost larger digit when a smaller
#   digit appears and removals (k) are still allowed.
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY GREEDY WORKS:
# - Higher digits on the left contribute more to the number
# - Removing a bigger digit earlier always gives a smaller number
# - If a digit cannot be removed now, it will never be better later
# ---------------------------------------------------------

# ---------------------------------------------------------
# STEP-BY-STEP DRY RUN:
#
# num = "1432219"
# k = 3
#
# Start:
# stack = []
#
# ---------------------------------------------------------
# i=0 → curr='1'
# stack empty → push '1'
# stack = ['1']
#
# ---------------------------------------------------------
# i=1 → curr='4'
# top='1' < '4' → push
# stack = ['1','4']
#
# ---------------------------------------------------------
# i=2 → curr='3'
# top='4' > '3' and k>0 → pop '4', k=2
# now top='1' < '3' → push
# stack = ['1','3']
#
# ---------------------------------------------------------
# i=3 → curr='2'
# top='3' > '2' and k>0 → pop '3', k=1
# top='1' < '2' → push
# stack = ['1','2']
#
# ---------------------------------------------------------
# i=4 → curr='2'
# top='2' == '2' → push
# stack = ['1','2','2']
#
# ---------------------------------------------------------
# i=5 → curr='1'
# top='2' > '1' and k>0 → pop '2', k=0
# cannot pop further (k=0)
# push '1'
# stack = ['1','2','1']
#
# ---------------------------------------------------------
# i=6 → curr='9'
# k=0 → just push
# stack = ['1','2','1','9']
#
# ---------------------------------------------------------
# k is already 0 → no extra pops
#
# Result before cleanup:
# "1219"
#
# Remove leading zeros (none here)
#
# FINAL RESULT:
# "1219"
# ---------------------------------------------------------

# ---------------------------------------------------------
# EDGE CASE HANDLING:
# - If all digits are removed → return "0"
# - Leading zeros are stripped using lstrip("0")
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n) — each digit pushed and popped at most once
#
# SPACE COMPLEXITY:
# O(n) — stack storage
# ---------------------------------------------------------
