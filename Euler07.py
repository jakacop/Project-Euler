def je_prastevilo(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nto_prastevilo(n):
    stevec = 1
    zacetek = 2
    while stevec < n:
        zacetek += 1
        if je_prastevilo(zacetek):
             stevec += 1
    return zacetek

print(nto_prastevilo(10001))