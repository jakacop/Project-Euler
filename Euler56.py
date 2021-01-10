def vsota_stevk(n):
    vsota = 0
    while n:
        vsota += (n % 10)
        n //= 10
    return vsota

def googol(a, b):
    x = 0
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if vsota_stevk(i ** j) >= x:
                x = vsota_stevk(i ** j)
    return x

print(googol(100, 100))

