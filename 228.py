nums = [0,1,2,4,5,7]

d={0:[]}
count=0

for i in nums:
    if i+1 in nums:
        d[count].append(i)
    else:
        count+=1
        d[count]=[]
print(d)