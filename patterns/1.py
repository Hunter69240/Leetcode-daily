inputStr = "a3b5c2a2"

res=""
for i in range(0,len(inputStr)-1,2):
    res+=(inputStr[i]* int(inputStr[(i+1)]))
    print(i,inputStr[i])
print(res)