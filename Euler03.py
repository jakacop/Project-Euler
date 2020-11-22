def krneki(m, n):
    while n * n <= m:
        while m % n == 0:
            m = m // n
        n += 1
    return m

print(krneki(600851475143, 2))