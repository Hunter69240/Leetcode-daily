path = "/.../a/../b/c/../d/./"

path=path.split("/")
stack=[]
print(path)
for i in path:
    if i=="" or i==".":
        continue
    elif i=="..":
        if stack:
            stack.pop()
    else:
        stack.append(i)
print("/"+"/".join(stack))
    

