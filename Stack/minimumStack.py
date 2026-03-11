# Implements a MinStack that supports push, pop, top, and getMin operations in O(1) time
# Uses two stacks: one for all elements, and one to track the current minimum
# Ensures getMin() always returns the smallest element present in the stack

class MinStack:
    def __init__(self):
        # Main stack to store values
        self.stack = []
        # Auxiliary stack to store current minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        # Add the value to the main stack
        self.stack.append(val)
        # If min_stack is empty or val is <= current min, push it to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the top value from the main stack
        if self.stack:
            val = self.stack.pop()
            # If the popped value is the current min, also pop from min_stack
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        # Return the top of the main stack if not empty
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top of the min stack (current minimum)
        return self.min_stack[-1] if self.min_stack else None
