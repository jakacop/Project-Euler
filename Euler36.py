def palindrom(n):
    return str(n)[::-1] == str(n)

def dvojiski(m, n = 2):
    sez = []
    while m:
        sez.append(str(m % n))
        m //= 2
    return int(''.join(sez[::-1]))

def resitev():
    vsota = 0
    for i in range(1, 1000000):
        if palindrom(i) and palindrom(dvojiski(i)):
            vsota += i
    return vsota

print(resitev())