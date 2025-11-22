nums = [3,6,9]
res = 0

for i in nums:
    # i % 3 gives the remainder when i is divided by 3
    # For numbers divisible by 3, remainder = 0 → condition becomes False
    # For numbers NOT divisible by 3, remainder ≠ 0 → condition becomes True
    if i % 3:
        res += 1   # count numbers NOT divisible by 3

print(res)  # all numbers are divisible by 3 → result = 0
