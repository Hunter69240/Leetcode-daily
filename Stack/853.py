# Concept:
# We compute how long each car takes to reach the target.
# Sort cars by starting position (from nearest to target to farthest).
# Use a stack to track fleet leaders.
# If a car takes less or equal time than the one in front, it merges into that fleet.

target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

# Pair up each car's position and speed
pair = [[p, s] for p, s in zip(position, speed)]

stack = []

# Sort cars based on position (from farthest to closest to target)
for p, s in sorted(pair)[::-1]:
    # Calculate time taken to reach the target
    time = (target - p) / s
    # Add this car's time to the stack (potential fleet)
    stack.append(time)
    
    # If the current car takes less or equal time than the car ahead,
    # it will catch up and become part of that fleet — so we pop it
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()

# The number of car fleets is the number of remaining times in the stack
result = len(stack)
print(result)  # Output the number of fleets arriving at the destination
