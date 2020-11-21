def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

i = 0

#while True:
#    print(x, fibonacci(x))
#    x += 1

#for i in range(33):
#    if (fibonacci(i) == 0):
#        print(0)
#    elif fibonacci(i) % 2 == 0:
#        print(fibonacci(i))
#    else:
#        print('j')

#for i in range(33):
#    print(fibonacci(i))

def stetje_fibonaccija(i):
    if (fibonacci(i) == 0):
        return(0)
    else (fibonacci(i) % 2 == 0):
        return(fibonacci(i) + fibonacci(i+3))

fibonacci_2 = stetje_fibonaccija(33)

print(fibonacci_2)