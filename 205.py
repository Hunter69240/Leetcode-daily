s = "badc"
t = "baba"

std={}
tsd={}

for i,j in zip(s,t):
    if i in std and std[i] != j:
        print('false')
        break
    if j in tsd and tsd[j] != i:
        print('false')
        break

    if i not in std:
        std[i] = j
    if j not in tsd:
        tsd[j] = i
    
else:
    print('true')


