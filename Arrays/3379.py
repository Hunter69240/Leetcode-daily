def a():
    nums = [-10,-10,-4]
    n=len(nums)
    res=[]

    for i in range(len(nums)):
       
        position=(i+nums[i])%n
            
       
        
        res.append(nums[position])
    return res

#print(a())

for x in range(-10, 1):
    print(x, x % 3)
