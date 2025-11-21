#include<stdio.h>
int main(){
    
    int n;
    printf("Enter the number of elements in the array: ");
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        printf("Enter element %d: ", i+1);
        scanf("%d",&arr[i]);
    }
    
    for(int i=0;i<n-1;i++){
        if(arr[i]>arr[i+1]){
            printf("Array is not sorted\n");
            return 0;
        }
    }
    printf("Array is sorted\n");
    return 0;
}