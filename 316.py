s = "cbacdcbc"

i = 1
res = [s[0]]

while i < len(s):
    if s[i] in res:
        i += 1
        continue
    while res and s[i] < res[-1] and res[-1] in s[i:]:
        res.pop()
    res.append(s[i])
    i += 1

print("".join(res))
