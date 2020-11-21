def krneki(n, i):
    while i * i <= n:
        while n % i == 0:
            n = n // i
        i += 1
    return n

print(krneki(600851475143, 2))