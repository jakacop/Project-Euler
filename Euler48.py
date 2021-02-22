def vsota_potenc(n):
    vsota = 0
    for i in range(1, n):
        vsota += i ** i
    return vsota

print(vsota_potenc(1001))