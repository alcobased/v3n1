d = dict()

def f(n):
    if n == 1:
        return 0
    elif n in d:
        return d[n]
    else:
        if n % 2 == 0:
            t = f(n // 2) + 1
        else:
            t = f(n * 3 + 1) + 1
        d[n] = t
        return t

print(f(27))