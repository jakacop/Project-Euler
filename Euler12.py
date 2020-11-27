def vsota_n(n):    
    return n * (n + 1) // 2

def delitelji(n):
    l = int(n ** 0.5)
    stevec = 0
    for i in range(1, l):
        if n % i == 0:
            stevec += 1
    if n % l == 0:
        return 2 * stevec + 1
    return 2 * stevec

def resitev(j):
    n = 1
    i = 1
    while delitelji(n) < j:
        n = vsota_n(i)
        i += 1
    return n 

print(resitev(500))