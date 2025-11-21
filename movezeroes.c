#include<stdio.h>
void main(){
    int i=0,j=0;
    int nums[]={0,1,0,3,12};
    int numSize=5;
    for(i=0; i<numSize; i++){
        if(nums[i]!=0){
            int temp = nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            j++;
        }
    }
    for(i=0; i<numSize; i++) printf("%d ", nums[i]);
}