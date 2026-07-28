def a():
    n=4
    dist={1:'1'}
    def construct(number):
        to_be=dist[number-1]
        res=""
        i=0
        count=1
        while i<len(to_be):
            count=1
            while i<len(to_be)-1 and to_be[i]==to_be[i+1]:
                i+=1
                count+=1
            res+=f'{count}{to_be[i]}'
            i+=1
        dist[number]=res
    if n==1:
        return 1
    for i in range(2,n+1):
        construct(i)
    return dist[n]
print(a())