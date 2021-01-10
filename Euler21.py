import math
def vsota_deliteljev(n):
    delitelji = []
    for i in range(1, n):
        if n % i == 0:
            delitelji.append(i)
    return sum(set(delitelji))

#Ce je stevilo popolni kvadrat npr. 9 potem bo drugace 3 stelo dvakrat!!! <------Ce pristevamo pare, kar je sicer veliko hitreje.

def resitev(n):
    vsota = 0
    for i in range(1, n):
        a = vsota_deliteljev(vsota_deliteljev(i))
        if i == a and i != vsota_deliteljev(i):
            vsota += i
    return vsota

print(resitev(10000))