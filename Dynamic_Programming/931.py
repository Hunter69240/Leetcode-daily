'''
This is Falling Path DP (Pattern 3) because I'm falling row by row through a rectangular matrix, each cell depends on 3 neighbors above (top-left, top, top-right), and the answer is the min of the last row.
'''


# def a():
#     matrix = [[2,1,3],[6,5,4],[7,8,9]]

#     row=len(matrix)
#     col=len(matrix[0])

#     dp=[[0]*col for _ in range(row)]
#     dp[0]=matrix[0]

#     for i in range(1,row):
#         for j in range(col):
#             top_value=dp[i-1][j] 
#             top_left=dp[i-1][j-1] if ((j-1)>=0) else 99999
#             top_right=dp[i-1][j+1] if ((j+1)<col) else 99999
#             value=min(top_value,min(top_left,top_right))

#             dp[i][j]=matrix[i][j]+value
#     return min(dp[-1])
# print(a())

def a():
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    row=len(matrix)
    col=len(matrix[0])

    dp=matrix[0]

    for i in range(1,row):
        prev_row=dp.copy()
        for j in range(col):
            
            top_value=prev_row[j]
            top_left=prev_row[j-1] if j-1>=0 else 9999 
            top_right=prev_row[j+1]if j+1<col else 9999
            
            value=min(top_value,min(top_left,top_right))

            dp[j]=matrix[i][j]+value
        
    return min(dp)
print(a())