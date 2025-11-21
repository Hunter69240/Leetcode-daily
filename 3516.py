# You are given three integers x, y, z representing positions on a number line:
# x -> Person 1's position
# y -> Person 2's position
# z -> Person 3's position (fixed, does not move)
#
# Both Person 1 and Person 2 move toward Person 3 at the same speed.
# We need to determine who reaches Person 3 first:
#   - Return 1 if Person 1 reaches first
#   - Return 2 if Person 2 reaches first
#   - Return 0 if they reach at the same time

x = 2
y = 7
z = 4

# Calculate absolute distance from Person 1 to Person 3
xtoz = abs(z - x)

# Calculate absolute distance from Person 2 to Person 3
ytoz = abs(z - y)

# Compare distances to decide the winner
if xtoz > ytoz:
    print("2")   # Person 2 is closer -> reaches first
elif ytoz > xtoz:
    print("1")   # Person 1 is closer -> reaches first
else:
    print("0")   # Both distances equal -> reach at the same time
