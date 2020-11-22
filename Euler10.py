def je_prastevilo(n):
    if n == 1: 
        return False
    for i in range(2, int((n ** 0.5) + 1)):
        if n % i == 0:
            return False
    return True

def nto_prastevilo(n):
    stevec = 0
    zacetek = 1
    while stevec < n:
        zacetek += 1
        if je_prastevilo(zacetek):
            stevec += 1
    return zacetek

def vsota_prastevil(n):
    vsota = 0
    i = 1
    while nto_prastevilo(i) < n:
        vsota += nto_prastevilo(i)
        i += 1
    return vsota

vsota = 2
for i in range(3, 2000000):
    if je_prastevilo(i):
        vsota += i

print(vsota)

#i = 0
#while nto_prastevilo(i) < 2000000:
#    i += 1
#    print(i, nto_prastevilo(i), vsota_prastevil(i))