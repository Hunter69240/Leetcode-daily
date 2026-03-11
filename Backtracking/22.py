# This code generates all valid combinations of n pairs of parentheses.
# It uses the concept of **backtracking** to build each valid combination step by step,
# and uses a stack (list) to build strings recursively while ensuring balance between '(' and ')'.

n = 3  # Total number of pairs of parentheses

stack = []  # Temporary list to hold current combination of parentheses
res = []    # Final list to store all valid combinations

# Recursive backtracking function
def backtrack(openN, closeN):
    # If we've used all n opening and n closing brackets, add to result
    if openN == closeN == n:
        res.append("".join(stack))  # Join characters into a string and store it
        return

    # If we can still add an opening bracket, do it and recurse
    if openN < n:
        stack.append("(")                  # Add '('
        backtrack(openN + 1, closeN)       # Recurse with one more open
        stack.pop()                        # Backtrack (remove last added '(')

    # If we can add a closing bracket (must not exceed opening), do it and recurse
    if closeN < openN:
        stack.append(")")                  # Add ')'
        backtrack(openN, closeN + 1)       # Recurse with one more close
        stack.pop()                        # Backtrack (remove last added ')')

# Start the recursive process with 0 opening and 0 closing brackets
backtrack(0, 0)

# Print all valid combinations
print(res)
