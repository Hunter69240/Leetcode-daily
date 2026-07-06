s = "cb"
p = "?a"

dp=[[False] * (len(p) + 1) for _ in range(len(s) + 1)]

dp[0][0]=True
for i in range(1,len(s)+1):
    dp[i][0]=False

for j in range(1,len(p)+1):
    dp[0][j]=dp[0][j-1] and p[j-1]=="*"

for i in range(1,len(s)+1):
    for j in range(1,len(p)+1):
        if p[j-1] == '*':
            dp[i][j] = dp[i][j-1] or dp[i-1][j]
        elif p[j-1] == '?' or p[j-1] == s[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = False
print(dp)