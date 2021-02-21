import math
def binom(m, n):
    return int(math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))

def resitev(n):
    sez = []
    for i in range(1, n):
        for j in range(1, n):
            if i > j:
                if binom(i, j) > 1000000:
                    sez.append(binom(i, j))
    return len(sez)

print(resitev(101))