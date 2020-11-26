def vsota_n(n):
    return n * (n + 1) // 2

def st_deliteljev(n):
    stevec = 0
    for i in range(1, n + 1):
        stevec = len([i for i in range(1, n + 1) if n % i == 0])
    return stevec

def delitelji(n):
    stevec = 0
    for i in range(1, n + 1):
        if int(n ** 0.5 + 0.5) ** 2 == n:
            stevec = 2 * len([i for i in range(1, int(n ** 0.5)) if n % i == 0]) + 1
        else:
            stevec = 2 * len([i for i in range(1, int(n ** 0.5) + 1) if n % i == 0])
    return stevec

n = 0
def resitev():
    n = 0
    while delitelji(n) < 500:
        n += 1
        n = vsota_n(n)
    return n

print(resitev())