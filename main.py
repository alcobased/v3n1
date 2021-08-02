from datetime import timedelta, datetime


current = datetime.now()

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


n = 1
while True:
    if timedelta(seconds=30) + current < datetime.now():
        break
    print(f"N: {n}, f: {f(n)}")
    n += 1