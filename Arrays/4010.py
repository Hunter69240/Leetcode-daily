def gcd(a,b):
            while b:
               a,b=b,a%b
            return a
def a():
    nums = [2,3,5]
    res=0
    i=0
    j=i+1
    while i<len(nums):
        while j<len(nums):
            denom=gcd(nums[i],nums[j])
            res=max(res,((nums[i]*nums[j])//(denom**2)))
            j+=1
        i+=1
        j=i+1
    return res
print(a())