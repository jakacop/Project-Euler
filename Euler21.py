def delitelji(n):
    sez = []
    for i in range(1, n):
        if n % i == 0:
            sez.append(i)
    return sez

def sorodni_st(m, n):
    for i in range(1, max(m, n) + 1):
        if sum(delitelji(m)) == n and sum(delitelji(n)) == m:
            return True
        return False

def resitev(n):
    vsota = 0
    for i in range(1, n + 1):
        if