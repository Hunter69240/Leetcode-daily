# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         # Add virtual balloons with value 1 at both ends
#         nums = [1] + nums + [1]
        
#         # Memo: (l, r) -> max coins from bursting balloons in nums[l:r]
#         dp = {}

#         def dfs(l, r):
#             # No balloons left in interval
#             if l > r:
#                 return 0

#             # Return cached result
#             if (l, r) in dp:
#                 return dp[(l, r)]
            
#             best = 0
            
#             # Choose each balloon i as the last one to burst in this interval
#             for i in range(l, r + 1):
#                 # Coins gained from bursting i last
#                 coins = nums[l - 1] * nums[i] * nums[r + 1]
                
#                 # Add optimal coins from left and right sub-intervals
#                 coins += dfs(l, i - 1) + dfs(i + 1, r)
                
#                 best = max(best, coins)
            
#             dp[(l, r)] = best
#             return best
        
#         # Solve for the full interval (excluding the artificial boundaries)
#         return dfs(1, len(nums) - 2)


# dp(L,R) = maximum coins from bursting all balloons in range [L,R], by trying every balloon as the final one to burst in that range
def a():
    nums = [3,1,5,8]
    nums.insert(0,1)
    nums.append(1)
    res=0
    memo={}
    def dp(L,R):
        nonlocal res
        if ((L,R) in memo):
            return memo[(L,R)]
        if L>R:
            return 0
        best=0
        for i in range(L,R+1):
            coins=(dp(L,i-1) + dp(i+1,R) +  nums[L-1]*nums[i]*nums[R+1] )
            best=max(best,coins)
        memo[(L,R)]=best
        return best
    return dp(1,len(nums)-2)
print(a())