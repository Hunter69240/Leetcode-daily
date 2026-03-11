matrix=[[1,1,1],[1,0,1],[1,1,1]]
tbz=[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
           tbz.append([i,j])
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        for k in range(len(tbz)):
            if i == tbz[k][0] or j == tbz[k][1]:
                matrix[i][j] = 0
                      
print(matrix)
