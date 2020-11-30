def vsota_stevk(n, i):
    vsota = 0
    while n:
        vsota += (n % 10) ** i
        n = n // 10
    return vsota

def resitev(j, m):
    sez = []
    for i in range(2, j):
        if vsota_stevk(i, m) == i:
            sez.append(vsota_stevk(i, m))
    return sum(sez)

print(resitev(10000000, 5))