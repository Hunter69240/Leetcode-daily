class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val is None or min_val > val:
            min_val = val
        self.st.append([val, min_val])

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None


# ---------------------------------------------------------
# EXPLANATION:
# This is the "Min Stack" problem.
#
# Goal:
# Implement a stack that supports:
# - push
# - pop
# - top
# - getMin
# all in O(1) time.
#
# KEY IDEA:
# Instead of storing only values in the stack,
# we store PAIRS:
#   [current_value, minimum_value_so_far]
#
# This way:
# - The minimum at any point is always available
#   at the top of the stack.
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW EACH FUNCTION WORKS:
#
# push(val):
# - Get the current minimum using getMin()
# - Compare it with val
# - Store the smaller one as the new minimum
# - Push [val, min_val] into the stack
#
# pop():
# - Remove the top element
#
# top():
# - Return the value part of the top element
#
# getMin():
# - Return the minimum part of the top element
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# Operations:
#
# push(5)
# st = [[5,5]]
#
# push(3)
# current min = 5
# new min = 3
# st = [[5,5], [3,3]]
#
# push(7)
# current min = 3
# new min = 3
# st = [[5,5], [3,3], [7,3]]
#
# getMin() → 3
#
# pop()
# st = [[5,5], [3,3]]
#
# getMin() → 3
#
# pop()
# st = [[5,5]]
#
# getMin() → 5
#
# top() → 5
# ---------------------------------------------------------

# ---------------------------------------------------------
# WHY THIS WORKS:
# - Every stack level knows the minimum up to that point
# - No extra traversal is needed
# - All operations are O(1)
#
# SPACE COMPLEXITY:
# O(n) because each element stores one extra value
# ---------------------------------------------------------
