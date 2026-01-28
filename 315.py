def a():
    nums = [5, 2, 6, 1]
    n = len(nums)
    result = [0] * n

    # Pair each value with its original index
    arr = [(nums[i], i) for i in range(n)]

    def merge_sort(left, right):
        if right - left <= 1:
            return

        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        temp = []
        i, j = left, mid
        right_smaller = 0

        # Merge two sorted halves
        while i < mid and j < right:
            if arr[i][0] <= arr[j][0]:
                # All previously counted right_smaller elements
                # are smaller than arr[i]
                result[arr[i][1]] += right_smaller
                temp.append(arr[i])
                i += 1
            else:
                # arr[j] is smaller than arr[i]
                right_smaller += 1
                temp.append(arr[j])
                j += 1

        # Remaining elements in left half
        while i < mid:
            result[arr[i][1]] += right_smaller
            temp.append(arr[i])
            i += 1

        # Remaining elements in right half
        while j < right:
            temp.append(arr[j])
            j += 1

        # Copy back to original array slice
        arr[left:right] = temp

    merge_sort(0, n)
    return result


s = a()
print(s)


# ---------------------------------------------------------
# EXPLANATION:
# This code solves:
# "Count of Smaller Numbers After Self"
#
# For each element nums[i], we count how many elements
# to its RIGHT are smaller than it.
#
# Example:
# nums = [5, 2, 6, 1]
# result = [2, 1, 1, 0]
#
# Brute force is O(n²), but this solution is O(n log n)
# using MERGE SORT.
# ---------------------------------------------------------

# ---------------------------------------------------------
# CORE IDEA:
# While performing merge sort, we can count how many
# elements from the RIGHT half move before elements
# in the LEFT half.
#
# Those elements are exactly the "smaller elements
# to the right".
# ---------------------------------------------------------

# ---------------------------------------------------------
# DATA STRUCTURES:
#
# arr = [(value, original_index)]
#   - keeps track of original positions
#
# result[index] = count of smaller elements after nums[index]
# ---------------------------------------------------------

# ---------------------------------------------------------
# HOW COUNTING WORKS DURING MERGE:
#
# right_smaller = number of elements taken from right half
#                 before the current left element
#
# When arr[i] <= arr[j]:
#   → all previously moved right elements are smaller
#   → add right_smaller to result of arr[i]
#
# When arr[j] < arr[i]:
#   → arr[j] is smaller than arr[i]
#   → increment right_smaller
# ---------------------------------------------------------

# ---------------------------------------------------------
# DRY RUN:
#
# nums = [5,2,6,1]
# arr = [(5,0),(2,1),(6,2),(1,3)]
#
# After full merge sort and counting:
#
# For 5:
#   smaller elements after = [2,1] → 2
#
# For 2:
#   smaller elements after = [1] → 1
#
# For 6:
#   smaller elements after = [1] → 1
#
# For 1:
#   smaller elements after = [] → 0
#
# result = [2,1,1,0]
# ---------------------------------------------------------

# ---------------------------------------------------------
# TIME COMPLEXITY:
# O(n log n)
#
# SPACE COMPLEXITY:
# O(n)
# ---------------------------------------------------------
