void rotate(int** matrix, int matrixSize, int* matrixColSize) {
    // Concept: To rotate a square matrix 90 degrees clockwise:
    // Step 1: Transpose the matrix (swap rows with columns)
    // Step 2: Reverse each row to complete the rotation

    int m = matrixSize;           // m = number of rows
    int n = *matrixColSize;       // n = number of columns (same as rows in square matrix)
    int temp;

    // Step 1: Transpose the matrix
    for(int i = 0; i < m; i++) {
        for(int j = i + 1; j < n; j++) {
            temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2: Reverse each row
    for(int i = 0; i < m; i++) {
        int start = 0;
        int end = n - 1;
        while(start <= end) {
            temp = matrix[i][start];
            matrix[i][start] = matrix[i][end];
            matrix[i][end] = temp;
            start++;
            end--;
        }
    }
}
