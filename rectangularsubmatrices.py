def count_even_sum_submatrices(matrix):
    N, M = len(matrix), len(matrix[0])
    count = 0
    
    for top in range(N):
        arr = [0] * M
        for bottom in range(top, N):
            for col in range(M):
                arr[col] += matrix[bottom][col]
            
            prefix_counts = [1, 0]  # counts of prefix sums mod 2: even=1 (empty), odd=0
            prefix_sum = 0
            for val in arr:
                prefix_sum += val
                mod = prefix_sum % 2
                count += prefix_counts[mod]
                prefix_counts[mod] += 1
                
    return count

# Input
N, M =2,2
matrix = [[1, 2], [3, 4]]
print(count_even_sum_submatrices(matrix))
