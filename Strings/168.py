def a():
    dict={
        0:'Z',1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',
        11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',
        21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',
    }
    
    n=52
   
    remainder=0
    if n<=26:
        return dict[n]
    res=""
    while n >26:
        remainder=n%26
        print("n",n,"remainder",remainder)
        res+=dict[remainder]
        if remainder==0:
            n=(n-1)//26
        else:
            n=n//26
    print(n)
    if n<=26:
        res+=dict[n]
    
    return res[::-1]
print(a())