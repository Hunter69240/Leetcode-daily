nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

i = 0
n = len(nums)
j = n - 1

# Binary search loop
while i <= j:
    mid = (i + j) // 2  # Calculate middle index
    
    # If target found at mid, print and break
    if nums[mid] == target:
        print(mid)
        break

    # Check if the left half [i to mid] is sorted
    if nums[i] <= nums[mid]:
        # If target lies within the sorted left half
        if nums[i] <= target <= nums[mid]:
            j = mid - 1  # Search in the left half
        else:
            i = mid + 1  # Search in the right half
    else:
        # Right half [mid to j] is sorted
        # If target lies within the sorted right half
        if nums[mid] <= target <= nums[j]:
            i = mid + 1  # Search in the right half
        else:
            j = mid - 1  # Search in the left half
else:
    # If loop ends without finding the target
    print(-1)
