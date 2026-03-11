def s():
    nums = [-1, 0, 1, 2, -1, -4]
    res = []
    nums.sort()

    # ---------------------------------------------------------
    # EXPLANATION:
    # This is the classic 3SUM problem.
    # We need to find all UNIQUE triplets [a, b, c]
    # such that:
    #   a + b + c = 0
    #
    # APPROACH: SORT + TWO POINTERS
    #
    # Steps:
    # 1) Sort the array
    # 2) Fix one element nums[i]
    # 3) Use two pointers:
    #       j = i + 1 (next element)
    #       k = last index
    # 4) Move j and k based on the sum:
    #       sum > 0 → move k left (reduce sum)
    #       sum < 0 → move j right (increase sum)
    #       sum = 0 → valid triplet
    #
    # We skip duplicates to avoid repeating triplets.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # DRY RUN:
    #
    # Original nums: [-1,0,1,2,-1,-4]
    # After sort:   [-4,-1,-1,0,1,2]
    #
    # ---------------------------------------------------------
    # i = 0 → nums[i] = -4
    # j = 1 (-1), k = 5 (2)
    #
    # total = -4 + -1 + 2 = -3 < 0
    # → move j
    #
    # j = 2 (-1), k = 5 (2)
    # total = -3 < 0 → move j
    #
    # j = 3 (0), k = 5 (2)
    # total = -2 < 0 → move j
    #
    # j = 4 (1), k = 5 (2)
    # total = -1 < 0 → move j
    #
    # j == k → stop inner loop
    # ---------------------------------------------------------
    #
    # i = 1 → nums[i] = -1
    # j = 2 (-1), k = 5 (2)
    #
    # total = -1 + -1 + 2 = 0
    # → FOUND triplet [-1,-1,2]
    # → add to res
    # → j++
    #
    # j = 3 (0), k = 5 (2)
    # total = -1 + 0 + 2 = 1 > 0
    # → move k
    #
    # j = 3 (0), k = 4 (1)
    # total = -1 + 0 + 1 = 0
    # → FOUND triplet [-1,0,1]
    # → add to res
    # → j++
    #
    # skip duplicates if any
    # ---------------------------------------------------------
    #
    # i = 2 → nums[i] = -1
    # nums[i] == nums[i-1] → SKIP (duplicate)
    #
    # i = 3 → nums[i] = 0
    # j = 4 (1), k = 5 (2)
    # total = 3 > 0 → move k
    #
    # j == k → stop
    #
    # FINAL RESULT:
    # res = [[-1,-1,2], [-1,0,1]]
    # ---------------------------------------------------------

    for i in range(len(nums)):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1           # decrease sum
            elif total < 0:
                j += 1           # increase sum
            else:
                # Found a valid triplet
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                # Skip duplicate values for j
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
    return res


a = s()
print(a)
