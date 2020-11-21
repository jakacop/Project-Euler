def palindrom(n):
    if int(str(n)[::-1]) == n:
        return True
    return False

def st_palindrom(m, n):
    st = 0
    for i in range(m, n):
        for j in range(m, n):
            z = i * j
            if z > st:
                if palindrom(z):
                    st = i * j
    return st

print(st_palindrom(100, 1000))