def palindrom(n):
    if int(str(n)[::-1]) == n:
        return True
    return False

def st_palindrom(m, n):
    for i in range(m, n):
        for j in range(m, n):
            z = i * j
            st = 0
            if z == palindrom(z):
                st = z
            return st

print(st_palindrom(1, 1))