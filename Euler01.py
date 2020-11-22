def stetje_veckratnikov(n, a):
    if (n == 0):
        return 0
    elif (n % a == 0):
        return n + stetje_veckratnikov(n - a, a) 
    else:
        return stetje_veckratnikov(n-1, a)

veckratniki_3 = stetje_veckratnikov(999, 3)
veckratniki_5 = stetje_veckratnikov(999, 5)
veckratniki_15 = stetje_veckratnikov(999, 15)

print(veckratniki_3 + veckratniki_5 - veckratniki_15)

input()
