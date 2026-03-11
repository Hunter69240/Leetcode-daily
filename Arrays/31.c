#include<stdio.h>

void main() {
    // Initial array
    int a[] = {3, 2, 1};
    int size = 3;
    int ind = -1;

    // Step 1: Find the first index 'ind' from the end where a[ind] < a[ind + 1]
    // This is the pivot point where the order starts decreasing
    for (int i = size - 2; i >= 0; i--) {
        if (a[i] < a[i + 1]) {
            ind = i;
            break;
        }
    }

    // Step 2: If no such index is found, the array is in descending order (last permutation)
    // So, reverse the whole array to get the first permutation (sorted ascending)
    if (ind == -1) {
        for (int i = 0, j = size - 1; i < j; i++, j--) {
            int temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }

        // Print the result
        printf("Next permutation: ");
        for (int i = 0; i < size; i++) {
            printf("%d ", a[i]);
        }
        return;  // Exit since the next permutation is already printed
    }

    // Step 3: Find the smallest element greater than a[ind] from the right side
    // Swap it with a[ind] to form a slightly larger permutation
    for (int i = size - 1; i > ind; i--) {
        if (a[i] > a[ind]) {
            int temp = a[i];
            a[i] = a[ind];
            a[ind] = temp;
            break;
        }
    }

    // Step 4: Reverse the subarray to the right of 'ind' to make it the smallest possible order
    for (int i = ind + 1, j = size - 1; i < j; i++, j--) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }

    // Print the result
    printf("Next permutation: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", a[i]);
    }
}
