# Concept:
# We use a monotonic increasing stack to keep track of bar heights and their starting indices.
# When we find a bar shorter than the one on top of the stack, we pop and calculate area.
# This helps find the largest rectangle in a histogram efficiently.

heights = [2, 1, 5, 6, 2, 3]

maxArea = 0
stack = []  # Stack stores tuples of (index, height)

for i, h in enumerate(heights):
    start = i
    # Pop bars from stack while current height is less than the top of stack
    while stack and stack[-1][1] > h: #the height i got is smaller than the height on top of the stack so i cant extend the greater one so i pop it
        index, height = stack.pop()
        # Calculate area with popped height and width from its start index to current index
        maxArea = max(maxArea, height * (i - index))
        start = index  # Update start to the index of the popped bar
    # Push current bar with its correct start index
    stack.append((start, h))

# Final cleanup: process remaining bars in stack
for i, h in stack:
    maxArea = max(maxArea, h * (len(heights) - i))

print(maxArea)
