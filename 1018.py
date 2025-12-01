# Intuition:
# We build a binary number step by step from the list `nums`.
# Instead of converting the entire prefix each time, we update the current value using:
#       cur = cur * 2 + n
# (This works because left-shifting in binary is equivalent to multiplying by 2.)
# After updating, we simply check whether the number so far is divisible by 5.

# Example:
# nums = [1, 0, 1]
# Step 1: cur = 1       -> 1 % 5 = 1 -> False
# Step 2: cur = 2       -> 2 % 5 = 2 -> False
# Step 3: cur = 5       -> 5 % 5 = 0 -> True
# Result: [False, False, True]

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0
        for n in nums:
            # Update current binary number: shift left (×2) and add the new bit
            cur = (cur << 1) + n

            # Check if divisible by 5
            res.append(cur % 5 == 0)

        return res



# Intuition:
# We build a binary number step by step using the bits in `nums`.
# Each time, instead of recomputing the entire number, we update it efficiently:
#       cur = cur * 2 + n
# (Using left shift: cur = (cur << 1) + n)
#
# Since we only care about divisibility by 5, we can take modulo 5 at each step
# to keep the number small. (cur = cur % 5)
#
# Example:
# nums = [1, 0, 1]
#
# Step 1: cur = 1
#         1 % 5 = 1 -> False
#
# Step 2: cur = (1*2 + 0) % 5 = 2
#         2 % 5 = 2 -> False
#
# Step 3: cur = (2*2 + 1) % 5 = 5 % 5 = 0
#         0 % 5 = 0 -> True
#
# Result: [False, False, True]


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        cur = 0
        for n in nums:
            # Update current number using binary left shift, keep it small using mod 5
            cur = ((cur << 1) + n) % 5

            # Check if the current prefix is divisible by 5
            res.append(cur % 5 == 0)
            
        return res
