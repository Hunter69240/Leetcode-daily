s="+1"
nums=[]
def stoi(s):
    INT_MIN = -2**31        
    INT_MAX = 2**31 - 1     
    neg=False
    s=s.strip()
    if(s[0]=="-"):
        if s[1:]:
            s=s[1:]
            neg=True
        else:
            return -1
    elif s[0]=="+":
        if s[1:]:
            s=s[1:]
        else:
            return -1
    
    for i in s:
        if not i.isdigit():
            break
        nums.append(int(i))
    num=0
    for i in nums:
        num=num*10+i
    if(neg):
        num=-num
    return max(INT_MIN, min(INT_MAX, num))  
print(stoi(s))