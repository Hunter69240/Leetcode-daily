def a():
    # Input array
    nums = [1, 1, 1]

    # Threshold value for product
    k = 1

    # Left pointer of sliding window
    i = 0

    # Right pointer of sliding window
    j = 0

    # Result to store count of valid subarrays
    res = 0

    # Product of elements in current window
    product = 1

    # If k is 0, no positive-product subarray can be < 0
    if k == 0:
        return 0

    # Sliding window traversal
    while j < len(nums) and i <= j:

        # Include current element in the window
        product *= nums[j]

        # If current window product is valid
        if product < k:
            # All subarrays ending at j starting from i to j are valid
            res += (j - i + 1)
            j += 1

        # If product is invalid (>= k), shrink window from left
        else:
            while product >= k and i <= j:
                # Remove leftmost element from product
                product = product // nums[i]
                i += 1

            # After shrinking, count valid subarrays ending at j
            res += (j - i + 1)
            j += 1

    # Return total count of valid subarrays
    return res


# Call the function
s = a()

# Print the result
print(s)
