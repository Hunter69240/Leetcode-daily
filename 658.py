# Given sorted array
arr = [1, 2, 3, 4, 5]

# Number of closest elements required
k = 4

# Target value to compare distances from
x = 3

# Precompute absolute differences of each element from x
# diff[i] = |arr[i] - x|
diff = [abs(i - x) for i in arr]

# Left pointer at start of array
i = 0

# Right pointer at end of array
j = len(arr) - 1

# Shrink the window until its size becomes exactly k
while (j - i + 1) != k:

    # If left element is closer to x than right element,
    # discard the right element
    if diff[i] < diff[j]:
        j -= 1

    # If right element is closer to x than left element,
    # discard the left element
    elif diff[i] > diff[j]:
        i += 1

    # If both elements are equally distant from x
    else:
        # If left value is greater, discard left (keep smaller values)
        if arr[i] > arr[j]:
            i += 1
        # Otherwise discard right
        else:
            j -= 1

# The remaining window of size k contains the answer
print(arr[i:j+1])
