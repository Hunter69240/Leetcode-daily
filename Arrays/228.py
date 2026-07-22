# nums = [0,1,2,4,5,7]

# d={0:[]}
# count=0

# for i in nums:
#     if i+1 in nums:
#         d[count].append(i)
#     else:
#         count+=1
#         d[count]=[]
# print(d)



#With Formating

nums = [0,1,2,4,5,7]

d={
    0:[]
}
res=[]
count=0
for i in nums:
    if i+1 in nums :
        d[count].append(i)   
    else:
        d[count].append(i)
        count+=1
        d[count]=[]
print(d)

for i in d:
    if d[i]:
        start=min(d[i])
        end=max(d[i])
        if start !=end:
            res.append(f"{start}->{end}")
        else:
            res.append(f"{start}")
print(res)


#OR
#Since array is sorted i just have to check forward positions as doing and in check in array is O(n)
nums = [0,1,2,4,5,7]
res = []
i = 0
n = len(nums)
while i < n:
        start = i
        while i + 1 < n and nums[i+1] == nums[i] + 1:
            i += 1
        if start == i:
            res.append(f"{nums[start]}")
        else:
            res.append(f"{nums[start]}->{nums[i]}")
        i += 1
print(res)
