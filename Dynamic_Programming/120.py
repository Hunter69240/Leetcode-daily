def a():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

    row=len(triangle)
    
    dp=triangle[0]

    for i in range(1,row):
        prev_row=dp.copy()
        new_dp=[]
        for j in range(len(triangle[i])):
          
            if j==0:
                value=prev_row[0]
            elif j == len(triangle[i]) - 1:
                value=prev_row[j-1]
            else:
                value1 = prev_row[j]
                value2 = prev_row[j-1] if j-1 >= 0 else 9999
                value=min(value1,value2)
            new_value=triangle[i][j]+value
            new_dp.append(new_value)
        dp=new_dp.copy()
    return min(dp)
print(a())
    