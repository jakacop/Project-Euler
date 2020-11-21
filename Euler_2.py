def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

#n = 0
#while fibonacci(n) < 4000000:
#    n += 1
#    print(n, fibonacci(n))

def stetje(n):
    vsota = 0
    for i in range(n):
        if fibonacci(i) % 2 == 0:
            vsota = vsota + fibonacci(i)
    return vsota

print(stetje(33))