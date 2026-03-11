# Calculates the total amount of water that can be trapped between bars (heights)
# Uses dynamic programming with precomputed left and right max arrays
# For each index, water trapped = min(left max, right max) - current height

height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

leftmax = [0] * len(height)   # Stores max height to the left of each position
rightmax = [0] * len(height)  # Stores max height to the right of each position
count = []                    # Stores trapped water at each position

# Fill leftmax array
for i in range(len(height)):
    if i == 0:
        leftmax[i] = height[i]  # First element has no left, so it's its own max
    else:
        leftmax[i] = max(leftmax[i - 1], height[i])  # Max so far from the left

# Fill rightmax array
for i in range(len(height) - 1, -1, -1):
    if i == len(height) - 1:
        rightmax[i] = height[i]  # Last element has no right, so it's its own max
    else:
        rightmax[i] = max(rightmax[i + 1], height[i])  # Max so far from the right

# Calculate trapped water at each index
for i in range(len(height)):
    # Water = min of left and right max - current height
    count.append(min(leftmax[i], rightmax[i]) - height[i])

# Total trapped water
print(sum(count))
