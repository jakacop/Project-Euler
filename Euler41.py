from itertools import permutations 
def je_prastevilo(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True

#def vsota_stevk(n):
#    vsota = 0
#    while n:
#        vsota += (n % 10)
#        n //= 10
#    return vsota

#def prastevilo(n):
#    for i in range(n):
#        najvecje = 0
#        if (vsota_stevk(i) == 45) and (je_prastevilo(i)) and (i > najvecje):
#            najvecje = i
#    return najvecje

def permutacije(m):
    return list(permutations(range(1, m + 1)))

print(permutacije(3))