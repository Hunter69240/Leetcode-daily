#include<stdio.h>
void main(){
    long x=8;
    long left=0,right=x;
    long mid=0;
    while(left<=right){
        mid=(left+right)/2;
        if(mid*mid==x){
            printf("%d", mid);
            return;
        } else if(mid*mid<x) {
            left=mid+1;
        } else {
            right=mid-1;
        }
    }
    printf("%d", right);
}