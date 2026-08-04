def a():
        pre = list(accumulate(A))
        p = 0
        res = []
        n = len(A)
        for a in shifts:
            p += a
            res.append(n - bisect_right(pre, p))
            if p >= pre[-1]:
                p = 0
        return res
print(a())