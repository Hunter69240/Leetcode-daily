def longestHarmoniousSubsequence(nums):
    # ---------------------------------------------------------
    # PROBLEM:
    # Given an integer array nums, return the length of the
    # longest harmonious subsequence.
    #
    # A harmonious subsequence is one where the difference
    # between its maximum and minimum values is exactly 1.
    # ---------------------------------------------------------

    # ---------------------------------------------------------
    # STEP 1: Sort the array
    # Sorting allows us to use a sliding window where
    # min and max can be tracked using pointers.
    # ---------------------------------------------------------
    nums.sort()

    # ---------------------------------------------------------
    # STEP 2: Initialize pointers and variables
    # i -> left pointer of window
    # j -> right pointer of window
    # length -> stores the maximum harmonious length found
    # minimum / maximum -> values at window boundaries
    # ---------------------------------------------------------
    i = 0
    j = 0
    length = 0
    minimum = float('inf')
    maximum = float('-inf')

    # ---------------------------------------------------------
    # STEP 3: Sliding window traversal
    # ---------------------------------------------------------
    while j < len(nums):
        # Update current window min and max
        minimum = nums[i]
        maximum = nums[j]
        diff = maximum - minimum

        # -----------------------------------------------------
        # STEP 4: Check harmonious condition
        # If difference is exactly 1, update max length
        # -----------------------------------------------------
        if diff == 1:
            length = max(length, j - i + 1)

        # -----------------------------------------------------
        # STEP 5: Shrink window if difference exceeds 1
        # Move left pointer until window becomes valid
        # -----------------------------------------------------
        else:
            while (maximum - minimum) > 1:
                i += 1
                minimum = nums[i]

        j += 1

    # ---------------------------------------------------------
    # FINAL ANSWER:
    # length contains the longest harmonious subsequence size
    # ---------------------------------------------------------
    return length
