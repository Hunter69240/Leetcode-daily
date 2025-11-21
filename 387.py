s="leetcode"
d = {}

for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = (1, i)
            else:
                count = d[s[i]][0] + 1
                d[s[i]] = (count, d[s[i]][1])

       
for i in range(len(s)):
            if d[s[i]][0] == 1:
                print(i)
                break
else:      
 print(-1)