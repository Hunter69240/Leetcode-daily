#2 Solutions

def a():
    nums = [1, 2, 3, 3]

    nums.sort()
    
    req_len = len(nums) // 2
    for i in range(len(nums)):
        if nums.count(nums[i]) == req_len:
            return nums[i]
        
print(a())


# ---------------------------------------------------------
# EXPLANATION (METHOD 1 – COUNTING AFTER SORT):
#
# This code finds the element that appears exactly n/2 times
# in the array.
#
# Steps:
# 1) Sort the array
# 2) Compute required frequency = len(nums) // 2
# 3) For each element:
#    - Count how many times it appears
#    - If it equals required frequency, return it
#
# ---------------------------------------------------------
# DRY RUN:
#
# nums = [1,2,3,3]
# After sort → [1,2,3,3]
#
# len(nums) = 4 → req_len = 2
#
# i=0 → nums[i]=1 → count=1 ≠ 2
# i=1 → nums[i]=2 → count=1 ≠ 2
# i=2 → nums[i]=3 → count=2 == req_len → return 3
#
# FINAL RESULT: 3
#
# NOTE:
# - This approach is simple
# - But nums.count() is O(n), making total time O(n²)
# ---------------------------------------------------------



def a():
    nums = [1, 2, 3, 3]
    s = set()

    for i in nums:
        if i in s:
            return i
        else:
            s.add(i)

print(a())


# ---------------------------------------------------------
# EXPLANATION (METHOD 2 – SET / HASHING):
#
# This code finds the FIRST DUPLICATE element.
#
# Steps:
# 1) Use a set to track seen elements
# 2) Traverse the array:
#    - If element already exists in set → duplicate found
#    - Else → add it to set
#
# ---------------------------------------------------------
# DRY RUN:
#
# nums = [1,2,3,3]
#
# s = {}
#
# i=1 → not in set → add → {1}
# i=2 → not in set → add → {1,2}
# i=3 → not in set → add → {1,2,3}
# i=3 → already in set → return 3
#
# FINAL RESULT: 3
#
# ---------------------------------------------------------
# COMPLEXITY:
#
# Time:  O(n)
# Space: O(n)
#
# This is much more efficient than Method 1.
# ---------------------------------------------------------
