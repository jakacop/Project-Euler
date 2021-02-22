def stevke(n):
    sez = []
    while n:
        sez.append(n % 10)
        n //= 10
        sez.sort()
    return sez

def resitev():
    i = 1
    while stevke(i) != stevke(2 * i) or stevke(i) != stevke(3 * i) or stevke(i) != stevke(4 * i) or stevke(i) != stevke(5 * i) or stevke(i) != stevke(6 * i):
        i += 1
        #print(i) 
    return i

print(resitev())