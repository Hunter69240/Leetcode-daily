def searchMatrix(matrix, target):
    # Iterate through each row in the matrix
    for row in matrix:
        length = len(row)
        # If target is greater than the last element of the current row,
        # it cannot be in this row as rows are sorted, so skip to next row
        if target > row[length - 1]:
            continue
        else:
            # Perform binary search on the current row
            low = 0
            high = length - 1
            while low <= high:
                mid = (low + high) // 2
                # Check if the middle element is the target
                if row[mid] == target:
                    return True
                # If target is greater, ignore left half
                elif row[mid] < target:
                    low = mid + 1
                # If target is smaller, ignore right half
                else:
                    high = mid - 1
    # If target not found in any row, return False
    return False


# Example usage:
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
result = searchMatrix(matrix, target)
print(result)  # Output: True
