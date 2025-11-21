#DP because questions asks number of ways asked
class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize base cases: one way to reach the first two steps (step 0 and step 1)
        one, two = 1, 1

        # Iterate n-1 times to update the number of ways to reach each step
        for i in range(n-1):
            temp = one           # Store the previous value of 'one'
            one = one + two      # Update 'one' as sum of the previous two steps
            two = temp           # Update 'two' to the old value of 'one'
        
        # Final answer is the number of ways to reach nth step
        return one
