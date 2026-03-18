nums = [1,2,3,1]
dp=[0 for i in range(len(nums)+1)]
dp[-2]=nums[-1]
print(dp)
for i in range(len(nums)-2,-1,-1):
    print(i)
    dp[i]=max(nums[i]+dp[i+2],dp[i+1])
print(dp)