def a():
    s = "1-11"
    res = 0
    sign = "+"
    stack = []
    num = 0   # builds multi-digit numbers

    for i in s:
        if i.isdigit():
            num = num * 10 + int(i)

        elif i == "+" or i == "-":
            if sign == "+":
                res += num
            else:
                res -= num
            sign = i
            num = 0

        elif i == "(":
            stack.append((res, sign))
            res = 0
            sign = "+"
            num = 0

        elif i == ")":
            if sign == "+":
                res += num
            else:
                res -= num
            num = 0

            prev_res, prev_sign = stack.pop()
            if prev_sign == "+":
                res = prev_res + res
            else:
                res = prev_res - res

    # apply last pending number
    if sign == "+":
        res += num
    else:
        res -= num

    return res


print(a())

# ---------------------------------------------------------
# EXPLANATION:
# This code evaluates a BASIC MATHEMATICAL EXPRESSION
# containing:
# - digits (0–9)
# - + and -
# - parentheses ()
#
# This is similar to the "Basic Calculator" problem.
#
# CORE IDEA:
# - Traverse the string character by character
# - Build numbers digit by digit
# - Apply the previous sign when an operator or bracket appears
# - Use a stack to save results when entering parentheses
# ---------------------------------------------------------

# ---------------------------------------------------------
# VARIABLES MEANING:
#
# res   → current calculated result
# sign  → sign (+ or -) to apply to the next number
# num   → currently building number (handles multi-digit)
# stack → stores (previous_result, previous_sign)
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# s = "1-11"
#
# Initial:
# res = 0, sign = '+', num = 0
#
# -------------------------
# char = '1'
# digit → num = 1
#
# -------------------------
# char = '-'
# sign was '+'
# res += num → res = 1
# sign = '-'
# num = 0
#
# -------------------------
# char = '1'
# num = 1
#
# -------------------------
# char = '1'
# num = 11
#
# -------------------------
# END OF STRING
# apply last number:
# sign = '-'
# res = 1 - 11 = -10
#
# FINAL RESULT:
# -10
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW PARENTHESES WORK (IMPORTANT):
#
# When '(' is found:
# - Save current (res, sign) onto stack
# - Reset res and sign for inside expression
#
# When ')' is found:
# - Finish current number
# - Pop previous result and sign
# - Merge inner result with outer result
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME & SPACE COMPLEXITY:
#
# Time:  O(n)  → single pass through string
# Space: O(n)  → stack for parentheses
# ---------------------------------------------------------
