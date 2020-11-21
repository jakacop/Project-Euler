def najvecji_prafaktor(n):
    i = 2
    while i * i <= n:
        while n % i == 0:
            n = n // i
        i = i + 1
    return max(n, i-1)
input()

