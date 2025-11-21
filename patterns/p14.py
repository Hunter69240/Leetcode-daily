'''
A
B C 
D E F 
G H I J 
K L M N O 
'''

count = 0
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + count), end=' ')
        count += 1
    print()
