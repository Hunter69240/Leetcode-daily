# Evaluating Reverse Polish Notation (RPN) using a stack
# Supports operators: +, -, *, /
# Division truncates toward zero as required by standard RPN behavior

tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []

for i in tokens:
    # If token is a number (handles negatives too), convert to int and push to stack
    if i not in "+-*/":
        stack.append(int(i))
    else:
        # Pop two operands from the stack
        b = stack.pop()
        a = stack.pop()
        
        # Apply the operator and push the result back
        if i == "+":
            stack.append(a + b)
        elif i == "-":
            stack.append(a - b)
        elif i == "*":
            stack.append(a * b)
        elif i == "/":
            stack.append(int(a / b))  # Truncate toward 0

# Final result is the only item left on the stack
result = stack.pop()
print(int(result))
