a=[23,32,45,12,10,11,16,19,70,12,100,90,-1,-90]
largest=0
secondlargest=0
for i in a:
    if i > largest:
        secondlargest = largest
        largest = i
    elif i > secondlargest and i != largest:
        secondlargest = i
print(secondlargest)