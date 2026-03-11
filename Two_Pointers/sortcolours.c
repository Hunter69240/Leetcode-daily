#include<stdio.h>
void main(){
    int nums[]={2,0,2,1,1,0};
    int numSize=6;
    int count0=0, count1=0;
    for(int i=0; i<numSize; i++){
        if(nums[i]==0) count0++;
        else if(nums[i]==1) count1++;
    }
    for(int i=0; i<count0; i++) nums[i]=0;
    for(int i=count0; i<count0+count1; i++) nums[i]=1;
    for(int i=count0+count1; i<numSize; i++) nums[i]=2;
    for(int i=0; i<numSize; i++) printf("%d ", nums[i]);
}