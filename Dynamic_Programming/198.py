nums = [1,1]

# DP array
# res[i] = maximum money that can be robbed from houses [0 … i]
res = [0 for _ in range(len(nums))]

# Base case 1:
# Only one house → must take it
res[0] = nums[0]

# Base case 2:
# Two houses → cannot take both (adjacent constraint)
# Choose the better of the two
if len(nums) > 1:
    res[1] = max(nums[0], nums[1])

# Why this is DP:
# - Overlapping subproblems:
#   best up to i reuses results from i-1 and i-2
# - Optimal substructure:
#   best(i) = max(skip current, take current + best(i-2))
# - We store results → avoid recomputation (tabulation)

# Build from smaller indices → larger indices
# Recurrence valid only for i ≥ 2
for i in range(2, len(nums)):

    # Choice 1: skip current house
    # → take best till previous house
    skip = res[i - 1]

    # Choice 2: rob current house
    # → add current value + best till i-2
    take = nums[i] + res[i - 2]

    # Take the better of the two choices
    res[i] = max(skip, take)

# Final DP table
print(res)


# ---------------- DRY RUN (nums = [1,1]) ----------------

# Initial:
# res = [0, 0]

# After base case:
# res[0] = 1
# res = [1, 0]

# Handle i = 1:
# res[1] = max(nums[0], nums[1])
#        = max(1, 1)
#        = 1
# res = [1, 1]

# Loop:
# range(2, len(nums)) → range(2, 2) → no iterations

# Final:
# res = [1, 1]
# Answer = res[n-1] = res[1] = 1

# Interpretation:
# Two houses with equal value:
# - can only pick one (adjacent restriction)
# - max money = 1


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # rob1: maximum money robbed up to 2 houses before current house
#         # rob2: maximum money robbed up to 1 house before current house
#         rob1, rob2 = 0, 0

#         # Pattern: [rob1, rob2, n, n+1, ...]
#         # At each house, we decide: rob current house + rob1, or skip it and keep rob2
#         for n in nums:
#             # Calculate max money if we include current house (n + rob1) 
#             # vs if we skip it (rob2)
#             temp = max(n + rob1, rob2)
            
#             # Shift the window forward:
#             # rob1 becomes what rob2 was (move 2 houses back → 1 house back)
#             rob1 = rob2
            
#             # rob2 becomes the new maximum (move 1 house back → current position)
#             rob2 = temp
        
#         # rob2 contains the maximum money that can be robbed from all houses
#         return rob2
