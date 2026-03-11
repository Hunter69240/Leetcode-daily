#include<stdio.h>

void main() {
    // Initialize the array and its size
    int nums[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int numsSize = 8;

    int sum = 0;            // Running sum of the current subarray
    int maxi = nums[0];     // Stores the maximum subarray sum found so far

    // Iterate through the array to apply Kadane's Algorithm
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];     // Add current element to the running sum

        // Update maximum if current sum is greater than previous maximum
        if (sum > maxi) {
            maxi = sum;
        }

        // If sum becomes negative, reset it to 0
        // (A negative sum would reduce any future subarray total)
        if (sum < 0) {
            sum = 0;
        }
    }

    // Print the maximum subarray sum
    printf("%d\n", maxi);

    return;
}
