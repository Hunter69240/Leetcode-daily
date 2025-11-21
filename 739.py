# For each day, we want to know in how many days a warmer temperature will come.
# We use a stack to keep track of unresolved (temperature, index) pairs.
# If current temperature is warmer than the top of the stack, we resolve it and update the result.

temperatures = [30, 38, 30, 36, 35, 40, 28]
stack = []  # Stack to store pairs: [temperature, index] of unresolved days
result = [0] * len(temperatures)  # Default answer: 0 for all days

for i, t in enumerate(temperatures):
    # While current temp is warmer than the top temp in stack:
    while stack and t > stack[-1][0]:
        stackT, stackInd = stack.pop()        # Pop the colder temp
        result[stackInd] = i - stackInd        # Calculate days waited and store
    # Push current day onto stack (waiting for a warmer day)
    stack.append([t, i])

print(result)
