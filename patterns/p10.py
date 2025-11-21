'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        * 
      * * * 
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

rows=5
for i in range(rows,0,-1):
    for j in range(1,rows-i+1):
        print(" ", end="")
    for j in range(1,2*i):
        print("*", end="")
    print()
for i in range(2,rows+1):
    for j in range(1,rows-i+1):
        print(" ", end="")
    for j in range(1,2*i):
        print("*", end="")
    print()