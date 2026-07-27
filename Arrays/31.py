def a():
    nums = [1,2,3]
    pivot=float('inf')
    for i in range(len(nums)-1,0,-1):
        if nums[i]>nums[i-1]:
            pivot=i-1
            break
    j=float('inf')
    if pivot == float('inf'):
        nums.reverse()
    else:
        for i in range(len(nums)-1,pivot,-1):
            if nums[i]>nums[pivot]:
                j=i
                break
        nums[j],nums[pivot]=nums[pivot],nums[j]
        nums[pivot+1:] = nums[pivot+1:][::-1]
    return (nums)



print(a())