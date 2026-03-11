def a():
    # First input array
    nums1 = [1, 2, 3, 2, 1]

    # Second input array
    nums2 = [3, 2, 1, 4, 7]

    # Lengths of both arrays
    n, m = len(nums1), len(nums2)

    # Stores the maximum length of repeated subarray found
    result = 0

    # Slide nums1 over nums2 starting from each index in nums1
    for start1 in range(n):
        # Pointer for nums1 starting at start1
        i = start1

        # Pointer for nums2 always starting at index 0
        j = 0

        # Length of current matching subarray
        max_len = 0

        # Compare elements while both pointers are in bounds
        while i < n and j < m:
            # If elements match, extend current subarray
            if nums1[i] == nums2[j]:
                max_len += 1
                # Update global maximum
                result = max(result, max_len)
            else:
                # Reset length when elements differ
                max_len = 0

            # Move both pointers forward diagonally
            i += 1
            j += 1

    # Slide nums2 over nums1 starting from index 1 (to avoid duplicate overlap)
    for start2 in range(1, m):
        # Pointer for nums1 always starting at index 0
        i = 0

        # Pointer for nums2 starting at start2
        j = start2

        # Length of current matching subarray
        max_len = 0

        # Compare elements while both pointers are in bounds
        while i < n and j < m:
            # If elements match, extend current subarray
            if nums1[i] == nums2[j]:
                max_len += 1
                # Update global maximum
                result = max(result, max_len)
            else:
                # Reset length when elements differ
                max_len = 0

            # Move both pointers forward diagonally
            i += 1
            j += 1

    # Return the length of the longest repeated subarray
    return result


# Print the result
print(a())
