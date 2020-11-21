def najvecji_prafaktor(n):
    x = 2
    while x * x <= n:
        if n % x: #ce ostanek n / x ni 0...
            x += 1
        else:
            n //= x
    return n

#def neki(n):
#    if 5 % n:
#        return 1
#    else:
#        return 0
input()

