# def pascal(i,j):
#     if(i==j):
#         return 1
#     if(j==0):
#         return 1
#     return pascal(i-1,j-1) + pascal(i-1,j)
# a=pascal(3,1)
# print(a)

def pascal(i):
    numRows=i

    triangle=[]
    for i in range(numRows):
        row = [1] * (i + 1)
        print(row)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
a=pascal(3)
print(a)