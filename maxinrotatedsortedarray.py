nums = [3,4,5,0,1,2]

i=0
j=len(nums)-1
while(i<j):
    mid=(i+j)//2
    if(nums[j]<nums[mid]):
        i=mid
    else:   
        j=mid-1
print(nums[i])  