

def checkword(word):
    vowel="aeiouAEIOU"
    vowelc=consc=digitc=0
    if(len(word)<3):
        return False
    if(not word.isalnum()):
        return False
    for i in word:
        if i in vowel:
            vowelc+=1
        elif i not in vowel and i.isalpha():
            consc+=1
        else:
            digitc+=1
    if(vowelc==len(word)-digitc or consc==len(word)-digitc):
        return False
    return True
a=checkword('3pp')
print(a)
    



