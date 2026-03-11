class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Step 1: Alias shorter array as A to optimize binary search
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)  # Total number of elements
        half = total // 2  # Half index for median splitting

        # Always binary search on the shorter array for efficiency
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1  # Binary search bounds for array A

        # Binary search begins
        while True:
            i = (l + r) // 2             # Mid index in A
            j = half - i - 2             # Corresponding index in B so that left half has 'half' elements

            # Get values around the cut (use ±infinity to handle edge cases)
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Check if partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # If total length is odd, return the middle element
                if total % 2:
                    return min(Aright, Bright)
                # If even, return average of middle two
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # If Aleft > Bright, we are too far on the right side of A → move left
            elif Aleft > Bright:
                r = i - 1
            # If Bleft > Aright, we are too far on the left side of A → move right
            else:
                l = i + 1
