s = "3+2*2/2"

li = []
is_num = True
num = 0

for i in s:
    if i == " ":
        continue
    if i.isdigit():
        num = num * 10 + int(i)
        is_num = True
    else:
        li.append(num)
        li.append(i)
        num = 0
        is_num = False

if is_num:
    li.append(num)

print(li)

i = 0
stack = []
prev_op = "+"

while i < len(li):
    if type(li[i]) == int:
        if prev_op == "+":
            num = li[i]
        elif prev_op == "-":
            num = -li[i]
        elif prev_op == "*":
            num1 = stack.pop()
            num = num1 * li[i]
        elif prev_op == "/":
            num1 = stack.pop()
            num = num1 / li[i]

        stack.append(int(num))
    else:
        if li[i] == "+":
            prev_op = "+"
        elif li[i] == "-":
            prev_op = "-"
        elif li[i] == "*":
            prev_op = "*"
        elif li[i] == "/":
            prev_op = "/"
    i += 1

print(sum(stack))


# ---------------------------------------------------------
# EXPLANATION:
# This code evaluates a BASIC MATHEMATICAL EXPRESSION string
# containing:
#   - non-negative integers
#   - +, -, *, /
#   - NO parentheses
#
# Operator precedence rules:
#   * and / have higher precedence than + and -
#
# The solution is done in TWO PHASES:
# 1) Tokenization (convert string → list of numbers & operators)
# 2) Evaluation using a stack
# ---------------------------------------------------------

# ---------------------------------------------------------
# PHASE 1: TOKENIZATION
#
# Input:
#   s = "3+2*2/2"
#
# We build numbers digit by digit to handle multi-digit numbers.
#
# Walkthrough:
# '3' → num=3
# '+' → append 3, '+'
# '2' → num=2
# '*' → append 2, '*'
# '2' → num=2
# '/' → append 2, '/'
# '2' → num=2
#
# Final list:
# li = [3, '+', 2, '*', 2, '/', 2]
# ---------------------------------------------------------

# ---------------------------------------------------------
# PHASE 2: EVALUATION USING STACK
#
# IDEA:
# - Handle * and / immediately
# - Delay + and - by pushing signed numbers into stack
#
# prev_op keeps track of the operator BEFORE the number.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# li = [3, '+', 2, '*', 2, '/', 2]
#
# Initial:
# stack = []
# prev_op = '+'
#
# i=0 → 3 (int)
# prev_op='+' → push 3
# stack = [3]
#
# i=1 → '+'
# prev_op = '+'
#
# i=2 → 2
# prev_op='+' → push 2
# stack = [3, 2]
#
# i=3 → '*'
# prev_op = '*'
#
# i=4 → 2
# prev_op='*'
# pop 2 → 2 * 2 = 4 → push 4
# stack = [3, 4]
#
# i=5 → '/'
# prev_op = '/'
#
# i=6 → 2
# prev_op='/'
# pop 4 → 4 / 2 = 2 → push 2
# stack = [3, 2]
#
# Final stack sum:
# 3 + 2 = 5
# ---------------------------------------------------------

# ---------------------------------------------------------
# FINAL ANSWER:
# 5
#
# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)
# ---------------------------------------------------------
