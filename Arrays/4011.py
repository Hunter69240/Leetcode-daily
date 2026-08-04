def a():
    nums = [1,2,1,2]
    a = 3
    b = 2

    even=0
    odd=0
    res=0
    for i in range(len(nums)):
        even=0
        odd=0
        for j in range(i,len(nums)):
            if nums[j] %2 ==0:
                even+=1
            else:
                odd+=1
            
            if odd !=0 :
                if even*b <= odd *a:
                    res+=1
    return res
print(a())