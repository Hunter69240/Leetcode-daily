#a parking lot in a mall has r*c number of parking spaces. Each parking space will either be empty which is represented by 0 or full which is represented by 1
#the task is to find the index of the row in the parking lot that has the most number of parking spaces full
parking=[[1, 0, 0],
         [1, 1, 0],
         [0, 0, 0]
         ]
sumr=-1
row=-1
for i in parking:
    sumr=max(sumr,sum(i))
    if sum(i)==sumr:
        row=parking.index(i)

print(row+1)