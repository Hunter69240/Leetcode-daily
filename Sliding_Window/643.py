# def findMaxAverage(nums, k):
#     window_sum = sum(nums[:k])
#     max_sum = window_sum

#     for i in range(k, len(nums)):
#         window_sum += nums[i]
#         window_sum -= nums[i - k]
#         max_sum = max(max_sum, window_sum)

#     return max_sum / k


# nums = [1, 12, -5, -6, 50, 3]
# k = 4
# a = findMaxAverage(nums, k)
# print(a)
# 
# 

def a():
    nums = [1,12,-5,-6,50,3]
    k = 4
    temp_sum=0
    res_sum=temp_sum=sum(nums[:k])
    for i in range(k,len(nums)):
        print(i,res_sum)
        temp_sum+=nums[i]
        temp_sum-=nums[i-k]
        res_sum=max(res_sum,temp_sum)
    return res_sum/k
print(a())