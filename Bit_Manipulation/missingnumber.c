#include<stdio.h>
#include<stdlib.h>

void main(){
    int nums[]={3, 0, 1};
    int numSize=3;
    int totalSum = 0, expectedSum = 0;
    for(int i=0; i<numSize; i++){
        totalSum += nums[i];
    }
    expectedSum = (numSize * (numSize + 1)) / 2;
    int missingNumber = expectedSum - totalSum;
}