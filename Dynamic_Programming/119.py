def getRow(rowIndex):
    row = [1]
    for i in range(2,rowIndex+2):
        prev=row
        row=[1]
        for j in range(1,i-1):
            value=prev[j]+prev[j-1]
            row.append(value)
        row.append(1)
    return row
print(getRow(3))