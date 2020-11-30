def vsota_stevk(n):
    vsota = 0
    while n:
        vsota += n % 10
        n = n // 10
    return vsota
    
print(vsota_stevk(2 ** 1000))