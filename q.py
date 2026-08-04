#1 time limit

# def gcd(a,b):
#     if b>a:
#         a,b=b,a
#     while b%a !=0:
#         rem=b%a
#         b=a
#         a=rem
#     return a

# def a():
#     nums = [2,3,5]
#     res=0
#     dict={}
#     i=0
#     j=i+1
#     while i<len(nums):
#         while j<len(nums):
#             denom=gcd(nums[i],nums[j])
#             res=max(res,((nums[i]*nums[j])//(denom**2)))
#             j+=1
#         i+=1
#         j=i+1
        

#     return res
# print(a())

# def a():
#     nums = [1,2,1,2] 
#     a = 3
#     b = 2
#     res=0
#     even=0
#     odd=0
    
#     for i in range(len(nums)-1):
#         even
#         for j in range(i+1,len(nums)):

            
# print(a())


def a():
    tasks = [2,3,4]
    shifts = [20,4,5]

    res=[]
    max=sum(tasks)
    sub_tasks=tasks.copy()
    running_sum=0
    completed=0
    not_completed=0
    for i in range(len(shifts)):
        curr_shift=shifts[i]
        if not_completed == 0:
            sub_tasks=tasks.copy()
            completed=0
        for j in range(len(sub_tasks)):
            if sub_tasks[j]==0:
                print("continuye")
                continue
            elif sub_tasks[j]<= curr_shift:
                curr_shift-=sub_tasks[j]
                completed+=1
            else:
                buffer=sub_tasks[j]-curr_shift
                completed+=1
                
        
        print(shifts[i],sub_tasks,completed)
        not_completed=len(tasks)-completed
        
        res.append(not_completed)
        
    return res
print(a())
        