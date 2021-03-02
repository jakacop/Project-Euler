def pravi_delitelji(n):
    sez = []
    while n:
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                sez.append(i)
                if i != (n // i):
                    sez.append(n // i)
        sez.sort()
        del sez[-1]
        return sez

def presezno_st(n):
    if sum(pravi_delitelji(n)) > n:
        return True
    return False

def vsota_preseznih(n):
    for i in range(1, n // 2 + 1):
        if presezno_st(i) and presezno_st(n - i):
            return True
    return False

def resitev(n):
    vsota = 0
    for i in range(1, n + 1):
        if not vsota_preseznih(i):
            vsota += i
            print(i)
    return vsota

print(resitev(28123))