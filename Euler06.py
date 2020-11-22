def vsota_kvadratov(n):
    vsota = 0
    for i in range(1, n + 1):
        vsota += i ** 2
    return int(vsota)

def kvadrat_vsote(n):
    return int((n * (n + 1)) / 2) ** 2

print(kvadrat_vsote(100) - vsota_kvadratov(100))