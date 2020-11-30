import math
def vsota_stevk(n):
    vsota = 0
    while n:
        vsota += n % 10
        n //= 10
    return vsota

print(vsota_stevk(math.factorial(100)))