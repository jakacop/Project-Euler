import math
def vsota_deliteljev(n):
    vsota = 0 
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and (i ** 0.5 + 0.5) ** 2 == i:
            vsota = vsota + (i + (n // i))
            return vsota
        else:
            for j in range(1, n):
                if n % j == 0:
                    vsota += j
            return vsota

def delitelji(n):
    sez = []
    for i in range(1, n):
        if n % i == 0:
            sez.append(i)
    return sez

print(sum(delitelji(100000000)))
#print(delitelji(100000000))
print(vsota_deliteljev(100000000))