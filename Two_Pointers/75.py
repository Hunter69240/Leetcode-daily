class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        This problem is solved using the Dutch National Flag Algorithm.
        
        WHY IS THIS A 2-POINTER (ACTUALLY 3-POINTER) PROBLEM?
        ------------------------------------------------------
        We want to sort ONLY 3 values: 0, 1, and 2.
        Instead of using sorting algorithms (O(n log n)),
        we can partition the array into 3 regions in ONE PASS (O(n)):

            - left region      → all 0s
            - middle region    → all 1s
            - right region     → all 2s

        This uses THREE pointers:
            lo   = boundary for 0s
            mid  = current index being examined
            hi   = boundary for 2s

        The algorithm goes like this:
            If nums[mid] == 0:
                swap it to the LEFT side (lo region)
                move lo++ and mid++

            If nums[mid] == 1:
                already in the correct middle region
                just mid++

            If nums[mid] == 2:
                swap it to the RIGHT side (hi region)
                move hi-- (DO NOT move mid because the swapped value must be checked)

        This is an IN-PLACE, ONE-PASS, O(n) solution.
        """


        n = len(nums)
        
        lo = 0            # boundary for 0s
        mid = 0           # current pointer
        hi = n - 1        # boundary for 2s
        
        
        # Process until mid crosses hi
        while mid <= hi:

            if nums[mid] == 0:
                # If we see a 0, it belongs to the front region.
                # Swap nums[mid] with nums[lo]
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo += 1
                mid += 1

            elif nums[mid] == 1:
                # 1 is already in correct region (middle),
                # just move mid forward.
                mid += 1

            else:
                # nums[mid] == 2
                # 2 belongs to the right region,
                # Swap nums[mid] with nums[hi]
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1    # shrink the right region boundary
                # DO NOT increment mid here
                # because the swapped value at nums[mid] must be re-checked.


        """
        ===========================
        DRY RUN ON INPUT: [2,0,2,1,1,0]
        ===========================

        Initial state:
            nums = [2,0,2,1,1,0]
            lo = 0, mid = 0, hi = 5

        -------------------------------------------
        STEP 1:
            mid = 0 → nums[mid] = 2
            swap(nums[mid], nums[hi]) → swap(nums[0], nums[5])
            nums = [0,0,2,1,1,2]
            hi = 4
            (mid stays = 0)

        -------------------------------------------
        STEP 2:
            mid = 0 → nums[mid] = 0
            swap(nums[mid], nums[lo]) → swap(nums[0], nums[0]) (same index)
            nums = [0,0,2,1,1,2]
            lo = 1, mid = 1

        -------------------------------------------
        STEP 3:
            mid = 1 → nums[mid] = 0
            swap(nums[mid], nums[lo]) → swap(nums[1], nums[1])
            nums = [0,0,2,1,1,2]
            lo = 2, mid = 2

        -------------------------------------------
        STEP 4:
            mid = 2 → nums[mid] = 2
            swap(nums[mid], nums[hi]) → swap(nums[2], nums[4])
            nums = [0,0,1,1,2,2]
            hi = 3
            (mid stays = 2)

        -------------------------------------------
        STEP 5:
            mid = 2 → nums[mid] = 1
            1 is correct region → mid = 3

        -------------------------------------------
        STEP 6:
            mid = 3 → nums[mid] = 1
            1 is correct region → mid = 4

        -------------------------------------------
        Loop ends because mid > hi

        Final array:
            [0,0,1,1,2,2]
        """

