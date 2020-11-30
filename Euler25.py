def fibonacci(n):
    sez = [1, 1]
    for _ in range(2, n + 1):
        sez.append(sez[-1] + sez[-2])
    return sez

def dolzina_zadnjega(n):
    return len(str(fibonacci(n - 1)[-1]))

def resitev(n):
    stevec = 0
    while dolzina_zadnjega(stevec) != n:
        stevec += 1
    return stevec

print(resitev(1000))