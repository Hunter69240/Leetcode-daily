def a():
    nums  = [-1,2,3]
    
    nums=set(nums)
    print("Set",nums)
    if len(nums)>2:
        nums=list(nums)
        nums.sort()
        return (nums[len(nums)-3])
    else:
        return max(nums)
    

print(a())