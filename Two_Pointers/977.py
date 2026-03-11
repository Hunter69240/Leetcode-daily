nums = [-7, -3, 2, 3, 11]

res = [0 for _ in range(len(nums))]

k = len(nums) - 1   # position to fill in result (from the end)
i = 0               # left pointer
j = len(nums) - 1   # right pointer

# ---------------------------------------------------------
# EXPLANATION:
# nums is already sorted, but may contain negative numbers.
# Squaring negatives can make them large.
#
# Idea:
# - The largest square will come from either the leftmost
#   (most negative) or rightmost (most positive) number.
# - Compare abs(nums[i]) and abs(nums[j]).
# - Place the larger square at position k in res.
# - Move the corresponding pointer.
# - Decrease k.
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [-7, -3, 2, 3, 11]
# res  = [0, 0, 0, 0, 0]
#
# i=0, j=4, k=4
# abs(-7)=7 < abs(11)=11
# res[4] = 11^2 = 121
# j=3, k=3
# res = [0,0,0,0,121]
#
# i=0, j=3, k=3
# abs(-7)=7 > abs(3)=3
# res[3] = (-7)^2 = 49
# i=1, k=2
# res = [0,0,0,49,121]
#
# i=1, j=3, k=2
# abs(-3)=3 == abs(3)=3
# res[2] = (-3)^2 = 9
# i=2, k=1
# res = [0,0,9,49,121]
#
# i=2, j=3, k=1
# abs(2)=2 < abs(3)=3
# res[1] = 3^2 = 9
# j=2, k=0
# res = [0,9,9,49,121]
#
# i=2, j=2, k=0
# abs(2)=2 == abs(2)=2
# res[0] = 2^2 = 4
# i=3, k=-1
#
# FINAL RESULT:
# res = [4, 9, 9, 49, 121]
# ---------------------------------------------------------

while i <= j:
    if abs(nums[i]) < abs(nums[j]):
        res[k] = nums[j] ** 2
        j -= 1
    else:
        res[k] = nums[i] ** 2
        i += 1
    k -= 1

print(res)
