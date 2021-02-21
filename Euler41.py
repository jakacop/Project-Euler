def je_prastevilo(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                return False
    return True

def je_pandigitalno(n):
    sez = []
    kontrola = [1, 2, 3, 4, 5, 6, 7]
    while n:
        sez.append(n % 10)
        n //= 10
    if len(set(sez)) == len(sez) and all(elem in sez for elem in kontrola):
        return True
    return False

def resitev(n):
    for i in range(n, -1, -1):
        if je_prastevilo(i) and je_pandigitalno(i):
            return i

print(resitev(7777777))