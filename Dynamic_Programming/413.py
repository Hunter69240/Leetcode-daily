def numberOfArithmeticSlices(nums):
    # ---------------------------------------------------------
    # PROBLEM:
    # Given an integer array nums, return the number of
    # arithmetic subarrays (slices) of length >= 3.
    #
    # An arithmetic array is one where the difference between
    # consecutive elements is constant.
    #
    # Example:
    # nums = [1,2,3,4]
    # Arithmetic slices:
    # [1,2,3], [2,3,4], [1,2,3,4]
    # Output = 3
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # STEP 0: HANDLE EDGE CASE
    #
    # If array length < 3, no arithmetic slice is possible
    # because at least 3 elements are needed.
    # ---------------------------------------------------------
    n = len(nums)
    if n < 3:
        return 0

    # ---------------------------------------------------------
    # STEP 1: BUILD DIFFERENCE ARRAY
    #
    # diff[i] = nums[i+1] - nums[i]
    #
    # Any arithmetic subarray in nums corresponds to a
    # contiguous segment in diff where all values are equal.
    #
    # Example:
    # nums = [1,2,3,4]
    # diff = [1,1,1]
    # ---------------------------------------------------------
    diff = []
    for i in range(n - 1):
        diff.append(nums[i + 1] - nums[i])

    # ---------------------------------------------------------
    # count → total number of arithmetic slices
    # i     → pointer for traversing diff array
    # ---------------------------------------------------------
    count = 0
    i = 0

    # ---------------------------------------------------------
    # STEP 2: FIND CONTIGUOUS SEGMENTS WITH SAME DIFFERENCE
    # ---------------------------------------------------------
    while i < len(diff) - 1:

        # Check if an arithmetic run starts
        if diff[i] == diff[i + 1]:
            j = i

            # -------------------------------------------------
            # Extend j while differences remain equal
            #
            # This finds a continuous segment:
            # diff[i], diff[i+1], ..., diff[j]
            # -------------------------------------------------
            while j + 1 < len(diff) and diff[j] == diff[j + 1]:
                j += 1

            # -------------------------------------------------
            # LENGTH OF RUN (IMPORTANT PART)
            #
            # L = number of equal consecutive differences
            #
            # Example:
            # diff = [1,1,1,1]
            # L = 4
            #
            # This corresponds to L+1 numbers in nums.
            # -------------------------------------------------
            L = j - i + 1

            # -------------------------------------------------
            # WHY THE FORMULA (L - 1) * L // 2 ?
            #
            # For a run of L equal differences:
            #
            # Number of arithmetic slices of length >= 3 is:
            #
            #   1 + 2 + 3 + ... + (L - 1)
            #
            # Explanation:
            # - From the first index, you can form (L - 1) slices
            # - From the second index, you can form (L - 2) slices
            # - ...
            # - From the second-last index, you can form 1 slice
            #
            # This sum is a triangular number:
            #
            #   (L - 1) * L / 2
            #
            # Example:
            # nums = [1,2,3,4,5]
            # diff = [1,1,1,1] → L = 4
            #
            # Arithmetic slices:
            # [1,2,3]
            # [2,3,4]
            # [3,4,5]
            # [1,2,3,4]
            # [2,3,4,5]
            # [1,2,3,4,5]
            #
            # Total = 6
            # (4 - 1) * 4 // 2 = 6
            # -------------------------------------------------
            count += (L - 1) * L // 2

            # Move i past this entire run
            i = j + 1
        else:
            # No arithmetic run starting here
            i += 1

    # ---------------------------------------------------------
    # FINAL ANSWER
    # ---------------------------------------------------------
    return count


# ---------------------------------------------------------
# FUNCTION CALL
# ---------------------------------------------------------
a = numberOfArithmeticSlices([1, 2, 3, 4])
print(a)

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [1,2,3,4]
#
# diff = [1,1,1]
#
# i = 0:
# diff[0] == diff[1] → YES
#
# j moves to index 2
# L = 2 - 0 + 1 = 3
#
# count += (3 - 1) * 3 // 2
# count += 3
#
# End loop
#
# Final Answer = 3
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n) for difference array
# ---------------------------------------------------------
