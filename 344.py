s = ["h","e","l","l","o"]
# i=0
# j=len(s)-1
# while i < j:
#     s[i], s[j] = s[j], s[i]
#     i += 1
#     j -= 1
# print(s)

r=[]
while s:
    r.append(s.pop())
print(r)
s = r
print(s)