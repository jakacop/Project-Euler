import math
def vsota_fact(n):
    vsota = 0
    while n:
        vsota += math.factorial(n % 10)
        n //= 10
    return vsota

def resitev(n):
    vsota = 0
    for i in range(3, n + 1):
        if vsota_fact(i) == i:
            vsota += i
    return vsota

print(resitev(100000))