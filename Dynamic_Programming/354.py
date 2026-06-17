import bisect
#This is pattern 9 greedy 
# Maintain smallest possible tail for each chain length (tails array),
# greedily replace or extend based on height,
# len(tails) = max envelopes that can be nested
def a():
    envelopes = [[1,1], [2,2], [3,3], [1,4]]
    # dp=[1] * len(envelopes)
    # print(dp)
    # envelopes.sort(key=lambda x:x[1])
    # for i in range(len(envelopes)):
    #     for j in range(i):
    #         if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
    #             dp[i]=max(dp[i],dp[j]+1)
    # return max(dp)
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    heights = [e[1] for e in envelopes]
    tails = []
    for h in heights:
        pos = bisect.bisect_left(tails, h)  
        if pos == len(tails):
            tails.append(h)    
        else:
            tails[pos] = h     
    return len(tails)
print(a())