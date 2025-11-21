#include<stdio.h>
#include<stdlib.h>
void main(){
    int height[]={0,1,0,2,1,0,1,3,2,1,2,1};
    int heightSize=12;
    int left[heightSize], right[heightSize];
    int i, j, water = 0;
  
    left[0] = height[0];    
    for(i = 1; i < heightSize; i++) {
        left[i] = (height[i] > left[i-1]) ? height[i] : left[i-1];
    }
    right[heightSize-1] = height[heightSize-1];
    for(i = heightSize - 2; i >= 0; i--) {
        right[i] = (height[i] > right[i+1]) ? height[i] : right[i+1];
    }   
   
    for(i = 0; i < heightSize; i++) {
        water += (left[i] < right[i]) ? left[i] - height[i] : right[i] - height[i];
    }
    printf("Trapped rainwater: %d\n", water);
}